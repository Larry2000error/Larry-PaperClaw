# Daily Reports

最近三天日报（最新在前）：

# [20260806](./202608/20260806.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦多模态检索与持续学习两大方向。视觉语言模型通过链式思维与难负样本优化检索反馈机制；遥感领域则探索双适配器架构与排序感知蒸馏，解决跨模态对齐中的灾难性遗忘问题。

## ✨ 今日亮点

- 难负样本驱动的检索中心CoT框架，从失败案例中强化多模态推理能力
- 双适配器架构实现遥感图文检索的持续学习，兼顾新旧知识迁移
- 排序感知蒸馏策略优化跨模态对齐，缓解增量训练中的性能退化

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260806] Learning from Failures: Retrieval-Centric CoT via Hard Negatives for Unified Multimodal Retrieval | Sun Zelong, Wang Jun, Yang Kaicheng, Gu Tiancheng, Feng Ziyong, Lu Zhiwu | Glint Lab | 提出检索中心链式思维方法，利用难负样本构建失败感知反馈机制，提升统一多模态检索的推理能力。 | [#399](https://github.com/Larry2000error/Larry-PaperClaw/issues/399) |
| [20260806] DARAD: Dual Adapters and Ranking-Aware Distillation for Continual Remote Sensing Image-Text Retrieval | Chen Xi, Chen Xu, Jia Xiangyang, Wang Wei, Zhang Xu, Sun Zhenyuan | School of Computer Science, Wuhan University；Beijing Institute for General Artificial Intelligence (BIGAI) | 设计双适配器与排序感知蒸馏框架，实现遥感图像-文本检索的持续学习，有效缓解跨模态对齐中的灾难性遗忘。 | [#400](https://github.com/Larry2000error/Larry-PaperClaw/issues/400) |

## 🔎 观察

- 遥感多模态检索正从静态训练转向持续学习范式，知识蒸馏成为保留历史知识的关键技术路径。
- 难负样本挖掘从分类任务扩展至检索-推理联合优化，显示视觉语言模型自我纠错能力的提升趋势。

---

Powered by OpenClaw🦞

---

# [20260805](./202608/20260805.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI领域聚焦多模态检索与视觉语言理解。三项研究分别探索上下文组合图像检索、长文本监督的视觉语言对齐，以及视频时序预测检索，体现出从静态匹配向动态推理、从短文本向长文本扩展的技术演进趋势。

## ✨ 今日亮点

- CoCo-IR提出上下文组合图像检索新范式，融合多模态大模型与交互推理
- 长段落文本监督取代传统短标题，重塑视觉语言对比学习框架
- 视频前缀预测未来状态，实现跨实例时序检索新机制

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260805] CoCo-IR: Contextual Composed Image Retrieval | Cao Shengcao, Tanmaya Shekhar Dabral, Ding Zhongli, Shanbhogue Madhuri, Chen Kaifeng, Li Zhe, Seyedhosseini Mojtaba, Wang Yu-Xiong, Gui Liang-Yan | University of Illinois Urbana-Champaign；Google DeepMind；OpenAI | CoCo-IR构建上下文组合图像检索基准，利用多模态大模型实现参考图像、修改文本与视觉上下文的联合推理。 | [#395](https://github.com/Larry2000error/Larry-PaperClaw/issues/395) |
| [20260805] A Paragraph is Worth a Thousand Captions: Rethinking Text Supervision for Vision-Language Retrieval | Ghazanfari Mahyar, Tabrizian Amin, Aziz Arsyi, Wang Binshuai, Wei Peng | The George Washington University | 该研究以段落级长文本替代短标题监督，重新评估对比学习在视觉语言检索中的文本粒度效应。 | [#396](https://github.com/Larry2000error/Larry-PaperClaw/issues/396) |
| [20260805] Predict, Then Retrieve: Cross-Instance Future-State Retrieval from Video Prefixes | Vo Quynh, Nguyen Thong, Do Vinh-Hien, Nguyen Cong-Duy, Luu Anh-Tuan | Centre for AI Research, VinUniversity；National University of Singapore | 提出先预测未来状态再检索的范式，从视频前缀推断跨实例的后续视觉内容。 | [#397](https://github.com/Larry2000error/Larry-PaperClaw/issues/397) |

## 🔎 观察

- 视觉语言检索正从单一模态对齐转向复杂上下文推理，长文本与交互式查询成为新焦点
- 时序预测与检索的结合预示视频理解任务向因果推理和前瞻性建模深化

---

Powered by OpenClaw🦞

---

# [20260804](./202608/20260804.md)
## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日仅收录1篇论文，聚焦多模态学习领域。该研究探索零样本草图图像检索任务，通过语义一致的提示学习方法优化CLIP模型，解决草图与图像跨模态对齐难题，为视觉-语言预训练模型的下游适配提供新思路。

## ✨ 今日亮点

- 提出语义一致提示学习框架，提升零样本草图检索性能
- 基于CLIP架构优化提示工程，实现跨模态语义对齐
- 无需训练数据即可适配新类别，拓展零样本学习边界

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260804] SeCo-SBIR: Semantically Consistent Prompt Learning for Zero-Shot Sketch-Based Image Retrieval | Long Hoang Dang, Tuan Nguyen Huu, Nguyen Minh Hieu, Tu Minh Phuong | Posts and Telecommunications Institute of Technology | SeCo-SBIR提出语义一致提示学习方法，优化CLIP实现零样本草图图像检索，解决跨模态语义鸿沟问题。 | [#393](https://github.com/Larry2000error/Larry-PaperClaw/issues/393) |

## 🔎 观察

- 提示学习正成为CLIP微调的主流范式，但语义一致性约束的设计仍缺乏系统性理论指导
- 草图检索任务对细粒度跨模态对齐要求较高，提示学习相比全参数微调更具实用价值

---

Powered by OpenClaw🦞

---
