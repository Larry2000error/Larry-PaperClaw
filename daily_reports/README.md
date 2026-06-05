# Daily Reports

最近三天日报（最新在前）：

# [20260529](./202605/20260529.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦多模态大模型的空间推理与地理定位能力，涵盖具身智能基准测试、持续学习检索及密集城市场景视觉定位。学界正推动MLLM从分类任务向动态推理与真实环境适应演进，同时关注GPS拒止条件下的鲁棒定位方案。

## ✨ 今日亮点

- ERGeoBench构建具身推理与地理定位综合评测体系，填补MLLM空间认知能力评估空白
- 动态适配器路由机制解决多模态检索中的持续学习难题，实现任务自适应模型融合
- 中国城中村案例验证视觉定位在密集城市环境的可行性，为GPS拒止导航提供新思路

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260529] ERGeoBench:A Comprehensive Benchmark for Embodied Reasoning and Geo-localization in Multimodal Large Language Models | Xue Kaiwen, Wei Tao, Zhang Guoxin, Ou Zhonghong, Lu Kaoyan, Feng Yu, Zhu Yifan, Luo Haoran | Institution unavailable | ERGeoBench建立多模态大模型具身推理与地理定位基准，系统评估视觉感知与空间推理能力。 | [#226](https://github.com/Larry2000error/Larry-PaperClaw/issues/226) |
| [20260602] Beyond Classification: Dynamic Adapter Routing for Continual Multimodal Retrieval | Dobrzeniecka Alicja, Szatkowski Filip, Cygert Sebastian, Łukasik Szymon, Twardowski Bartłomiej | NASK National Research Institute；IDEAS Research Institute；Warsaw University of Technology；Universitat Autonoma de Barcelona | 提出动态适配器路由方法，通过任务特定适配器选择与模型合并实现持续多模态检索。 | [#227](https://github.com/Larry2000error/Larry-PaperClaw/issues/227) |
| [20260602] Vision-Based Localization in Dense Urban Environments: A Case Study of an Urban Village in China | Wu Menglin, Cao Rui | The Hong Kong University of Science and Technology (Guangzhou) | 以中国城中村为案例，验证全景视觉定位在密集城市GPS拒止环境中的有效性。 | [#229](https://github.com/Larry2000error/Larry-PaperClaw/issues/229) |

## 🔎 观察

- 具身智能与地理定位交叉成为新热点，但现有MLLM空间推理能力缺乏标准化评测，ERGeoBench或推动该领域规范化发展
- 持续学习与模型合并技术向多模态检索渗透，动态路由机制可能缓解视觉-语言模型任务增量时的灾难性遗忘问题

---

Powered by OpenClaw🦞

---

# [20260528](./202605/20260528.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 0 篇；最终纳入日报 4 篇。

今日研究聚焦多模态检索与智能体推理两大方向。单向量模型通过晚期交互实现多向量级性能，SAM3特征融合推动零样本第一人称视频理解，而检索增强的智能体框架则为图像地理定位引入证据验证机制。数据集构建与跨域一致性亦受关注。

## ✨ 今日亮点

- 单向量嵌入模型通过晚期交互策略逼近多向量检索性能，降低部署成本
- SAM3多阶段特征融合实现厨房场景零样本物体重识别，无需标注训练
- REVERSE框架以多轮证据验证强化智能体图像地理定位的可解释性

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260528] Your Embedding Model is SMARTer Than You Think | Zhang Jianrui, Hyun Jung Lee, Ganguly Sukanta, Kam Tae-Eui, Kim Donghyun, Yong Jae Lee | UW-Madison；Korea University；NetApp, Inc. | 提出SMART方法，以单向量模型实现晚期交互，在保持效率的同时达到多向量检索精度。 | [#220](https://github.com/Larry2000error/Larry-PaperClaw/issues/220) |
| [20260528] Zero-Shot Object Re-Identification in Egocentric Kitchen Videos via Multi-Stage SAM3 Feature Fusion | Klepachevskyi Dmytro, Wong Alexander, Rambhatla Sirisha, Chen Yuhao | University of Waterloo | 利用SAM3分割模型的多阶段特征融合，解决第一人称厨房视频中零样本物体重识别难题。 | [#221](https://github.com/Larry2000error/Larry-PaperClaw/issues/221) |
| [20260528] REVERSE: Reinforcing Evidence Verification and Search for Agentic Image geo-localization | Li Yong, Jia Furong, Yin Dacheng, Rong Kang, Rao Fengyun, LYU Jing, Zhang Fan | Peking University；The Hong Kong University of Science and Technology；WeChat Vision, Tencent Inc | 构建REVERSE智能体框架，通过多轮证据检索与验证提升图像地理定位的准确性与可靠性。 | [#222](https://github.com/Larry2000error/Larry-PaperClaw/issues/222) |
| [20260528] CIRCLED: A Multi-turn CIR Dataset with Consistent Dialogues across Domains | Takeda Tomohisa, Lin Yu-Chieh, Nozawa Yuji, Ng Youyang, Torii Osamu, Matsui Yusuke | Graduate School of Information Science and Technology, The University of Tokyo；Kioxia Corporation | 发布CIRCLED多轮组合图像检索数据集，确保时尚等跨域对话的一致性与连贯性。 | [#223](https://github.com/Larry2000error/Larry-PaperClaw/issues/223) |

## 🔎 观察

- 晚期交互与单向量模型的结合可能成为检索系统轻量化部署的新范式，平衡精度与效率。
- SAM系列模型正从分割工具向通用视觉特征提取器演进，跨任务迁移价值持续显现。

---

Powered by OpenClaw🦞

---

# [20260523](./202605/20260523.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦组合图像检索（CIR）技术，涵盖不确定性量化与地球观测应用两大方向。清华团队引入共形预测解决检索歧义问题，希腊-捷克联合团队则首次系统评估CIR在卫星影像中的实际表现，推动视觉语言模型向遥感专用场景落地。

## ✨ 今日亮点

- 共形预测校准交互不确定性，提升零样本组合图像检索可靠性
- 首份遥感CIR基准测试揭示视觉语言模型在卫星影像应用中的性能差距
- 多机构跨国合作推动组合检索技术从通用视觉向地球观测迁移

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260523] Resolving Ambiguity in Composed Image Retrieval via Calibrated Interaction | Tran Amsisan, Le Baogh, Tuan Kiet Pham, Sui Yang Guang | Tsinghua University；Chinese Academy of Sciences | 提出基于共形预测的校准交互框架，通过量化不确定性解决组合图像检索中的意图歧义问题。 | [#217](https://github.com/Larry2000error/Larry-PaperClaw/issues/217) |
| [20260523] Benchmarking Composed Image Retrieval for Applied Earth Observation | Psomas Bill, Christopoulos Dionysis, Petropoulos Thanasis, Efthymiadis Nikos, Kakogeorgiou Ioannis, Chum Ondřej, Avrithis Yannis, Tolias Giorgos, Karantzalos Konstantinos | Visual Recognition Group, Department of Cybernetics, Czech Technical University in Prague；Remote Sensing Laboratory, School of Rural, Surveying and Geoinformatics Engineering, National Technical University of Athens；Institute of Informatics & Telecommunications, National Centre for Scientific Research "Demokritos"；Department of Informatics and Telecommunications, National and Kapodistrian University of Athens | 构建首个面向地球观测的组合图像检索基准，系统评估CLIP等视觉语言模型在卫星影像检索任务中的适用性。 | [#218](https://github.com/Larry2000error/Larry-PaperClaw/issues/218) |

## 🔎 观察

- 组合图像检索正从通用视觉向垂直领域渗透，遥感场景的特殊性（如光谱特征、地理尺度）对现有VLMs构成挑战
- 不确定性量化方法（如共形预测）与检索任务的结合，反映出社区对模型可靠性而非单纯精度的关注转向

---

Powered by OpenClaw🦞

---
