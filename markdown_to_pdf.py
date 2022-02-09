######################################################################
## 参考にさせていただいたコード
## Qita PythonでマークダウンをPDFに変換する
## 株式会社ラクス @t_okkan
## https://qiita.com/t_okkan/items/2efcb35c43f2bb29858e
######################################################################

import markdown
import pdfkit
from pygments import highlight
from pygments.formatters import HtmlFormatter
import sys

# wkhtmltopdf をビルドしておく
input_path = sys.argv[1]
outputfile = sys.argv[2]

def mark_to_html():
    # マークダウンファイルの読み込み
    f = open(input_path, mode='r', encoding='UTF-8')
    with f:
        text = f.read()
        # Pygmentsでハイライト用のスタイルシートを作成
        style = HtmlFormatter(style='default').get_style_defs('.codehilite')
        # # マークダウン -> HTMLの変換を行う
        md = markdown.Markdown(extensions=['extra', 'codehilite', 'sane_lists' , 'smarty' , 'wikilinks', 'toc'])
        body = md.convert(text)
        # HTML書式に合わせる
        html = '<html lang="ja"><meta charset="utf-8"><body>'
        # Pygmentsで作成したスタイルシートを取り込む
        html += '<style>{}</style>'.format(style)
        # Tableタグに枠線を付けるためにスタイルを追加
        html += '''<style> table,th,td { 
            border-collapse: collapse;
            border:1px solid #333; 
            } </style>'''
        html += body + '</body></html>' 
        return html

def html_to_pdf(html: str):
    pdfkit.from_string(html, outputfile)
    
if __name__=='__main__':
    html = mark_to_html()
    html_to_pdf(html)
