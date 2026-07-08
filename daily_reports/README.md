# Daily Reports

最近三天日报（最新在前）：

# [20260707](./202607/20260707.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦跨模态检索与不确定性建模。遥感领域出现基于证据学习的图像-文本检索新方法；同时可见细粒度图像哈希、多模态视频音乐推荐等方向进展，体现多模态融合与可信赖AI的技术趋势。

## ✨ 今日亮点

- 遥感跨模态检索引入证据学习，显式量化不确定性以提升可靠性
- 细粒度食品图像检索结合关系建模与频域感知，优化哈希表示
- 视频到音乐推荐采用语义检索与时序重排，增强音视频对齐效果

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260707] RFHNet: Relational and Frequency-Aware Hashing Network for Large-Scale Fine-Grained Food Image Retrieval | Wang Junsong, Min Weiqing, Sheng Guorui, Yao Tao, Wang Lili, Jiang Shuqiang | College of Computer Science and Artificial Intelligence, Ludong University；Institute of Computing Technology, Chinese Academy of Sciences；University of Chinese Academy of Sciences | RFHNet提出关系与频域感知哈希网络，通过挖掘细粒度食品图像的语义关系与频率特征，实现大规模高效检索。 | [#322](https://github.com/Larry2000error/Larry-PaperClaw/issues/322) |
| [20260707] Uncertainty-Aware Cross-Modal Remote Sensing Image-Text Retrieval via Evidential Learning | Wang Zhuoyue, Wang Xueqian, Li Gang, Li Chengxi, Liu Yongpan, Ban Yifang | Institution unavailable | 该工作将证据学习引入遥感跨模态检索，显式建模预测不确定性，缓解图像-文本匹配中的置信度校准问题。 | [#323](https://github.com/Larry2000error/Larry-PaperClaw/issues/323) |
| [20260707] Multimodal Video-to-Music Recommendation via Semantic Retrieval and Temporal Reranking | Doh Seungheon, Lee Minhee, Lee Sangmoon, Ben Sangbae Chon, Nam Juhan | Korea Advanced Institute of Science and Technology；Kakao Entertainment Corp. | 研究提出语义检索联合时序重排框架，利用多模态线索实现视频到音乐的精准推荐，强化时序一致性约束。 | [#324](https://github.com/Larry2000error/Larry-PaperClaw/issues/324) |

## 🔎 观察

- 证据学习在遥感跨模态任务中的应用表明，不确定性量化正成为提升模型可靠性的关键方向
- 细粒度检索与多模态推荐均强调语义关系建模，反映表示学习从单一特征向结构化理解的演进

---

Powered by OpenClaw🦞

---

# [20260706](./202607/20260706.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究聚焦视觉-语言多模态检索的效率优化。两篇论文分别探索零样本组合图像检索的直接学习方法，以及视觉令牌压缩中的对象感知合并策略，均致力于在保持精度的同时降低计算开销，体现多模态检索向高效化、精细化发展的趋势。

## ✨ 今日亮点

- DiCE-CIR提出直接组合学习框架，无需显式特征分解即可实现高效零样本组合图像检索
- OPTMeR方法通过对象证据保留的令牌合并，解决视觉-语言检索中的令牌冗余问题
- 两项研究均针对多模态检索的计算瓶颈，分别从学习范式与表示压缩角度优化效率

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260706] DiCE-CIR: Direct Composition Learning for Efficient Zero-Shot Composed Image Retrieval | Na Gwang-Ho, Kim Ho-Joong, Lee Seong-Whan | Korea University | DiCE-CIR通过直接组合学习替代传统显式分解，在零样本组合图像检索中实现效率与精度的平衡。 | [#318](https://github.com/Larry2000error/Larry-PaperClaw/issues/318) |
| [20260706] Do All Visual Tokens Matter Equally? Object-Evidence Preserving Token Merging for Vision-Language Retrieval | Park Suhyeong, Jung Junha, Park Jungwoo, Kang Jaewoo | The Catholic University of Korea；Korea University；AIGEN Sciences Inc. | OPTMeR提出对象证据感知的令牌合并策略，在视觉-语言检索中保留关键对象信息的同时压缩视觉表示。 | [#320](https://github.com/Larry2000error/Larry-PaperClaw/issues/320) |

## 🔎 观察

- 视觉-语言检索正从追求精度转向效率-精度联合优化，令牌压缩与轻量化学习成为关键方向。
- 零样本组合检索与细粒度对象感知结合，反映多模态模型对可解释性与可控性的需求提升。

---

Powered by OpenClaw🦞

---

# [20260705](./202607/20260705.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日聚焦自动驾驶场景下的道路施工区智能感知。清华与中科院团队发布多模态数据集，融合高精度地图与多源传感器数据，推动施工区检测与地理定位的协同研究，体现遥感与自动驾驶交叉领域的数据基础设施建设趋势。

## ✨ 今日亮点

- 多模态数据融合：整合视觉、LiDAR与HD Maps实现施工区精准感知
- 地理定位闭环：检测与定位联合框架服务自动驾驶导航安全
- 开源数据集建设：填补道路施工场景标准化数据空白

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260705] Framework and Multi-modal Dataset for Roadwork Zone Detection and Geo-localization | Yan Zhiran, Xin Yutong, S Shyam Shenoi, Song Rui, Elger Gordon | Tsinghua University；Chinese Academy of Sciences | 清华-中科院团队构建道路施工区检测与地理定位多模态数据集，融合高精度地图支撑自动驾驶安全。 | [#317](https://github.com/Larry2000error/Larry-PaperClaw/issues/317) |

## 🔎 观察

- 施工区动态场景感知成为自动驾驶落地关键瓶颈，多模态融合是主流技术路线
- 学术机构主导数据基础设施建设，但工程化部署与车端实时性仍是待验证环节

---

Powered by OpenClaw🦞

---
