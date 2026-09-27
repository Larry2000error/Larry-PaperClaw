# Daily Reports

最近三天日报（最新在前）：

# [20260923](./202609/20260923.md)
## 📌 今日概况

今日共检索候选论文 13 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日仅收录1篇论文，聚焦多目标跟踪领域。研究将SAM2与生命周期感知记忆机制结合，解决视频分割中轨迹初始化与长期鲁棒性问题，体现视觉基础模型在时序任务中的深化应用趋势。

## ✨ 今日亮点

- SAM2引入生命周期感知记忆，增强视频分割时序一致性
- 针对多目标跟踪中轨迹初始化难题提出新机制
- 丰田欧洲团队推动自动驾驶感知算法创新

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260923] LiAM-SAM: Lifecycle-Aware Memory for Robust SAM2-Based MOT | Francisco Grégoire, D'Amico Alessandro, Costantini Samuele, Francesca Gianpiero, Garattoni Lorenzo | Toyota Motor Europe | LiAM-SAM提出生命周期感知记忆机制，使SAM2在多目标跟踪中实现更鲁棒的轨迹初始化和长期分割稳定性。 | [#510](https://github.com/Larry2000error/Larry-PaperClaw/issues/510) |

## 🔎 观察

- 单一论文收录量反映该日期可能为节假日或会议间歇期，需关注后续集中发布。
- SAM2生态持续扩展，工业界（丰田）主导优化表明该技术正从学术原型向自动驾驶实用化演进。

---

Powered by OpenClaw🦞

---

# [20260915](./202609/20260915.md)
## 📌 今日概况

今日共检索候选论文 0 篇；关键词+LLM 智能匹配遥感交叉论文 0 篇；最终纳入日报 2 篇。

今日研究聚焦多模态大模型的跨模态对齐与检索能力优化。两项工作分别从区域级细粒度检索和统一一维token表示两个角度切入，探索提升多模态模型在检索与生成任务中的性能，体现了向更灵活、更精准的多模态交互发展的趋势。

## ✨ 今日亮点

- RegRet提出区域级检索新范式，增强大模型对图像局部区域的精准定位与理解能力
- FLAT创新性地将图文重采样为一维可变长对齐token，统一检索与生成架构
- 两项工作均来自产业界与学术界合作，显示多模态技术正加速向实用化落地

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260915] RegRet: Enhancing Region-Level Retrieval in Large Multimodal Models | Liang Xun, Yang Honghui, Pan Weihang, Zhao Ruisi, Pan Boyuan, Hu Yao, Wang Wenxiao, Lin Binbin, Cai Deng | State Key Lab of CAD&CG, Zhejiang University；Xiaohongshu Inc.；School of Software Technology, Zhejiang University | RegRet通过区域感知编码器与对比学习，提升大多模态模型在区域级检索任务中的细粒度定位能力。 | [#507](https://github.com/Larry2000error/Larry-PaperClaw/issues/507) |
| [20260915] FLAT: Resampling Image and Text into 1D Flexible-Length Aligned Transmodal Tokens for Retrieval and Generation | Sun Guangyu, Shlok Kumar Mishra, Bao Wentao, Robert Zhenheng Yang, Wang Xiao, Wang Xiyuan, Ma Yujunrong, Yuan Chen, Max Xiangjun Fan, Xiao Jun, Cheng Jianpeng | Meta AI | FLAT将图像与文本重采样为一维灵活长度对齐token，实现跨模态检索与生成的统一表示框架。 | [#508](https://github.com/Larry2000error/Larry-PaperClaw/issues/508) |

## 🔎 观察

- 区域级细粒度理解正成为多模态大模型的新竞争点，超越全局表征的局限
- 一维token化趋势显现，或推动多模态架构向更简洁、更通用的方向演进

---

Powered by OpenClaw🦞

---

# [20260914](./202609/20260914.md)
## 📌 今日概况

今日共检索候选论文 0 篇；关键词+LLM 智能匹配遥感交叉论文 0 篇；最终纳入日报 4 篇。

今日研究聚焦多模态检索与智能文档理解两大方向。检索领域涌现球面质心聚合与超图正则化等新方法，强调查询条件化与嵌入优化；文档理解则探索Agentic视觉RAG，通过显式证据选择提升稀疏场景下的生成可靠性。语言评估方面关注低资源语言基准的有效性边界。

## ✨ 今日亮点

- Agentic视觉RAG新范式：显式上下文选择与整合机制应对稀疏证据挑战
- 球面质心聚合：查询条件化的多模态检索方法，支持动态模态权重学习
- 超图正则化Gramian体积：利用高阶结构约束优化跨模态嵌入空间

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260914] Navigating Sparse Evidence: Agentic Visual RAG via Explicit Context Selection and Consolidation | Shen Yucheng, Yan Lingyong, Wu Jiulong, Wang Shuaiqiang, WU Jianmin, Yin Dawei, Cao Min | School of Computer Science and Technology, Soochow University；Baidu Inc. | 提出Agentic视觉RAG框架，通过显式证据选择与上下文整合机制，解决文档理解中证据稀疏导致的检索增强生成可靠性问题。 | [#502](https://github.com/Larry2000error/Larry-PaperClaw/issues/502) |
| [20260914] Turkish MMLU Pro: Traceable Option Augmentation and Its Validity Limits in Turkish Multiple-Choice Evaluation | M. Ali Bayram | Yıldız Technical University | 构建土耳其语MMLU Pro基准，系统研究选项增强技术的有效性边界，揭示多选题评估中答案可溯源性的关键局限。 | [#503](https://github.com/Larry2000error/Larry-PaperClaw/issues/503) |
| [20260914] Query-Conditioned Spherical Centroid Aggregation for Multimodal Retrieval | Mehrish Ambuj, Nag Anindya, Vascon Sebastiano | Ca' Foscari University of Venice | 设计查询条件化球面质心聚合方法，结合LoRA适配器实现模态权重动态学习，提升多模态检索的查询适应性。 | [#504](https://github.com/Larry2000error/Larry-PaperClaw/issues/504) |
| [20260914] Hypergraph-Regularized Gramian Volumes for Multimodal Retrieval | Nag Anindya, Mehrish Ambuj, Vascon Sebastiano | Ca' Foscari University of Venice | 引入超图正则化Gramian体积损失，通过高阶结构关系约束嵌入空间几何，增强跨模态检索的判别性与鲁棒性。 | [#505](https://github.com/Larry2000error/Larry-PaperClaw/issues/505) |

## 🔎 观察

- 多模态检索正从简单对齐向几何感知、结构约束的精细嵌入优化演进，球面空间与高阶图结构成为新工具。
- RAG系统研究重心从检索规模转向证据质量，显式选择与整合机制反映领域对可解释性与可靠性的迫切需求。

---

Powered by OpenClaw🦞

---
