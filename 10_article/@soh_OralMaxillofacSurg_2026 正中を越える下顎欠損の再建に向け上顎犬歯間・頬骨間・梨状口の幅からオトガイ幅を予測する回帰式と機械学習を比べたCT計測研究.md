---
tags:
  - PMID/42809024
citekey: "soh_OralMaxillofacSurg_2026"
dateread: '2026-09-30'
read: false
topic: head_neck_general
domain: head_neck
title_ja: '正中を越える下顎欠損の再建に向け上顎犬歯間・頬骨間・梨状口の幅からオトガイ幅を予測する回帰式と機械学習を比べたCT計測研究'
title: 'Comparison of multivariate linear regression and random forest model in developing mandibular chin prediction reconstruction equation.'
first_author: 'Soh HY'
year: 2026
journal: 'Oral Maxillofac Surg'
design: 'CT morphometric prediction study'
domain_ja: '頭頸部再建'
topic_ja: '頭頸部再建 一般'
---
> [!Data]
> **PDF**
> （全文なし）
> **Link**
> https://doi.org/10.1007/s10006-026-01644-3

# 1 AI要約
![[90_attachments/soh_OralMaxillofacSurg_2026/infographic.png]]


## 要約

正中を越えて下顎を広く切除すると、元のオトガイの形の手がかりが残らず、どの幅で再建すればよいか分からなくなる。北京大学口腔医学院は、**残っている中顔面の寸法から元のオトガイ幅を予測する式**を、頭部CTの計測から作った。予測に使ったのは**上顎の犬歯間距離、左右の頬骨の間の距離、梨状口の幅**である。

普通の重回帰（最小二乗法）とランダムフォレスト（機械学習）を比べると、**重回帰の誤差は平均2.35mm**で、予測値と実測値に有意差はなかった（P=0.092）。500回のブートストラップでも誤差2.45mmと安定しており、**機械学習は精度を上げなかった**。著者らは、単純な回帰式のほうが解釈しやすく、計算資源の限られた施設でも術前計画に使えるとした。

**ただし予測の力は弱い。** 決定係数R²は0.25（ブートストラップで0.17）で、オトガイ幅の個人差の2割前後しか説明できていない。予測と実測で「有意差がない」のは、平均としてずれていないことを示すだけで、一人ひとりで一致することの証明ではない。症例数も抄録には書かれておらず、実際の再建で使って結果を確かめたわけでもない。

なお、ダイジェストでは上顎の語で上顎の論文として分類されていたが、内容は**下顎の正中の再建**である。

## AI要約
### **研究の概要**
- 正中を越える下顎欠損の再建で、**元のオトガイ幅を中顔面の寸法から予測する式**を作り、**重回帰とランダムフォレスト**を比べたCT計測研究。
- 北京大学口腔医学院 口腔顎顔面外科。

### **先行研究との差異および優位性**
- 対側の下顎が残らない**正中越えの欠損**では、鏡像で形を決める方法が使えない。その代わりに**残っている上顔面・中顔面の寸法**から予測するという発想。
- 機械学習が単純な回帰に勝てなかったことを、そのまま報告している。

### **研究手法**
- 頭部CTから解剖学的な計測点と寸法を抽出（対象と人数は抄録に記載なし）。
- 目的変数: オトガイの幅。説明変数: 上顎犬歯間距離、両側頬骨間距離、梨状口幅など。
- 重回帰（最小二乗法）と、訓練80%・検証20%に分けたランダムフォレストを比較。ブートストラップ500回で検証。
- 評価: 平均絶対誤差（MAE）、決定係数（R²）、予測と実測の対応のあるt検定。
- 本文未入手（Springer、非OA）。以下は抄録による。

### **結果**
- 上顎犬歯間距離・両側頬骨間距離・梨状口幅が、オトガイ幅と相関。
- **重回帰: MAE 2.35 mm、R² 0.25。** 予測と実測の差 P=0.092（対応のあるt検定）。
- **ブートストラップ500回: MAE 2.45 mm、R² 0.17。**
- 同じ説明変数のランダムフォレストは、重回帰より誤差が大きかった。

### **考察および課題**
- **機械学習が単純な回帰に勝てなかった**のは、説明変数が少なく関係がほぼ直線的な場合には当然の結果で、正直な報告として評価できる。
- ⚠️ **予測の力は弱い。** R² 0.25（0.17）は、オトガイ幅の個人差の大半を説明できていないことを意味する。MAE 2.35mmがオトガイ幅に対してどの程度の誤差かも抄録からは分からない。抄録の「満足できる性能」は言いすぎ。
- ⚠️ **「有意差なし」は一致の証明ではない。** 対応のあるt検定は平均の偏りを見るだけで、個々の予測誤差の大きさ（Bland-Altman の一致限界など）は示していない。
- 実務では、正中越えの欠損でも**術前CTに元の下顎が写っていれば、それを使って計画する**のが普通で、この式が必要になるのは腫瘍で形が崩れている場合や二次再建の場合に限られる（[[バーチャルサージカルプランニング]]）。
- [[下顎再建]] に整理した。

### **キーワード**
- #mandibular_reconstruction, #chin, #prediction_model, #machine_learning, #CT_morphometry

### **wikilink**
- [[下顎再建]]
- [[バーチャルサージカルプランニング]]
- [[遊離腓骨皮弁]]

# 2 Citation
Soh HY, Yu Y, Feng Z, Du W, Liu S, Peng X, Zhang WB. Comparison of multivariate linear regression and random forest model in developing mandibular chin prediction reconstruction equation.. Oral Maxillofac Surg. 2026;30(1).

# 3 Related
>[!Info]
> **FirstAuthor**:: Soh HY
> **Title**: Comparison of multivariate linear regression and random forest model in developing mandibular chin prediction reconstruction equation.
> **Year**: 2026
> **Citekey**: soh_OralMaxillofacSurg_2026
> **itemType**: journalArticle
> **Journal**: *Oral Maxillofac Surg*
> **Volume**: 
> **Issue**: 

> [!Abstract]
>
> Reconstruction of extensive mandibular defects that cross midline is technically challenging, as the surgeons lack normal anatomical references. This study aims to compare multivariate linear regression and machine learning (random forest) algorithms in predicting the premorbid shape of the mandibular chin to guide surgical reconstruction. Anatomical landmarks and measurements were extracted from the computed tomography (CT) data of the head. The multivariate regression model was developed based on Ordinary Least Squares (OLS), while the dataset was randomly split into training set (80%) and testing set (20%) to develop a machine learning-based algorithm. Correlation was observed among the maxillary intercanine distance, distance of bilateral zygoma, width of piriform aperture and the width of chin in multivariate linear regression model, and satisfactory performance was achieved, (MAE (2.35), R² (0.25)). No significant difference was noted between the predicted width of chin and actual measurement in paired t-test. (P = 0.092) Bootstrap validation with 500 repetitions demonstrated stable performance (MAE 2.45 mm; R² = 0.17). Machine learning models using the same predictors did not improve predictive accuracy. Both models demonstrated comparable accuracy in predicting chin width; however, the multivariate regression model achieved lower prediction error compared with machine learning approaches using the same predictors. The interpretability and simplicity of multivariate linear regression may make it more clinically practical for reconstructing midline mandibular defects. A straightforward regression model can provide surgeons with a reliable, accessible tool for preoperative planning in complex mandibular reconstructions, especially where advanced computational resources are limited.
