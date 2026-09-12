# このVaultのルール

AI（Claude）がこのvaultで作業するとき、必ずこれに従う。
迷ったら既存ノートの書き方に合わせる。形式を変えたくなったら勝手に変えず先に相談する。

---

## 1. 三層構造 — どこに何を置くか

| 層 | 実体 | AIの権限 |
|---|---|---|
| **原典 raw** | Zotero `C:\Users\user\Zotero` | **読むだけ。書き換え禁止** |
| **ノート wiki** | このvault | 書いてよい |
| **閲覧** | Obsidian | 人が読む |

- `zotero.sqlite` と `storage\` には一切書き込まない。PDFのリネーム・移動・削除も禁止。
- **PDFはvaultに置かない。** 文献を増やすときは Zotero にインポートする。
- vaultはgit管理下。`.git\` `.obsidian\` `key.txt` `token.txt` に触らない。

---

## 2. 論文ノート

### 起点は必ず Zotero

citekey は Better BibTeX が付けたものだけを使う。**AIがcitekeyを創作しない。**
Zoteroに実体がない文献のノートを先に作らない。順序は固定:

1. Zoteroに登録（RIS取込 / ブラウザコネクタ）
2. `zotero.bib` から citekey を読む（DOIで照合する。推測しない）
3. `papers\<topic>\notes_content.json` に内容を書き、**`build_vault_notes.ps1` でノートを生成する**

### ⚠️ Obsidian の Zotero Integration でノートを作らない（2026-09-12 決定）

ノートを作る経路は **`build_vault_notes.ps1` の1つだけ**にする。
Zotero Integration プラグインでも同じ論文のノートを作ると、ファイル名が違うため
**2つのノートができ、wikilinkは片方にしか張られない。**
実際に4組（stigger / mallik / cordeiro / deng）が重複していた。

ビルダーは `# 1 AI要約` に加えて **`# 2 Citation`・`# 3 Related`・`> [!Abstract]` も
Zotero Integration と同じ形式で出力する**ので、プラグインを使わなくても情報は落ちない。
重複の検査は `check.ps1` の項目7b。

### ファイル名

`@<citekey> <日本語の要約タイトル>.md`

日本語タイトルは「何を・どう調べた・何研究か」が一文で分かるようにする。
例: `@makiuchi_Microsurgery_2025-頸部郭清術や放射線治療歴が受容血管選択と皮弁不全に与える影響を671症例で解析した後方視的研究。.md`

### 置き場所

| 内容 | 場所 |
|---|---|
| 特定プロジェクトの文献 | `<プロジェクト名>\`（例 `traumatic neuroma\`） |
| それ以外 | `10_article\` |
| 図・インフォグラフィック | `90_attachments\<citekey>\` |

---

## 3. AI要約の書式（固定）

`# 1 AI要約` の下は必ずこの構成。増減させない。

```
## 要約            ← 読み物としての要約
## AI要約
### **研究の概要**
### **先行研究との差異および優位性**
### **研究手法**
### **結果**
### **考察および課題**
### **キーワード**
### **wikilink**
```

**`## 要約` と `## AI要約` は役割が違う。**

- `## 要約` — **読んで理解するための文章。** 段落で書く。箇条書きにしない。
  何が問題で、何をして、何が分かり、それが何を意味するか、を通して読める形にする。
  3〜4段落程度。全文を読んだ場合は、**抄録だけでは分からなかった点を必ず書く。**
- `## AI要約` 以下 — **抽出データ。** 箇条書きで、後から表にできる粒度にする。

- **結果には必ず実数を書く。** n、%、p値、HR、95%CI、追跡期間。
  「有意に高かった」で終わらせない。後から表にできる粒度にする。
- **キーワード** は `- #tag1, #tag2, #tag3` の1行形式。
- **wikilink** は `- [[概念名]]` の箇条書き。既存の概念ノートがあれば必ずそれに合わせる。

---

## 4. 概念ノート — これが「思い出せる」を作る

論文ノートだけでは論文単位の記憶しかできない。**論文をまたいで結び直すのが概念ノート。**

- 置き場所: `20_concept\<概念名>.md`
- 論文ノートの `### **wikilink**` から張られたリンクの受け皿になる
- 構成は「定義」「このvaultでの知見」「論点」「関連概念」
- **知見には実数を書き、必ず出典の論文ノートへ張り返す**
- **論点**が最も価値がある。文献間の食い違い・欠落・未検証の前提をここに書く

### 名前は日本語、表記ゆれは aliases に集約する

**既存と似た名前のノートを増やさない。** `[[遊離腓骨皮弁]]` と `[[腓骨皮弁]]` を
併存させてはいけない。正式名を日本語1つに決め、英語表記も略語も表記ゆれも
frontmatter の `aliases` に全部登録する。

```yaml
aliases:
  - "Fibula Free Flap"
  - "腓骨皮弁"
  - "fibula flap"
```

Obsidianのaliasはリンク解決に効くので、**既存ノートを1文字も書き換えずに
切れていたリンクが繋がる。** 新しい概念を作る前に必ず `20_concept\` を確認し、
既存ノートのaliasに追加できないかを先に検討する。

### 概念ノートは category で分類する（フォルダ分けはしない）

frontmatter に `category`（複数可）と入れ子タグを付ける。8区分:

`領域` `皮弁` `手技` `神経` `評価` `合併症` `補綴` `横断`

```yaml
category:
  - 皮弁
  - 手技
tags:
  - 概念/皮弁
  - 概念/手技
source_topic: head_neck_general
```

**フォルダ分けはしない。** `血管柄付き骨移植` のように複数区分に属する概念があり、
フォルダは1つの居場所を強制してしまうため。タグペインから `概念/領域` で辿れる。

`source_topic` は**どのプロジェクトで作ったかという出自**であって分類ではない。
混同しないこと（以前 `topic` という名前にしていて実際に混乱の元になった）。

分類の定義は `papers\concept_categories.json`。
概念ノートを追加・再生成したら**必ず** `papers\build_concept_index.ps1` を実行する
（frontmatterが上書きされるため）。`20_concept\000_INDEX.md` も同時に再生成される。

### 未解決リンクを潰すときは3分類する

機械的に1件1ノート作ると、中身のない箱が増える。必ず次の3つに仕分ける。

1. **実体のある概念** → 独立したノートを作る
2. **既存概念の表記ゆれ・関連語** → 既存ノートの `aliases` に足す
3. **概念ではない語**（`コホート研究` `外科手技` など） → ハブノートを1枚作って
   `aliases` でまとめる。`研究デザイン` と `再建外科` がその例。

2026-09-08に `10_article` の未解決67件をこの方法で **18ノート**に統合した。

---

## 5. 目次（MOC）

プロジェクトフォルダには目次ノートを1枚置く。

- ファイル名: `000_MOC.md`（フォルダ先頭に並ぶ）
- リサーチクエスチョンを冒頭に明記する
- 論文を**群（そのRQで果たす役割）ごとに**並べる。年代順や著者順ではない
- 各論文に一行、なぜそこに置いたかを書く

---

## 6. 書き換えてはいけない箇所

Zoteroが生成・再生成する領域。手で直すと次回の再生成で消える。

- `# 2 Citation`
- `# 3 Related` の `> [!Info]` ブロック
- `> [!Abstract]` ブロック
- frontmatter の `citekey`
- `15_zotero\zotero.bib`（Better BibTeXが自動出力）

`read: false` は読み終えたら `true` にしてよい。

---

## 7. ノートを生成したあと必ず検証する

書きっぱなしにしない。最低限これを確認する。

1. **拡張子が `.md` になっているか。** PowerShellで `Clean-Name("x") + '.md'` と書くと
   `.md` が第2引数として捨てられ、拡張子なしのファイルができる。Obsidianはノートとして
   認識しない。正しくは `(Clean-Name "x") + '.md'`。
2. **wikilinkが解決するか。** vault全体のノート名とfrontmatterの `aliases` を集め、
   `[[...]]` がすべて該当するか照合する。新規作成分の未解決はゼロにする。
3. 論文ノートへのリンクは**フルファイル名**で書く。`[[@citekey]]` だけでは解決しない。
   `[[@citekey 長い日本語タイトル|著者 年]]` の形にする。
   （`papers\build_vault_notes.ps1` は短縮形を自動展開するが、手書きするときは要注意）

## 8. 何を収集するか — 2層構造

このvaultの目的は **形成外科領域の論文収集**。特定の研究テーマ（上顎再建など）は
その中の**プロジェクトの1つ**にすぎない。収集の仕組みをRQに縛らないこと。

収集範囲の定義は **`papers\watchlist.json`** にある。**ここだけを書き換える。**
配信タスクのプロンプトにクエリを直接書かない（関心が変わるたびにタスクを触る羽目になる）。

| 層 | 対象 | 絞り | 実測 |
|---|---|---|---|
| **層1** | 深追いする専門領域 | デザインを問わず全部 | 頭頸部再建 72件/30日、リンパ浮腫 86件/30日 |
| **層2** | 形成外科全体 | 主要10誌のレビュー・SR・メタ解析・RCT・比較研究のみ | 25件/30日 |

**単純に範囲を広げると破綻する。** 実測で形成外科MeSH全般は630件/30日（49件/配信）、
主要10誌全部でも452件（35件/配信）。層ごとに絞りを変えるのが解。

### 論文はRQから独立して蓄積する

| 場所 | 役割 | frontmatter |
|---|---|---|
| `10_article\` | **一般収集の受け皿** | `domain` のみ |
| `20_concept\` | 領域横断の知識層 | `category` |
| `<プロジェクト>\` | RQが立ったときに作る | `domain` + `relevance` + `arm` |

`relevance`（core/high/medium）と `arm`（比較のどの群か）は **特定のRQに対する評価**なので、
プロジェクトに組み入れた論文にだけ付ける。一般収集では `domain` だけでよい。
領域の一覧は `papers\domains.json`。

## 9. 論文を追加するときの標準手順

起点は、朝のダイジェストからユーザーが選んだ論文をチャットに貼ること。

**まずアクセス種別を判定し、ルートを分ける。** PubMedのメタデータに `pmc` があるかで決まる。

### ルートA — PMC掲載・オープンアクセス（ユーザーの操作は不要）

**順序を守ること。** PDFを先に取ってからRISを作れば、Zoteroが取り込み時に
`L1` タグで自動添付する。逆順だと添付が手作業になる。

1. 書誌を取得し `papers\<topic>\library.json` に追記
   （`relevance`・`arm`・`authors_full` を必ず埋める）
2. **PDFを取得** — `fetch_pmc_pdf.ps1` を使い `fulltext\<libid>.pdf` に置く。

   PMCのPDF URLは素で叩くと **1817バイトのJS中間ページ**が返る（proof-of-work式のbot対策）。
   ブラウザで一度PDFのURLを開いてJSを走らせると `cloudpmc-viewer-pow` Cookie が発行され、
   以後は `curl.exe` でも取れる。**Cookieはセッション単位で論文ごとではない。一度取れば使い回せる。**

   ```
   1. navigate https://pmc.ncbi.nlm.nih.gov/articles/<PMCID>/pdf/
      → 「Preparing to download ...」が出て記事ページに戻る。この時点でCookieが入る
   2. javascript_tool で document.cookie を読む
   3. pwsh -File fetch_pmc_pdf.ps1 -PmcId <PMCID> -Out <path> -Cookie "<document.cookie>"
   ```

   スクリプトが magic bytes を検査して落ちるが、**1ページ目を `pdftotext -f 1 -l 1` で
   目視照合する**こと（別論文のPDFを掴んでいないか）。
   出版社が直接PDFを配っている場合（Frontiers など）はそちらのほうが早い。
3. **全文テキストも取る** — `fetch_pmc_fulltext.ps1`。
   抄録に無い数値（追跡期間・欠損サイズ・骨長・救済手術の有無）はここにある。
   保存前に `<license>` を確認し、CC-BY等でなければ要約作成にのみ使う
4. 追加分RISを作る — `export_ris_subset.ps1`（**`-Command` で呼ぶこと**）
5. **Zoteroへ取り込む。コレクションを判定して指定する**（次項参照）

```bash
pwsh -File C:\Users\user\claude\papers\zotero_import.ps1 -Ris <path> -Collection "Head & Neck"
```

### ⚠️ Ovid の論文はルートBを使わない

DOIが `10.1097/` で始まる論文（Wolters Kluwer / Ovid。PRS、Ann Plast Surg、PRS-GO など）は、
**Zotero Connector が論文として認識せずウェブページとして保存する。**
citekey が `_Ovid_` になり、添付もPDFでなくHTMLになる。2026-09-08と09-09に2回発生。

→ **RIS経由（ルートA の手順4-5）で取り込む。** PDFはユーザーが別途ダウンロードして
`fulltext\<libid>.pdf` に置く。

### ルートB — 有料誌（PDFはユーザーが1キーで取る）

**Zotero Connectorは私からは起動できない。** 拡張のショートカットはブラウザ本体が
処理するため、CDP経由のキー入力（`computer` の key）は届かない。2026-09-08に実測で確認済み。
拡張アイコンもツールバー上にありページ操作ツールでは押せない。

1. 書誌を `library.json` に追記（ルートAと同じ）
2. **Chromeでその論文のページを開くところまでやる。**
   ユーザーは表示されたページで **Ctrl+Shift+S** を押すだけ。
   コネクタが機関セッションを使ってPDFごとZoteroに保存する
3. 取り込みを待ち、`zotero.bib` の更新を確認する。
   **私が `/connector/import` を叩いてはいけない** — コネクタ保存と重複する
4. PDFが取れなかった場合は抄録ベースで進め、ノートにその旨を明記する

### 共通（ルートA・Bとも）

6. **citekeyを `zotero.bib` から読む**（DOIで照合する。推測しない）
7. `notes_content.json` に `youyaku` と7見出しを書き、
   `build_vault_notes.ps1` → `build_concepts.ps1` を実行
8. **既存の概念ノートに新しい論文への言及を足す。** これを忘れると孤立したノートになる
9. リンク解決を検証する（未解決0件を確認）

### Zoteroのコレクション振り分け

ユーザーはZoteroを**形成外科の主要分類**で整理している。取り込むときに判定して入れる。

振り分け定義は **`papers\zotero_collections.json`**。判定ルールもそこにある。

**2種類が混在していることに注意する。**

| 種類 | コレクション | 自動振り分け |
|---|---|---|
| **分類** | Head & Neck / Breast / Flap / lymphedema / Sarcoma | **する** |
| **プロジェクト** | maxillary_reconstruction / Breast Implant Neuroma / CAPS_freeflap_references | **しない** |

プロジェクトはRQに沿って選別した集合なので、機械判定で汚すと選別の意味が失われる。
**ユーザーが明示的に指示したときだけ**追加する。上顎の論文も自動では
`Head & Neck` に入れ、`maxillary_reconstruction` には入れない。

どのルールにも当たらなければ**コレクションに入れず、ユーザーに判断を仰ぐ**。推測で入れない。

コレクションIDは `zotero_import.ps1 -ListCollections` で確認する。
**C番号を決め打ちしない** — 名前から解決すること。

### プロジェクトに属さない論文の置き場

ダイジェストから拾った論文が既存プロジェクトのRQに関係しない場合、
**`papers\<domain>_general\`** に入れ、`notes_content.json` の `folder` を
`10_article` にする。プロジェクト固有のRQを持たないので**MOCは作らない**。

`<domain>` は `papers\domains.json` の key。現在あるのは `head_neck_general`、
`lymphedema_general`。**該当するフォルダが無ければ作る**（`library.json`・
`notes_content.json`・`fulltext\` の3つ。`check.ps1` は `library.json` のある
直下フォルダを自動検出するので、別途の登録作業は要らない）。
`library.json` の `topic` はフォルダ名、`notes_content.json` の `folder` は
`10_article` で固定。**ノートの置き場は領域が違っても `10_article` 1つにまとめる。**

### 検証は雑にやらない

「取り込めたか」をキーワード検索で確かめると誤検出する。
2026-09-08に `masseteric` で検索して別論文の抄録にヒットし、失敗を成功と誤判定した。
**必ずDOIかcitekeyで厳密に照合すること。**

### 追加が終わったら必ず check.ps1 を走らせる

```bash
pwsh -File C:\Users\user\claude\papers\check.ps1
```

JSON構文・PLACEHOLDERの残存・citekeyの実在・PDFのmagic bytes・拡張子なしノート・
短縮形リンク・wikilink解決を一括で検査する。**失敗0件を確認してから完了と報告すること。**

検査項目はすべて過去に実際にやらかした失敗に対応している。
経緯と対策の全一覧は **`C:\Users\user\claude\papers\LESSONS.md`** にある。
新しい失敗をしたら、対策を文章で書くのではなく **`check.ps1` の検査項目に足すこと。**
注意書きは読み飛ばされるが、スクリプトは落ちる。

## 10. 自動化できること / できないこと（2026-09-12 更新）

| やりたいこと | 手段 | 可否 |
|---|---|---|
| Zoteroへの取り込み | `POST http://127.0.0.1:23119/connector/import` に RIS を投げる | **可**（Zotero起動中） |
| コレクションの一覧取得 | `POST /connector/getSelectedCollection` が全ツリーを返す | **可** |
| 取り込み先コレクションの指定 | 取り込み後に `POST /connector/updateSession` に `{sessionID, target}` | **可** |
| citekey の取得 | `15_zotero\zotero.bib` を読む | **可** |
| PMC論文の全文取得 | E-utilities の `efetch.fcgi?db=pmc` | **可**（XML／本文テキスト） |
| PMCからのPDF取得 | ブラウザでPoW Cookieを1回取り `fetch_pmc_pdf.ps1` | **可**（2026-09-12に確立。Cookieはセッション単位で使い回せる） |
| 有料誌のPDF取得 | Zotero Connector（**ユーザーがCtrl+Shift+S**） | **可**。ただし私からは起動できない |
| Zotero Connectorの起動 | — | **不可**（拡張ショートカットはブラウザ本体が処理。CDPキーは届かない） |

注意点:
- Zoteroのローカルサーバは **HTTP/1.0** で応答するため `Invoke-WebRequest` は失敗する。
  **`curl.exe` を使うこと。**
- 2回目以降の取り込みは `{"error":"SESSION_EXISTS"}` で **409** になる。
  URLに**一意のセッションIDを付ける**と通る:
  `POST /connector/import?session=<ランダム文字列>`
- **PMCへの自動アクセスを続けると reCAPTCHA が出る。** 2026-09-08に実際に発生した。
  出たら**そこで自動取得を止めること。** 押し切るとより強いブロックを招き、
  ユーザー自身のPMCアクセスに影響しうる。PDFはユーザーにクリックしてもらう。
  CAPTCHAは絶対に突破しない。
- `/connector/import` は **Zoteroで現在選択中のコレクション**に入る。取り込み後に場所を確認する。
- Zoteroのローカル**API**（`/api/users/0/items`）は **GETのみ。読み取り専用**。
  「他のアプリケーションとの通信を許可」をオンにしても書けない（POST 400 / PATCH 501。2026-09-12実測）。
  読めるようになる利点は大きい — **アイテムの実在・コレクション所属・添付の有無をキーで厳密に確認できる。**
  ただし**既存アイテムへのPDF添付はできない。**
  → **PDFを先に取ってからRISを作り、`L1` で取り込み時に添付させる。** 手順の順序が重要なのはこのため。
  後からPDFが手に入った場合だけは、ユーザーがZoteroのアイテムにドラッグする（数秒）。
- efetch が返すのは本文XMLであって PDF ではない。図表は含まれない。
- 保存する前に `<license>` を確認する。CC-BY等なら保存してよい。ライセンス不明なものは
  本文を保存せず、要約の作成にのみ使う。

## 11. 出典の扱い

- PubMed由来の情報を示すときは、PubMedへの帰属明示とDOIリンクを必ず付ける。
- 抄録は原文のまま `> [!Abstract]` に入れる。**要約は自分の言葉で書く。**
- PDF本文の丸写しをノートに貼らない。
- 数値を引くときは出典の論文ノートを併記する。

