# Daily Reports

最近三天日报（最新在前）：

# [20260512](./202605/20260512.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦多模态模型的鲁棒性与泛化能力。三篇论文分别针对视觉语言模型的持续学习、跨视角地理定位的天气鲁棒性，以及多图像检索中的位置偏置问题，体现出遥感与视觉AI领域对真实场景适应性的高度关注。

## ✨ 今日亮点

- 提出增强型EWC方法，实现视觉语言模型的跨模态知识保持与终身学习
- 基于原型学习的语义部件发现，提升跨视角地理定位的天气鲁棒性
- 设计Logit-注意力散度校准机制，缓解多图像检索中的位置偏置

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260512] Lifelong Learning in Vision-Language Models: Enhanced EWC with Cross-Modal Knowledge Retention | Hamza Ahmed Durrani, Rafay Suleman Durrani | Sejong University；Technische Universität Ilmenau | 提出增强弹性权重整合方法，通过跨模态知识保持机制缓解视觉语言模型持续学习中的灾难性遗忘问题。 | [#191](https://github.com/Larry2000error/Larry-PaperClaw/issues/191) |
| [20260512] Weather-Robust Cross-View Geo-Localization via Prototype-Based Semantic Part Discovery | Tran Chi-Nguyen, Dao Sy Duy Minh, Huynh Trung Kiet, Nguyen Lam Phu Quy, Pham Phu-Hoa, Tran-Thanh Long | University of Warwick | 基于原型学习与语义部件发现，构建天气鲁棒的跨视角地理定位框架，提升恶劣天气条件下的定位精度。 | [#192](https://github.com/Larry2000error/Larry-PaperClaw/issues/192) |
| [20260512] Logit-Attention Divergence: Mitigating Position Bias in Multi-Image Retrieval via Attention-Guided Calibration | Xian Mingtao, Yang Yifeng, Gu Qinying, Wang Xinbing, Ye Nanyang | Tsinghua University；Chinese Academy of Sciences | 揭示多图像检索中的位置偏置现象，提出Logit-注意力散度校准方法，通过注意力引导优化检索排序。 | [#193](https://github.com/Larry2000error/Larry-PaperClaw/issues/193) |

## 🔎 观察

- 跨模态对齐与鲁棒性成为核心议题，三篇论文均涉及模态间交互机制的优化设计
- 注意力机制的分析与干预持续受到关注，从可解释性角度切入解决实际任务偏置

---

Powered by OpenClaw🦞

---

# [20260511](./202605/20260511.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究聚焦视觉基础模型在跨视角地理定位与图像检索中的高效适配。西电团队主导两项工作，分别探索DINOv2参数高效微调与超网络动态风格调制；昆士兰大学团队则关注生成式外观先验的无监督细粒度检索，整体呈现基础模型轻量化适配与生成式表征学习的双重趋势。

## ✨ 今日亮点

- BGG提出DINOv2参数高效适配框架，弥合跨视角图像几何差异
- HYSTAR以超网络驱动动态SVD调制，实现风格自适应图像检索
- 生成式外观先验对齐方法推进无监督细粒度图像检索性能

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260511] BGG: Bridging the Geometric Gap between Cross-View images by Vision Foundation Model Adaptation for Geo-Localization | Wang Wei, Quan Dou, Huyan Ning, Wang Shuang, Li Yi, He Pei, Jiao Licheng | Xidian University | BGG通过适配DINOv2并设计多粒度特征增强模块，以参数高效方式解决跨视角地理定位中的几何差距问题。 | [#187](https://github.com/Larry2000error/Larry-PaperClaw/issues/187) |
| [20260513] HYSTAR: HYPERNETWORK-DRIVEN STYLE-ADAPTIVE RETRIEVAL VIA DYNAMIC SVD MODULATION | Cai Yujia, Li Boxuan, Xu Chenghao, Yan Jiexi | School of Computer Science and Technology, Xidian University；School of Electronic Engineering, Xidian University | HYSTAR利用超网络预测动态SVD调制参数，使视觉-语言模型能够自适应不同风格，提升图像检索泛化能力。 | [#188](https://github.com/Larry2000error/Larry-PaperClaw/issues/188) |
| [20260511] Learning to Align Generative Appearance Priors for Fine-grained Image Retrieval | Wang Shijie, Luo Yadan, Wang Zijian, Yu Xin, Huang Zi | The University of Queensland；The University of Adelaide | 该方法通过归一化流学习生成式外观先验，并在无监督设定下对齐先验分布以实现细粒度图像检索。 | [#189](https://github.com/Larry2000error/Larry-PaperClaw/issues/189) |

## 🔎 观察

- 西电大学单日贡献两篇论文，显示其在视觉基础模型适配领域的集中布局与技术积累优势。
- 参数高效微调与超网络动态调制成为当前平衡模型性能与计算成本的主流技术路径。

---

Powered by OpenClaw🦞

---

# [20260507](./202605/20260507.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI领域聚焦智能视觉识别技术，两篇论文分别针对遮挡行人重识别与文本-图像车辆检索任务，核心趋势为细粒度特征学习与跨模态对齐，通过动态掩码学习和部件级感知提升复杂场景下的检索鲁棒性。

## ✨ 今日亮点

- DPM++提出动态掩码度量学习，解决遮挡行人重识别中的特征对齐难题
- T2I-VeRW实现部件级细粒度感知，推动文本到图像车辆检索精度提升
- 两篇工作均强调局部特征与全局语义的联合建模，反映当前研究热点

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260507] DPM++: Dynamic Masked Metric Learning for Occluded Person Re-identification | Tan Lei, Luan Yingshi, Zou Pincong, Dai Pingyang, Cao Liujuan | Institution unavailable | DPM++通过动态掩码度量学习策略，有效缓解遮挡干扰，提升行人重识别在复杂场景下的准确性。 | [#184](https://github.com/Larry2000error/Larry-PaperClaw/issues/184) |
| [20260507] T2I-VeRW: Part-level Fine-grained Perception for Text-to-Image Vehicle Retrieval | Wang Xiao, Wang Ziwen, Kong Weizhe, Wu Wentao, Li Yuehang, Zheng Aihua, Li Chenglong, Tang Jin | Institution unavailable | T2I-VeRW构建部件级细粒度跨模态对齐框架，实现文本描述与车辆图像的精准检索匹配。 | [#185](https://github.com/Larry2000error/Larry-PaperClaw/issues/185) |

## 🔎 观察

- 遮挡处理与细粒度感知成为视觉检索的关键技术方向，局部特征学习的重要性持续凸显
- 跨模态检索任务从粗粒度向部件级演进，对多源数据对齐精度提出更高要求

---

Powered by OpenClaw🦞

---
