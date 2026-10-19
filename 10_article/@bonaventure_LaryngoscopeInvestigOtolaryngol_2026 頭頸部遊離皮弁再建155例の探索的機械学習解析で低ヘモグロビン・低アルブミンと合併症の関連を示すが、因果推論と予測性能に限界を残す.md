---
tags:
  - PMID/42870824
citekey: "bonaventure_LaryngoscopeInvestigOtolaryngol_2026"
dateread: '2026-10-18'
read: false
topic: head_neck_general
domain: head_neck
title_ja: '頭頸部遊離皮弁再建155例の探索的機械学習解析で低ヘモグロビン・低アルブミンと合併症の関連を示すが、因果推論と予測性能に限界を残す'
title: 'A Machine Learning Model to Predict Complications Following Head and Neck Microvascular Surgery'
first_author: 'Bonaventure CA'
year: 2026
journal: 'Laryngoscope Investig Otolaryngol'
design: '後ろ向き観察研究・探索的予測モデル'
n: 155
domain_ja: '頭頸部再建'
topic_ja: '頭頸部再建 一般'
---
> [!Data]
> **PDF**
> [bonaventure_LaryngoscopeInvestigOtolaryngol_2026 PDF](file://C:/Users/user/Zotero/storage/5NEL9KUZ/Bonaventure_2026_ML_head_neck_complications_LIO.pdf)
> **Link**
> https://doi.org/10.1002/lio2.70588

# 1 AI要約
![[90_attachments/bonaventure_LaryngoscopeInvestigOtolaryngol_2026/infographic.png]]


## 要約

[[頭頸部再建]]後の欠損部合併症に関わる因子を探索した単施設後ろ向き研究。2022–2025年の遊離皮弁再建155例を対象に、前処理・変換後の116特徴量を用いて関連性の評価と因果構造の仮説生成を行った。著者のエビデンスレベル表記は3である。

相互情報量とSVMによる予測解析に加え、Peter–Clarkアルゴリズム、専門家の知識、LLMの提案を統合し、構造方程式モデルで経路を検討した。全皮弁壊死は5例（3.2%）、欠損部合併症は49例（31.6%）であった。これらの数値は抄録と全文の双方に記載されている。

全文では、低い術前Hb（標準化β=−0.237、P<0.001）とAlb（β=−0.162、P=0.02）が切除部合併症と関連した。非線形SVMの正解率／均衡正解率は0.654、Macro F1は0.538で、予測性能は限定的だった。相互情報量では骨・軟骨放射線壊死、術前Alb、末梢血管疾患が比較的一貫した情報を持った。

術前・術中・術後変数を同じ探索枠組みに含み、治療後バイアスやcollider bias、未測定交絡、少数イベント、高次元性が問題となる。経路の統計的有意性は臨床的因果を証明せず、HbやAlbを補正すれば合併症を減らせるという介入効果も確立していない。外部・前向き検証が必要である。

## AI要約
### **研究の概要**
- 単施設後ろ向き研究（2022–2025年、155例、116特徴量）。
- [[術後合併症評価]]を対象とする予測モデルと探索的因果構造解析。
- 低Hb・低Albと合併症の関連を仮説生成として提示。

### **先行研究との差異および優位性**
- 相互情報量・SVMに加え、PCアルゴリズム、専門家、LLMの候補経路を構造方程式モデルに統合。
- LLMは仮説生成の用途であり、統計解析や臨床判断の代替として使われたものではない。

### **研究手法**
- 単一施設・2名の術者による遊離皮弁再建症例を後ろ向きに収集。
- 80%訓練・20%テストのSVM、ブートストラップ、5分割の相互情報量評価を実施。
- 術前・術中・術後変数を含む。PC探索後の重み付き経路をSEMで評価。

### **結果**
- 全皮弁壊死5/155（3.2%）、欠損部合併症49/155（31.6%）；部分壊死なし。
- 術前Hb：β=−0.237、P<0.001；術前Alb：β=−0.162、P=0.02。
- 非線形RBF-SVM：accuracy/balanced accuracy 0.654、Macro F1 0.538（著者表記）。

### **考察および課題**
- [[研究デザイン]]：観察データからの探索的因果経路であり、因果関係や栄養・貧血介入の有効性を証明しない。
- 術後変数を含むため、純粋な術前予測ツールとしての性能と解釈は分ける必要がある。治療後・collider bias、未測定交絡、カテゴリ変数の符号化や疎な特徴量による見かけの経路に注意。
- 情報源：[PubMed PMID 42870824](https://pubmed.ncbi.nlm.nih.gov/42870824/)と[PMC全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC13657859/)を2026-10-18に照合。
- 抄録確認：155例・116特徴量・5例の壊死・49例の合併症。全文補完：βとP値、SVM性能、術後変数とバイアスの説明。提示ダイジェストの数値は一致。
- PDFはNLM/PMC公式公開データ（CC BY-NC-ND）から取得し、公式MD5と一致。
- [[@hidaka_J.Surg.Oncol._2025 頭頸部遊離皮弁再建術後のComprehensive Complication Index（CCI）による合併症評価の有用性を検討した後向き研究。]]：Hidakaの合併症負荷解析は評価尺度の違いを考える接点になる。BonaventureのCCIはCharlson Comorbidity Indexであり、HidakaのComprehensive Complication Indexとは別の指標である。
- [[@adams_Laryngoscope_2026 頭頸部遊離皮弁215例でトラネキサム酸の使用は輸血も皮弁成績も変えず術後1日目のヘモグロビン低下だけが小さかった後ろ向き研究]]：AdamsのTXA使用と術後Hb低下の観察研究とは、介入とリスクマーカーの区別が論点となる。術前低Hbとの関連から、Hbを補正すれば合併症が減ると推定することはできない。
- DOI：[検証済み原著](https://doi.org/10.1002/lio2.70588)。確認日：2026-10-18。既存論文との関連づけは既存ノートに基づく整理で、新論文で直接比較した結果ではない。
- 保存PDFの第1頁の題名とDOIを抽出して一致を確認（全7頁）。

### **キーワード**
- #head_neck_reconstruction, #free_flap, #machine_learning, #postoperative_complications, #hypoalbuminemia

### **wikilink**
- [[術後合併症評価]]
- [[頭頸部再建]]
- [[研究デザイン]]

# 2 Citation
Bonaventure CA, Bess A, Smith R, Mukhopadhyay S, Mualla R, DiLeo M, Yao C, Kansara S. A Machine Learning Model to Predict Complications Following Head and Neck Microvascular Surgery. Laryngoscope Investig Otolaryngol. 2026;11(5):e70588.

# 3 Related
>[!Info]
> **FirstAuthor**:: Bonaventure CA
> **Title**: A Machine Learning Model to Predict Complications Following Head and Neck Microvascular Surgery
> **Year**: 2026
> **Citekey**: bonaventure_LaryngoscopeInvestigOtolaryngol_2026
> **itemType**: journalArticle
> **Journal**: *Laryngoscope Investig Otolaryngol*
> **Volume**: 11
> **Issue**: 5

> [!Abstract]
>
> OBJECTIVES: Microvascular free tissue transfer is the primary reconstructive method in patients with complex defects of the head and neck. Defect site complications vary; incidence ranges from 15% to 70%. The use of machine learning via mutual information analysis has recently been described in the context of head and neck cancer, but this does not distinguish between causal relationships. The current study explores the first causal machine learning model to predict surgical outcomes in patients undergoing head and neck microvascular reconstruction.
> 
> METHODS: A retrospective chart review was conducted at a single institution from 2022 to 2025. A causal machine learning analysis using Peter-Clark algorithmic discovery, external knowledge inputs, and large language models was performed to determine predictors of complications.
> 
> RESULTS: The dataset included 155 subjects with 116 features. These 116 features were generated from the extracted clinical variables after preprocessing, categorical encoding, numerical transformation, and derivation of model-ready analytic features. Flap failure occurred in 3.2% (n = 5) of patients, and defect site complications occurred in 31.6% (n = 49). Mutual information analysis identified osteoradionecrosis/chondroradionecrosis, preoperative albumin, and peripheral vascular disease as the most consistently informative features. Lower preoperative hemoglobin and albumin were identified as potential causal predictors in the structural model.
> 
> CONCLUSIONS: Causal machine learning analysis is a powerful tool that assists in the prediction of outcomes for patients undergoing head and neck free flap reconstruction and can identify potentially modifiable preoperative factors to aid in risk assessment.
> 
> LEVEL OF EVIDENCE: 3.
