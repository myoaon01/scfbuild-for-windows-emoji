# -*- coding: utf-8 -*-
# SCFBuild is released under the GNU General Public License v3.
# See LICENSE.txt in the project root directory.

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# ZERO WIDTH JOINER (ZWJ)
ZWJ_INT = 0x200d
ZWJ = '\u200d'
# VARIATION SELECTOR-16 - Used as emoji variation selector.
VS16_INT = 0xfe0f
VS16 = '\ufe0f'
# COMBINING ENCLOSING KEYCAP - Used to create keycap emoji.
KEYCAP_INT = 0x20e3
KEYCAP = '\u20e3'

# A list of all ZWJ indexed by the no ZJW/EVS sequence.
# Details: http://unicode.org/emoji/charts/emoji-zwj-sequences.html
# Emoji variation selectors are included, ligatures should make them optional.
# Uses 'U' instead of 'u' to allow 8 digit unicode literals
ZWJ_SEQUENCES = {
    # Sequences for ‍kiss: 💏
    # kiss: woman, man
    "\U0001f469\u2764\U0001f48b\U0001f468": "\U0001f469\u200d\u2764\ufe0f\u200d\U0001f48b\u200d\U0001f468",
    # kiss: man, man
    "\U0001f468\u2764\U0001f48b\U0001f468": "\U0001f468\u200d\u2764\ufe0f\u200d\U0001f48b\u200d\U0001f468",
    # kiss: woman, woman
    "\U0001f469\u2764\U0001f48b\U0001f469": "\U0001f469\u200d\u2764\ufe0f\u200d\U0001f48b\u200d\U0001f469",
    # Sequences for couple with heart: 💑
    # couple with heart: woman, man
    "\U0001f469\u2764\U0001f468": "\U0001f469\u200d\u2764\ufe0f\u200d\U0001f468",
    # couple with heart: man, man
    "\U0001f468\u2764\U0001f468": "\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468",
    # couple with heart: woman, woman
    "\U0001f469\u2764\U0001f469": "\U0001f469\u200d\u2764\ufe0f\u200d\U0001f469",
    # Sequences for family: ‍👪
    # family: man, woman, boy
    "\U0001f468\U0001f469\U0001f466": "\U0001f468\u200d\U0001f469\u200d\U0001f466",
    # family: man, woman, girl
    "\U0001f468\U0001f469\U0001f467": "\U0001f468\u200d\U0001f469\u200d\U0001f467",
    # family: man, woman, girl, boy
    "\U0001f468\U0001f469\U0001f467\U0001f466": "\U0001f468\u200d\U0001f469\u200d\U0001f467\u200d\U0001f466",
    # family: man, woman, boy, boy
    "\U0001f468\U0001f469\U0001f466\U0001f466": "\U0001f468\u200d\U0001f469\u200d\U0001f466\u200d\U0001f466",
    # family: man, woman, girl, girl
    "\U0001f468\U0001f469\U0001f467\U0001f467": "\U0001f468\u200d\U0001f469\u200d\U0001f467\u200d\U0001f467",
    # family: man, man, boy
    "\U0001f468\U0001f468\U0001f466": "\U0001f468\u200d\U0001f468\u200d\U0001f466",
    # family: man, man, girl
    "\U0001f468\U0001f468\U0001f467": "\U0001f468\u200d\U0001f468\u200d\U0001f467",
    # family: man, man, girl, boy
    "\U0001f468\U0001f468\U0001f467\U0001f466": "\U0001f468\u200d\U0001f468\u200d\U0001f467\u200d\U0001f466",
    # family: man, man, boy, boy
    "\U0001f468\U0001f468\U0001f466\U0001f466": "\U0001f468\u200d\U0001f468\u200d\U0001f466\u200d\U0001f466",
    # family: man, man, girl, girl
    "\U0001f468\U0001f468\U0001f467\U0001f467": "\U0001f468\u200d\U0001f468\u200d\U0001f467\u200d\U0001f467",
    # family: man, man, girl, girl
    "\U0001f469\U0001f469\U0001f466": "\U0001f469\u200d\U0001f469\u200d\U0001f466",
    # family: woman, woman, girl
    "\U0001f469\U0001f469\U0001f467": "\U0001f469\u200d\U0001f469\u200d\U0001f467",
    # family: woman, woman, girl, boy
    "\U0001f469\U0001f469\U0001f467\U0001f466": "\U0001f469\u200d\U0001f469\u200d\U0001f467\u200d\U0001f466",
    # family: woman, woman, boy, boy
    "\U0001f469\U0001f469\U0001f466\U0001f466": "\U0001f469\u200d\U0001f469\u200d\U0001f466\u200d\U0001f466",
    # family: woman, woman, girl, girl
    "\U0001f469\U0001f469\U0001f467\U0001f467": "\U0001f469\u200d\U0001f469\u200d\U0001f467\u200d\U0001f467",
    # eye, left speech bubble: 👁‍🗨
    "\U0001f441\U0001f5e8": "\U0001f441\u200d\U0001f5e8",
}

# A list of keycap emoji sequences indexed by the no VS16 sequence.
# Details: http://unicode.org/emoji/charts/emoji-sequences.html
# Structure: base character + U+20E3 (COMBINING ENCLOSING KEYCAP)
# VS16 (fe0f) is inserted between the base character and the keycap.
KEYCAP_SEQUENCES = {
    # Digit keycaps: 0️⃣ ~ 9️⃣
    '0\u20e3': '0\ufe0f\u20e3',   # 0️⃣
    '1\u20e3': '1\ufe0f\u20e3',   # 1️⃣
    '2\u20e3': '2\ufe0f\u20e3',   # 2️⃣
    '3\u20e3': '3\ufe0f\u20e3',   # 3️⃣
    '4\u20e3': '4\ufe0f\u20e3',   # 4️⃣
    '5\u20e3': '5\ufe0f\u20e3',   # 5️⃣
    '6\u20e3': '6\ufe0f\u20e3',   # 6️⃣
    '7\u20e3': '7\ufe0f\u20e3',   # 7️⃣
    '8\u20e3': '8\ufe0f\u20e3',   # 8️⃣
    '9\u20e3': '9\ufe0f\u20e3',   # 9️⃣
    # Special character keycaps
    '#\u20e3': '#\ufe0f\u20e3',   # #️⃣
    '*\u20e3': '*\ufe0f\u20e3',   # *️⃣
}
