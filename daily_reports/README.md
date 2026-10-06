# Daily Reports

最近三天日报（最新在前）：

# [20260929](./202609/20260929.md)
## 📌 今日概况

今日共检索候选论文 82 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI日报候选论文聚焦视觉-语言预训练与目标重识别领域。三篇论文分别探索扩散模型特征学习、视觉基础模型令牌路由机制，以及多模态意图表示优化，体现基础模型与多模态融合的持续深化趋势。

## ✨ 今日亮点

- DiffReID将扩散模型引入目标重识别，通过判别式扩散过程增强特征判别性
- FM-ReID基于DINOv3提出选择性竞争令牌路由，优化局部特征学习机制
- 零样本组合图像检索研究聚焦视觉-语言对齐中的视觉实例化修正问题

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260929] DiffReID: Discriminative Diffusion Model for Object Re-Identification | Wang Yingquan, Zhang Pingping, Wang Dong, Lu Huchuan | Institution unavailable | DiffReID提出判别式扩散模型，通过CLIP引导的提示调优与扩散过程实现目标重识别的判别性特征学习。 | [#532](https://github.com/Larry2000error/Larry-PaperClaw/issues/532) |
| [20260929] FM-ReID: Selective Competitive Token Routing for Object Re-Identification | Li Zhiqi, Zhou Xiaowei, Sun Zeyuan, Gao Feng, Dong Junyu | Faculty of Information Science and Engineering, Ocean University of China；Sanya Oceanographic Institution, Ocean University of China | FM-ReID基于DINOv3视觉基础模型，设计选择性竞争令牌路由机制，动态筛选判别性局部令牌用于重识别。 | [#533](https://github.com/Larry2000error/Larry-PaperClaw/issues/533) |
| [20260929] Optimizing VLP-aligned Multimodal Intent Representation with Correct Visual Instantiation for Zero-Shot Composed Image Retrieval | Ge Xuri, Wang Chunhao, Fu Junchen, Wen Haokun, Xu Zhiwei, Zhou Ying, Chen Zhumin, Ren Pengjie, Ren Zhaochun, Xin Xin | School of Artificial Intelligence, Shandong University；School of Computer Science and Technology, Shandong University；School of Computing Science, University of Glasgow；School of Computer Science and Technology, Harbin Institute of Technology (Shenzhen)；Leiden University | 该研究针对零样本组合图像检索，提出视觉实例化修正方法优化VLP对齐的多模态意图表示。 | [#534](https://github.com/Larry2000error/Larry-PaperClaw/issues/534) |

## 🔎 观察

- 目标重识别领域正加速融合视觉基础模型，从CLIP向DINOv3演进体现技术迭代
- 多模态检索研究开始关注对齐质量的细粒度修正，而非仅追求模态间粗粒度对齐

---

Powered by OpenClaw🦞

---

# [20260928](./202609/20260928.md)
## 📌 今日概况

今日共检索候选论文 84 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦跨模态匹配与多模态学习，涵盖无监督可见光-红外行人重识别、野生动物保护中的多模态动物重识别，以及视觉文档重排序。研究趋势显示语义补偿、环境元数据融合与高效轻量模型成为关键方向。

## ✨ 今日亮点

- 无监督跨模态行人重识别提出语义模态补偿机制，缓解非配对场景下的模态差异
- 野生动物保护研究整合视觉特征与环境元数据，推动多模态动物个体识别
- RidgeRank以岭回归浅层读出实现高效视觉文档重排序，降低计算开销

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260928] Semantic Modality Compensation for Unsupervised Visible-Infrared Person Re-identification under Unpaired Settings | Chen Duanning, He Ke, Yang Bin, Yao Yongxiang | Wuhan University | 提出语义模态补偿网络，在无监督非配对设置下缩小可见光与红外图像的模态鸿沟。 | [#525](https://github.com/Larry2000error/Larry-PaperClaw/issues/525) |
| [20260928] Advancing Wildlife Conservation through Multimodal Animal Re-Identification with Environmental Metadata | Li Yuzhuo, Zhao Di, Qiao Tingrui, Wu Yihao, Pang Bo, Yun Sing Koh | School of Computer Science, University of Auckland | 构建融合环境元数据的多模态框架，提升野外场景下动物重识别的鲁棒性与可解释性。 | [#526](https://github.com/Larry2000error/Larry-PaperClaw/issues/526) |
| [20260928] RidgeRank: Efficient Visual Document Reranking via Score Fusion and a Shallow Linear Readout | Yang Shubing, Zhao Dongfang | University of Washington | 设计基于分数融合与岭回归浅层读出的轻量重排序方法，优化视觉文档检索效率。 | [#527](https://github.com/Larry2000error/Larry-PaperClaw/issues/527) |

## 🔎 观察

- 跨模态重识别研究正从配对数据向非配对、无监督设置迁移，降低标注成本成为核心诉求
- 环境元数据与视觉模态的融合或将成为生态监测领域的新范式，但数据异质性挑战仍待解决

---

Powered by OpenClaw🦞

---

# [20260927](./202609/20260927.md)
## 📌 今日概况

今日共检索候选论文 33 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日研究呈现多模态表征与自监督学习的交叉趋势。漫画角色重识别、变分隐推理嵌入、几何视角合成检索及扩散Transformer结构优化等方向并进，工业界与学术界合作紧密，视觉-语言模型与生成式架构持续受到关注。

## ✨ 今日亮点

- 变分隐推理为多模态嵌入学习提供新范式
- 几何视角合成助力细粒度商品图像检索
- 结构化残差连接优化扩散Transformer性能

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260927] Re:Cognize -- Open-Set Comic Character Re-Identification | Baranwal Aaditya, Kataria Madhav, Yogesh S Rawat, Vyas Shruti | Institute of Artificial Intelligence, University of Central Florida | 提出开放集漫画角色重识别框架，结合自监督学习与序列建模解决跨场景角色匹配难题。 | [#519](https://github.com/Larry2000error/Larry-PaperClaw/issues/519) |
| [20260927] VaME: Exploring Variational Latent Reasoning for Multimodal Embeddings | Wu Peixi, Jiang Mingzhou, Ma Feipeng, Yang Biao, Zhou Yunhao, Yuan Wei, Chai Bosong, Lin Huizu, Chen Jie, Hu Zhangchi, Yang Fan, Ou Wenwu, Li Hebei, Sun Xiaoyan | University of Science and Technology of China；Tsinghua University；Kuaishou；Zhejiang University | 探索变分隐推理机制，通过自回归模型学习多模态嵌入的潜在表征空间。 | [#520](https://github.com/Larry2000error/Larry-PaperClaw/issues/520) |
| [20260927] When Does Geometric View Synthesis Help Wine Label Retrieval? A Public One-Shot Benchmark Across Self-Supervised and Vision-Language Backbones | Huang Yueh-Cheng | Department of Computer Science and Information Engineering, National Dong Hwa University | 构建葡萄酒标签检索基准，系统评估几何视角合成对自监督与视觉语言模型的增益。 | [#521](https://github.com/Larry2000error/Larry-PaperClaw/issues/521) |
| [20260927] Structured Residual Connectivity Matters for Diffusion Transformers | Liu Yuhe, Ma Xinyin, Fang Gongfan, Liu Songhua, Wang Xinchao | National University of Singapore；Shanghai Jiao Tong University | 揭示结构化残差连接对扩散Transformer的关键作用，优化跳跃连接设计提升图像合成质量。 | [#523](https://github.com/Larry2000error/Larry-PaperClaw/issues/523) |

## 🔎 观察

- 自监督学习与视觉-语言模型的融合成为跨域检索的主流技术路线。
- 生成模型架构研究从规模扩张转向结构精细化设计，残差连接重新受到重视。

---

Powered by OpenClaw🦞

---
