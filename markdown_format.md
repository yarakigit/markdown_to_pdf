---
# 自分用 マークダウン 書き方
---
# menu
## markdown menu
* [markdown 記述](#markdown-記述)
* [見出し](#見出し)
* [箇条書きリスト](#箇条書きリスト)
* [番号付きリスト](#番号付きリスト)
* [引用 二重バージョン](#引用-二重バージョン)
* [コード記法](#コード記法)
* [強調](#強調)
* [水平線](#水平線)
* [リンク](#リンク)
* [定義参照リンク](#定義参照リンク)
* [GFM](#gfm)
* [取り消し線](#取り消し線)
* [pre記法](#pre記法)
* [表](#表)
* [ページ内リンク](#ページ内リンク)
* [Reference](#reference)

<!-- some long code -->

[return to menu](#menu)
***
## markdown 記述
***
### 見出し
***
#### 記述例
```
# 見出し1
## 見出し2
### 見出し3
#### 見出し4
##### 見出し5
###### 見出し6
```
### 表示例
# 見出し1     
## 見出し2    
### 見出し3   
#### 見出し4  
##### 見出し5 
###### 見出し6
***
### 箇条書きリスト
***
#### 記述例 
```
- リスト1
  - ネスト リスト1_1
    - ネスト リスト1_1_1
    - ネスト リスト1_1_2
  - ネスト リスト1_2
- リスト2
- リスト3
```
#### 表示例
- リスト1                
  - ネスト リスト1_1     
    - ネスト リスト1_1_1 
    - ネスト リスト1_1_2 
  - ネスト リスト1_2     
- リスト2                
- リスト3
***
### 番号付きリスト
***
#### 記述例 
```
1. 番号付きリスト1
   1. 番号付きリスト1_1
   1. 番号付きリスト1_2
1. 番号付きリスト2
1. 番号付きリスト3
```
#### 表示例
1. 番号付きリスト1     
   1. 番号付きリスト1_1
   1. 番号付きリスト1_2
1. 番号付きリスト2     
1. 番号付きリスト3
***
### 引用 (二重バージョン)
***
#### 記述例　
```
> お世話になります。xxxです。
> 
> ご連絡いただいた、バグの件ですが、仕様です。
>> お世話になります。 yyyです。
>> 
>> あの新機能バグってるっすね
```
#### 表示例
> お世話になります。xxxです。
> 
> ご連絡いただいた、バグの件ですが、仕様です。
>> お世話になります。 yyyです。
>> 
>> あの新機能バグってるっすね
***
### コード記法
***
#### 記述例
```
インストールコマンドは `gem install hoge` です
```
#### 表示例
インストールコマンドは `gem install hoge` です
***
### 強調
***
#### 記述例
```
normal **bold** normal
normal __bold__ normal
```
#### 表示例
normal **bold** normal
normal __bold__ normal
***
### 水平線
***
#### 記述例
```

***

___

---

*    *    *


```
#### 表示例

***

___

---

*    *    *
***
### リンク
***
#### 記述例
```
[Google先生](https://www.google.co.jp/)
```
#### 表示例
[Google先生](https://www.google.co.jp/)

***
### 定義参照リンク
***
#### 
```
[こっちからgoogle][google]
その他の文章
[こっちからもgoogle][google]

[google]: https://www.google.co.jp/
```
#### 表示例
[こっちからgoogle][google]

その他の文章

[こっちからもgoogle][google]


[google]: https://www.google.co.jp/ 
***
## GFM
***
- GFM : GitHub Flavored Markdown
### 取り消し線
***
#### 記述例
```
~~取り消し線~~
```
#### 表示例
~~取り消し線~~
***
### pre記法
***
- チルダ×3
- バッククォート×3
- チルダ、もしくはバッククォート3つの後ろに対象シンタックスの言語名を記述
#### 表示例
~~~ c
int main(void){
/*

*/
return 0;	
}

~~~
***
### 表
***
#### 記述例
```
|header1|header2|header3|
|:--|--:|:--:|
|align left|align right|align center|
|a|b|c|
```
#### 表示例
|header1|header2|header3|
|:--|--:|:--:|
|align left|align right|align center|
|a|b|c|
***
### ページ内リンク
***
- [Qiita Markdownのページ内リンクの罠, @hennin](https://qiita.com/hennin/items/7ee58dd7d7c013a23be7)
#### 記述例
```
## menu
* [to header1](#header1)
* [to header2](#header2)

<!-- some long code -->

[return to menu](#menu)
### header1
### header2
```

---
## Reference
---
- [qita : Markdown記法 サンプル集, @tbpgr](https://qiita.com/tbpgr/items/989c6badefff69377da7)
  - こちらを写経しました
***