---
tags:
  - PMID/42791924
citekey: "ceddia_BioengineeringBasel_2026"
dateread: '2026-09-29'
read: false
topic: head_neck_general
domain: head_neck
title_ja: '腓骨で再建した下顎の患者固有モデルで長さ3・5・12mmのインプラントの応力とひずみを比べた有限要素解析'
title: 'Finite Element Analysis of Ultra-Short, Extra-Short, and Conventional Dental Implants in Fibula Free Flap Mandibular Reconstruction.'
first_author: 'Ceddia M'
year: 2026
journal: 'Bioengineering (Basel)'
design: 'Finite element analysis'
n: 1
domain_ja: '頭頸部再建'
topic_ja: '頭頸部再建 一般'
---
> [!Data]
> **PDF**
> [Ceddia_2026_short_implants_fibula_mandible_FEA_Bioengineering.pdf](file://C:/Users/user/claude/papers/head_neck_general/fulltext/Ceddia_2026_short_implants_fibula_mandible_FEA_Bioengineering.pdf)
> **Link**
> https://doi.org/10.3390/bioengineering13091052

# 1 AI要約


## 要約

腓骨で下顎を再建すると、腓骨は元の歯槽堤より低いので、長いインプラントを入れる高さが足りないことがある。では短いインプラントで力学的に問題ないのか。イタリアのバーリ工科大学が、**1人の患者（口底癌で下顎角から犬歯部まで切除し腓骨で再建）のCTから作った有限要素モデル**で、**直径4mm・長さ3、5、12mmのインプラント3本**をチタンバーで連結した場合を比べた。

条件は**術直後**を想定し、咬合力は生理的な値の12.5%（片側40N）、インプラントと骨はまだ骨結合していない摩擦接触とした。

**インプラント自体の応力（36.8-37.1 MPa）と腓骨の皮質骨の応力（52.5-53.1 MPa）は、長さによってほとんど変わらなかった。** 違いが出たのは周りで、**5mmで周囲骨のひずみと後方の再建プレートの応力が最も小さく**（プレート 71.3 MPa、3mm 75.4、12mm 107.8）、**12mmでは根尖側にひずみが集中**し、骨の微小損傷の目安（0.004）を超える部分があった。著者らは、腓骨の高さが足りないときに短いインプラントは力学的に選択肢になりうるとした。

**ただし1人のモデル、1つの荷重条件、術直後だけの静的な解析**である。骨結合後の通常の咬合力、繰り返しの荷重、照射された骨は再現していない。プレートの応力はどれもチタンが壊れる値の9-13%にすぎず、差に臨床的な意味があるかは分からない。

## AI要約
### **研究の概要**
- 腓骨で再建した下顎に入れる**インプラントの長さ（3・5・12mm）**で、インプラント・骨・固定プレートにかかる力がどう変わるかを調べた**有限要素解析**。
- 1人の患者から作ったモデル。術直後の咬合を想定。
- イタリア・バーリ工科大学（機械工学）。

### **先行研究との差異および優位性**
- 腓骨再建下顎で、**インプラントの長さと連結（スプリント）の組み合わせ**を患者固有のモデルで調べたのは初めてとしている。
- インプラントだけでなく、**再建プレート・ミニプレート・残存下顎**への力の伝わり方まで見ている。

### **研究手法**
- 有限要素解析。Ruf らのモデル（57歳女性、口底の扁平上皮癌、下顎角〜右犬歯部の区域切除を腓骨で再建）を使用。
- 固定: 下顎角部に厚さ2mmの再建プレート（両皮質スクリュー7本）、前方にミニプレート2枚。
- インプラント: 直径4mm、長さ3・5・12mmを各3本、腓骨の頂部に埋入し、チタンバーで連結。
- 荷重: 片側の大臼歯部での噛みしめ。咀嚼筋の力は生理的な値の**12.5%（片側40N）**で術直後を想定。患側の浅咬筋は切離、深咬筋は50%。
- 境界条件: 顆頭は固定、**インプラントと骨は摩擦接触（骨結合なし）**、仮骨は肉芽組織の物性。
- 皮質骨は直交異方性・線形弾性、他は等方性。
- 評価: von Mises 応力（プレートはチタンの降伏応力830 MPa、骨は引張強さ133 MPaと比較）、インプラント周囲1mmの骨のひずみ（閾値0.004）。
- CC-BY。全文・PDFとも `head_neck_general/fulltext/` に取得済み。

### **結果**
- **インプラントの応力: 36.8-37.1 MPa**（長さでほぼ不変）。
- **腓骨の皮質骨: 52.5（5mm）・52.7（3mm）・53.1（12mm）MPa**。最大は遠位の骨切り部の頂部。
- **後方の再建プレート: 3mm 75.4、5mm 71.3、12mm 107.8 MPa**。降伏応力に対する割合 9.1%・8.6%・13.0%。
- 前方の上ミニプレート: 56.8・57.4・62.2 MPa（長さとともに増加）。
- 残存下顎: 3mm 51.6、5mm 47.8、12mm 56.8 MPa。
- **周囲骨のひずみ（遠位・中央・近心）**: 3mm 0.0035・0.0016・0.0034、**5mm 0.0027・0.0012・0.0023**、12mm 0.0038・**0.0045・0.0047**（中央・近心で閾値0.004超）。
- 健側での噛みしめでは、どの部位の応力も患側より低い。

### **考察および課題**
- **「腓骨の高さが足りないなら短いインプラントでもよい」という臨床の判断を、力学の面から支える材料**にはなる。臨床でも短いインプラントの生存は97-100%と報告されている。
- ⚠️ **一般化はできない。** 1人のモデル、1つの荷重（術直後の40N）、静的な解析で、骨結合後の通常の咬合力・繰り返し荷重（疲労）・照射骨の脆さは再現していない（著者も明記）。3mmより5mmが良いという順位も、この1条件での結果にすぎない。
- ⚠️ **差の臨床的な意味は不明。** プレートの応力は最大でもチタンの降伏応力の13%で、どの長さでも破損の域からは遠い。12mmの根尖側のひずみが閾値を少し超えたのが最も意味のありそうな所見だが、これも術直後の条件での話である。
- 照射された骨では短いインプラントの失敗が多いとする古い報告もあり、**照射例に当てはめるときは慎重に**。
- 腓骨を下顎下縁に合わせると歯槽堤との高さの差が大きくなる、という根本の問題への対処（折り畳み腓骨など）は [[下顎再建]] と [[歯科リハビリテーション]] を参照。
- [[遊離腓骨皮弁]]、[[再建プレート合併症]] に整理した。

### **キーワード**
- #finite_element_analysis, #dental_implant, #short_implant, #fibula_flap, #mandibular_reconstruction

### **wikilink**
- [[下顎再建]]
- [[歯科リハビリテーション]]
- [[遊離腓骨皮弁]]
- [[再建プレート合併症]]
- [[血管柄付き骨移植]]

# 2 Citation
Ceddia M, Lamberti L, Trentadue B. Finite Element Analysis of Ultra-Short, Extra-Short, and Conventional Dental Implants in Fibula Free Flap Mandibular Reconstruction.. Bioengineering (Basel). 2026;13(9):1052.

# 3 Related
>[!Info]
> **FirstAuthor**:: Ceddia M
> **Title**: Finite Element Analysis of Ultra-Short, Extra-Short, and Conventional Dental Implants in Fibula Free Flap Mandibular Reconstruction.
> **Year**: 2026
> **Citekey**: ceddia_BioengineeringBasel_2026
> **itemType**: journalArticle
> **Journal**: *Bioengineering (Basel)*
> **Volume**: 13
> **Issue**: 9

> [!Abstract]
>
> Dental rehabilitation of fibula free flap mandibular reconstructions can be limited by the reduced vertical bone height available for implant placement. This study evaluated the biomechanical influence of ultra-short, extra-short, and conventional implants in a reconstructed fibula. A patient-specific finite element model of a fibula-reconstructed mandible was developed. Three splinted implants with a diameter of 4 mm and lengths of 3, 5, or 12 mm were compared under postoperative unilateral molar loading. Von Mises stresses were evaluated in the implants, fibula, residual mandible, and fixation plates, while equivalent elastic strain was assessed in peri-implant bone. Implant length had minimal influence on implant stress (36.8-37.1 MPa) and fibular cortical bone stress (52.5-53.1 MPa). The 5 mm implants produced the lowest peri-implant strains and the lowest posterior reconstruction-plate stress (71.3 MPa), compared with 75.4 MPa for 3 mm and 107.8 MPa for 12 mm implants. The 12 mm implants generated greater apical strain concentrations, exceeding the adopted mechanobiological threshold around the central and mesial implants. Within the limitations of this study and under the simulated immediate postoperative loading condition, shorter implants, particularly 5 mm implants, showed a favorable biomechanical response.
