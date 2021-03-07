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
    'b_0': 'CAACAgQAAx0EUZtq5wADRWBEevvdNaGPo-fXedducxzpu7utAALZAQACX1eZAAEqnpNt3SpG_x4E',
    'b_1': 'CAACAgQAAxUAAWBEeSI5_vQKUfOU1u4Dv3gMSWd8AALbAQACX1eZAAHluPl_BVzaDh4E',
    'b_2': 'CAACAgQAAxUAAWBEeSLdgvoF0YwvP8hFfe3mig2sAALdAQACX1eZAAEFe5JBdpP-cx4E',
    'b_3': 'CAACAgQAAxUAAWBEeSK4m0zPL6NBZ8CqAkUpRQAE3wEAAl9XmQABUCV1h0Ng-7oeBA',
    'b_4': 'CAACAgQAAxUAAWBEeSIzAWGwU15pF7rtzbUpxcWnAALhAQACX1eZAAHo1SP4devY_x4E',
    'b_5': 'CAACAgQAAxUAAWBEeSL8HDyPUaaSnMLoe5i9_J3kAALjAQACX1eZAALf6g-FruzaHgQ',
    'b_6': 'CAACAgQAAxUAAWBEeSKqB1S3WkIy3Wk7xmSbW3CdAALlAQACX1eZAAHwMoU1Nb4Ogh4E',
    'b_7': 'CAACAgQAAxUAAWBEeSLsl_q0nBS5cEy6Z4IwHmDwAALnAQACX1eZAAFOBAnoop1fWh4E',
    'b_8': 'CAACAgQAAx0EUZtq5wADQmBEenUFOHRVqgZyyybFJ_vk0wxPAALpAQACX1eZAAHmKrizqjwJ3h4E',
    'b_9': 'CAACAgQAAxUAAWBEeSJYSoomT7lY6FCAN-FWr8kRAALrAQACX1eZAAHvul-ZztVWih4E',
    'b_draw': 'CAACAgQAAxUAAWBEeSIdEHDbyd0vpS8FsqDRfPrsAALtAQACX1eZAAGdURg9n6qvEx4E',
    'b_skip': 'CAACAgQAAxUAAWBEeSLecCPgVJkemysJibP0m0NTAALxAQACX1eZAAHAf0ks_Y82Jx4E',
    'b_reverse': 'CAACAgQAAxUAAWBEeSIAAW3HNMbtVrwYU9xWfKSpJwAC7wEAAl9XmQABYwGXOd-V8zUeBA',
    'g_0': 'CAACAgQAAxUAAWBEeSL07V2Da4uu7H25bnO8HDjrAAL3AQACX1eZAAH7m-CsNWDzBR4E',
    'g_1': 'CAACAgQAAxUAAWBEeSJq6UKrVlv-6q7jZFUikbf4AAL5AQACX1eZAAFVNSG--aqs9B4E',
    'g_2': 'CAACAgQAAxUAAWBEeSJ5qs724d0V_VwpvTGSyJueAAL7AQACX1eZAAHDX5Qn7VbSdB4E',
    'g_3': 'CAACAgQAAxUAAWBEeSJMTW9IuS-Bi7XBm_r6Gz7IAAL9AQACX1eZAAGwUxSSKSNPah4E',
    'g_4': 'CAACAgQAAxUAAWBEeSKf96UPuYFptkMkhJ1eHO-7AAL_AQACX1eZAAEBEgKqT0vs4B4E',
    'g_5': 'CAACAgQAAxUAAWBEeSLKzUVluNRxL9hSKbgavsVaAAIBAgACX1eZAAGN2wN5nVhf3x4E',
    'g_6': 'CAACAgQAAxUAAWBEeSLVTrJlEacyfLwZnQ36V18gAAIDAgACX1eZAAFaJA80kw1XfR4E',
    'g_7': 'CAACAgQAAxUAAWBEeSIkqr4uQhuvU_IyNddGBFwNAAIFAgACX1eZAAGDbLTCiNGLBh4E',
    'g_8': 'CAACAgQAAxUAAWBEeSKeCFL_EJ2J38rIMEAVohyHAAIHAgACX1eZAAGnWrRTRZj7gR4E',
    'g_9': 'CAACAgQAAxUAAWBEeSIz0d4OZgbeWirv5jSbQuwfAAIJAgACX1eZAAHODOPdhwzltx4E',
    'g_draw': 'CAACAgQAAxUAAWBEeSLjIp35tiRgXN9u1EILwnoAAwsCAAJfV5kAAVaDTq4amUdXHgQ',
    'g_skip': 'CAACAgQAAxUAAWBEeSL2jeF2JJF-7P5QWZgVvZS3AAIPAgACX1eZAAHn-hBXxRvYQh4E',
    'g_reverse': 'CAACAgQAAxUAAWBEeSLan80ctsIPUm3mnK-fMycDAAINAgACX1eZAAFMYqmCS3vfyR4E',
    'r_0': 'CAACAgQAAxUAAWBEeSKyeEkTxP98rceacEG9i5ZeAAIRAgACX1eZAAHK9atgT_cu_h4E',
    'r_1': 'CAACAgQAAxUAAWBEeSIrFCztThkC35kPGeR6VfSLAAITAgACX1eZAAH_6pt2airFER4E',
    'r_2': 'CAACAgQAAxUAAWBEeSJO2X9T1shPZq24HZkZowHlAAIVAgACX1eZAAHQrmSSeMDfgB4E',
    'r_3': 'CAACAgQAAxUAAWBEeSKgmblDhneUTnZrjmGi2o1fAAIXAgACX1eZAAFeHWWPa-piRx4E',
    'r_4': 'CAACAgQAAxUAAWBEeSKhmPCDpWb-uM5zmctf2XdqAAIZAgACX1eZAAE7VUWywkd3KB4E',
    'r_5': 'CAACAgQAAxUAAWBEeSLm6T0pcze5IUP2vuIwJUsGAAIbAgACX1eZAAF1s0b9V-PUJB4E',
    'r_6': 'CAACAgQAAxUAAWBEeSLyAAHNZONoeA4cKXrswJCm4QACHQIAAl9XmQABfIUs9dXsSFIeBA',
    'r_7': 'CAACAgQAAxUAAWBEeSI8aCW3Rh2FP3X0MyZaCfAaAAIfAgACX1eZAAEVnCo1RKSqnB4E',
    'r_8': 'CAACAgQAAxUAAWBEeSLLQbtFmSH97Y7kzfgur1TIAAIhAgACX1eZAAEhXezQrbzKOh4E',
    'r_9': 'CAACAgQAAxUAAWBEeSKiO54aGdbYnqtgt_UwJdZ7AAIjAgACX1eZAAHN4GBkUaxpqh4E',
    'r_draw': 'CAACAgQAAxUAAWBEeSJWOlQ9f02OVBSPgQaGvkdaAAIlAgACX1eZAAGZvG1zNp2cVh4E',
    'r_skip': 'CAACAgQAAxUAAWBEeSKTPfD1WaHMcEDzVETTP6WAAAIpAgACX1eZAAFprUDwYHBu3R4E',
    'r_reverse': 'CAACAgQAAxUAAWBEeSIlnrPDefJ6rC7oPzCQZuLVAAInAgACX1eZAAGay7EvXnoVZh4E',
    'y_0': 'CAACAgQAAxUAAWBEeSIWWakqFDT_PY3hO8-ZV-b6AAIrAgACX1eZAAG1mgAB2D5sIc8eBA',
    'y_1': 'CAACAgQAAxUAAWBEeSI85dNj4GfLRs-I69Rx584mAAItAgACX1eZAAHqNCCjuSEQjh4E',
    'y_2': 'CAACAgQAAxUAAWBEeSKC9u6EUDm9pnteNWXlHS1RAAIvAgACX1eZAAH4u547rBAiBB4E',
    'y_3': 'CAACAgQAAxUAAWBEeSIbTlCfMnUpy2bTtTGWS8o0AAIxAgACX1eZAAFBQ00TMrpMeh4E',
    'y_4': 'CAACAgQAAxUAAWBEeSJONlCcK3BrA837y5LNtopnAAIzAgACX1eZAAF7IOqIuGqyDR4E',
    'y_5': 'CAACAgQAAxUAAWBEeSIE9MUJB5WhMwy0HNaPa1I-AAI1AgACX1eZAAHyIiYzI-E-Lh4E',
    'y_6': 'CAACAgQAAxUAAWBEeSIOPir3l8cUsrJNtD3R9hSQAAI3AgACX1eZAAH_E8fuZ374hx4E',
    'y_7': 'CAACAgQAAxUAAWBEeSKMOtj_ylfKG3kkGe0Gc22rAAI5AgACX1eZAAHPK6qSI6Ku_B4E',
    'y_8': 'CAACAgQAAxUAAWBEeSK_7RH2H_tSA1JNODZsAjCKAAI7AgACX1eZAAHXiL4XwJi0ex4E',
    'y_9': 'CAACAgQAAxUAAWBEeSIDXVs7B11M2bUZGz79msMoAAI9AgACX1eZAAGG_opl6vQSOB4E',
    'y_draw': 'CAACAgQAAxUAAWBEeSIKz7CuY7JcBp-XorIGLmlTAAI_AgACX1eZAAFrjyuhcA2ksx4E',
    'y_skip': 'CAACAgQAAxUAAWBEeSKFW-iE9bSeLPiHHM-YVhoOAAJDAgACX1eZAAF1m63alvMoxx4E',
    'y_reverse': 'CAACAgQAAxUAAWBEeSIBbavGiV_MDWzoLz0T1q6_AAJBAgACX1eZAAEIekObsw9tqR4E',
    'draw_four': 'CAACAgQAAxUAAWBEeSLuadKMP1ifUlsu9RVPRW2xAAL1AQACX1eZAAHXOgABZUCgVkkeBA',
    'colorchooser': 'CAACAgQAAxUAAWBEeSL7UoHK8TAOn36PQtJx7ig3AALzAQACX1eZAAHI5jbpFQE9bB4E',
    'option_draw': 'CAACAgQAAxUAAWBEeSLzdrGURyFtrR3UD5l1FWXJAAL4AgACX1eZAAH-TdXSlvEa2x4E',
    'option_pass': 'CAACAgQAAxUAAWBEeSL2ywhOBOog7s67GC8f7qzOAAL6AgACX1eZAAFuilR5QnD-Vx4E',
    'option_bluff': 'CAACAgQAAx0EUZtq5wADkWBEni4WtIAOWBgGeWWfdo2CQletAALKAgACX1eZAAHBw478rNqN0B4E',
    'option_info': 'CAACAgQAAxUAAWBEeSJj62TJvYgXghC9Q1uAd7eaAALEAgACX1eZAAGi2Qy93IIQwh4E'
}

STICKERS_GREY = {
    'b_0': 'CAACAgQAAxUAAWBEeSLnAAHv5T4xqu7S9oRSV2CDAgACRQIAAl9XmQAB8F2BTWYUGiMeBA',
    'b_1': 'CAACAgQAAxUAAWBEeSJ3WdiLXlIiBJata-4mg-h8AAJHAgACX1eZAAF_ZxC64wgdNB4E',
    'b_2': 'CAACAgQAAxUAAWBEeSJ0UnnHgf7zMBhLGKfGVjUhAAJJAgACX1eZAAF-GuNgJ25IAAEeBA',
    'b_3': 'CAACAgQAAxUAAWBEeSLxJzh9Uvhqni14lYTmdR16AAJLAgACX1eZAAHIJQ71XJ39mB4E',
    'b_4': 'CAACAgQAAxUAAWBEeSJGJ8mwJcBWFMMNCDQqGtfFAAJNAgACX1eZAAEjmR2mhJ8SsR4E',
    'b_5': 'CAACAgQAAxUAAWBEeSLNmaIbH9FwAZ3p_ZYDHyqrAAJPAgACX1eZAAEjfAwvM_8nsR4E',
    'b_6': 'CAACAgQAAxUAAWBEeSLfaux-pVfUG1vgP9qi2mw6AAJRAgACX1eZAAG_fl6oWmnXzx4E',
    'b_7': 'CAACAgQAAxUAAWBEeSLdjjvDYweLV9TdKStaxDZ5AAJTAgACX1eZAAG_xVqK-u2dzB4E',
    'b_8': 'CAACAgQAAxUAAWBEeSJpxpNBLgzxje19DnAOflhxAAJVAgACX1eZAAF8hUb4bS_NdB4E',
    'b_9': 'CAACAgQAAxUAAWBEeSKbeW8B7e-pGHOF4BZf3vHTAAJXAgACX1eZAAGXAmJ0BKvi1x4E',
    'b_draw': 'CAACAgQAAxUAAWBEeSJfzk5CcbaRKvERhLQR7vS-AAJZAgACX1eZAAFS-DsDXK7zdh4E',
    'b_skip': 'CAACAgQAAxUAAWBEeSKiZEQQRoF-vIa8XPjXuNYAA10CAAJfV5kAAXOwGJNGxkh6HgQ',
    'b_reverse': 'CAACAgQAAxUAAWBEeSIfq3uJPmCFeIeuIZODQShjAAJbAgACX1eZAAHRLf8w4EEJfx4E',
    'g_0': 'CAACAgQAAxUAAWBEeSKIt-bkpOkqxo9ZRsk5dFK4AAJjAgACX1eZAAG_c8FzjSBlOB4E',
    'g_1': 'CAACAgQAAxUAAWBEeSLogS7mK8fc3j_FEMyenv8pAAJlAgACX1eZAAH2R3CHmHduZB4E',
    'g_2': 'CAACAgQAAxUAAWBEeSIVXQMQmU_QzHTpl0D3YkhyAAJnAgACX1eZAAHB14u8vZ5pjR4E',
    'g_3': 'CAACAgQAAxUAAWBEeSIpVNB6QDwFLlaI8Cys-WF0AAJpAgACX1eZAAFaZGnJmMcN9B4E',
    'g_4': 'CAACAgQAAxUAAWBEeSI11AXHV9st9qFsOAd2xTZJAAJrAgACX1eZAAF3KxLEqQq8Kx4E',
    'g_5': 'CAACAgQAAxUAAWBEeSIPAUlencQG48txxGUarpFoAAJtAgACX1eZAAGObwogvTEInB4E',
    'g_6': 'CAACAgQAAxUAAWBEeSLYPp8dkLBJp9HTSRrb_e5vAAJvAgACX1eZAAEpOGFMRnLGmR4E',
    'g_7': 'CAACAgQAAxUAAWBEeSLsxgyqOXeuFVDxk72hB6M_AAJxAgACX1eZAAEe_yu4DVELEh4E',
    'g_8': 'CAACAgQAAxUAAWBEeSKcQy3fRmof-xueHrGp1RxIAAJzAgACX1eZAAH26plyNxWZuB4E',
    'g_9': 'CAACAgQAAxUAAWBEeSLS0wESi1l49SFI41mBe4RKAAJ1AgACX1eZAAGrwYoTMk8UPR4E',
    'g_draw': 'CAACAgQAAxUAAWBEeSI9fFywnUWy6_ATuaW8-CWTAAJ3AgACX1eZAAFnlFIJWhbZIx4E',
    'g_skip': 'CAACAgQAAxUAAWBEeSJkmRTt50NQmXSNJ67o_FYYAAJ7AgACX1eZAAFO5CqgPxquYR4E',
    'g_reverse': 'CAACAgQAAxUAAWBEeSKRvEqg4fjgaOybhJmuItDfAAJ5AgACX1eZAAE9cd3JVwlSEh4E',
    'r_0': 'CAACAgQAAxUAAWBEeSKLXeHXqARM8mMHlsV0o9QiAAJ9AgACX1eZAAEZAg2nRervSB4E',
    'r_1': 'CAACAgQAAxUAAWBEeSL-u8r7C35hNWUAASZCiNUbqQACfwIAAl9XmQABbSzzA-oXqA8eBA',
    'r_2': 'CAACAgQAAxUAAWBEeSIm9m00ELHgJRlDUiY5MpgLAAKBAgACX1eZAAGuvzFU0Su89R4E',
    'r_3': 'CAACAgQAAxUAAWBEeSK_XEe-_UQl9AnzRdMICJKTAAKDAgACX1eZAAEFFjwwFZ7GiR4E',
    'r_4': 'CAACAgQAAxUAAWBEeSKOCzr_4-T3zt2BfwP-TvBkAAKFAgACX1eZAAHZFzRnwree-x4E',
    'r_5': 'CAACAgQAAxUAAWBEeSKlGz6Ksrcjk8xN2QUSmEsoAAKHAgACX1eZAAHsdpjtu9I2IR4E',
    'r_6': 'CAACAgQAAxUAAWBEeSKYqG-SaB1fP-Oa_V7tJIKnAAKJAgACX1eZAAG2D__a-tqZBR4E',
    'r_7': 'CAACAgQAAxUAAWBEeSIex4wGZgNwoSHdAAH91uKk6AACiwIAAl9XmQABl2gLcOWBc7UeBA',
    'r_8': 'CAACAgQAAxUAAWBEeSL21_6ekKHoksg2oMaD1xZ_AAKNAgACX1eZAAGkCOaURWQl8B4E',
    'r_9': 'CAACAgQAAxUAAWBEeSLsoNKuVzcgJe61frdl2SBTAAKPAgACX1eZAAH-WS6bmv9CgR4E',
    'r_draw': 'CAACAgQAAxUAAWBEeSLquQnenT01JXFjA_Pc5bq6AAKRAgACX1eZAAF2dldgt636fx4E',
    'r_skip': 'CAACAgQAAxUAAWBEeSL54qxcyQg2v8s9U7AqxwABQgAClQIAAl9XmQABnna_S2IFXmweBA',
    'r_reverse': 'CAACAgQAAxUAAWBEeSLcuR-Gzi2lknVoOlBn_-o6AAKTAgACX1eZAAECR8T0lu-Kmx4E',
    'y_0': 'CAACAgQAAxUAAWBEeSLauyoLqZ1qNkahcaBkdIR3AAKXAgACX1eZAALmpUbJzkaKHgQ',
    'y_1': 'CAACAgQAAxUAAWBEeSIuBzIj10O3YZz-3UIcZUpbAAKZAgACX1eZAAGB_02-C22Pkx4E',
    'y_2': 'CAACAgQAAxUAAWBEeSKi08vh77rjEmYlkMwjdWGyAAKbAgACX1eZAAHVmZUJxJwqmB4E',
    'y_3': 'CAACAgQAAxUAAWBEeSKaxImpkuq6NkKV82XQEhIsAAKdAgACX1eZAAGnajv8YZQj-x4E',
    'y_4': 'CAACAgQAAxUAAWBEeSJ4T2PoRGYCbbKLZzIScizuAAKfAgACX1eZAAEmxeENpAa35R4E',
    'y_5': 'CAACAgQAAxUAAWBEeSLhGF8kjXb66nutNBisGeniAAKhAgACX1eZAAH2evQmPPzx8h4E',
    'y_6': 'CAACAgQAAxUAAWBEeSLR6KCIofFNRF-mRDQux0wlAAKjAgACX1eZAAGYOfBpuoRg_B4E',
    'y_7': 'CAACAgQAAxUAAWBEeSIUC7x7b_5fWkt18lATv7Q1AAKlAgACX1eZAAFYxwrVWROuix4E',
    'y_8': 'CAACAgQAAxUAAWBEeSKJuOipoLE2ZQAB_IsY0WgcuQACpwIAAl9XmQABddI9S-qwEgkeBA',
    'y_9': 'CAACAgQAAxUAAWBEeSIif1Phics-MnvvNixuE20vAAKpAgACX1eZAAGV1nEmuqjoJB4E',
    'y_draw': 'CAACAgQAAxUAAWBEeSKH7AL60Iji-j5sl4tVPVpjAAKrAgACX1eZAAGfJ2XK_ooNFh4E',
    'y_skip': 'CAACAgQAAxUAAWBEeSI2xMgAAdWSEtxdwYWxflqefwACrwIAAl9XmQABFUkpE3B8SVweBA',
    'y_reverse': 'CAACAgQAAxUAAWBEeSKxY_d54JtWfeGUk-4VCZdiAAKtAgACX1eZAAEiP9aakPoiDx4E',
    'draw_four': 'CAACAgQAAxUAAWBEeSLhNFOhtwJnR0QqHTT_hMx3AAJhAgACX1eZAAHWx9PCWaCqkx4E',
    'colorchooser': 'CAACAgQAAxUAAWBEeSJREV3yYbce0hXJIAncg2TFAAJfAgACX1eZAAH4WHYrSCRGIh4E'
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
