#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Telegram bot to play UNO in group chats
# Copyright (c) 2016 Jannes Höke <uno@jhoeke.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


# Colors
RED = 'r'
BLUE = 'b'
GREEN = 'g'
YELLOW = 'y'
BLACK = 'x'

COLORS = (RED, BLUE, GREEN, YELLOW)

COLOR_ICONS = {
    RED: '❤️',
    BLUE: '💙',
    GREEN: '💚',
    YELLOW: '💛',
    BLACK: '⬛️'
}

# Values
ZERO = '0'
ONE = '1'
TWO = '2'
THREE = '3'
FOUR = '4'
FIVE = '5'
SIX = '6'
SEVEN = '7'
EIGHT = '8'
NINE = '9'
DRAW_TWO = 'draw'
REVERSE = 'reverse'
SKIP = 'skip'

VALUES = (ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, DRAW_TWO,
          REVERSE, SKIP)
WILD_VALUES = (ONE, TWO, THREE, FOUR, FIVE, DRAW_TWO, REVERSE, SKIP)

# Special cards
CHOOSE = 'colorchooser'
DRAW_FOUR = 'draw_four'

SPECIALS = (CHOOSE, DRAW_FOUR)

STICKERS = {
    'b_0': 'CAACAgQAAxkDAAPaYLuVLQmXhze6Ly-o99oY7tiOUuIAAr0CAAJcO9xRGrpx4M5lH7ofBA',
    'b_1': 'CAACAgQAAxkDAAPbYLuVL1Z8iIgdfDeiNCZc9_tVcxYAAosCAAL9eORR57ji20znij4fBA',
    'b_2': 'CAACAgQAAxkDAAPcYLuVMFEB3QLur4mMh3WZ1Q87IEYAAlUCAAKjluRRo0CQtGtz1uMfBA',
    'b_3': 'CAACAgQAAxkDAAPdYLuVMiz1kBTv2LmdJMZxeHiDHz0AAq4CAAIQINxRVjNjA4mCAhcfBA',
    'b_4': 'CAACAgQAAxkDAAPeYLuVNBXyX7X9dYKYZNLij1VPA9gAAloCAAL6gORRcEUqrLQnHV8fBA',
    'b_5': 'CAACAgQAAxkDAAPfYLuVNiz-g36gRPt7O4sztzA20igAAnoCAAKtn-RRHlZF1VQmoJgfBA',
    'b_6': 'CAACAgQAAxkDAAPgYLuVN5rnrvphwqMg2k92InvYQLoAArECAAIaPtxRhyQkUsx1GzAfBA',
    'b_7': 'CAACAgQAAxkDAAPhYLuVORJDeBo2VUkXkAJ6AvfnltgAApACAAJoz-VRy-5l1KZ1jFMfBA',
    'b_8': 'CAACAgQAAxkDAAPiYLuVOiPrdPCAIdf2FvBjAAEZXAXqAAKLAgACL4XkUTnbZI1K7KaTHwQ',
    'b_9': 'CAACAgQAAxkDAAPjYLuVPCOlO6E7ccPEJsrZwjQ6Gi8AAkYCAALkn-RRGqIYxmGggGofBA',
    'b_draw': 'CAACAgQAAxkDAAPkYLuVPVEgEdqAarUf-EOpWKjBM9MAAm0CAAJEVuVRs2ogPRQNLYYfBA',
    'b_skip': 'CAACAgQAAxkDAAPlYLuVP3OOktkFtPLWgUNzRwhKTe8AApkCAAIKo-RRUyEGWAnLd0QfBA',
    'b_reverse': 'CAACAgQAAxkDAAPmYLuVQQV1Vl_hIFcIIZywSWnjMskAAoQCAAJjEeVRwkytbm7r8pUfBA',
    'g_0': 'CAACAgQAAxkDAAPnYLuVQkJSHnUUepLS50RDlO9xzGUAAokCAAKm5NxRn2-SmpmqnlofBA',
    'g_1': 'CAACAgQAAxkDAAPoYLuVRNs5xd8GrHSd2goKckD3znIAApUCAAKJ5uRRx47D25aQIDofBA',
    'g_2': 'CAACAgQAAxkDAAPpYLuVRanMhltmm2aFhkPHvK9W4iAAAo0CAAKC2-VRjpjTxVY18PAfBA',
    'g_3': 'CAACAgQAAxkDAAPqYLuVR0vcn6SFFNgWDzJ34rKAaYEAAkICAAKpNuVR9Pnzgn0brgABHwQ',
    'g_4': 'CAACAgQAAxkDAAPrYLuVSZeJ5cakVG9SLXi4MZEECIUAAq0CAAI2_t1RHYZ6OQl6WpwfBA',
    'g_5': 'CAACAgQAAxkDAAPsYLuVSp7KjP3k64czW_gXGO5AtaAAAo0CAAJz8eVRMt-7LMLVYDcfBA',
    'g_6': 'CAACAgQAAxkDAAPtYLuVTLj9U1FGk4szQmlhDSfuMO0AArYCAAJncd1RBkvtojsQnlcfBA',
    'g_7': 'CAACAgQAAxkDAAPuYLuVTlqxmgxMBtDbKGdr7gLGIUEAAnoCAAIHFuVRoMWfc2WNtLMfBA',
    'g_8': 'CAACAgQAAxkDAAPvYLuVTzW4epcepPmlhMeUXmHG6WsAAnsCAAKMp-RRsPBpdLMLqWMfBA',
    'g_9': 'CAACAgQAAxkDAAPwYLuVUY3SDIsYo5Nu6hrendaBphgAAqgCAAKvTORRz6TEXfdp-MwfBA',
    'g_draw': 'CAACAgQAAxkDAAPxYLuVUphODyOlsfSxn7YU_sUKtywAApsCAAKPhOVRLzwJaFuiLrwfBA',
    'g_skip': 'CAACAgQAAxkDAAPyYLuVVMGcM4y9AWN_FLVPYXZXFtsAAsACAALrcd1R7V2jF5sa9KofBA',
    'g_reverse': 'CAACAgQAAxkDAAPzYLuVVv6iy8z36W5007paX1SLyL8AAlACAAL1meRRq4rm5f3_yGAfBA',
    'r_0': 'CAACAgQAAxkDAAP0YLuVVw8BKmPpaD7Xu7VtXW-3rLMAAp8CAAIU-N1Rx34KaTIDYuAfBA',
    'r_1': 'CAACAgQAAxkDAAP1YLuVWm9UG7N5cn8yCw6j2rlhhkUAAl4CAAJOA9xR9e6PCTKRkRsfBA',
    'r_2': 'CAACAgQAAxkDAAP2YLuVW9RfBkc0_6gEthsKwfjXrowAAnoCAAKq6uRRfuFTll4qfuUfBA',
    'r_3': 'CAACAgQAAxkDAAP3YLuVXWW44OcQCf3IxuaE0YlKOlkAAoUCAALjKORRqu1Ua61fDqkfBA',
    'r_4': 'CAACAgQAAxkDAAP4YLuVXhOo5wnwXvsPwth296LIgmUAAtsCAAI-dtxRzM9oCqMNax4fBA',
    'r_5': 'CAACAgQAAxkDAAP5YLuVYDrrJ0HyRlDyDbx4bDvJKn8AArgCAAIsodxRvYRRRRbgy4kfBA',
    'r_6': 'CAACAgQAAxkDAAP6YLuVYqauBifae2u5LNsAAdOaracyAAKAAgACFC_lUXo37fNGJkbdHwQ',
    'r_7': 'CAACAgQAAxkDAAP7YLuVYyGP3PctMRCrGaWBe8b57yUAAs8CAAIBrtxRgooljlipBE0fBA',
    'r_8': 'CAACAgQAAxkDAAP8YLuVZQKcPbYd800NygNrpQABWJCTAALdAgACT_XdUarZa7-01oJKHwQ',
    'r_9': 'CAACAgQAAxkDAAP9YLuVZryKll1-UhYwfuDwsmRuURIAAq8CAALKNd1R531BdNP7NnYfBA',
    'r_draw': 'CAACAgQAAxkDAAP-YLuVaGvnRYQoiaJo8z7GB86J_XsAAukCAAKjcNxRN2cTlXr5d6cfBA',
    'r_skip': 'CAACAgQAAxkDAAP_YLuVakMN37giDztbq8hQz72bh7UAApICAALDIeVRpRrPE_R1MTofBA',
    'r_reverse': 'CAACAgQAAxkDAAIBAAFgu5Vs0iudZx65VnAsWUKIbcX1nwAC3AIAAoMI3VHcBgtkpvNj4h8E',
    'y_0': 'CAACAgQAAxkDAAIBAWC7lW1CC-vKoeVlQlK5Ybcgm70tAAKsAgACnKjcUdHBxxt_acGQHwQ',
    'y_1': 'CAACAgQAAxkDAAIBAmC7lW9KVvB4pdo9ROeXvfBnXk8sAAK1AgAC5fLcUeCYn16uXlVGHwQ',
    'y_2': 'CAACAgQAAxkDAAIBA2C7lXBJsf1Ev5nf4GINkrLk8IIEAAL9AgACn-zcUSI4IXVmIb-yHwQ',
    'y_3': 'CAACAgQAAxkDAAIBBGC7lXP1-FtZifNzW3Od3TnPL0BNAAMDAAKumdxRntRnDD24q7gfBA',
    'y_4': 'CAACAgQAAxkDAAIBBWC7lXTJVxepoQABLyhITmNY8u9SkwAC5wIAAiAP3VGxOi6QlsP6xh8E',
    'y_5': 'CAACAgQAAxkDAAIBBmC7lXZsdCFF3cXgtzO--skpTXG2AAKKAgAC5XHkUfJDdfaagBAPHwQ',
    'y_6': 'CAACAgQAAxkDAAIBB2C7lXdQCt-KkKJoHdFBdlocmq65AAJBAgACSOLlUQZZbQ8UI6YpHwQ',
    'y_7': 'CAACAgQAAxkDAAIBCGC7lXmktR1f8U1VbdhX3CtHfytFAAKHAgACmHfkUSsVb8QSDYRUHwQ',
    'y_8': 'CAACAgQAAxkDAAIBCWC7lXoV29uSDdm-P22n_crRiEDEAAKZAgAClVrdUTLAxkBgqwhVHwQ',
    'y_9': 'CAACAgQAAxkDAAIBCmC7lXxuYUQ8dbT9JDpyu5_9CdGYAAKJAgACpSzlUSrJIpIPuehMHwQ',
    'y_draw': 'CAACAgQAAxkDAAIBC2C7lX3n69_qcGBwzk2MGBxLKCnOAAJiAgACY_vlUQqxCK7Lcbw0HwQ',
    'y_skip': 'CAACAgQAAxkDAAIBDGC7lX-ntoqgXVSWJ58opst2cNfKAAJ5AgACliLlUVPQD5ae9CsCHwQ',
    'y_reverse': 'CAACAgQAAxkDAAIBDWC7lYAYMb32xqvvOYzJNV2XsVzoAAJXAgAC7pzkUVIc7G7qyIvtHwQ',
    'draw_four': 'CAACAgQAAxkDAAIBDmC7lYJGEZ9soGv2FowgqFv5SNVmAAI-AgAC0BjlUZLl4rmiIfu8HwQ',
    'colorchooser': 'CAACAgQAAxkDAAIBD2C7lYPNvqKWcFw3LAQ6HAxm-qoeAAK7AgACrcXdUR3SoKdvzeHKHwQ',
    'option_draw': 'CAACAgQAAxkDAAIBEGC7lYXAcHk9NL-G17JGgbEcZ9t8AAKJAgAC6vbkUS09qMazeY-pHwQ',
    'option_pass': 'CAACAgQAAxkDAAIBEWC7lYZZrPbin_4yX_9UbL0rgg_yAAKtAgACXBfkUQvYY5njAaoLHwQ',
    'option_bluff': 'CAACAgQAAxkDAAIBEmC7lYjm4OcWYOKXeHMV1hB5TkBmAAKsAgACQI_dUZQZ-VR0tYSIHwQ',
    'option_info': 'CAACAgQAAxkDAAIBE2C7lYmjCbb2ejTorEXWweWLmR4NAALNAgACd_LdURvZc6AkZH_cHwQ'
}

STICKERS_GREY = {
    'b_0': 'CAACAgQAAxkDAAIBPWC7lpZhgbDoIybEyRdaMdIfCKX8AAKCAgAC8gjlUQABGjXAibxrzR8E',
    'b_1': 'CAACAgQAAxkDAAIBPmC7lpkLjZ3XR32U-XPm0crBEH8xAAJsAgADteVRyBsz7maXAvQfBA',
    'b_2': 'CAACAgQAAxkDAAIBP2C7lpxCV6PPnj6nUd6yvHrz51XrAAKlAgACD4fkUXGhH5kUCs-DHwQ',
    'b_3': 'CAACAgQAAxkDAAIBQGC7lp6zzhD0-u_1XA25QU52nxFXAAKsAgAC5czdUcV5ireBtNIBHwQ',
    'b_4': 'CAACAgQAAxkDAAIBQWC7lqF2KTnfh6afuf9p30ZXqZWvAAK8AgACsk3lURGwEpjki4F1HwQ',
    'b_5': 'CAACAgQAAxkDAAIBQmC7lqQpLd328-2AgrzC7DbsK8IOAAKdAgACv2DkUbHKeuICKpTrHwQ',
    'b_6': 'CAACAgQAAxkDAAIBQ2C7lqYyxdItIvAWEe7BVGJWFBgSAAKuAgACu1zcUcLgUngLFH_-HwQ',
    'b_7': 'CAACAgQAAxkDAAIBRGC7lqnO9lhG57LM5FPkTAzKMEDZAAKVAgACCwLkUd-s1P8c5_G1HwQ',
    'b_8': 'CAACAgQAAxkDAAIBRWC7lquARjdbE4HSm-J_-6Lg2UFgAAJ4AgACQFrlUeQZmYkXVT6wHwQ',
    'b_9': 'CAACAgQAAxkDAAIBRmC7lq71h3ANwHctq_CC3eyi-PdbAAJ6AgACppLkUaEdfjeXNcbuHwQ',
    'b_draw': 'CAACAgQAAxkDAAIBR2C7lrEWsuDJWPBG3iKKHvDX83WIAAK3AgACwrndUfBBUKOphgUZHwQ',
    'b_skip': 'CAACAgQAAxkDAAIBSGC7lrQ37zUdtBSoPoeN5D0NCWEKAAJuAgACbQXkUSFGHBlICG17HwQ',
    'b_reverse': 'CAACAgQAAxkDAAIBSWC7lrbqMG5zzcRBvAa1BMDoG6EPAAJyAgACZcjlURL6zsSq6EhLHwQ',
    'g_0': 'CAACAgQAAxkDAAIBSmC7lrnZXyGdjhzMIiH5-brHytVmAAKSAgACJeDlUbQ_oUAonLboHwQ',
    'g_1': 'CAACAgQAAxkDAAIBS2C7lrvUVYXs9MAtYuwb6bXF7aiKAALYAgACIvTcUYHQ2Wx0K4qjHwQ',
    'g_2': 'CAACAgQAAxkDAAIBTGC7lr5V-xAAAWgj6Wq2g8uS-OZU3gACuAIAAk1B3FHYuNAEMtNZTx8E',
    'g_3': 'CAACAgQAAxkDAAIBTWC7lsBKuxL8gkFaBsV_vV_FoJCwAAKjAgACQSTcUe10_-nnYZ01HwQ',
    'g_4': 'CAACAgQAAxkDAAIBTmC7lsTsffZXadCpUY9YIqb_lbSEAAK2AgACMpLcUQs3IqQooR47HwQ',
    'g_5': 'CAACAgQAAxkDAAIBT2C7lse9R4bgHYk1SwZAbZDW_4vIAALEAgACAaPdUWNUl6VMVGQWHwQ',
    'g_6': 'CAACAgQAAxkDAAIBUGC7lsmbRW2oCehK_WtFCuMKNN0mAALvAgACJNHdUYtLf28vzOpPHwQ',
    'g_7': 'CAACAgQAAxkDAAIBUWC7lsxIkLq2nlFzFPQvRZL0lLemAAKAAgACWGjdUf_MIgAB_ItJmx8E',
    'g_8': 'CAACAgQAAxkDAAIBUmC7ls5idaAKOeMwLw9xWvLrFlMTAAKDAgAC5PncUU8hniDfiFJVHwQ',
    'g_9': 'CAACAgQAAxkDAAIBU2C7ltHxKblhYUhST6dbE8y0cKBVAAKMAgAC40_lUf93WloipOpfHwQ',
    'g_draw': 'CAACAgQAAxkDAAIBVGC7ltSYAAFO6YyzXITL3ik54Vi5yQACjAIAAseL5VHIgXujCBhFSh8E',
    'g_skip': 'CAACAgQAAxkDAAIBVWC7ltbAiwX4_Z5DXjynad8PZjfRAAKvAgAC8dnlUUDfeJW-nHJbHwQ',
    'g_reverse': 'CAACAgQAAxkDAAIBVmC7ltk5S_1rHVRCWvp-jkz5vSvjAAJWAgACYu_lUaBDVHXnYRQ7HwQ',
    'r_0': 'CAACAgQAAxkDAAIBV2C7ltwOb8rht0A3lRDoTydATlzKAAJ3AgACb3LkUTqIzvrgbScBHwQ',
    'r_1': 'CAACAgQAAxkDAAIBWGC7lt_zG-CJOfcvV8nGtxyc-AbjAALCAgACVgvdUYWXRGkGxtcEHwQ',
    'r_2': 'CAACAgQAAxkDAAIBWWC7luEX7a0t8MmFaSsPVQABkOIz9wACogIAApAw5FFIBBetE7iTHh8E',
    'r_3': 'CAACAgQAAxkDAAIBWmC7luP6KMKHyfhJv1op5xOrPE-sAAJ6AgACzzXdUXs18Icw-xpcHwQ',
    'r_4': 'CAACAgQAAxkDAAIBW2C7luZI93FQyAPDxixSZordOEWsAAKhAgACOiDcUbEhp7GhzYXyHwQ',
    'r_5': 'CAACAgQAAxkDAAIBXGC7lul2MiGRpp46oseq3lYelUOEAAJmAgACWYbkUTlwWyG5MhlTHwQ',
    'r_6': 'CAACAgQAAxkDAAIBXWC7luumveD2CxtrcL8YKLdMseXNAAJyAgACQbjlUeb-mSvNCK8dHwQ',
    'r_7': 'CAACAgQAAxkDAAIBXmC7lu7bA2FOjL2rKztxkr-HW9QZAAKrAgACQEzlURA243p5QZHpHwQ',
    'r_8': 'CAACAgQAAxkDAAIBX2C7lvDCa0SGRbika_2i_MLJrG7IAAJhAgAC-NflUbtutGXBVAABKx8E',
    'r_9': 'CAACAgQAAxkDAAIBYGC7lvST7B9jZ_OR3yEDhOC_7lCZAAKrAgACIq_lUXRigWH-iKHTHwQ',
    'r_draw': 'CAACAgQAAxkDAAIBYWC7lvYgDq37CxRaxu44MmhCor9nAAKJAgACNF7lUTFhA0YvGBOcHwQ',
    'r_skip': 'CAACAgQAAxkDAAIBYmC7lvkoKWBUmyNmbpneKyNeP7AzAAKcAgAC2fTlUWmD1dq1hQYoHwQ',
    'r_reverse': 'CAACAgQAAxkDAAIBY2C7lvsCg4nEUbm0e1HOLk5u2q45AAKeAgACnsrlUQXjS37miqGOHwQ',
    'y_0': 'CAACAgQAAxkDAAIBZGC7lv6c-5bbVHSUgU7AlWLGcldGAAIGAwAC2IbcUZlPf2vk8QwlHwQ',
    'y_1': 'CAACAgQAAxkDAAIBZWC7lwHgzM_FhtBfah0sKnNv3zJxAAKHAgAC_UHlUZwnt2Txi1mtHwQ',
    'y_2': 'CAACAgQAAxkDAAIBZmC7lwSmdkRc6PmKVBR7JDUNflJrAAKWAgACAaHlUe1y9nevvwH4HwQ',
    'y_3': 'CAACAgQAAxkDAAIBZ2C7lwa5S3UpmLEGLLkuuKxKaKjMAAJ7AgACSd7dUYW3HFq-9jUQHwQ',
    'y_4': 'CAACAgQAAxkDAAIBaGC7lwlN9QJ56vskGVwSagxYzr9YAAJkAgAC_EvkUZowPFOgUNI9HwQ',
    'y_5': 'CAACAgQAAxkDAAIBaWC7lwyR5ShowfOdrql8nRagvoFXAAKNAgACLFvcUTFGl85gi17oHwQ',
    'y_6': 'CAACAgQAAxkDAAIBamC7lw4pkfvIAAF7o_PBdJmzyIQ-wQACmAIAArZD3VH3QHmmBbm9rx8E',
    'y_7': 'CAACAgQAAxkDAAIBa2C7lxGpAtUPVQ8IxIFtbTqNZLmwAALDAgACjUXcUfZY6aL1qtPuHwQ',
    'y_8': 'CAACAgQAAxkDAAIBbGC7lxM9SS2FAvFJmq0tbL4GdqtCAAKQAgACyPzkUUu4DtZPg8H6HwQ',
    'y_9': 'CAACAgQAAxkDAAIBbWC7lxY-gzutcijQVoMOlpxcDkD_AAKfAgACZHzcUZQ3fWY-f1-DHwQ',
    'y_draw': 'CAACAgQAAxkDAAIBbmC7lxiGHfb5GyucmUb9pxCKu-q9AALdAgACLD_cUfRy4_6fJ4nsHwQ',
    'y_skip': 'CAACAgQAAxkDAAIBb2C7lxuowCWA6yknv2PLItWFd3MuAAKXAgACCx_cUdOLrnMk6GaZHwQ',
    'y_reverse': 'CAACAgQAAxkDAAIBcGC7lx33oZaCPs9FPQI5AAH7bZTSyAACyAIAAkEJ3FF9RuPkqyQmjx8E',
    'draw_four': 'CAACAgQAAxkDAAIBcWC7lyB-48Ksepu3PlMLmwuKIuaLAAKJAgACv7jkUStcVgYPiInoHwQ',
    'colorchooser': 'CAACAgQAAxkDAAIBcmC7lyOWBBKhjVGCCMvCYgUsrUarAAJuAgACjOzkUW_UX1sPPkDkHwQ'
}


class Card(object):
    """This class represents an UNO card"""

    def __init__(self, color, value, special=None):
        self.color = color
        self.value = value
        self.special = special

    def __str__(self):
        if self.special:
            return self.special
        else:
            return '%s_%s' % (self.color, self.value)

    def __repr__(self):
        if self.special:
            return '%s%s%s' % (COLOR_ICONS.get(self.color, ''),
                               COLOR_ICONS[BLACK],
                               ' '.join([s.capitalize()
                                         for s in self.special.split('_')]))
        else:
            return '%s%s' % (COLOR_ICONS[self.color], self.value.capitalize())

    def __eq__(self, other):
        """Needed for sorting the cards"""
        return str(self) == str(other)

    def __lt__(self, other):
        """Needed for sorting the cards"""
        return str(self) < str(other)


def from_str(string):
    """Decodes a Card object from a string"""
    if string not in SPECIALS:
        color, value = string.split('_')
        return Card(color, value)
    else:
        return Card(None, None, string)
