# Daily Reports

最近三天日报（最新在前）：

# [20260805](./202608/20260805.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI领域聚焦多模态检索与视觉语言理解。三项研究分别探索上下文组合图像检索、长文本监督的视觉语言对齐，以及视频时序预测检索，体现出从静态匹配向动态推理、从短文本向长文本扩展的技术演进趋势。

## ✨ 今日亮点

- CoCo-IR提出上下文组合图像检索新范式，融合多模态大模型与交互推理
- 长段落文本监督取代传统短标题，重塑视觉语言对比学习框架
- 视频前缀预测未来状态，实现跨实例时序检索新机制

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260805] CoCo-IR: Contextual Composed Image Retrieval | Cao Shengcao, Tanmaya Shekhar Dabral, Ding Zhongli, Shanbhogue Madhuri, Chen Kaifeng, Li Zhe, Seyedhosseini Mojtaba, Wang Yu-Xiong, Gui Liang-Yan | University of Illinois Urbana-Champaign；Google DeepMind；OpenAI | CoCo-IR构建上下文组合图像检索基准，利用多模态大模型实现参考图像、修改文本与视觉上下文的联合推理。 | [#395](https://github.com/Larry2000error/Larry-PaperClaw/issues/395) |
| [20260805] A Paragraph is Worth a Thousand Captions: Rethinking Text Supervision for Vision-Language Retrieval | Ghazanfari Mahyar, Tabrizian Amin, Aziz Arsyi, Wang Binshuai, Wei Peng | The George Washington University | 该研究以段落级长文本替代短标题监督，重新评估对比学习在视觉语言检索中的文本粒度效应。 | [#396](https://github.com/Larry2000error/Larry-PaperClaw/issues/396) |
| [20260805] Predict, Then Retrieve: Cross-Instance Future-State Retrieval from Video Prefixes | Vo Quynh, Nguyen Thong, Do Vinh-Hien, Nguyen Cong-Duy, Luu Anh-Tuan | Centre for AI Research, VinUniversity；National University of Singapore | 提出先预测未来状态再检索的范式，从视频前缀推断跨实例的后续视觉内容。 | [#397](https://github.com/Larry2000error/Larry-PaperClaw/issues/397) |

## 🔎 观察

- 视觉语言检索正从单一模态对齐转向复杂上下文推理，长文本与交互式查询成为新焦点
- 时序预测与检索的结合预示视频理解任务向因果推理和前瞻性建模深化

---

Powered by OpenClaw🦞

---

# [20260804](./202608/20260804.md)
## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究聚焦于多模态检索技术的创新，涵盖工业级生成-判别统一框架与零样本草图检索。快手团队提出UniGD解决梯度干扰问题，越南学者探索语义一致的提示学习，均体现跨模态表示学习向实用化与高效化演进。

## ✨ 今日亮点

- UniGD统一生成与判别检索，缓解工业场景梯度干扰难题
- SeCo-SBIR设计语义一致提示学习，提升零样本草图检索精度
- 两研究均聚焦CLIP多模态架构的工业适配与零样本泛化

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260804] UniGD: A Unified Generative-Discriminative Framework for Industrial Retrieval | Ji Shujie, Kong Yawei, Zhao Yilin, Wang Li, Liu Xialong, Jiang Peng | Kuaishou Technology | UniGD提出统一生成-判别框架，通过梯度解耦策略解决工业搜索广告中两类模型的训练冲突。 | [#392](https://github.com/Larry2000error/Larry-PaperClaw/issues/392) |
| [20260804] SeCo-SBIR: Semantically Consistent Prompt Learning for Zero-Shot Sketch-Based Image Retrieval | Long Hoang Dang, Tuan Nguyen Huu, Nguyen Minh Hieu, Tu Minh Phuong | Posts and Telecommunications Institute of Technology | SeCo-SBIR引入语义一致性约束的提示学习，使CLIP在零样本草图图像检索中保持类别语义对齐。 | [#393](https://github.com/Larry2000error/Larry-PaperClaw/issues/393) |

## 🔎 观察

- 生成-判别联合优化成为工业检索系统新方向，但梯度管理复杂度将随规模显著上升
- 提示学习正从NLP向视觉-语言任务迁移，语义一致性约束或成零样本性能关键

---

Powered by OpenClaw🦞

---

# [20260803](./202608/20260803.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日研究聚焦多模态表示学习与跨视角识别技术。四篇论文涵盖知识型视觉问答、空-地行人重识别、开放集动物重识别及通用多模态嵌入，核心趋势在于通过贝叶斯重加权、3D表征、图聚类校准等方法提升模型鲁棒性与泛化能力，尤其关注跨域、跨视角及开放场景下的识别难题。

## ✨ 今日亮点

- 贝叶斯数据重加权策略有效缓解多模态检索中的假阴性噪声问题
- VR3D框架通过视角鲁棒的3D表征学习突破空-地行人重识别瓶颈
- WildFusion方法结合相似度校准与图聚类实现开放集动物个体识别

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260803] Bayesian Data Reweighting Improves Multimodal Retrieval for Knowledge-Based Visual Question Answering | Sun Jingchen, Han Shaobo, Zhang Ruiyi, Naresh Kumar Devulapally, Liu Ming, Long Yitao, Vishnu Suresh Lokhande, Chen Changyou | University at Buffalo；NEC Laboratories America；Adobe Research；Iowa State University；New York University | 提出贝叶斯数据重加权框架，通过对比学习优化多模态检索，降低知识型视觉问答中的假阴性样本干扰。 | [#387](https://github.com/Larry2000error/Larry-PaperClaw/issues/387) |
| [20260803] VR3D: View-Robust 3D Representation Learning for Aerial-Ground Person Re-Identification | Ji Chao, Xuan Shiyu, Li Zechao | Nanjing University of Science and Technology | 构建视角鲁棒的3D表征学习网络VR3D，解决无人机与地面摄像头间行人重识别的跨视角匹配难题。 | [#388](https://github.com/Larry2000error/Larry-PaperClaw/issues/388) |
| [20260803] Calibrated Similarity and Graph Clustering for Open-Set Animal Re-Identification | ElBassat Mohamed, Elkerdany Seifeldin, ElBialy Mohamed, Abouelhamd Gamal, Ghoneim Jana, Elkady Assem, Elboraay Mohamed, Semenova Nelly | Made In Alexandria Artificial Intelligence Team；Faculty of Computer Science and Engineering, Alamein International University；Faculty of Computers and Data Science, Alexandria University；Faculty of Engineering, Alexandria University；Alexandria Higher Institute of Engineering and Technology；Moscow Pedagogical State University | 设计WildFusion系统，融合相似度校准与图聚类技术，提升开放集场景下野生动物个体重识别的可靠性。 | [#389](https://github.com/Larry2000error/Larry-PaperClaw/issues/389) |
| [20260803] Illuminating Visual Identity in Universal Multimodal Embeddings | Cao Jiawei, Feng Junyi, Hua Jiashen, Huang Ziheng, Deng Bing, Wu Kaijie, Gu Chaochen, Ye Jieping | Shanghai Jiao Tong University；Alibaba Group | 探索多模态大语言模型中的视觉身份保持机制，优化通用嵌入空间下的实例检索与跨模态对齐性能。 | [#390](https://github.com/Larry2000error/Larry-PaperClaw/issues/390) |

## 🔎 观察

- 重识别任务正从封闭集向开放集、从单一模态向跨视角/跨域扩展，3D表征与图结构方法成为关键突破口
- 多模态学习研究重心从规模扩张转向质量优化，数据重加权和嵌入空间校准技术受到更多关注

---

Powered by OpenClaw🦞

---
