# -*- coding: utf-8 -*-

##########################################################################
# Ambiguous mappings of simplified to traditional characters
##########################################################################
"""
Source: https://en.wikipedia.org/wiki/Ambiguities_in_Chinese_character_simplification

Special cases:
寧⇄宁, 宁⇄㝉:

薴⇄苧, 苧⇄苎: 薴 níng (limonene) is simplified to 苧 which is the traditional character for zhù (boehmeria) that in turn is simplified to 苎.

甚⇄甚什, 什⇄甚什: 甚 shèn (extremely, exceed) and 什 shí (ten, various) are the same in both simplified and traditional, while shén (what) is written 甚 in traditional and 什 in simplified (and also as a variant in traditional).

徵⇄徵征, 征⇄徵征: 徵 zhǐ (a musical note) and 征 zhēng (journey, campaign) are the same in both simplified and traditional. However, another zhēng (punish, seek, characteristic, levy) is written 徵 in traditional and 征 in simplified.

夥⇄夥伙, 伙⇄夥伙: A similar, but not entirely comparable situation is 夥 and 伙, both pronounced huǒ. The literary meaning "many, much" is written 夥 in both sets, and the meaning "meals" is written 伙 in both sets, but the meaning "partner, group, combine" generally prefers 夥 for traditional and 伙 for simplified, although as there is some overlap with the other meanings, the character choice is less strict.

乾⇄乾干, 干⇄乾干幹:
"""

# Mappings of 1 simplified to 3 traditional characters
map_1s_3t = {
    "系": ["系", "係", "繫"], 
    "只": ["只", "衹", "隻"]
}
# Mappings of 1 simplified to 4 traditional characters
map_1s_4t = {
    "蒙": ["蒙", "懞", "濛", "矇"], 
    "台": ["台", "檯", "臺", "颱"]
}
# Mappings of 2 simplified to 1 traditional character
map_2s_1t = {
    "著": ["著", "着"], 
    "藉": ["藉", " 借"], 
    "瞭": ["瞭", " 了"], 
    "麽": ["麽", "么"], 
    "蘋": ["苹", "𬞟"]
}
# Mappings of 1 simplified to 2 traditional characters
map_1s_2t = {
    "板": ["板", "闆"], 
    "辟": ["辟", "闢"], 
    "表": ["表", "錶"], 
    "别": ["別", "彆"], 
    "卜": ["卜", "蔔"], 
    "布": ["布", "佈"], 
    "才": ["才", "纔"], 
    "彩": ["彩", "綵"], 
    "虫": ["虫", "蟲"], 
    "丑": ["丑", "醜"], 
    "出": ["出", "齣"], 
    "村": ["村", "邨"], 
    "当": ["當", "噹"], 
    "党": ["黨", "党"], 
    "淀": ["澱", "淀"], 
    "吊": ["弔", "吊"], 
    "冬": ["冬", "鼕"], 
    "发": ["發", "髮"], 
    "范": ["范", "範"], 
    "丰": ["豐", "丰"], 
    "谷": ["谷", "穀"], 
    "雇": ["雇", "僱"], 
    "刮": ["刮", "颳"], 
    "广": ["廣", "广"], 
    "哄": ["哄", "鬨"], 
    "后": ["後", "后"], 
    "获": ["獲", "穫"], 
    "几": ["幾", "几"], 
    "机": ["機", "机"], 
    "饥": ["飢", "饑"], 
    "奸": ["奸", "姦"], 
    "姜": ["姜", "薑"], 
    "借": ["借", "藉"], 
    "卷": ["捲", "卷"], 
    "克": ["克", "剋"], 
    "困": ["困", "睏"], 
    "夸": ["夸", "誇"], 
    "罗": ["羅", "囉"], 
    "累": ["累", "纍"], 
    "厘": ["厘", "釐"], 
    "漓": ["漓", "灕"], 
    "梁": ["梁", "樑"], 
    "了": ["了", "瞭"], 
    "霉": ["霉", "黴"], 
    "弥": ["彌", "瀰"], 
    "蔑": ["蔑", "衊"], 
    "么": ["么", "麼"], 
    "麽": ["麽", "麼"], 
    "苹": ["蘋", "苹"], 
    "仆": ["僕", "仆"], 
    "铺": ["鋪", "舖"], 
    "朴": ["朴", "樸"], 
    "签": ["簽", "籤"], 
    "舍": ["舍", "捨"], 
    "沈": ["沈", "瀋"], 
    "胜": ["勝", "胜"], 
    "术": ["術", "朮"], 
    "松": ["松", "鬆"], 
    "他": ["他", "祂"], 
    "叹": ["嘆", "歎"], 
    "坛": ["壇", "罈"], 
    "你": ["你", "妳"], 
    "体": ["體", "体"], 
    "同": ["同", "衕"], 
    "涂": ["涂", "塗"], 
    "团": ["團", "糰"], 
    "喂": ["喂", "餵"], 
    "为": ["為", "爲"], 
    "纤": ["纖", "縴"], 
    "咸": ["鹹", "咸"], 
    "弦": ["弦", "絃"], 
    "绣": ["綉", "繡"], 
    "须": ["須", "鬚"], 
    "熏": ["熏", "燻"], 
    "腌": ["醃", "腌"], 
    "叶": ["葉", "叶"], 
    "佣": ["傭", "佣"], 
    "涌": ["湧", "涌"], 
    "游": ["游", "遊"], 
    "于": ["於", "于"], 
    "余": ["余", "餘"], 
    "吁": ["籲", "吁"], 
    "郁": ["郁", "鬱"], 
    "欲": ["欲", "慾"], 
    "御": ["御", "禦"], 
    "愿": ["願", "愿"], 
    "岳": ["岳", "嶽"], 
    "云": ["雲", "云"], 
    "赞": ["贊", "讚"], 
    "脏": ["臟", "髒"], 
    "扎": ["扎", "紮"], 
    "占": ["占", "佔"], 
    "折": ["折", "摺"], 
    "证": ["證", "証"], 
    "志": ["志", "誌"], 
    "制": ["制", "製"], 
    "致": ["致", "緻"], 
    "钟": ["鍾", "鐘"], 
    "种": ["種", "种"], 
    "周": ["周", "週"], 
    "注": ["註", "注"], 
    "准": ["準", "准"], 
    "冢": ["塚", "冢"], 
    "庄": ["庄", "莊"], 
    "涩": ["澀", "澁"], 
    "蚕": ["蠶", "蚕"], 
    "忏": ["懺", "忏"], 
    "吨": ["噸", "吨"], 
    "赶": ["趕", "赶"], 
    "构": ["構", "构"], 
    "柜": ["櫃", "柜"], 
    "怀": ["懷", "怀"], 
    "坏": ["壞", "坏"], 
    "极": ["極", "极"], 
    "茧": ["繭", "茧"], 
    "家": ["家", "傢"], 
    "价": ["價", "价"], 
    "洁": ["潔", "洁"], 
    "惊": ["驚", "惊"], 
    "腊": ["臘", "腊"], 
    "蜡": ["蠟", "蜡"], 
    "帘": ["簾", "帘"], 
    "怜": ["憐", "怜"], 
    "岭": ["嶺", "岭"], 
    "扑": ["撲", "扑"], 
    "秋": ["秋", "鞦"], 
    "千": ["千", "韆"], 
    "确": ["確", "确"], 
    "扰": ["擾", "扰"], 
    "洒": ["灑", "洒"], 
    "晒": ["曬", "晒"], 
    "适": ["適", "适"], 
    "听": ["聽", "听"], 
    "洼": ["窪", "洼"], 
    "网": ["網", "网"], 
    "旋": ["旋", "鏇"], 
    "踊": ["踴", "踊"], 
    "优": ["優", "优"], 
    "症": ["症", "癥"], 
    "朱": ["朱", "硃"], 
    "荐": ["薦", "荐"], 
    "离": ["離", "离"], 
    "卤": ["鹵", "滷"], 
    "气": ["氣", "气"], 
    "圣": ["聖", "圣"], 
    "万": ["萬", "万"], 
    "与": ["與", "与"], 
    "摆": ["擺", "襬"], 
    "虮": ["蟣", "虮"], 
    "篱": ["籬", "篱"], 
    "宁": ["寧", "宁"], 
    "泞": ["濘", "泞"], 
    "恶": ["惡", "噁"], 
    "托": ["托", "託"], 
    "咽": ["嚥", "咽"], 
    "线": ["線", "綫"], 
    "咨": ["咨", "諮"], 
    "荡": ["蕩", "盪"], 
    "亘": ["亘", "亙"], 
    "仑": ["侖", "崙"], 
    "趟": ["趟", "蹚"], 
    "杯": ["杯", "盃"], 
    "斗": ["斗", "鬥"], 
    "曲": ["曲", "麯"], 
    "苏": ["蘇", "囌"], 
    "胡": ["胡", "鬍"], 
    "划": ["划", "劃"], 
    "回": ["回", "迴"], 
    "汇": ["匯", "彙"], 
    "里": ["里", "裏"], 
    "历": ["歷", "曆"], 
    "向": ["向", "嚮"], 
    "冲": ["冲", "衝"], 
    "尽": ["盡", "儘"], 
    "面": ["面", "麵"], 
    "复": ["復", "複"], 
    "据": ["据", "據"]
} 
 