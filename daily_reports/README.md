# Daily Reports

最近三天日报（最新在前）：

# [20260513](./202605/20260513.md)
## 📌 今日概况

今日共检索候选论文 2 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日仅收录1篇论文，聚焦图像检索领域的新挑战——上下文依赖语义理解。该研究由东京都立大学与CyberAgent合作完成，探索如何让图像检索系统理解同一图像在不同叙事语境中的差异化语义，代表了多模态表征学习向更高层次语义抽象演进的方向。

## ✨ 今日亮点

- 突破传统图像检索的静态语义假设，引入动态语境建模
- 探索叙事上下文对图像语义表征的重塑机制
- 推动多模态嵌入向情境感知型语义理解升级

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260513] Same Image, Different Meanings: Toward Retrieval of Context-Dependent Meanings | Tsutsumi Ayuto, Kohita Ryosuke | Tokyo Metropolitan University；CyberAgent | 该研究提出上下文依赖的图像检索框架，使同一图像能根据叙事语境生成差异化语义表征，突破传统检索中语义静态固定的局限。 | [#195](https://github.com/Larry2000error/Larry-PaperClaw/issues/195) |

## 🔎 观察

- 单篇收录反映该方向尚处早期探索阶段，但语义动态化是检索技术的重要演进方向
- 产学研合作模式（高校+CyberAgent）显示该研究具备较强的应用转化潜力

---

Powered by OpenClaw🦞

---

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

今日研究聚焦视觉基础模型在跨域图像任务中的适配与检索应用。西电团队主导两项工作：跨视角地理定位的几何差距弥合，以及超网络驱动的风格自适应检索；昆士兰大学团队则探索生成式外观先验在细粒度检索中的对齐学习。整体趋势显示参数高效适应与动态特征调制成为关键技术方向。

## ✨ 今日亮点

- BGG利用DINOv2适配实现跨视角地理定位的几何对齐，采用多粒度特征增强策略
- HYSTAR提出超网络驱动的SVD动态调制机制，解决图像检索中的风格适应难题
- 生成式外观先验结合标准化流，为无监督细粒度图像检索提供新范式

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260511] BGG: Bridging the Geometric Gap between Cross-View images by Vision Foundation Model Adaptation for Geo-Localization | Wang Wei, Quan Dou, Huyan Ning, Wang Shuang, Li Yi, He Pei, Jiao Licheng | Xidian University | BGG通过视觉基础模型参数高效适配，弥合跨视角图像几何差距以提升地理定位精度。 | [#187](https://github.com/Larry2000error/Larry-PaperClaw/issues/187) |
| [20260513] HYSTAR: HYPERNETWORK-DRIVEN STYLE-ADAPTIVE RETRIEVAL VIA DYNAMIC SVD MODULATION | Cai Yujia, Li Boxuan, Xu Chenghao, Yan Jiexi | School of Computer Science and Technology, Xidian University；School of Electronic Engineering, Xidian University | HYSTAR以超网络驱动奇异值分解动态调制，实现视觉-语言模型在风格变化场景下的自适应检索。 | [#188](https://github.com/Larry2000error/Larry-PaperClaw/issues/188) |
| [20260511] Learning to Align Generative Appearance Priors for Fine-grained Image Retrieval | Wang Shijie, Luo Yadan, Wang Zijian, Yu Xin, Huang Zi | The University of Queensland；The University of Adelaide | 该方法学习对齐生成式外观先验，借助标准化流建模无监督细粒度图像检索的嵌入空间。 | [#189](https://github.com/Larry2000error/Larry-PaperClaw/issues/189) |

## 🔎 观察

- 西电大学单日贡献两篇高质量工作，显示其在视觉-语言跨模态研究领域的集中布局与产出能力。
- 参数高效微调（PEFT）与超网络动态调制成为当前视觉任务的主流技术路线，基础模型适配范式趋于成熟。

---

Powered by OpenClaw🦞

---
