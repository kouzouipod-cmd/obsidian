#!/usr/bin/env python3
"""
Generate infographic using Google AI Python SDK (google-genai).
Based on clinical paper infographic specification.
"""

import os
import sys
import base64
import argparse
from pathlib import Path

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("ERROR: google-genai package not installed. Run: pip install google-genai", file=sys.stderr)
    sys.exit(1)


INFOGRAPHIC_PROMPT_TEMPLATE = """
臨床論文のインフォグラフィックを生成してください。以下の仕様に厳密に従ってください。

# 論文情報
タイトル: {title}
著者: {author}
ジャーナル: {journal}
年: {year}

# Abstract
{abstract}

# AI要約
{summary}

---

# インフォグラフィック仕様

## 全体デザイン設定
- **形式**: 1:1正方形
- **テーマ**: Clinical Paper Infographic – 3-column layout
- **構成**: 上部ヘッダー + 下部3カラム（左: Setting / 中央: Key Results / 右: Discussion, Limitation, Conclusion）

## 色設定
- 背景色全体: #E5E7EB 〜 #F3F4F6 のグレー調
- ヘッダー背景色: #374151
- 左カラム背景: #F9FAFB
- 中央カラム背景: #FFFFFF
- 右カラム背景: #F3F4F6
- メイン文字色: #111827
- サブ文字色: #4B5563
- ヘッダー文字: #FFFFFF
- アクセントカラー: #2563EB

## レイアウト構成

### 1. Header（上部 15%）
- 背景色: #374151
- 文字色: #FFFFFF
- 内容:
  * 日本語のインフォグラフィックタイトル（結論を含む短い一文）
  * サブタイトル: "{title}" by {author}, {journal} ({year})
- デザイン: タイトルを大きく中央揃え、サブタイトルを小さめに配置

### 2. Left Column – SETTING（左30%）
- 背景色: #F9FAFB
- 見出し: "SETTING"（白文字、濃いグレー背景バー）
- 内容:
  * Study design（研究デザイン）
  * Population（対象集団）
  * Exclusion criteria（除外基準）
  * Data source / Setting（データソース）
  * Primary outcome（主要評価項目）
  * Key secondary outcomes（副次評価項目）
  * Statistical methods（統計手法）
- デザイン: 各項目の左にカラーアイコンを配置

### 3. Center Column – KEY RESULTS（中央40%）
- 背景色: #FFFFFF
- 見出し: "KEY RESULTS"
- 内容: 重要な結果をグラフ・図表中心で表示
- デザイン: グラフを主役とし、テキストは最小限

### 4. Right Column – DISCUSSION / LIMITATION / CONCLUSION（右30%）
- 背景色: #F3F4F6
- 3つのブロック:
  * **| DISCUSSION**: 主要な臨床的解釈を日本語で1〜3文
  * **| LIMITATION**: 外的妥当性、選択バイアス、データ欠損、追跡期間などの制約
  * **| CONCLUSION**: 実臨床での位置づけや推奨、今後の研究の方向性

## タイポグラフィ
- タイトル: 太めのサンセリフ体（日本語・英語両対応）
- セクション見出し: 中サイズ・太字・オールキャップ
- 本文: 読みやすいサンセリフ体、行間はやや広め
- 強調表現: 太字またはアクセントカラー

## デザインルール
1. セクション見出しは英語で統一、本文は日本語
2. 中央カラムのKEY RESULTSを最も視覚的に強調
3. アイコンは左カラムのみ使用
4. 色数はグレー系ベース + アクセントの青1色 + アイコン用の穏やかな色合い
5. 150 DPI以上、読みやすい文字サイズを確保

---

上記の仕様に基づき、プロフェッショナルな臨床論文インフォグラフィックを生成してください。
AbstractとAI要約から適切に情報を抽出し、各セクションに配置してください。
"""


def generate_infographic(
    entry_key: str,
    title: str,
    author: str,
    journal: str,
    year: str,
    abstract: str,
    summary: str,
    output_path: str
) -> bool:
    """
    Generate infographic using Google AI Python SDK.

    Returns:
        bool: True if successful, False otherwise
    """
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        print("ERROR: GEMINI_API_KEY environment variable not set", file=sys.stderr)
        return False

    # Prepare prompt
    prompt = INFOGRAPHIC_PROMPT_TEMPLATE.format(
        title=title,
        author=author,
        journal=journal,
        year=year,
        abstract=abstract,
        summary=summary
    )

    print(f"Generating infographic for: {entry_key}")

    try:
        # Initialize client
        client = genai.Client(api_key=api_key)

        # Generate content with image
        response = client.models.generate_content(
            model="gemini-3-pro-image-preview",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=["TEXT", "IMAGE"]
            )
        )

        print(f"Response received. Candidates: {len(response.candidates) if response.candidates else 0}")

        # Debug: print response structure
        if not response.candidates:
            print(f"ERROR: No candidates in response", file=sys.stderr)
            print(f"Response: {response}", file=sys.stderr)
            return False

        # Extract image from response
        image_data = None
        for part in response.candidates[0].content.parts:
            if hasattr(part, 'inline_data') and part.inline_data:
                image_data = part.inline_data.data
                mime_type = part.inline_data.mime_type
                print(f"Found image: {mime_type}, size: {len(image_data)} bytes")
                break
            elif hasattr(part, 'text') and part.text:
                print(f"Text response: {part.text[:200]}...")

        if not image_data:
            print(f"ERROR: No image data in response", file=sys.stderr)
            # Try to show what we got
            for i, part in enumerate(response.candidates[0].content.parts):
                print(f"Part {i}: {type(part)}", file=sys.stderr)
            return False

        # Decode if base64 encoded
        if isinstance(image_data, str):
            image_bytes = base64.b64decode(image_data)
        else:
            image_bytes = image_data

        # Ensure output directory exists
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, 'wb') as f:
            f.write(image_bytes)

        print(f"✅ Infographic saved: {output_path}")
        return True

    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Generate clinical paper infographic using Gemini API"
    )
    parser.add_argument("--entry-key", required=True, help="BibTeX entry key")
    parser.add_argument("--title", required=True, help="Paper title")
    parser.add_argument("--author", required=True, help="Author(s)")
    parser.add_argument("--journal", required=True, help="Journal name")
    parser.add_argument("--year", required=True, help="Publication year")
    parser.add_argument("--abstract", required=True, help="Abstract text")
    parser.add_argument("--summary", required=True, help="AI-generated summary")
    parser.add_argument("--output", required=True, help="Output PNG file path")

    args = parser.parse_args()

    success = generate_infographic(
        entry_key=args.entry_key,
        title=args.title,
        author=args.author,
        journal=args.journal,
        year=args.year,
        abstract=args.abstract,
        summary=args.summary,
        output_path=args.output
    )

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
