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
n: 150
domain_ja: '頭頸部再建'
topic_ja: '頭頸部再建 一般'
---
> [!Data]
> **PDF**
> [soh_OralMaxillofacSurg_2026 PDF](file://C:/Users/user/Zotero/storage/9UIC5MPH/Soh%20et%20al.%20-%202026%20-%20Comparison%20of%20multivariate%20linear%20regression%20and%20random%20forest%20model%20in%20developing%20mandibular%20chin%20p.pdf)
> **Link**
> https://doi.org/10.1007/s10006-026-01644-3

# 1 AI要約


## 要約

正中を越えて下顎を広く切除すると、元のオトガイの形の手がかりが残らず、どの幅で再建すればよいか分からなくなる。北京大学口腔医学院は、**残っている中顔面の寸法から元のオトガイ幅を予測する式**を、頭部CTの計測から作った。予測に使ったのは**上顎の犬歯間距離、左右の頬骨の間の距離、梨状口の幅**である。

普通の重回帰（最小二乗法）とランダムフォレスト（機械学習）を比べると、**重回帰の誤差は平均2.35mm**で、予測値と実測値に有意差はなかった（P=0.092）。500回のブートストラップでも誤差2.45mmと安定しており、**機械学習は精度を上げなかった**。著者らは、単純な回帰式のほうが解釈しやすく、計算資源の限られた施設でも術前計画に使えるとした。

**ただし予測の力は弱い。** 決定係数R²は0.25（ブートストラップで0.17）で、オトガイ幅の個人差の2割前後しか説明できていない。予測と実測で「有意差がない」のは、平均としてずれていないことを示すだけで、一人ひとりで一致することの証明ではない。もとになったのは**病変のない中国人の成人150例**のCTで、3つの寸法とオトガイ幅の相関はそれぞれ0.41、0.35、0.33と弱い。検証に使った40例も同じ施設のデータである。実際の再建で使ったのは腓骨再建の1例の提示だけで、結果を確かめたわけではない。

なお、ダイジェストでは上顎の語で上顎の論文として分類されていたが、内容は**下顎の正中の再建**である。

## AI要約
### **研究の概要**
- 正中を越える下顎欠損の再建で、**元のオトガイ幅を中顔面の寸法から予測する式**を作り、**重回帰とランダムフォレスト**を比べたCT計測研究。
- 北京大学口腔医学院 口腔顎顔面外科。

### **先行研究との差異および優位性**
- 対側の下顎が残らない**正中越えの欠損**では、鏡像で形を決める方法が使えない。その代わりに**残っている上顔面・中顔面の寸法**から予測するという発想。
- 機械学習が単純な回帰に勝てなかったことを、そのまま報告している。

### **研究手法**
- 対象: 北京大学口腔医学院で2020-2023年に撮影された頭頸部CTのうち、**18-55歳、全歯列、先天奇形・外傷・腫瘍・顎矯正手術の既往なし**の150例。ProPlan CMF で上下顎の3Dモデルを作り、計測点を手動で設定。
- 候補の説明変数は16（SNA・SNB・ANB、頬骨上顎縫合間、頬骨突起間、上顎犬歯間、梨状口幅、下顎角間、下顎頭間、下顎体長など）。
- 目的変数: オトガイの幅。説明変数: 上顎犬歯間距離、両側頬骨間距離、梨状口幅など。
- 重回帰（最小二乗法）と、訓練80%・検証20%に分けたランダムフォレストを比較。ブートストラップ500回で検証。
- 評価: 平均絶対誤差（MAE）、決定係数（R²）、予測と実測の対応のあるt検定。
- 検証: 同じ施設の別の40例（2023-2024年）で予測と実測を対応のあるt検定で比較。
- 計測の信頼性: 30例を再計測し級内相関係数（ICC）で評価。
- Springer（非OA）。PDFは `head_neck_general/fulltext/` に取得済み（要約作成にのみ使用）。

### **結果**
- **150例**（男87・女63、全員中国人）。
- オトガイ幅との相関: **上顎犬歯間 r=0.41、頬骨上顎縫合間 r=0.35、梨状口幅 r=0.33**。下顎角間 0.24、下顎体長 0.23-0.25。SNA・SNBなどの角度はほぼ無相関。
- **重回帰（3変数）: MAE 2.35 mm、RMSE 3.03 mm、R² 0.25。** 予測と実測の相関 r=0.476。
- **ブートストラップ500回: MAE 2.45 mm（95%CI 2.09-2.82）、R² 0.17。**
- 同じ3変数のランダムフォレスト: MAE 2.96 mm（ブートストラップ 2.68 mm）で重回帰より悪い。
- 下顎の変数（下顎角間距離・左右の下顎体長）を使ったランダムフォレスト: MAE 2.71 mm、**R² 0.42**。
- 検証40例: 予測と実測に有意差なし（P=0.092）。**予測はやや大きめに出る傾向。**
- オトガイ幅の計測の検者間信頼性: **ICC 0.78**（0.65-0.87）。
- 症例提示: 65歳女性、前方下顎のエナメル上皮腫。両側の区域切除後、予測したオトガイ幅で腓骨再建を計画。

### **考察および課題**
- **機械学習が単純な回帰に勝てなかった**のは、説明変数が少なく関係がほぼ直線的な場合には当然の結果で、正直な報告として評価できる。
- ⚠️ **予測の力は弱い。** R² 0.25（0.17）は、オトガイ幅の個人差の大半を説明できていないことを意味する。3つの寸法との相関はどれも0.4前後で、予測と実測の相関も0.48にとどまる。抄録の「満足できる性能」は言いすぎ。
- ⚠️ **計測そのものの誤差が大きい。** オトガイ幅の検者間信頼性は ICC 0.78 で、予測の誤差（2-3mm）には計測のばらつきも含まれる。
- ⚠️ **検証は同じ施設の同じ民族の40例**で、外部検証とは言えない。他の集団（日本人を含む）で使えるかは分からない。
- **下顎の寸法を使えば予測は良くなる**（R² 0.42）が、再建が必要な患者ではその寸法が失われている、というのがこの問題の核心である。
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
