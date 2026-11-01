# Daily Reports

最近三天日报（最新在前）：

# [20261016](./202610/20261016.md)
## 📌 今日概况

今日共检索候选论文 32 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究聚焦多模态大语言模型在视频理解与检索中的应用，以及多模态表征学习的精细化设计。MLLM在视频问答与搜索重排序任务中展现潜力，同时正交解耦的共享-特定表征方法为跨模态目标重识别提供了新思路。

## ✨ 今日亮点

- MLLM子集集成策略提升音视频问答性能，重排序优化视频搜索效果
- 正交解耦网络分离模态共享与特有表征，增强多模态目标重识别能力
- 跨模态对齐与特征解耦技术持续演进，推动多模态表征学习精细化

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261016] MLLM Frame Subset Ensembling for Audio-Visual Video QA and MLLM-based Reranking for Ad-hoc Video Search in TRECVID 2025 | Goulas Andreas, Galanopoulos Damianos, Patras Ioannis, Mezaris Vasileios | Information Technologies Institute (ITI), Centre of Research and Technology Hellas (CERTH)；Queen Mary University of London | 该研究提出MLLM帧子集集成方法用于音视频问答，并设计基于MLLM的重排序机制优化特定视频搜索任务。 | [#632](https://github.com/Larry2000error/Larry-PaperClaw/issues/632) |
| [20261016] ODSS-Net: Orthogonally Decoupled Shared-Specific Representations for Multi-Modal Object Re-Identification | Ma Zhifeng, Feng Yuhong, Huang Chongyi, Zhou Mingyang, Deng Minwen | College of Computer Science and Software Engineering, Shenzhen University；Tencent | ODSS-Net通过正交投影将多模态特征解耦为共享与模态特有表征，提升多模态目标重识别性能。 | [#633](https://github.com/Larry2000error/Larry-PaperClaw/issues/633) |

## 🔎 观察

- 多模态大模型正从通用理解向特定视频任务（搜索、问答）的精细化适配演进
- 特征解耦与正交约束成为跨模态表征学习的重要技术路线，兼顾共享性与判别性

---

Powered by OpenClaw🦞

---

# [20261015](./202610/20261015.md)
## 📌 今日概况

今日共检索候选论文 43 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日研究聚焦于视觉检索效率与多模态理解两大主线。CertEx提出可认证排除机制实现精确kNN检索加速；病理基础模型探索零训练肿瘤病例检索；DINOv3向3D几何理解延伸；视频生成领域则通过稀疏注意力优化扩散Transformer效率。

## ✨ 今日亮点

- CertEx以可认证排除实现大规模精确视觉检索，兼顾精度与GPU加速
- 病理基础模型首次实现唾液腺肿瘤零训练病例检索，助力罕见癌诊断
- DINOv3引入自监督几何感知，突破部分3D形状匹配瓶颈

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261015] CertEx: Exact Visual Retrieval at Scale by Certified Exclusion | Zhao Dongfang | Tacoma School of Engineering & Technology and eScience Institute；University of Washington | CertEx提出可认证排除框架，通过GPU加速近似索引实现精确kNN检索，解决大规模视觉检索中精度与效率的权衡难题。 | [#612](https://github.com/Larry2000error/Larry-PaperClaw/issues/612) |
| [20261015] Stuck on Shuffle: On Attribute-Object Binding in Vision-Language Models | Netanel Y. Tamir, Green Michael, Tzachor Issar, Shimshi Or, Samuel Dvir, Patashnik Or, Ben-Ari Rami | OriginAI；NVIDIA；Tel Aviv University | 研究揭示视觉语言模型在属性-对象绑定任务中存在系统性缺陷，提出新基准测试评估组合理解能力。 | [#628](https://github.com/Larry2000error/Larry-PaperClaw/issues/628) |
| [20261015] Pathology foundation models for training-free case retrieval in salivary gland tumors | Maximilian J. Roesel, Kiermeyer Niklas, Keyl Philipp, Klauschen Frederick | Institute of Pathology, Ludwig-Maximilians-Universität München；German Cancer Consortium (DKTK), German Cancer Research Center (DKFZ), Munich partner site；Institute of Pathology, Charité-Universitätsmedizin Berlin；BIFOLD-Berlin Institute for the Foundations of Learning and Data | 基于病理基础模型的零训练检索方法，可直接应用于唾液腺肿瘤全切片图像的相似病例检索。 | [#629](https://github.com/Larry2000error/Larry-PaperClaw/issues/629) |
| [20261015] Teaching DINOv3 About Partial 3D Geometry: A Self-Supervised Geometry-Aware Approach | Ehm Viktoria, Cao Dongliang, Marin Riccardo, Scholz Daniel, Wang Weikang, Bernard Florian, Cremers Daniel | Technical University of Munich；Munich Center for Machine Learning；University of Bonn | 通过LoRA微调与自监督几何感知策略，赋予DINOv3部分3D形状匹配能力，无需3D标注数据。 | [#630](https://github.com/Larry2000error/Larry-PaperClaw/issues/630) |
| [20261015] Sparse Attention for Video Generation Acceleration via Growing Sparsity and Reduced Search | Dai Yun, Chen Yuyun, Wen Jiarui, Zhuang Huiping, Chen Cen, Zeng Ziqian | South China University of Technology | 提出渐进稀疏注意力机制，通过动态增长稀疏性与减少搜索开销加速视频扩散Transformer生成。 | [#631](https://github.com/Larry2000error/Larry-PaperClaw/issues/631) |

## 🔎 观察

- 视觉基础模型正从通用表征向垂直领域（病理诊断、3D几何）深度渗透，零训练或少训练迁移成为新范式
- 检索任务呈现两极分化：既追求CertEx的精确性保障，又探索病理领域的语义相似性，反映应用场景对确定性的差异化需求

---

Powered by OpenClaw🦞

---

# [20261014](./202610/20261014.md)
## 📌 今日概况

今日共检索候选论文 33 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日研究聚焦多模态智能体与机器人学习，涵盖视觉-语言-动作统一嵌入、多模态知识图谱构建及上下文学习优化。强化学习与知识蒸馏成为提升智能体推理能力的关键技术路径，跨机构合作特征显著。

## ✨ 今日亮点

- Robota-Embed提出统一VLA嵌入框架，实现机器人上下文学习与进化
- ActICL探索后训练优化策略，提升多模态智能体上下文学习能力
- MMKG-R1以强化学习驱动多模态知识图谱自动构建

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261014] Robota-Embed: Unified VLA Embeddings for Robot In-Context Learning and Evolution | Liu Yunze, Wang Jing, Wu Shenrui, He Wenkun, Zhan Guanqi, Ma Xianzheng, Chen Junyu, Ge Wenhang, Tang Haozhan, Gu Yuchao, Zhang Zhuoyang, Wang Zekai, Niu Dantong, Dong Zhen, Zhu Yuke, Darrell Trevor, Linxi "Jim" Fan, Han Song, Cai Han | NVIDIA；MIT；UCB；Oxford；CMU | NVIDIA等提出Robota-Embed统一嵌入模型，将视觉-语言-动作映射至共享空间，支持机器人上下文学习与跨任务迁移。 | [#623](https://github.com/Larry2000error/Larry-PaperClaw/issues/623) |
| [20261014] ActICL: Post-Training for Agentic Multimodal In-Context Learning | Li Yanshu, Tang Ruixiang, Junyi Jessy Li, Stengel-Eskin Elias | University of Texas at Austin；Rutgers University | UT Austin等提出ActICL后训练框架，通过智能体检索与工具增强推理优化多模态上下文学习中的示例选择策略。 | [#624](https://github.com/Larry2000error/Larry-PaperClaw/issues/624) |
| [20261014] MMKG-R1: Constructing Multimodal Knowledge Graphs via Reinforcement Learning | Wu Zongyu, Wang Yilong, Wang Xiaochen, Lin Minhua, Zhong Yuan, Ma Fenglong, Zhang Xiang, Wang Suhang | The Pennsylvania State University | Penn State提出MMKG-R1方法，以强化学习自动化构建多模态知识图谱，提升图检索增强生成质量。 | [#625](https://github.com/Larry2000error/Larry-PaperClaw/issues/625) |
| [20261014] Information-Gain Calibrated On-Policy Distillation for Deep Search Agents | Li Chenxi, Feng Xueyang, Liu Songyang, Wang Chenxu, Tang Xiaoying, Li Chaozhuo, Zhang Litian | The Chinese University of Hong Kong, Shenzhen；Renmin University of China；Beijing University of Posts and Telecommunications；Beijing Academy of Artificial Intelligence (BAAI) | 港中深等提出信息增益校准的在线策略蒸馏方法，解决深度搜索智能体中证据盲监督导致的知识迁移低效问题。 | [#626](https://github.com/Larry2000error/Larry-PaperClaw/issues/626) |

## 🔎 观察

- 上下文学习正从NLP向机器人与智能体领域深度渗透，VLA统一表征成为关键瓶颈
- 强化学习在知识图谱构建中的应用显示结构化知识获取正从人工设计转向自动化生成

---

Powered by OpenClaw🦞

---
