"""统一文本清洗；默认数据流程保留原文，对照实验显式启用。"""
import html
import re


def clean_text(text,version="known_html_tags_v2"):
    """仅修复实体/HTML痕迹，保留普通词、数字、大小写和原始新闻语义。"""
    for _ in range(2):
        text=html.unescape(text)
        text=re.sub(r'#(34|36|38|39|60|62|160);',lambda m:chr(int(m[1])),text)
        text=re.sub(r'\b(quot|amp|lt|gt|nbsp);',lambda m:html.unescape('&'+m[1]+';'),text)
    if version=="legacy_all_tags_v1":
        text=re.sub(r'</?[a-zA-Z][^>]*>',' ',text)
    elif version=="known_html_tags_v2":
        tags=r'p|b|i|br|em|strong|font|a|span|div|ul|ol|li|h[1-6]|blockquote|table|tr|td|th|img|hr|u|sup|sub'
        text=re.sub(r'</?(?:'+tags+r')(?:\s[^>]*)?/?>',' ',text,flags=re.IGNORECASE)
    else:
        raise ValueError(f'未知清洗规则版本：{version}')
    return re.sub(r'\s+',' ',text).strip()

