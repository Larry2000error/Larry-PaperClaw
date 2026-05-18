# Daily Reports

最近三天日报（最新在前）：

# [20260513](./202605/20260513.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日遥感AI领域研究聚焦于图像语义理解的深层挑战，东京都立大学与CyberAgent联合团队提出上下文依赖的图像检索新范式，突破传统视觉语义单一表征的局限，探索叙事语境与多模态嵌入的融合机制，推动图像检索从内容匹配向语义推理演进。

## ✨ 今日亮点

- 突破固定语义表征，实现图像意义的动态上下文建模
- 融合叙事语境与多模态嵌入，提升检索语义适配性
- 推动图像检索从内容匹配向情境化理解转型

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260513] Same Image, Different Meanings: Toward Retrieval of Context-Dependent Meanings | Tsutsumi Ayuto, Kohita Ryosuke | Tokyo Metropolitan University；CyberAgent | 该研究提出上下文依赖的图像检索框架，通过语义抽象与叙事语境建模，解决同一图像在不同情境下的多义性表征问题。 | [#195](https://github.com/Larry2000error/Larry-PaperClaw/issues/195) |

## 🔎 观察

- 该研究标志着图像检索正从'所见即所得'向'所见随境异'演进，语义抽象层的设计将成为关键瓶颈
- 多模态嵌入与叙事语境的结合路径，可能为遥感图像解译中的场景语义歧义问题提供迁移思路

---

Powered by OpenClaw🦞

---

# [20260512](./202605/20260512.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦多模态模型的鲁棒性与可靠性提升。视觉-语言模型持续学习、跨视角地理定位的天气鲁棒性、多图像检索中的位置偏置缓解成为核心议题，体现领域对实际部署场景适应性的高度关注。

## ✨ 今日亮点

- 跨模态知识保留机制增强弹性权重巩固，缓解灾难性遗忘
- 原型学习驱动语义部件发现，提升恶劣天气下跨视角定位精度
- 注意力引导的logit校准策略，有效抑制多图像检索中的位置偏置

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260512] Lifelong Learning in Vision-Language Models: Enhanced EWC with Cross-Modal Knowledge Retention | Hamza Ahmed Durrani, Rafay Suleman Durrani | Sejong University；Technische Universität Ilmenau | 提出增强型弹性权重巩固方法，通过跨模态知识保留机制解决视觉-语言模型终身学习中的灾难性遗忘问题。 | [#191](https://github.com/Larry2000error/Larry-PaperClaw/issues/191) |
| [20260512] Weather-Robust Cross-View Geo-Localization via Prototype-Based Semantic Part Discovery | Tran Chi-Nguyen, Dao Sy Duy Minh, Huynh Trung Kiet, Nguyen Lam Phu Quy, Pham Phu-Hoa, Tran-Thanh Long | University of Warwick | 基于原型学习的语义部件发现框架，实现天气鲁棒的跨视角地理定位，增强模型对恶劣条件的适应能力。 | [#192](https://github.com/Larry2000error/Larry-PaperClaw/issues/192) |
| [20260512] Logit-Attention Divergence: Mitigating Position Bias in Multi-Image Retrieval via Attention-Guided Calibration | Xian Mingtao, Yang Yifeng, Gu Qinying, Wang Xinbing, Ye Nanyang | Tsinghua University；Chinese Academy of Sciences | 设计Logit-注意力散度校准方法，利用注意力机制引导缓解多图像检索任务中多模态大语言模型的位置偏置。 | [#193](https://github.com/Larry2000error/Larry-PaperClaw/issues/193) |

## 🔎 观察

- 位置偏置与灾难性遗忘等模型固有缺陷正获得针对性技术回应，显示领域从性能优化向可靠性深化的转型趋势。
- 天气鲁棒性与跨视角任务结合，反映遥感应用对复杂环境适应性的迫切需求，语义级部件建模成为关键突破口。

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
