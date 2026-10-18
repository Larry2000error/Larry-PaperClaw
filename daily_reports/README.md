# Daily Reports

最近三天日报（最新在前）：

# [20261006](./202610/20261006.md)
## 📌 今日概况

今日共检索候选论文 41 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日研究呈现三大趋势：一是视觉-语言模型在检索任务中的高效应用，探索免训练与知识蒸馏路径；二是模型合并与参数优化技术持续演进，提升部署效率；三是垂直领域AI基础设施加速建设，电信行业开源数据集与评测体系首次系统性发布。

## ✨ 今日亮点

- 免训练视频检索新范式：TF-PRVR通过时序分割与多尺度分析实现零样本视频检索
- VLM知识蒸馏深度解析：对比监督信号对视觉文档检索的迁移效果差异
- 电信AI基础设施开源：OTel发布首个大规模电信领域语言模型评测基准与数据集

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261006] TF-PRVR: Training-Free Partially Relevant Video Retrieval | Kim Giyeol, Eom Chanho | Chung-Ang University | TF-PRVR提出免训练部分相关视频检索方法，利用时序分割与多尺度CLIP特征对齐，无需微调即可定位视频片段。 | [#577](https://github.com/Larry2000error/Larry-PaperClaw/issues/577) |
| [20261006] What Transfers from a VLM Teacher? Comparing Supervision Signals for Visual Document Retrieval | Sturua Saba, Xiao Han | Jina AI by Elastic | 研究系统对比VLM教师模型的多种监督信号，发现对比学习结合难负样本挖掘对视觉文档检索蒸馏效果最优。 | [#578](https://github.com/Larry2000error/Larry-PaperClaw/issues/578) |
| [20261006] $α$Transfer: Coefficient Transfer for Efficient Model Merging | Huang Shih-Cheng, Zhi Rui Tam, Lin Chieh-Yen, Chen Yun-Nung, Lee Hung-yi, Sun Shao-Hua | Appier AI Research；National Taiwan University | αTransfer创新系数迁移机制，通过参数算术实现视觉Transformer的高效模型合并与弹性扩展。 | [#579](https://github.com/Larry2000error/Larry-PaperClaw/issues/579) |
| [20261006] OTel: Open Telco AI Datasets, Benchmarks, and Models | Tavakkoli Farbod, Diamos Gregory, Church Kenneth, Paulk Roderic, Terrazas Jorden, Kanter David, Austin Mark, Karim Imtiaz, Syed Ali Raza Zaidi, Bariah Lina, Merouane Abdelkader Debbah, Maatouk Ali, Powell Louis, Vasiloglou Nikolaos, Vaswani Ashish, Singla Somanshu, Chaluvaraju Adarsh | AT&T Chief Data Office；RelationalAI；Northeastern University；MLCommons；The University of Texas at Dallas；University of Leeds；Khalifa University；Yale University；GSMAOct；Essential AI | OTel开源电信AI全栈资源，涵盖多模态数据集、评测基准及专用语言模型，推动通信领域AI标准化。 | [#580](https://github.com/Larry2000error/Larry-PaperClaw/issues/580) |

## 🔎 观察

- 视频检索领域正从'训练密集'向'零样本高效'转型，时序理解成为免训练范式的关键瓶颈。
- 垂直行业大模型基础设施进入密集建设期，电信等关键领域的开源生态将重塑产业AI竞争格局。

---

Powered by OpenClaw🦞

---

# [20261005](./202610/20261005.md)
## 📌 今日概况

今日共检索候选论文 42 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日研究聚焦视觉-语言模型在图像检索与匹配任务中的创新应用。零样本学习、跨视角地理定位与弱监督适应成为核心方向，涵盖遥感、野生动物监测、医学影像等多领域场景，体现多模态大模型向专业化垂直领域渗透的趋势。

## ✨ 今日亮点

- 跨视角地理定位引入语言推理，实现零样本场景下的文本-图像跨模态定位
- 野生动物重识别提出弱监督图像匹配框架，降低相机陷阱数据标注成本
- 神经影像检索系统结合对比学习与变分自编码器，支持全脑及区域特异性MRI检索

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261005] From Transformation to Target State: Rethinking Query Representation for Zero-Shot Composed Image Retrieval | Zhao Yihe, Feng Songhe | School of Computer Science and Technology, Beijing Jiaotong University | 提出目标状态重构范式，通过视觉-语言模型直接预测目标图像表征，优化零样本组合图像检索性能。 | [#553](https://github.com/Larry2000error/Larry-PaperClaw/issues/553) |
| [20261005] WildMatch: Weakly Supervised Image Matcher Adaptation for Wildlife Re-Identification | Turhan Can Kargin, Kubaty Piotr, Rostovskaya Ekaterina, Wierzbowska Izabela, Zieliński Bartosz, Przewięźlikowski Marcin | Faculty of Mathematics and Computer Science, Jagiellonian University；Doctoral School of Exact and Natural Sciences, Jagiellonian University；Jagiellonian Center for Artificial Intelligence；NASK National Research Institute；Institute of Environmental Sciences, Faculty of Biology, Jagiellonian University | WildMatch框架以弱监督方式适配图像匹配器，解决野生动物重识别中相机陷阱图像的标注稀缺问题。 | [#573](https://github.com/Larry2000error/Larry-PaperClaw/issues/573) |
| [20261005] Identity-Conditioned Score Fusion for Open-Set Person Re-Identification | Yao Manyi, Nazarovs Jurijs, Chong Eunji, Sharma Abhishek, Sarkar Rohan, Guo Yue, Christian R. Shelton, Amit K. Roy-Chowdhury, Pal Debashish | University of California, Riverside；Amazon | 设计身份条件化分数融合机制，在开放集场景下提升换衣行人重识别的判别鲁棒性。 | [#574](https://github.com/Larry2000error/Larry-PaperClaw/issues/574) |
| [20261005] What Words Keep of a Place: Zero-Shot Language Reasoning for Cross-View Geo-Localization | Ayesh Abu Lehyeh, Jay Hwasung Jung, Wshah Safwan | Department of Computer Science, University of Vermont | 利用多模态大语言模型提取地点语义描述，实现跨视角地理定位的零样本语言推理。 | [#575](https://github.com/Larry2000error/Larry-PaperClaw/issues/575) |
| [20261005] NeuroCBIR: A Fast and Accurate Image Retrieval System for Whole-Brain and Region-Specific MRI | Nieto-del-Amor Felix, Fu Jingru, J. -Sebastian Muehlboeck, Westman Eric, Ferreira Daniel, Moreno Rodrigo | Institution unavailable | NeuroCBIR系统整合对比学习与变分自编码器，为MRI影像提供快速精准的内容检索能力。 | [#576](https://github.com/Larry2000error/Larry-PaperClaw/issues/576) |

## 🔎 观察

- 视觉-语言模型正从通用理解向专业检索任务深化，零样本范式显著降低领域适配成本
- 遥感与生态监测领域涌现弱监督与开放集解决方案，反映真实场景对低标注依赖技术的迫切需求

---

Powered by OpenClaw🦞

---

# [20261004](./202610/20261004.md)
## 📌 今日概况

今日共检索候选论文 28 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 6 篇。

今日研究聚焦于多模态智能系统的交互与检索能力优化。跨模态表征学习持续深化，涵盖推荐系统、医学病理与红外目标检测等垂直领域。Agentic AI架构成为新热点，强调动态交互与自主决策能力。边缘部署与隐私安全议题亦受关注，体现技术落地与伦理并重的趋势。

## ✨ 今日亮点

- 视觉-语言统一表征首次系统应用于多模态推荐场景，突破传统协同过滤瓶颈
- Agentic架构引入红外小目标检测，通过变焦引导交互实现动态视觉搜索
- 跨模态对比学习打通病理图像与免疫治疗分子标志物检索链路

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261004] OpticalRec: Unified Optical Vision-Language Representation for Multimodal Recommendation | Wang Yueqi, Guo Zitian, Hou Yupeng, Wang Yifei, Kim Kibum, Yue Zhenrui, Xing Shuo, Li Haodong, Xia Heming, Zhang Renrui, Tu Zhengzhong, McAuley Julian | University of California, San Diego；Alibaba Group；University of Illinois Urbana-Champaign；The Hong Kong Polytechnic University；The Chinese University of Hong Kong；Texas A&M University | 提出OpticalRec框架，以统一光学视觉-语言表征融合多模态推荐中的视觉语义与协同信号。 | [#546](https://github.com/Larry2000error/Larry-PaperClaw/issues/546) |
| [20261004] IRSTD-Agent: Agentic Infrared Small Target Detection via Zoom-Guided Interaction Learning | Xi Jiawen, Zhang Yu, Zhao Tianyi, Liu Zhu, Yuan Maoxun, Wei Xingxing | Beihang University；Dalian University of Technology | IRSTD-Agent构建智能体驱动的红外小目标检测系统，通过变焦引导交互学习实现自适应视觉搜索。 | [#547](https://github.com/Larry2000error/Larry-PaperClaw/issues/547) |
| [20261004] Cross-Modal Contrastive Learning for the Retrieval of Immunotherapy-Associated Molecular Signatures from Histopathology | Vila-Bagaria Sigrid, Teixidó Mar, Piñol Miquel, Vilardell Felip, Montal Robert, Vilaplana Veronica | Universitat Politècnica de Catalunya - BarcelonaTech (UPC)；IRB Lleida | 开发跨模态对比学习框架，从组织病理学图像中检索免疫治疗相关分子特征。 | [#548](https://github.com/Larry2000error/Larry-PaperClaw/issues/548) |
| [20261004] An Edge-First Multimodal Asset Management Studio and Retrieval Engine for Heterogeneous AI-Generated Media | Lin Chaoyu | Independent Researcher | 设计边缘优先的多模态资产管理与检索引擎，面向异构AI生成媒体的元数据提取与高效管理。 | [#570](https://github.com/Larry2000error/Larry-PaperClaw/issues/570) |
| [20261004] AgentDoxx: Agentic Re-identification of Anonymized Text with Web Search | Wen Jianing, Li Tianshi | Khoury College of Computer Sciences, Northeastern University | AgentDoxx揭示大模型结合网络搜索可对匿名化文本进行智能体重识别，凸显隐私风险。 | [#571](https://github.com/Larry2000error/Larry-PaperClaw/issues/571) |
| [20261004] When Does Retrieval Help? A Study of In-Context Adaptation in Vision-Language-Action Models | Liu Zixuan, Köster Joris, Zheng Zizhan, Khajavi Siavash | Tulane University；Aalto University | 系统研究检索增强在视觉-语言-动作模型中的上下文适应机制，明确检索生效的关键条件。 | [#572](https://github.com/Larry2000error/Larry-PaperClaw/issues/572) |

## 🔎 观察

- Agentic AI正从通用对话向专用视觉任务渗透，交互式学习成为提升复杂场景感知的新范式
- 跨模态检索技术加速向医疗、安防等高价值领域迁移，但隐私泄露风险同步放大需警惕

---

Powered by OpenClaw🦞

---
