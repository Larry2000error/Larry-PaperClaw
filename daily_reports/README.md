# Daily Reports

最近三天日报（最新在前）：

# [20260812](./202608/20260812.md)
## 📌 今日概况

今日共检索候选论文 9 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究聚焦视觉-语言模型的检索与定位任务。MASCOT提出模型感知的子模覆盖方法优化多属性图文检索；GeoBridge探索生成式图像地理定位，通过解耦语义条件与黎曼流匹配提升定位精度。两工作均体现多模态融合与结构化推理的前沿趋势。

## ✨ 今日亮点

- MASCOT将子模优化引入图文检索，实现模型感知的多属性覆盖与结果多样化
- GeoBridge提出解耦语义条件机制，结合黎曼流匹配生成地理坐标分布
- 两研究分别来自印度理工学院孟买分校与中国科学院系统，体现国际合作格局

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260812] MASCOT: Model-Aware Submodular Coverage for Composite-Attribute Text-to-Image Retrieval | Sharma Aaryan, Vishak Prasad C, Singh Virendra, Ramakrishnan Ganesh | Indian Institute of Technology Bombay | MASCOT提出模型感知的子模覆盖框架，通过复合属性优化实现多样化图文检索，解决传统方法忽视模型内部表征的问题。 | [#417](https://github.com/Larry2000error/Larry-PaperClaw/issues/417) |
| [20260812] GeoBridge: Decoupled Semantic Conditioning for Generative Image Geolocalization | Dou Zhiyang, Han Xumeng, Peng Fengde, Wang Zipeng, Zhao Moxuan, Huang Zhipei, Han Zhenjun | University of Chinese Academy of Sciences；School of Advanced Interdisciplinary Sciences；School of Electronic, Electrical and Communication Engineering；Shenzhen Institutes of Advanced Technology | GeoBridge采用解耦语义条件与黎曼流匹配，构建生成式图像地理定位新范式，将坐标预测转化为连续分布生成任务。 | [#418](https://github.com/Larry2000error/Larry-PaperClaw/issues/418) |

## 🔎 观察

- 图文检索正从相似度匹配转向结构化覆盖优化，子模函数与模型内部知识的结合值得遥感领域借鉴。
- 生成式范式开始渗透图像定位任务，流匹配等连续建模方法可能重塑地理坐标预测的技术路线。

---

Powered by OpenClaw🦞

---

# [20260811](./202608/20260811.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究聚焦多模态检索领域，两篇论文分别从通用大模型能力与垂直领域应用两个维度展开探索。前者评估前沿LLM在文本-图像检索中的零样本表现，后者针对特定场景（如安防监控）重新审视检索范式，体现从通用基准向实际落地的研究转向。

## ✨ 今日亮点

- 前沿LLM原生多模态嵌入能力获系统评估，Gemini等模型在难负样本检索中表现受关注
- 垂直领域文本图像检索提出新框架，解决安防监控等场景的多匹配与域适应难题
- 研究呈现从通用基准测试向特定场景实用化迁移的趋势

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260811] Can Frontier LLMs Match Natively Multimodal Embeddings? A Comparison on Hard-Negative Text-to-Image Retrieval | Dutta Archan, Kanungo Vyanktesh | Westcliff University | 该研究对比前沿大语言模型与原生多模态嵌入在难负样本文本-图像检索任务中的零样本排序性能。 | [#414](https://github.com/Larry2000error/Larry-PaperClaw/issues/414) |
| [20260811] Rethinking Text-Based Image Retrieval in Specific Domain | Tan Jingyang, Yang Sheng, Chen Yuanpeng, Wang Jian, Ye Nianjin, Xing Chen, Jia Lanpeng | Department of Electronic and Communication Engineering, Harbin Institute of Technology；School of Data Science, Fudan University；Changhong Intelligent Robot | 该工作针对安防监控等特定领域，重新思考文本图像检索范式，提出多匹配检索的新解决方案。 | [#415](https://github.com/Larry2000error/Larry-PaperClaw/issues/415) |

## 🔎 观察

- 多模态检索正从通用数据集基准测试向垂直领域深度适配演进，实际部署需求驱动研究范式转变
- 大模型零样本能力与专用嵌入模型的性能边界尚待厘清，评估方法论本身成为关键研究问题

---

Powered by OpenClaw🦞

---

# [20260810](./202608/20260810.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦跨视角地理定位与无人机视觉理解两大方向。前者致力于消除卫星-地面图像间的几何形变干扰，后者探索细粒度跨模态对齐技术。两项工作均体现特征空间学习与多源数据融合的持续深化趋势。

## ✨ 今日亮点

- 无变形跨视角地理定位：在特征空间共识挖掘替代传统几何校正
- 无人机细粒度理解：粒度感知区域对齐联合语义原型学习
- 中科院空天院主导无人机视觉-语言导航新框架

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260810] Warp-free Cross-view Geo-localization via Feature-space Consensus Mining | Song Zhuo, Xu Lian, Jiang Runqing, Zhang Yongjian, Li Kunhong, Zhang Ye, Guo Yulan | Sun Yat-sen University；The University of Western Australia | 中山大学团队提出特征空间共识挖掘方法，无需显式几何变形校正即可实现跨视角地理定位。 | [#411](https://github.com/Larry2000error/Larry-PaperClaw/issues/411) |
| [20260810] GRASP: Granularity-Aware Region Alignment and Semantic Prototype Learning for Fine-Grained Cross-Modal Understanding in Drone Views | Cui Jiahui, Zhao Yan, Wei Kan, Zhu Enze, Zhang Peirong, Wang Lei, Wang Yiru | Aerospace Information Research Institute, Chinese Academy of Sciences；Key Laboratory of Target Cognition and Application Technology (TCAT)；University of Chinese Academy of Sciences；School of Electronic, Electrical and Communication Engineering, University of Chinese Academy of Sciences | 中科院空天院提出GRASP框架，通过粒度感知区域对齐与语义原型学习提升无人机细粒度跨模态理解能力。 | [#412](https://github.com/Larry2000error/Larry-PaperClaw/issues/412) |

## 🔎 观察

- 跨视角任务正从几何显式建模转向特征隐式对齐，降低对先验配准精度的依赖
- 无人机视觉-语言研究向细粒度区域级理解演进，支撑更复杂的导航与交互应用

---

Powered by OpenClaw🦞

---
