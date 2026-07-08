# Daily Reports

最近三天日报（最新在前）：

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

# [20260703](./202607/20260703.md)
## 📌 今日概况

今日共检索候选论文 0 篇；关键词+LLM 智能匹配遥感交叉论文 0 篇；最终纳入日报 2 篇。

今日研究聚焦多模态学习优化与高效检索。CLIP模型向双曲空间扩展以提升长文本理解能力，同时无监督跨模态哈希通过属性提示与核方法实现数据高效检索，体现几何深度学习与轻量化表示学习的发展趋势。

## ✨ 今日亮点

- 双曲空间微调CLIP突破欧氏几何限制，增强长上下文图像-文本对齐能力
- 属性提示核哈希实现无监督跨模态检索，显著降低标注数据依赖
- 多机构国际合作凸显产学研融合，覆盖新加坡、韩国及中国顶尖高校

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260703] HyFL-CLIP: Hyperbolic Fine-Tuning of CLIP for Robust Long-Context Understanding | Ji Ha Jang, Kim Hayeon, Lee Chulwon, Junghun James Kim, Se Young Chun | Dept. of Electrical and Computer Engineering；IPAI；INMC & AIIS；Seoul National University | HyFL-CLIP将CLIP微调至双曲空间，利用双曲几何特性提升长上下文图像-文本理解鲁棒性。 | [#313](https://github.com/Larry2000error/Larry-PaperClaw/issues/313) |
| [20260703] Attribute-Prompted Kernel Hashing for Unsupervised Data-Efficient Cross-Modal Retrieval | Li Runhao, Ma Xiaoxu, Weng Zhenyu, Zhang Yue, Luo Guibo, Zhuang Huiping, Lin Zhiping, Tan Yap-Peng | Nanyang Technological University；Chinese Academy of Sciences；Guangdong University of Technology；University of Electronic Science and Technology of China | 提出属性提示核哈希方法，以无监督方式学习判别性跨模态哈希码，实现数据高效检索。 | [#314](https://github.com/Larry2000error/Larry-PaperClaw/issues/314) |

## 🔎 观察

- 双曲学习正成为突破Transformer长度外推瓶颈的新方向，但计算开销与可扩展性仍需验证
- 无监督跨模态检索从对比学习向属性语义引导演进，提示机制或成数据高效学习关键

---

Powered by OpenClaw🦞

---
