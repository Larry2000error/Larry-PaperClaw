# Daily Reports

最近三天日报（最新在前）：

# [20260722](./202607/20260722.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日研究聚焦跨模态检索与边缘智能，涵盖多项技术路线：从存内计算优化到多轮对话式时尚检索，从可见光-红外预训练采样策略到大倾角无人机-卫星地理定位，体现遥感与视觉AI在效率、精度与场景适配上的多维探索。

## ✨ 今日亮点

- PolySim提出确定性多项式代理，解决存内计算架构下的跨模态检索概率嵌入瓶颈
- OffNadirLoc构建大倾角无人机-卫星定位基准，针对透视畸变设计结构感知学习框架
- Ma等揭示可见光-红外预训练中补丁采样不均问题，提出重要性采样优化策略

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260722] PolySim: Deterministic Polynomial Surrogates for Cross-Modal Retrieval on CiM | Li Xinzhao, Power Charles, Ren Pengyu, Won Jongun, Pei Likai, Hu Yuting, Xiong Jinjun, Vardar Alptekin, Cao Ningyuan, Xiaobo Sharon Hu, Kämpfe Thomas, Ni Kai, Qin Ruiyang | Villanova University；University of Notre Dame；University at Buffalo；Fraunhofer IPMS；TU Braunschweig | PolySim为存内计算架构设计确定性多项式代理，替代概率嵌入实现高效跨模态检索。 | [#357](https://github.com/Larry2000error/Larry-PaperClaw/issues/357) |
| [20260722] Diverse-Intent Multi-Turn Fashion Image Retrieval | Tang Mingqiang, Wen Haokun, Liu Meng, Hu Yupeng, Guan Weili, Song Xuemeng | Southern University of Science and Technology；Harbin Institute of Technology (Shenzhen)；Shandong University；Shenzhen Loop Area Institute | 提出多轮时尚图像检索框架FashionAM，支持多样化意图的连续对话式视觉搜索。 | [#358](https://github.com/Larry2000error/Larry-PaperClaw/issues/358) |
| [20260722] Not All Patches are Equal: Sampling Matters for Visible-Infrared Pre-Training | Ma Qiwei, Deng Bin, Zhu Junjie, Huang Qiangjuan, Duan Puhong, Yang Ke, Kang Xudong, Li Shutao | School of Artificial Intelligence and Robotics, Hunan University；Yuelushan Center for Industrial Innovation；Intelligent Game and Decision Lab | 针对可见光-红外预训练，提出基于补丁重要性的采样策略，提升跨模态表征学习效率。 | [#359](https://github.com/Larry2000error/Larry-PaperClaw/issues/359) |
| [20260722] OffNadirLoc: Benchmark and Framework for Challenging UAV-to-Satellite Geo-Localization under Large Off-Nadir Views | Qiao Qian, Liu Wenye, Liu Ting, Shu Jiuhe, Wang Peng | Northwestern Polytechnical University | OffNadirLoc建立大倾角无人机-卫星定位基准，缓解极端视角下的透视畸变与匹配难题。 | [#360](https://github.com/Larry2000error/Larry-PaperClaw/issues/360) |
| [20260722] Using Hierarchical Controlled Vocabularies to Understand CLIP Retrieval Failures in Historical Photo Collections | Sebastian Ratan, Hoppe Anett, Rippe Christoph, Ewerth Ralph | TIB – Leibniz Information Centre for Science and Technology；L3S Research Center, Leibniz University Hannover；Marburg University；Hessian Center for Artificial Intelligence (hessian.AI)；Goethe University Frankfurt, University Library Frankfurt | 利用分层受控词表分析CLIP在历史照片检索中的失效模式，揭示语义鸿沟与改进路径。 | [#364](https://github.com/Larry2000error/Larry-PaperClaw/issues/364) |

## 🔎 观察

- 边缘智能与遥感交叉加速：存内计算(CiM)与无人机-卫星定位同步涌现，反映低功耗与极端场景的双重需求
- 预训练采样策略精细化：从均匀采样转向重要性感知，显示跨模态表征学习进入数据效率优化深水区

---

Powered by OpenClaw🦞

---

# [20260721](./202607/20260721.md)
## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 6 篇。

今日研究聚焦跨模态检索与多模态表征学习，涵盖病理图像视觉语言模型基准测试、3D场景检索优化、无GPS无人机定位、行人重识别几何可靠性建模及统一多模态嵌入空间构建，体现遥感与计算机视觉深度融合趋势。

## ✨ 今日亮点

- PathAgentBench发布病理全切片图像视觉语言模型基准，推动医学影像证据检索能力评估
- NGPS提出无GPS环境下卫星图像匹配与多速率传感器融合的无人机定位重建方案
- Fusion Embedding构建文本、图像、视频、音频的统一嵌入空间，实现跨模态检索

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260721] PathAgentBench: Benchmarking Evidence-Seeking Vision-Language Models on Whole-Slide Pathology Image | Liao Dankai, Zhang Tianyi, Wu Yufeng, Zhang Xinyue, Xue Qiaochu, Liu Zeyu, Zhao Dachun, Cai Linghan, Jin Yueming | National University of Singapore；National University Hospital；Singapore | PathAgentBench针对全切片病理图像构建证据搜寻型视觉语言模型基准测试框架。 | [#349](https://github.com/Larry2000error/Larry-PaperClaw/issues/349) |
| [20260721] CR-Refiner: An Object-Centric Optimal Transport Reranker for Edit-Conditioned 3D Scene Retrieval | Wu Hao, Zhu Jinjing, Wu Nanyu, Cai Qianyi, Lin Heyi, Wang Hao, Xiong Hui | Hong Kong University of Science and Technology；Hong Kong University of Science and Technology (Guangzhou) | CR-Refiner基于最优传输理论提出以对象为中心的编辑条件3D场景重排序方法。 | [#350](https://github.com/Larry2000error/Larry-PaperClaw/issues/350) |
| [20260721] NGPS: GPS-Denied Aerial Geo-Localization and 2.5D Reconstruction via Deep Satellite Image Matching and Multi-Rate Sensor Fusion | Sharma Sanket | Institution unavailable | NGPS通过深度卫星图像匹配与多速率传感器融合实现无GPS无人机地理定位与2.5D重建。 | [#351](https://github.com/Larry2000error/Larry-PaperClaw/issues/351) |
| [20260721] Reliability-Aware 3D Geometric Injection for Universal Person Re-identification | Su Bohan, Wang Jiashuo, Liu Fangyi, Ye Mang | National Engineering Research Center for Multimedia Software, School of Computer Science, Wuhan University | Reliability-Aware 3D Geometric Injection引入可靠性感知学习增强通用行人重识别的3D几何注入。 | [#353](https://github.com/Larry2000error/Larry-PaperClaw/issues/353) |
| [20260727] Dual-Edged Homogeneous-Modality Similarity: Towards Visible-Infrared Modality-Incomplete Person Re-Identification with Modality Adaptive Matching | Xu Xin, Zhan Shuhao, Liu Wei, Wang Zheng, Jiang Kui, Lin Chia-Wen | School of Computer Science and Technology, Wuhan University of Science and Technology；Hubei Province Key Laboratory of Intelligent Information Processing and Real-time Industrial System, Wuhan University of Science and Technology；School of Computer Science, Wuhan University；Faculty of Computing, Harbin Institute of Technology；Department of Electrical Engineering and the Institute of Communications Engineering, National Tsing Hua University | Dual-Edged Homogeneous-Modality Similarity针对模态缺失场景提出可见光-红外自适应匹配行人重识别。 | [#354](https://github.com/Larry2000error/Larry-PaperClaw/issues/354) |
| [20260721] Fusion Embedding: A Unified Embedding Space for Text, Image, Video, and Audio | Abdul Basit Tonmoy, Kazi Fardinul Hoque, Md. Shahrier Islam Arham, Luthra Arman | Eximius Labs；Wabash College；Skop Intelligence Co. | Fusion Embedding构建统一嵌入空间实现文本、图像、视频、音频的跨模态表征与检索。 | [#355](https://github.com/Larry2000error/Larry-PaperClaw/issues/355) |

## 🔎 观察

- 行人重识别领域同日出现两篇工作，分别聚焦3D几何可靠性与模态缺失自适应匹配，显示该方向正从特征对齐向鲁棒性建模深化。
- 多模态统一表征成为热点，Fusion Embedding与PathAgentBench分别从通用嵌入与垂直领域基准切入，反映基础模型与评测体系并行发展。

---

Powered by OpenClaw🦞

---

# [20260719](./202607/20260719.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日仅收录1篇论文，聚焦多目标跟踪中的重识别问题。研究针对高度相似物体的身份保持难题，提出视频级关联方法VLA-ReID，属于计算机视觉与遥感交叉领域的目标跟踪技术方向。

## ✨ 今日亮点

- VLA-ReID提出视频级关联框架，解决高度相似物体的重识别难题
- 针对多目标跟踪中身份漂移问题，强化时序一致性约束
- 方法适用于密集场景下的细粒度目标区分与长期跟踪

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260719] VLA-ReID: Video-Level Association for Re-Identification in Multi-Object Tracking with Highly Similar Objects | Qin Yanrong, Cao Xiaoyan, Yao Yao | Institution unavailable | VLA-ReID通过视频级关联机制，提升多目标跟踪中高度相似物体的重识别精度与身份保持能力。 | [#348](https://github.com/Larry2000error/Larry-PaperClaw/issues/348) |

## 🔎 观察

- 该研究关注细粒度重识别，对遥感视频中的密集小目标跟踪具有潜在借鉴价值
- 单篇收录反映该细分方向近期产出有限，或需关注更广泛的遥感智能解译进展

---

Powered by OpenClaw🦞

---
