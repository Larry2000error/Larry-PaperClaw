# Daily Reports

最近三天日报（最新在前）：

# [20260827](./202608/20260827.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日研究聚焦视觉-语言模型的可解释性与检索能力。学界关注VLM内部机制解析、跨模态地理定位、生成式图像检索及智能体驱动的图像组合，体现从模型机理理解到复杂视觉任务求解的纵深发展。

## ✨ 今日亮点

- KAIST团队揭示VLM视觉检索头机制，为模型可解释性提供新视角
- UniGeo实现文本引导跨视角地理定位，融合无人机影像与大语言模型
- 阿里团队提出隐式图像思考检索框架，推动生成式图像检索落地

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260827] Retrieval Heads Meet Vision: Uncovering How VLMs Locate and Extract Visual Information | Park Chanho, Choi Daehyeon, Lee Jihyun, Sung Minhyuk | KAIST；Independent Researcher | KAIST等提出视觉检索头概念，通过因果干预揭示VLM如何定位提取视觉信息，为视觉语言模型可解释性研究提供新工具。 | [#447](https://github.com/Larry2000error/Larry-PaperClaw/issues/447) |
| [20260827] UniGeo: A Multi-modal Large Language Model for Text-Guided Cross-View Geo-Localization | Wen Jiahao, Yu Hang, Zheng Zhedong | Institution unavailable | UniGeo构建多模态大语言模型，支持文本引导的跨视角地理定位，实现无人机影像与卫星图的双向检索匹配。 | [#448](https://github.com/Larry2000error/Larry-PaperClaw/issues/448) |
| [20260827] PailitaoGR: Latent Think-with-Images for Generative Image Retrieval | Fan Xiaomeng, Liu Yueran, Zhou Shengyu, Fu Chenghan, Guan Wanxian, Li Feng, Yu Chuan, Xu Jian, Zheng Bo | Alibaba Group | 阿里团队提出PailitaoGR框架，采用隐式图像思考机制进行生成式图像检索，优化电商场景下的视觉搜索体验。 | [#449](https://github.com/Larry2000error/Larry-PaperClaw/issues/449) |
| [20260827] Weaving Visual Narratives: Agentic Image Bundle Composition Beyond Atomic Visual Matching | Shan Rong, Xu Tianyi, Zheng Congmin, Chen Wenteng, Zhu Jiachen, Wu Junjie, Wang Teng, Liu Weiwen, Zhang Changwang, Zhang Weinan, Wang Jun, Lin Jianghao | Shanghai Jiao Tong University；Shanghai Innovation Institute；OPPO | 上海交大等提出智能体驱动的图像组合方法，超越原子级视觉匹配，实现个人照片集合中的视觉叙事自动构建。 | [#457](https://github.com/Larry2000error/Larry-PaperClaw/issues/457) |

## 🔎 观察

- 视觉检索正从单图匹配向生成式、叙事化方向演进，任务复杂度显著提升
- 工业界（阿里、OPPO）与学术界协同紧密，技术落地场景明确指向电商与智能终端

---

Powered by OpenClaw🦞

---

# [20260826](./202608/20260826.md)
## 📌 今日概况

今日共检索候选论文 9 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日研究聚焦于多模态检索与视觉理解技术，涵盖文档级视觉检索、组合图像检索、医疗多模态检索及基础设施合规检查等方向。研究趋势显示，领域特定应用（医疗、土木）与高效检索方法（稀疏化、训练无关）成为热点，跨模态对齐与RAG架构持续演进。

## ✨ 今日亮点

- DocPC提出文档级视觉检索新范式，通过代表性页面选择解决多页文档检索难题
- MulVec实现无需训练的零样本组合图像检索，采用细粒度角色感知匹配机制
- PlanSightRAG面向土木标准图纸，构建视觉优先的多模态RAG系统实现自动合规检查

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260826] DocPC: Document-Level Visual Retrieval via Representative Page Composition | You Chengsong, Zhou Junwei, Cao Xiaoyu, Wang Weiyao, Xu Yiwei, Zhao Ziyan, Sun Zhen, Zhu Qicheng, Fu Xuanyi, Chen Yufan, Li Yilun, Xiong Rongkang, Hu Yunhai, Du Nan | East China Normal University；Matter Innovation Inc.；Shandong University of Science and Technology；Thin Red Line；UC Berkeley；New York University | DocPC通过代表性页面组合策略，实现多页文档的高效视觉检索，无需处理全部页面。 | [#444](https://github.com/Larry2000error/Larry-PaperClaw/issues/444) |
| [20260826] MulVec: Fine-Grained Role-Aware Matching for Training-Free Zero-Shot Composed Image Retrieval | Zhang Zihao, Wu Dayan, Liu Xinze, Zhu Hengjie, Zhu Yiliang, Wang Ding, Fu Peng, Lin Zheng, Wang Weiping | Chinese Academy of Sciences | MulVec提出训练无关的零样本组合图像检索方法，利用细粒度角色感知匹配提升检索精度。 | [#445](https://github.com/Larry2000error/Larry-PaperClaw/issues/445) |
| [20260826] Case2Flow: Bridging Patient Cases and Guideline Flowcharts through Multimodal Retrieval | Wei Jiale, Chen Yufan, Jaus Alexander, Marinov Zdravko, Friedrich Julian, Reiß Simon, Kleesiek Jens, Stiefelhagen Rainer | Karlsruhe Institute of Technology；Helmholtz Information and Data Science School for Health (HIDSS4Health)；University Hospital Essen | Case2Flow构建多模态检索桥梁，连接患者病例与医疗指南流程图以支持临床决策。 | [#454](https://github.com/Larry2000error/Larry-PaperClaw/issues/454) |
| [20260826] PlanSightRAG: A Visual-First Multimodal RAG for Automating Question Answering and Compliance Checking for Civil Standard Plans | Subedi Nabaraj, Shuvo Dip Datta, Abdelaty Ahmed, Shivanand Venkanna Sheshappanavar | Institution unavailable | PlanSightRAG采用视觉优先架构，针对土木标准图纸实现自动化问答与合规性检查。 | [#455](https://github.com/Larry2000error/Larry-PaperClaw/issues/455) |
| [20260826] PUMA: Post-Hoc Sparsification of Universal Multimodal Embeddings for Efficient Retrieval | Attimonelli Matteo, Alessandro De Bellis, Franco Maria Nardini, Pomo Claudio, Rulli Cosimo, Venturini Rossano, Tommaso Di Noia | Politecnico di Bari；Sapienza University of Rome；ISTI–CNR；University of Pisa | PUMA通过后验稀疏化技术压缩通用多模态嵌入，在保持检索性能的同时提升效率。 | [#456](https://github.com/Larry2000error/Larry-PaperClaw/issues/456) |

## 🔎 观察

- 多模态检索正深度垂直化，医疗与基础设施等专业领域成为技术落地的重要场景
- 训练无关与后验优化方法涌现，反映学界对检索系统部署效率与成本的关注提升

---

Powered by OpenClaw🦞

---

# [20260824](./202608/20260824.md)
## 📌 今日概况

今日共检索候选论文 2 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日遥感AI领域研究聚焦于多模态大语言模型与扩散模型的融合应用，尤其关注无需训练的计算效率优化。跨模态检索任务成为热点，研究者探索伪融合机制以降低标注成本，推动视觉-语言模型的实用化部署。

## ✨ 今日亮点

- 提出免训练伪融合框架，结合扩散模型与多模态大语言模型实现组合图像检索
- 突破传统训练依赖瓶颈，显著降低计算资源消耗与数据标注需求
- 卢森堡大学团队推动视觉-语言跨模态检索的效率优化新范式

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260824] Training-Free Pseudo-Fusion for Composed Image Retrieval with Diffusion Models and Multimodal Large Language Models | Xu Fan, Luis A. Leiva | University of Luxembourg | 该研究提出无需训练的伪融合方法，整合扩散模型与多模态大语言模型，实现高效组合图像检索任务。 | [#443](https://github.com/Larry2000error/Larry-PaperClaw/issues/443) |

## 🔎 观察

- 免训练范式或成为多模态检索的重要方向，但需验证复杂场景下的泛化稳定性
- 扩散模型与MLLM的融合架构设计值得遥感领域借鉴，或提升卫星图像检索效率

---

Powered by OpenClaw🦞

---
