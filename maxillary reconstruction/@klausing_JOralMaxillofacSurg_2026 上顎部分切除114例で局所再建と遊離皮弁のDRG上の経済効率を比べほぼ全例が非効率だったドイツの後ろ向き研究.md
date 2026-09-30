---
tags:
  - PMID/42800476
citekey: "klausing_JOralMaxillofacSurg_2026"
dateread: '2026-09-29'
read: false
topic: maxillary_reconstruction
domain: head_neck
relevance: medium
arm: health-economics
title_ja: '上顎部分切除114例で局所再建と遊離皮弁のDRG上の経済効率を比べほぼ全例が非効率だったドイツの後ろ向き研究'
title: 'Economic Inefficiency in Maxillary Reconstruction: Patient-Specific Determinants and Implications for Reconstructive Strategy.'
first_author: 'Klausing A'
year: 2026
journal: 'J Oral Maxillofac Surg'
design: 'Retrospective cohort'
n: 114
domain_ja: '頭頸部再建'
topic_ja: '上顎・中顔面再建'
---
> [!Data]
> **PDF**
> [Klausing_2026_maxillary_reconstruction_DRG_economic_inefficiency_JOMS.pdf](file://C:/Users/user/claude/papers/maxillary_reconstruction/fulltext/Klausing_2026_maxillary_reconstruction_DRG_economic_inefficiency_JOMS.pdf)
> **Link**
> https://doi.org/10.1016/j.joms.2026.08.021

# 1 AI要約
![[90_attachments/klausing_JOralMaxillofacSurg_2026/infographic.png]]


## 要約

上顎を部分切除したあと、局所の再建で済ませるのと遊離皮弁で再建するのとでは、どちらが病院の経済効率が良いのか。ドイツのボン大学病院が、2010年から2025年に悪性腫瘍で上顎部分切除を受けた**114例**（局所再建70例、遊離皮弁44例）を、ドイツの包括支払い制度（DRG）の基準で調べた。

局所再建の中身は、粘膜前進弁27、頬脂肪体17、鼻唇溝皮弁7、一時的な栓塞子（obturator）19で、遊離皮弁は**前腕35**、外側広筋3、腓骨5、肩甲骨1だった。骨付きの再建は6例しかない。

**実際の入院は遊離皮弁のほうが長かった。** 在院日数の中央値は局所12日、遊離20.5日（P<.001）、手術時間は232分と598分である。それでも論文が「遊離皮弁のほうが効率的」と言えるのは、「効率」を**DRGが想定する在院日数に対する相対値**で測っているからである。DRGは遊離皮弁に19.9日、局所再建に11.0日を割り当てており、遊離皮弁は長く入院しても割当ての範囲に収まりやすい。ICUの割当ても局所€1130、遊離€2340で、1日€1400かかるので、局所再建は**ICUに1日入っただけで「非効率」**になる。

定義の影響はさらに大きい。「退院の遅れ」を想定在院日数の後半での退院と定義したため、96.5%がこれに当たり、**114例中112例（98.3%）が「非効率」**になった。著者ら自身、「効率的」が2例しかないので複合エンドポイントの多変量解析は推定できないと認めており、項目別のモデルでもどの因子も有意ではなかった。それでも同じエンドポイントで個人ごとの予測モデルを作り、**「84.6%の患者で遊離皮弁のほうが効率的」**と抄録に書いている。

**この研究が示したのは、遊離皮弁の方が安いということではなく、DRGの割当てが遊離皮弁に手厚いということである。** 局所再建が「高くつく」ように見えるのは、制度の割当てが少ないためで、実際の資源の消費（入院日数・手術時間）は遊離皮弁の方が大きい。

## AI要約
### **研究の概要**
- 上顎部分切除後の**局所再建と遊離皮弁**を、ドイツの**DRG（包括支払い）での入院の経済効率**で比べた後ろ向きコホート研究。
- 個人ごとの**反実仮想モデル**で、どちらの再建が効率的かを予測した。
- ドイツ・ボン大学病院 口腔顎顔面・形成外科。

### **先行研究との差異および優位性**
- 上顎再建の選択を、成績ではなく**病院の経済効率**から評価した。
- 「局所再建は安い」という通念に、データで反論しようとした。

### **研究手法**
- 後ろ向きコホート研究。単施設、2010-2025年。悪性腫瘍に対する上顎部分切除。記録不備・経済データ欠損は除外（117例中3例）。
- 説明変数: 再建法（局所 vs 遊離）、年齢、性別、ASA分類、Charlson併存症指数、Functional Comorbidity Index。
- 主要評価項目: **入院の経済効率**（効率的／非効率の2値）。非効率 = DRGの目標在院日数の超過、DRGの上限在院日数の超過、償還範囲を超えるICU/IMC利用のいずれか。
- 統計: 多変量ロジスティック回帰、決定木、個人ごとの反実仮想分析（各患者が逆の再建を受けた場合の効率の確率を推定）。
- **非効率の定義の中身**: (1)「退院の遅れ」＝症例ごとのDRG想定在院日数に対して第3・第4四分位で退院、(2) DRGの上限在院日数の超過、(3) ICU/IMCの利用がDRGの償還範囲（局所€1130、遊離€2340、1日€1400で換算）を超える。
- ICU/IMCへの入室は再建法ではなく施設の基準（気道、心肺の併存症、高齢、長時間麻酔など）で決めた。
- 複合エンドポイントは完全分離のため調整ORを推定できず、項目別のモデルを副次解析とした。
- 反実仮想: 再建法と臨床因子の交互作用を含むロジスティックモデルで、各患者が両方の再建を受けた場合の「効率的」の確率を予測。
- Elsevier（非OA）。PDFは `maxillary_reconstruction/fulltext/` に取得済み（要約作成にのみ使用）。

### **結果**
- **114例**: 女65・男49、平均69.1歳。扁平上皮癌79.8%。**局所再建70**（粘膜前進弁27、頬脂肪体17、鼻唇溝皮弁7、一時的な栓塞子19）、**遊離皮弁44**（前腕35、外側広筋3、腓骨5、肩甲骨1）。
- ASA・Charlson・FCIは両群で差なし。
- **手術時間: 局所232分 vs 遊離598分（P<.001）。**
- **在院日数: 中央値 12日 vs 20.5日、平均 15.3日 vs 23.6日（P<.001）。**
- DRGの想定在院日数: **局所11.0日 vs 遊離19.9日**、上限 21.5日 vs 35.5日。
- 想定の前半で退院できたのは全体で4例（3.5%）。第4四分位での退院は局所92.9%、遊離88.6%。
- **DRG上限超過: 局所20.0%（14/70）vs 遊離11.4%（5/44）、P=.164。**
- ICU/IMC入室 66.4%。ICUは局所7例・遊離19例。ICU/IMCの償還 **局所€1130 vs 遊離€2340**（1日€1400）。**償還超過: 局所48.6%（34/70）vs 遊離36.4%（16/44）、P=.2。**
- **非効率（複合）: 112/114（98.3%）。** 完全分離で調整ORは推定不能。項目別モデル（退院の遅れ・上限超過・ICU超過）でも**有意な因子なし**。
- FCI 1以上で非効率 95.3% vs 79.3%（P=.017、閾値の探索的検定）。
- 反実仮想の予測: **84.6%で遊離皮弁の方が「効率的」**。

### **考察および課題**
- ⚠️ **「効率」はDRGの割当てに対する相対値で、実際の費用ではない。** 遊離皮弁は入院が8日長く、手術時間も2.5倍だった。それでも「効率的」に見えるのは、DRGが遊離皮弁に長い在院日数とICU費用を割り当てているからである。**示されたのは「遊離皮弁が安い」ではなく「DRGが遊離皮弁に手厚い」**。
- ⚠️ **ほぼ全例が非効率になる定義。** 想定在院日数の後半での退院を「遅れ」とする定義では、96.5%が該当する。98.3%が非効率という結果は、患者や再建法の違いより定義の産物である。
- ⚠️ **84.6%は根拠にならない。** 著者自身が完全分離で推定不能と認めた複合エンドポイントで、交互作用を含むモデルから個人ごとの予測を出している。項目別のモデルでは何も有意でなかった。
- ⚠️ **比べている再建が違う。** 局所再建には一時的な栓塞子19例が含まれ、遊離皮弁の8割は前腕皮弁である。欠損の大きさの比較もない。上顎の骨を再建する症例（骨付き6例）についてはほとんど何も言えない。
- それでも、**局所再建でもICU・在院日数が長くなり、DRG上は損が出やすい**という観察には意味がある。「局所再建だから安い」とは限らない。ただし日本のDPCは点数設計が違うので、この数字は使えない。
- 本プロジェクトの問い（腓骨単独か、腓骨＋軟部皮弁か）には直接答えない。[[骨移植 vs 軟部再建]] の経済面を考えるなら、実際の費用を測った研究が必要である。
- [[上顎再建]]、[[遊離皮弁]] に整理した。

### **キーワード**
- #maxillary_reconstruction, #health_economics, #DRG, #local_flap, #free_flap, #retrospective_cohort

### **wikilink**
- [[上顎再建]]
- [[遊離皮弁]]
- [[骨移植 vs 軟部再建]]

# 2 Citation
Klausing A, Maier F, Thol F, Far F, Kramer FJ. Economic Inefficiency in Maxillary Reconstruction: Patient-Specific Determinants and Implications for Reconstructive Strategy.. J Oral Maxillofac Surg. 2026;Epub ahead of print.

# 3 Related
>[!Info]
> **FirstAuthor**:: Klausing A
> **Title**: Economic Inefficiency in Maxillary Reconstruction: Patient-Specific Determinants and Implications for Reconstructive Strategy.
> **Year**: 2026
> **Citekey**: klausing_JOralMaxillofacSurg_2026
> **itemType**: journalArticle
> **Journal**: *J Oral Maxillofac Surg*
> **Volume**: 
> **Issue**: 

> [!Abstract]
>
> Maxillary reconstruction after oncologic resection uses substantial hospital resources, but its economic efficiency within diagnosis-related group (DRG)-based reimbursement remains unclear. To identify determinants of economic inefficiency after partial maxillectomy. This retrospective single-center cohort study was conducted at University Hospital Bonn, Germany, and included patients undergoing partial maxillectomy for malignant tumors between 2010 and 2025. Patients with incomplete records or missing health-economic variables were excluded. Predictor variables were reconstructive strategy (local vs microvascular), age, sex, American Society of Anesthesiologists physical status classification, Charlson Comorbidity Index, and Functional Comorbidity Index. The primary outcome was inpatient economic efficiency, dichotomized as efficient or inefficient. Inefficiency was defined by prolonged hospitalization relative to DRG-specific length of stay targets, exceeding the DRG upper length of stay threshold, or intensive care unit/intermediate care unit utilization beyond reimbursed limits. Not applicable. All analyzed variables were incorporated as predictor variables. Multivariable logistic regression was used to identify predictors of inpatient economic inefficiency. Decision tree modelling and subject-level counterfactual analysis estimated individualized efficiency probabilities for both reconstructive strategies. Statistical significance was defined as P < .05. Of 117 eligible patients, 114 (97.4%) were included after 3 exclusions with incomplete data. The sample comprised 65 females (57.0%) and 49 males (43.0%); mean age was 69.1 (SD 14.4) years. Local reconstruction was performed in 70 subjects (61.4%) and microvascular reconstruction in 44 (38.6%). Economic inefficiency occurred in 112 subjects (98.3%), and 19 (16.7%) exceeded the DRG upper length of stay threshold. Intensive care unit/intermediate care overuse occurred in 34 of 70 locally reconstructed subjects (48.6%) and 16 of 44 microvascularly reconstructed subjects (36.4%; P = .2). Subject-level modelling predicted microvascular reconstruction as the economically more efficient strategy in 84.6% of subjects. Economic efficiency after maxillary reconstruction was associated with the interaction between patient-specific risk factors and reconstructive strategy rather than surgical complexity alone. In subject-level modelling, microvascular reconstruction was predicted to be the economically more efficient strategy in 84.6% of subjects, suggesting that assumptions regarding the inherent cost-effectiveness of local reconstruction should be reconsidered and may support more efficient resource allocation under DRG-based reimbursement.
