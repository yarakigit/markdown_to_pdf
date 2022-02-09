---

# pythonでマークダウンをPDFに変換

---

## 目次

---

* [Reference](#reference)
* [Enviroment](#enviroment)
* [Run](#run)
* [Src](#src)

## Reference

---

### 参考にさせていただいたサイト
- [Qita PythonでマークダウンをPDFに変換する, 株式会社ラクス @t_okkan](https://qiita.com/t_okkan/items/2efcb35c43f2bb29858e)

## Enviroment

---
- CentOS 7.9
  - python 3.9.9
    - lib : Markdown, pdfkit, Pygments
 
## Run

---

### 実行手順
1. **wkhtmltopdf**をビルドする

  - ビルド済みのバイナリ

    - [github, frappe, wkhtmltopdf](https://github.com/frappe/wkhtmltopdf)

2. 実行
   
~~~ bash
$ python markdown_to_pdf.py README.md README.pdf
~~~

## Src

---

|Name|Explanation|
|:-------------|:---|
|[README.md](./README.md) |入力するマークダウン形式のファイル|
|[README.pdf](./README.pdf)           |出力されたPDFファイル|
|[markdown_to_pdf.py](./markdown_to_pdf.py)|メインのプログラム|
|[markdown_format.md](./markdown_format.md)|自分用 マークダウン 書き方|

