# coding=utf-8

import operator

msg = [125, 66, 69, 10, 67, 89, 10, 94, 66, 79, 10, 75, 95, 94, 66, 69, 88, 10, 69, 76, 10, 8, 126, 66, 79, 10, 98, 67,
       94, 73, 66, 66, 67, 65, 79, 88, 13, 89, 10, 109, 95, 67, 78, 79, 10, 94, 69, 10, 94, 66, 79, 10, 109, 75, 70, 75,
       82, 83, 8, 21, 10, 122, 70, 79, 75, 89, 79, 10, 89, 79, 68, 78, 10, 83, 69, 95, 88, 10, 75, 68, 89, 93, 79, 88,
       10, 94, 69, 10, 64, 69, 72, 89, 106, 71, 69, 69, 68, 73, 75, 89, 73, 75, 78, 79, 4, 73, 69, 71, 6, 10, 93, 67,
       94, 66, 10, 83, 69, 95, 88, 10, 105, 124, 10, 69, 88, 10, 102, 67, 68, 65, 79, 78, 99, 68, 10, 127, 120, 102, 4]

'''
ascii = [chr(i) for i in xrange(128)]

print ''.join(ascii[x] for x in msg)

for i in xrange(128):
    print unicode(''.join(ascii[x - i] for x in msg))
    print i
    print "----"

en_symbol_frequency = [' ', 'e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'l', 'd', 'c', 'u', 'm', 'f', 'g', 'p', 'y',
                       'w', '\\r', 'b', '', '', '.', 'v', 'k', '-', '"', '_', "'", 'x', ')', '(', ';', '0', 'j', '1',
                       'q', '=', '2', ':', 'z', '/', '*', '!', '?', '$', '3', '5', '>', '{', '}', '4', '9', '[', ']',
                       '8', '6', '7', '\\', '+', '|', '&', '<', '%', '@', '#', '^', '`', '~']

custom_symbol_frequency = [' ', 'o', 'e', 'h', 's', 'a', 't', 'r', 'i', 'n', 'c', 'u', 'd', 'y', 'm', 'k', '.', '"',
                           'g', 'l', 'l', 'w', '', '', 'x', '?', '@', '-', 'j', '_', "i", 'b', 'w', 't', '\'', 'f', 'p',
                           '1', 'p', '=', '2', ':', 'z', '/', '*', '!', 'v', '$', '3', '5', '>', '{', '}', '4', '9',
                           '[', ']', '8', '6', '7', '\\', '+', '|', '&', '<', '%', '@', '#', '^', '`', '~']

en_letter_frequency = ['e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'l', 'd', 'c', 'u', 'm', 'f', 'g', 'p', 'y', 'w',
                       'b', 'v', 'k', 'x', 'j', 'q', 'z']

et_letter_frequency = 'A,E,I,S,T,L,U,N,K,D,O,M,R,V,G,H,J,P,Ä,Õ,B,Ü,Ö,F,Z,Q'.split(',')

msg_frequency_dict = {}
for symbol in msg:
    symbol = str(symbol)
    if symbol not in msg_frequency_dict:
        msg_frequency_dict[symbol] = 1
    else:
        msg_frequency_dict[symbol] += 1
msg_frequency_dict = sorted(msg_frequency_dict.items(), key=operator.itemgetter(1), reverse=True)
print [float(x[1]) / 139.00 * 100.00 for x in msg_frequency_dict]

msg_symbol_frequency = [x[0] for x in msg_frequency_dict]

frequency_percentages = [15.827338129496402, 8.633093525179856, 7.913669064748201, 5.755395683453238,
                         5.0359712230215825, 5.0359712230215825, 5.0359712230215825, 4.316546762589928,
                         4.316546762589928, 3.597122302158273, 2.877697841726619, 2.877697841726619, 2.877697841726619,
                         2.158273381294964, 1.4388489208633095, 1.4388489208633095, 1.4388489208633095,
                         1.4388489208633095, 1.4388489208633095, 1.4388489208633095, 1.4388489208633095,
                         1.4388489208633095, 0.7194244604316548, 0.7194244604316548, 0.7194244604316548,
                         0.7194244604316548, 0.7194244604316548, 0.7194244604316548, 0.7194244604316548,
                         0.7194244604316548, 0.7194244604316548, 0.7194244604316548, 0.7194244604316548,
                         0.7194244604316548, 0.7194244604316548, 0.7194244604316548, 0.7194244604316548,
                         0.7194244604316548, 0.7194244604316548]

msg_symbol_frequency = ['10', '69', '79', '66', '89', '75', '94', '88', '67', '68', '73', '95', '78', '83', '71', '65',
                        '4', '8', '109', '70', '102', '93', '127', '64', '82', '21', '106', '6', '105', '120', '99',
                        '98', '125', '126', '13', '76', '122', '124', '72']
decoded = []
for symbol in msg:
    symbol = str(symbol)
    # print msg_symbol_frequency.index(symbol)
    try:
        decoded.append(custom_symbol_frequency[msg_symbol_frequency.index(symbol)])
    except IndexError:
        decoded.append('X')

print ''.join(decoded)

my_replacements = {
    '125': 'W',
    '66': 'h',
    '69': 'o',
    '10': ' ',
    '67': 'i',
    '89': 's',
    '94': 't',
    '79': 'e',
    '75': 'a',
    '95': 'u',
    '88': 'r',
    '76': 'f',
    '8': '"',
    '126': 'T',
    '98': 'H',
    '73': 'c',
    '65': 'k',
    '13': '\'',
    '109': 'G',
    '78': 'd',
    '70': 'l',
    '82': 'x',
    '83': 'y',
    '21': '?',
    '122': 'P',
    '68': 'n',
    '93': 'w',
    '71': 'm',
    '106': '@',
    '4': '.',
    '72': 'b',
    '64': 'j',
    '102': 'L',
    '99': 'I',
    '103': 'M',
    '104': 'B',
    '105': 'C',
    '127': 'U',
    '120': 'R',
    '124': 'V',
    '114': 'X',
    '115': 'Y',
    '100': 'N',
    '101': 'O'
}

decoded = []
for symbol in msg:
    try:
        decoded.append(my_replacements[str(symbol)])
    except KeyError:
        # print str(symbol)
        decoded.append('X')

print ''.join(decoded)
'''

# [('4', '.'), ('8', '"'), ('10', ' '), ('13', "'"), ('21', '?'), ('64', 'j'), ('65', 'k'), ('66', 'h'), ('67', 'i'),
# ('68', 'n'), ('69', 'o'), ('70', 'l'), ('71', 'm'), ('72', 'b'), ('73', 'c'), ('75', 'a'), ('76', 'f'), ('78', 'd'),
# ('79', 'e'), ('82', 'x'), ('83', 'y'), ('88', 'r'), ('89', 's'), ('93', 'w'), ('94', 't'), ('95', 'u'), ('98', 'H'),
# ('99', 'I'), ('102', 'L'), ('106', '@'), ('109', 'G'), ('122', 'P'), ('125', 'W'), ('126', 'T')]
# print sorted(my_replacements.items(), key=lambda x: int(x[0]))

# a, b, c, d, e, f, g => 75, 72, 73, 78, 79, 76, ?
# h, i, j, k, l, m, n => 66, 67, 64, 65, 70, 71, 68
# o, p, q, r, s, t, u => 69, X, X, 88, 89, 94, 95
# v, w, x, y, z => 92, 93, 82, 83, ?

# SPACE is 32 in ASCII, 10 here
# " is 34 in ASCII, 8 here
# what is 6? Would be the $ sign according to this logic...
# . is 46 in ASCII, 4 here
# ' is 39 in ASCII, 13 here
# ? is 63 in ASCII, 21 here

# b, c => 72, 73
# d, e => 78, 79
# h, i => 66, 67
# j, k => 64, 65
# l, m => 70, 71
# n, o => 68, 69
# v => 92
# x, y => 82, 83

# B, C = 104, 105
# D, E = 110, 111
# H, I => 98, 99 (+32 from h, i)
# J, K => 96, 97
# L, M => 102, 103
# N, O => 100, 101
# V => 124
# X, Y => 114, 115

# Don't get the logic, the ASCII offsets seem to go in a repeating pattern, switching signs between blocks (32), thus:
offsets = [
    42, 42, 38, 38, 42, 42, 38, 38, 26, 26, 22, 22, 38, 38, 22, 22, 42, 42, 38, 38, 42, 42, 38, 38, 26, 26, 22, 22, 38, 38, 22, 22,
    -22, -22, -26, -26, -22, -22, -26, -26, -38, -38, -42, -42, -38, -38, -42, -42, -22, -22, -26, -26, -22, -22, -26, -26, -38, -38, -42, -42, -38, -38, -42, -42,
    42, 42, 38, 38, 42, 42, 38, 38, 26, 26, 22, 22, 38, 38, 22, 22, 42, 42, 38, 38, 42, 42, 38, 38, 26, 26, 22, 22, 38, 38, 22, 22,
    -22, -22, -26, -26, -22, -22, -26, -26, -38, -38, -42, -42, -38, -38, -42, -42, -22, -22, -26, -26, -22, -22, -26, -26, -38, -38, -42, -42, -38, -38, -42, -42,
]

deciphered_ascii = [i + offsets[i] for i in xrange(128)]
print ''.join([chr(deciphered_ascii[symbol]) for symbol in msg])
