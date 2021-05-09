---
layout:     post
title:      "如何使用Markdown撰写文档"
subtitle:   "How to use Markdown"
date:       2021-05-19 14:26:31
author:     "xxxbrian"
catalog: true
header-style: text
tags:
  - 笔记
  - Markdown
---

## Markdown

>[Markdown](https://daringfireball.net/projects/markdown/)是在 2004 由约翰·格鲁伯（John Gruber）创建的一种轻量级标记语言，它允许人们使用易读易写的纯文本格式编写文档。
>[Markdown](https://daringfireball.net/projects/markdown/)编写的文档可以导出 HTML 、Word、图像、PDF、Epub 等多种格式的文档。
>[Markdown](https://daringfireball.net/projects/markdown/)编写的文档后缀为 `.md`, `.markdown`。

### Markdown 应用

Markdown 能被使用来撰写电子书，如：Gitbook。

当前许多网站都广泛使用 Markdown 来撰写帮助文档或是用于论坛上发表消息。例如：GitHub、简书、reddit、Diaspora、Stack Exchange、OpenStreetMap 、SourceForge等。

### Markdown标题基础语法

#### 标题 | Title

Markdown 标题有两种格式。

__1. 使用 `=` 和 `-` 标记一级和二级标题__

```markdown
这是H1的标题
===========

这是H2的标题
-----------
```

![title 效果](/img/in-post/2021-05-09-how-to-use-markdown/markdown_title1.png)

__2. 使用 `#` 标记__

使用 `#` 号可表示 1-6 级标题，一级标题对应一个 `#` 号，二级标题对应两个 `#` 号，以此类推。

```markdown
# 一级标题

## 二级标题

### 三级标题

#### 四级标题

##### 五级标题

###### 六级标题
```

![title 效果](/img/in-post/2021-05-09-how-to-use-markdown/markdown_title2.png)

---

#### 段落 | Paragraph

Markdown 段落没有特殊的格式，可以直接编写文字就好，__段落的换行是使用两个以上空格加上回车__。
![paragraph 效果](/img/in-post/2021-05-09-how-to-use-markdown/markdown_paragraph1.png)

也可以在段落后面 __使用一个空行来表示重新开始一个段落__。
![paragraph 效果](/img/in-post/2021-05-09-how-to-use-markdown/markdown_paragraph2.png)

---

#### 斜体与加粗 | Phrase Emphasis

Markdown 使用 `*文本*` 或 `_文本_` 的方式来使用 __斜体文本__，`*文本*` 或 `_文本_` 的方式来使用 __粗体文本__。

|用法|效果|
|:-:|:-:|
|`*斜体文本*`|*斜体文本*|
|`_斜体文本_`|_斜体文本_|
|`**粗体文本**`|**粗体文本**|
|`__粗体文本__`| __粗体文本__|
|`***粗斜体文本***`|***粗斜体文本***|
|`___粗斜体文本___`|___粗斜体文本___|

---

#### 列表 | List

Markdown 支持无序列表和有序列表。

__无序列表__

无序列表使用 __星号__`*` __加号__`+` 或是 __减号__`-` 作为列表标记，这些标记后面要添加一个 __空格__，然后再填写内容：

```markdown
* 第一项
* 第二项
* 第三项

+ 第一项
+ 第二项
+ 第三项

- 第一项
- 第二项
- 第三项
```

![list 效果](/img/in-post/2021-05-09-how-to-use-markdown/markdown_list1.png)

__有序列表__

有序列表使用数字并加上 . 号来表示，如：

```markdown
1. 第一项
2. 第二项
3. 第三项
```

![list 效果](/img/in-post/2021-05-09-how-to-use-markdown/markdown_list2.png)

__列表嵌套__

列表嵌套只需在子列表中的选项前面添加四个空格即可:

```markdown
1. 第一项：
    - 第一项嵌套的第一个元素
    - 第一项嵌套的第二个元素
2. 第二项：
    - 第二项嵌套的第一个元素
    - 第二项嵌套的第二个元素
```

![list 效果](/img/in-post/2021-05-09-how-to-use-markdown/markdown_list3.png)

---

#### 区块引用 | Blockquotes

Markdown 区块引用是在段落开头使用 `>` 符号 ，然后后面紧跟一个 `空格` 符号：

```markdown
>Hi, this is xxxbrian.
>Brian's Blog
>等青春轻飘的烟雾把少年的欢乐袅袅曳去，之后，我们就能取得一切值得吸取的东西。 ——普希金
```

另外区块是可以嵌套的，一个 `>` 符号是最外层，两个 `>` 符号是第一层嵌套，以此类推：

```markdown
> 最外层
> > 第一层嵌套
> > > 第二层嵌套
```

__区块中使用列表__

```markdown
> 区块中使用列表
> 1. 第一项
> 2. 第二项
> + 第一项
> + 第二项
> + 第三项
```

__列表中使用区块__

```markdown
+ 第一项
    > Brian's Blog
    > Hi, this is xxxbrian.
+ 第二项
```

![blockquotes 效果](/img/in-post/2021-05-09-how-to-use-markdown/markdown_blockquotes.png)

---

#### 代码 | Code

如果是段落上的一个函数或片段的代码可以用 __反引号__`` ` ``把它包起来`` `代码` ``，例如想要显示: `printf()`函数

```markdown
`printf()`函数
```

__代码区块__

代码区块使用 __4 个空格__ 或者一个 __制表符（Tab 键）__。

```markdown
    $(document).ready(function () {
        alert('RUNOOB');
    });
```

显示结果如下：

    $(document).ready(function () {
        alert('RUNOOB');
    });

你也可以用 `` ``` `` 包裹一段代码，并指定一种语言（也可以不指定）：

    ```javascript
    $(document).ready(function () {
        alert('RUNOOB');
    });
    ```

显示结果如下：

```javascript
$(document).ready(function () {
    alert('RUNOOB');
});
```

---

#### 超链接 | Link

__链接__ 使用方法如下：

```markdown
[链接名称](链接地址)

或者

<链接地址>
```

例如：

```markdown
这是一个链接 [Brian's Blog](https://xxxbrian.me)
```

这是一个链接 [Brian's Blog](https://xxxbrian.me)

__直接使用链接地址__

```markdown
链接 <https://xxxbrian.me>
```

链接 <https://xxxbrian.me>

__高级链接__

我们可以通过变量来设置一个链接，变量赋值在文档末尾进行：

```markdown
这个链接用 1 作为网址变量 [Google][1]
这个链接用 Brian's Blog 作为网址变量 [xxxbrian][xxxbrian]

[1]: http://www.google.com/
[xxxbrian]: https://xxxbrian.me
```

![link 效果](/img/in-post/2021-05-09-how-to-use-markdown/markdown_link.png)

---

#### 图片 | Images

Markdown 图片语法格式如下：

```markdown
![alt 属性文本](图片地址)

![alt 属性文本](图片地址 "可选标题")
```

+ 开头一个感叹号 `!`
+ 接着一个方括号，里面放上图片的替代文字
+ 接着一个普通括号，里面放上图片的网址，最后还可以用引号包住并加上选择性的 `'title'` 属性的文字。

使用实例：

```markdown
![xxxbrian 图标](https://raw.githubusercontent.com/xxxbrian/xxxbrian.github.io/master/img/xxxbrian-192x192.png "xxxbrian")
```

效果如下：
![xxxbrian 图标](https://raw.githubusercontent.com/xxxbrian/xxxbrian.github.io/master/img/xxxbrian-192x192.png "xxxbrian")

---

#### 表格 | Sheet

Markdown 制作表格使用 `|` 来分隔不同的单元格，使用 `-` 来分隔表头和其他行。

```markdown
|  表头   | 表头  |
|  ----  | ----  |
| 单元格  | 单元格 |
| 单元格  | 单元格 |
```

__表格对齐__

+ `-:` 设置内容和标题栏居右对齐。
+ `:-` 设置内容和标题栏居左对齐。
+ `:-:` 设置内容和标题栏居中对齐。

```markdown
| 左对齐 | 右对齐 | 居中对齐 |
| :-----| ----: | :----: |
| 单元格 | 单元格 | 单元格 |
| 单元格 | 单元格 | 单元格 |
```

![sheet 效果](/img/in-post/2021-05-09-how-to-use-markdown/markdown_sheet.png)

---

#### 转义 | Backslash Escapes

Markdown 使用了很多特殊符号来表示特定的意义，如果需要显示特定的符号则需要使用转义字符，Markdown 使用反斜杠转义特殊字符：

```markdown
**文本加粗** 
\*\* 正常显示星号 \*\*
```

Markdown 支持以下这些符号前面加上反斜杠来帮助插入普通的符号：

```text
\   反斜线
`   反引号
*   星号
_   下划线
{}  花括号
[]  方括号
()  小括号
#   井字号
+   加号
-   减号
.   英文句点
!   感叹号
```
