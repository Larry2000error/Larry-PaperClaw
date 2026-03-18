# RS-PaperClaw Pipeline SOP（固化版）

## 目标
- 稳定生成并更新 arXiv 论文阅读报告到指定 GitHub Issue
- 质量门禁通过后才更新
- 降低耗时、提升可观测性

## 单篇标准流程
1. 输入：`arxiv_id` + `issue_number`
2. 从 arXiv abs 提取：标题、作者、日期、英文摘要
3. 下载 PDF（优先并发分片 Range 下载，失败回退单线程）
4. 生成预览图：PDF 前 3 页转 JPG，上传到仓库
5. LLM 子任务：
   - 摘要翻译（中文）
   - 标签提取（top5）
   - 10问总结（A1~A10）
6. 质量门禁：
   - 标题/作者/日期/摘要有效
   - Q1~Q10 非空，且不含占位词（待提取/待分析/待补充/待确认/分析中/Unknown/N/A）
7. 生成报告并更新指定 issue（update-only）

## 执行命令
```bash
python3 scripts/paper_processor.py <arxiv_id> <issue_number>
```

## 性能与可观测性
- 输出结构化日志：`STEP-1..STEP-5` + `GATE` + `ISSUE`
- 建议单篇超时控制：5~10分钟
- 推荐先单篇验证，再批量执行

## 批量修复（按文本占位词）
1. 扫描 open issues，找出包含占位词的 issue
2. 提取其 arXiv id
3. 逐篇重跑并更新
4. 复检 open issues 确认清零

## 已落地关键优化
1. 预览图文件名匹配修复：`page_<n>-*.jpg` 兼容
2. PDF 下载提速：HTTP Range 并发分片 + 回退
3. 10问输出规范：A1~A10 标记 + 缺失补齐
4. Markdown 可读性增强：答案段落/列表格式化

## 故障排查速记
- `preview_images=0`：检查 `pdftoppm`、文件匹配、上传权限
- `GATE FAILED`：看具体项（摘要、Qn、占位词）
- 无更新：确认 issue_number 存在且脚本运行到 `ISSUE UPDATED`

## 运维建议
- 批量任务禁止静默长跑；每篇必须有回执
- 先跑 1 篇测耗时，再开批量
- 失败篇单独重跑，不阻塞全队列
