# Daily Reports

最近三天日报（最新在前）：

# [20260707](./202607/20260707.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 3 篇。

今日研究聚焦跨模态检索与不确定性量化。遥感领域出现证据学习驱动的图文检索新方法；细粒度图像检索引入关系建模与频域感知；多模态推荐系统探索视频到音乐的语义对齐。整体趋势显示检索任务正向不确定性量化与细粒度语义理解深化。

## ✨ 今日亮点

- 证据学习首次系统应用于遥感跨模态检索，实现不确定性显式建模
- RFHNet融合关系推理与频域特征，突破细粒度食品图像哈希检索瓶颈
- 时序重排序机制创新性地桥接视频语义与音乐推荐的时间动态性

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260707] RFHNet: Relational and Frequency-Aware Hashing Network for Large-Scale Fine-Grained Food Image Retrieval | Wang Junsong, Min Weiqing, Sheng Guorui, Yao Tao, Wang Lili, Jiang Shuqiang | College of Computer Science and Artificial Intelligence, Ludong University；Institute of Computing Technology, Chinese Academy of Sciences；University of Chinese Academy of Sciences | RFHNet提出关系与频域感知哈希网络，通过图关系建模与离散余弦变换增强，解决大规模细粒度食品图像检索中的语义鸿沟与效率问题。 | [#322](https://github.com/Larry2000error/Larry-PaperClaw/issues/322) |
| [20260707] Uncertainty-Aware Cross-Modal Remote Sensing Image-Text Retrieval via Evidential Learning | Wang Zhuoyue, Wang Xueqian, Li Gang, Li Chengxi, Liu Yongpan, Ban Yifang | Institution unavailable | 该研究将证据学习引入遥感图文检索，构建不确定性感知跨模态框架，有效量化预测置信度以提升检索可靠性。 | [#323](https://github.com/Larry2000error/Larry-PaperClaw/issues/323) |
| [20260707] Multimodal Video-to-Music Recommendation via Semantic Retrieval and Temporal Reranking | Doh Seungheon, Lee Minhee, Lee Sangmoon, Ben Sangbae Chon, Nam Juhan | Korea Advanced Institute of Science and Technology；Kakao Entertainment Corp. | 研究提出语义检索与时序重排序两阶段框架，利用多模态Transformer编码视频-音乐语义关联，并通过时序对齐优化推荐时序连贯性。 | [#324](https://github.com/Larry2000error/Larry-PaperClaw/issues/324) |

## 🔎 观察

- 证据学习在遥感多模态任务中的应用尚处早期，其不确定性量化能力对高 stakes 地理决策具有潜在价值，但计算开销需权衡
- 细粒度食品检索与视频-音乐推荐均显示：领域特定语义（食材纹理、节拍情绪）需超越通用视觉表征的专用架构设计

---

Powered by OpenClaw🦞

---

# [20260706](./202607/20260706.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究聚焦视觉-语言多模态检索的效率优化。两篇论文分别探索零样本组合图像检索的直接学习方法，以及视觉令牌压缩中的对象感知策略，均致力于在保持精度的同时降低计算开销，体现多模态大模型轻量化部署趋势。

## ✨ 今日亮点

- DiCE-CIR提出直接组合学习框架，无需显式特征分解即可实现高效零样本组合图像检索
- OPT-MeR引入对象证据保留的令牌合并机制，解决视觉令牌冗余问题
- 两研究均针对Vision-Language检索的推理效率瓶颈，分别从学习范式与输入压缩切入

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260706] DiCE-CIR: Direct Composition Learning for Efficient Zero-Shot Composed Image Retrieval | Na Gwang-Ho, Kim Ho-Joong, Lee Seong-Whan | Korea University | DiCE-CIR通过直接组合学习统一处理图像-文本特征交互，避免传统两阶段分解带来的信息损失，提升零样本组合检索效率。 | [#318](https://github.com/Larry2000error/Larry-PaperClaw/issues/318) |
| [20260706] Do All Visual Tokens Matter Equally? Object-Evidence Preserving Token Merging for Vision-Language Retrieval | Park Suhyeong, Jung Junha, Park Jungwoo, Kang Jaewoo | The Catholic University of Korea；Korea University；AIGEN Sciences Inc. | OPT-MeR提出对象感知的令牌合并策略，基于对象证据保留关键视觉令牌，在Vision-Language检索中实现精度与效率的平衡。 | [#320](https://github.com/Larry2000error/Larry-PaperClaw/issues/320) |

## 🔎 观察

- 组合图像检索正从显式特征解耦转向端到端直接学习，简化流程的同时可能重塑多模态表征空间设计
- 视觉令牌压缩技术从均匀采样演进至对象感知选择，反映视觉-语言任务对语义一致性的刚性需求

---

Powered by OpenClaw🦞

---

# [20260705](./202607/20260705.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日遥感AI研究聚焦自动驾驶场景下的道路施工区域感知，清华大学与中科院团队提出多模态数据集与地理定位框架，融合高清地图与多源传感器数据，推动复杂交通场景下的高精度环境理解技术发展。

## ✨ 今日亮点

- 多模态数据集支撑道路施工区智能检测与定位
- 融合高清地图实现施工区域精准地理定位
- 面向自动驾驶的复杂场景感知框架创新

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260705] Framework and Multi-modal Dataset for Roadwork Zone Detection and Geo-localization | Yan Zhiran, Xin Yutong, S Shyam Shenoi, Song Rui, Elger Gordon | Tsinghua University；Chinese Academy of Sciences | 清华与中科院团队构建道路施工区检测与地理定位的多模态数据集及框架，服务自动驾驶高清地图应用。 | [#317](https://github.com/Larry2000error/Larry-PaperClaw/issues/317) |

## 🔎 观察

- 自动驾驶感知正从标准场景向施工等长尾场景延伸，数据稀缺性成为关键瓶颈
- 多模态融合与高清地图结合成为提升定位精度的主流技术路线

---

Powered by OpenClaw🦞

---
