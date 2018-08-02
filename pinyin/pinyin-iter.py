#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#########################################################################
# Author: Wang Wencan
# Created Time: Wed Aug  1 18:51:19 2018
# Description: 
#########################################################################
shengmu_list = [ u'b', u'p', u'm', u'f', u'd', u't', u'n', u'l', u'g', u'k', u'h', u'j', u'q', u'x', u'zh', u'ch', u'sh', u'r', u'z', u'c', u's']
yunmu_list = [
        u'\u012b', u'\xed', u'\u01d0', u'\xec', # 衣
        u'\u016b', u'\xfa', u'\u01d4', u'\xf9', # 乌
        u'\u01D6', u'\u01d8', u'\u01da', u'\u01dc', # 迂
        u'\u0101', u'\xe1', u'\u01ce', u'\xe0', # 啊
        u'i\u0101', u'i\xe1', u'i\u01ce', u'i\xe0', # 呀
        u'u\u0101', u'u\xe1', u'u\u01ce', u'u\xe0', # 蛙
        u'\u014d', u'\xf3', u'\u01d2', u'\xf2', # 喔
        u'u\u014d', u'u\xf3', u'u\u01d2', u'u\xf2', # 窝
        u'\u0113', u'\xe9', u'\u011b', u'\xe8', # 鹅
        u'i\u0113', u'i\xe9', u'i\u011b', u'i\xe8', # 耶
        u'u\u0113', u'u\xe9', u'u\u011b', u'u\xe8', # 约
        u'\u0101i', u'\xe1i', u'\u01cei', u'\xe0i', # 哀
        u'u\u0101i', u'u\xe1i', u'u\u01cei', u'u\xe0i', # 歪
        u'\u0113i', u'\xe9i', u'\u011bi', u'\xe8i',     # 欸
        u'u\u0113i', u'u\xe9i', u'u\u011bi', u'u\xe8i', # 威
        u'\u0101o', u'\xe1o', u'\u01ceo', u'\xe0o',     # 熬
        u'i\u0101o', u'i\xe1o', u'i\u01ceo', u'i\xe0o', # 腰
        u'\u014du', u'\xf3u', u'\u01d2u', u'\xf2u',     # 欧
        u'i\u014du', u'i\xf3u', u'i\u01d2u', u'i\xf2u', # 忧
        u'\u0101n', u'\xe1n', u'\u01cen', u'\xe0n',     # 安
        u'i\u0101n', u'i\xe1n', u'i\u01cen', u'i\xe0n', # 烟
        u'u\u0101n', u'u\xe1n', u'u\u01cen', u'u\xe0n', # 弯
        u'\xfc\u0101n', u'\xfc\xe1n', u'\xfc\u01cen', u'\xfc\xe0n', # 冤
        u'\u0113n', u'\xe9n', u'\u011bn', u'\xe8n', # 恩
        u'\u012bn', u'\xedn', u'\u01d0n', u'\xecn', # 因
        u'u\u0113n', u'u\xe9n', u'u\u011bn', u'u\xe8n', # 温
        u'\u01D6n', u'\u01d8n', u'\u01dan', u'\u01dcn', # 晕
        u'\u0101ng', u'\xe1ng', u'\u01ceng', u'\xe0ng', # 昂
        u'i\u0101ng', u'i\xe1ng', u'i\u01ceng', u'i\xe0ng', # 央
        u'u\u0101ng', u'u\xe1ng', u'u\u01ceng', u'u\xe0ng', # 汪
        u'\u0113ng', u'\xe9ng', u'\u011bng', u'\xe8ng', # 亨的韵母
        u'\u012bng', u'\xedng', u'\u01d0ng', u'\xecng', # 英
        u'u\u0113ng', u'u\xe9ng', u'u\u011bng', u'u\xe8ng', # 翁
        u'\u014dng', u'\xf3ng', u'\u01d2ng', u'\xf2ng', # 轰的韵母
        u'i\u014dng', u'i\xf3ng', u'i\u01d2ng', u'i\xf2ng', # 雍
        ]

# for yunmu in yunmu_list:
#     print yunmu

print len(shengmu_list)
print len(yunmu_list) / 4.0
