
import numpy as np

from nose.tools import assert_equal, assert_not_equal, assert_true

ford_2012_dates = np.asarray([ 20120103, 20120104, 20120105, 20120106, 20120109,
    20120110, 20120111, 20120112, 20120113, 20120117, 20120118, 20120119,
    20120120, 20120123, 20120124, 20120125, 20120126, 20120127, 20120130,
    20120131, 20120201, 20120202, 20120203, 20120206, 20120207, 20120208,
    20120209, 20120210, 20120213, 20120214, 20120215, 20120216, 20120217,
    20120221, 20120222, 20120223, 20120224, 20120227, 20120228, 20120229,
    20120301, 20120302, 20120305, 20120306, 20120307, 20120308, 20120309,
    20120312, 20120313, 20120314, 20120315, 20120316, 20120319, 20120320,
    20120321, 20120322, 20120323, 20120326, 20120327, 20120328, 20120329,
    20120330, 20120402, 20120403, 20120404, 20120405, 20120409, 20120410,
    20120411, 20120412, 20120413, 20120416, 20120417, 20120418, 20120419,
    20120420, 20120423, 20120424, 20120425, 20120426, 20120427, 20120430,
    20120501, 20120502, 20120503, 20120504, 20120507, 20120508, 20120509,
    20120510, 20120511, 20120514, 20120515, 20120516, 20120517, 20120518,
    20120521, 20120522, 20120523, 20120524, 20120525, 20120529, 20120530,
    20120531, 20120601, 20120604, 20120605, 20120606, 20120607, 20120608,
    20120611, 20120612, 20120613, 20120614, 20120615, 20120618, 20120619,
    20120620, 20120621, 20120622, 20120625, 20120626, 20120627, 20120628,
    20120629, 20120702, 20120703, 20120705, 20120706, 20120709, 20120710,
    20120711, 20120712, 20120713, 20120716, 20120717, 20120718, 20120719,
    20120720, 20120723, 20120724, 20120725, 20120726, 20120727, 20120730,
    20120731, 20120801, 20120802, 20120803, 20120806, 20120807, 20120808,
    20120809, 20120810, 20120813, 20120814, 20120815, 20120816, 20120817,
    20120820, 20120821, 20120822, 20120823, 20120824, 20120827, 20120828,
    20120829, 20120830, 20120831, 20120904, 20120905, 20120906, 20120907,
    20120910, 20120911, 20120912, 20120913, 20120914, 20120917, 20120918,
    20120919, 20120920, 20120921, 20120924, 20120925, 20120926, 20120927,
    20120928, 20121001, 20121002, 20121003, 20121004, 20121005, 20121008,
    20121009, 20121010, 20121011, 20121012, 20121015, 20121016, 20121017,
    20121018, 20121019, 20121022, 20121023, 20121024, 20121025, 20121026,
    20121031, 20121101, 20121102, 20121105, 20121106, 20121107, 20121108,
    20121109, 20121112, 20121113, 20121114, 20121115, 20121116, 20121119,
    20121120, 20121121, 20121123, 20121126, 20121127, 20121128, 20121129,
    20121130, 20121203, 20121204, 20121205, 20121206, 20121207, 20121210,
    20121211, 20121212, 20121213, 20121214, 20121217, 20121218, 20121219,
    20121220, 20121221, 20121224, 20121226, 20121227, 20121228, 20121231 ])

ford_2012 = {
    'open': np.asarray([ 11.00, 11.15, 11.33, 11.74, 11.83, 12.00, 11.74, 12.16,
        12.01, 12.20, 12.03, 12.48, 12.55, 12.69, 12.56, 12.80, 13.03, 11.96,
        12.06, 12.47, 12.73, 12.40, 12.47, 12.85, 12.93, 12.91, 12.89, 12.52,
        12.74, 12.46, 12.47, 12.38, 12.84, 12.74, 12.49, 12.27, 12.43, 12.11,
        12.34, 12.28, 12.48, 12.74, 12.67, 12.23, 12.21, 12.41, 12.53, 12.57,
        12.48, 12.64, 12.90, 12.86, 12.52, 12.48, 12.59, 12.48, 12.31, 12.45,
        12.51, 12.35, 12.33, 12.55, 12.50, 12.71, 12.46, 12.38, 12.26, 12.19,
        11.99, 11.94, 11.98, 12.01, 11.98, 11.81, 11.81, 11.71, 11.15, 11.61,
        11.51, 11.71, 12.03, 11.42, 11.25, 11.16, 11.13, 10.84, 10.53, 10.60,
        10.48, 10.83, 10.61, 10.41, 10.34, 10.23, 10.16, 10.08, 10.02, 10.25,
        10.32, 10.50, 10.61, 10.69, 10.73, 10.62, 10.33, 10.15, 10.01, 10.29,
        10.73, 10.48, 10.77, 10.47, 10.39, 10.27, 10.40, 10.35, 10.37, 10.58,
        10.65, 10.35, 10.13, 10.06, 10.05, 9.93, 9.95, 9.50, 9.53, 9.67, 9.47,
        9.46, 9.50, 9.33, 9.26, 9.16, 9.22, 9.28, 9.38, 9.45, 9.28, 9.08, 9.17,
        9.17, 9.05, 8.99, 9.04, 9.13, 9.29, 8.99, 9.02, 9.13, 9.18, 9.25, 9.31,
        9.30, 9.35, 9.45, 9.44, 9.50, 9.65, 9.58, 9.65, 9.50, 9.45, 9.42, 9.51,
        9.37, 9.33, 9.30, 9.39, 9.37, 9.45, 9.66, 9.95, 10.08, 10.18, 10.25,
        10.20, 10.41, 10.27, 10.30, 10.49, 10.48, 10.53, 10.30, 10.35, 9.98,
        10.13, 9.99, 9.89, 10.01, 9.82, 10.06, 10.17, 10.06, 10.21, 10.12,
        10.06, 10.14, 10.11, 10.26, 10.31, 10.36, 10.42, 10.14, 10.02, 10.08,
        10.42, 10.35, 10.70, 11.19, 11.31, 11.15, 11.33, 11.25, 11.07, 10.76,
        11.03, 10.89, 11.02, 10.57, 10.58, 10.65, 10.85, 10.84, 10.98, 11.05,
        11.10, 11.05, 11.32, 11.52, 11.56, 11.40, 11.32, 11.26, 11.27, 11.41,
        11.51, 11.52, 11.46, 11.27, 11.16, 11.48, 11.79, 11.74, 11.55, 11.67,
        12.31, 12.79, 12.55, 12.88, ]),

    'high': np.asarray([ 11.25, 11.53, 11.63, 11.80, 11.95, 12.05, 12.18, 12.18,
        12.08, 12.26, 12.37, 12.72, 12.64, 12.84, 12.86, 12.98, 13.05, 12.53,
        12.44, 12.51, 12.75, 12.43, 12.84, 13.00, 12.97, 12.96, 12.90, 12.66,
        12.74, 12.58, 12.57, 12.77, 12.88, 12.76, 12.51, 12.44, 12.46, 12.36,
        12.35, 12.55, 12.77, 12.94, 12.68, 12.25, 12.30, 12.55, 12.73, 12.59,
        12.72, 12.90, 13.04, 12.90, 12.68, 12.61, 12.67, 12.54, 12.37, 12.50,
        12.61, 12.36, 12.52, 12.58, 12.65, 12.95, 12.52, 12.58, 12.29, 12.28,
        12.02, 12.13, 12.03, 12.05, 12.00, 11.85, 11.88, 11.72, 11.40, 11.61,
        11.75, 11.93, 12.04, 11.47, 11.34, 11.17, 11.15, 10.87, 10.79, 10.64,
        10.81, 10.86, 10.83, 10.53, 10.34, 10.43, 10.25, 10.18, 10.23, 10.40,
        10.45, 10.62, 10.68, 10.88, 10.75, 10.68, 10.37, 10.18, 10.24, 10.58,
        10.78, 10.68, 10.80, 10.55, 10.49, 10.45, 10.42, 10.40, 10.64, 10.74,
        10.68, 10.40, 10.18, 10.08, 10.10, 10.09, 9.98, 9.60, 9.79, 9.74, 9.52,
        9.47, 9.55, 9.38, 9.28, 9.32, 9.32, 9.35, 9.52, 9.50, 9.35, 9.21, 9.24,
        9.20, 9.11, 9.10, 9.18, 9.28, 9.42, 9.03, 9.15, 9.21, 9.39, 9.38, 9.46,
        9.36, 9.42, 9.66, 9.54, 9.67, 9.66, 9.64, 9.70, 9.56, 9.54, 9.52, 9.52,
        9.44, 9.40, 9.34, 9.43, 9.47, 9.62, 9.96, 10.23, 10.28, 10.25, 10.30,
        10.38, 10.57, 10.42, 10.45, 10.66, 10.52, 10.54, 10.40, 10.37, 10.12,
        10.18, 10.00, 10.08, 10.05, 10.02, 10.15, 10.28, 10.12, 10.25, 10.12,
        10.26, 10.25, 10.25, 10.32, 10.41, 10.57, 10.43, 10.24, 10.11, 10.29,
        10.49, 10.42, 11.17, 11.30, 11.38, 11.35, 11.59, 11.34, 11.23, 11.10,
        11.16, 11.10, 11.05, 10.80, 10.64, 10.90, 11.02, 11.00, 11.10, 11.14,
        11.27, 11.26, 11.53, 11.60, 11.70, 11.44, 11.40, 11.31, 11.50, 11.53,
        11.58, 11.56, 11.50, 11.27, 11.41, 11.68, 11.85, 11.80, 11.86, 12.40,
        12.79, 12.81, 12.88, 13.08, ]),

    'low': np.asarray([ 10.99, 11.07, 11.24, 11.52, 11.70, 11.63, 11.65, 11.89,
        11.84, 11.96, 12.00, 12.43, 12.45, 12.55, 12.46, 12.70, 12.66, 11.79,
        12.00, 12.20, 12.29, 12.20, 12.39, 12.71, 12.83, 12.80, 12.67, 12.37,
        12.51, 12.34, 12.33, 12.38, 12.71, 12.46, 12.22, 12.16, 12.19, 11.99,
        12.20, 12.25, 12.45, 12.68, 12.41, 12.00, 12.15, 12.32, 12.48, 12.37,
        12.40, 12.63, 12.83, 12.51, 12.48, 12.39, 12.55, 12.24, 12.18, 12.39,
        12.30, 12.18, 12.24, 12.40, 12.44, 12.46, 12.32, 12.38, 12.11, 11.65,
        11.88, 11.86, 11.84, 11.83, 11.88, 11.72, 11.58, 11.39, 11.15, 11.36,
        11.43, 11.67, 11.52, 11.15, 11.11, 11.00, 10.85, 10.63, 10.52, 10.40,
        10.41, 10.66, 10.56, 10.30, 10.10, 10.15, 10.01, 9.96, 10.00, 10.15,
        10.22, 10.38, 10.51, 10.68, 10.52, 10.40, 10.06, 9.91, 9.97, 10.27,
        10.52, 10.38, 10.45, 10.31, 10.22, 10.21, 10.26, 10.26, 10.35, 10.52,
        10.25, 10.18, 9.95, 9.96, 9.97, 9.93, 9.46, 9.30, 9.49, 9.53, 9.40,
        9.31, 9.28, 9.26, 9.12, 9.14, 9.15, 9.12, 9.34, 9.33, 9.18, 9.05, 8.95,
        8.91, 8.83, 8.88, 9.01, 9.12, 8.99, 8.82, 8.96, 9.09, 9.18, 9.24, 9.30,
        9.23, 9.25, 9.42, 9.41, 9.49, 9.60, 9.51, 9.52, 9.40, 9.42, 9.41, 9.38,
        9.31, 9.29, 9.25, 9.31, 9.35, 9.39, 9.66, 9.93, 10.06, 10.13, 10.17,
        10.12, 10.39, 10.26, 10.28, 10.45, 10.35, 10.36, 10.26, 10.06, 9.86,
        10.02, 9.81, 9.88, 9.71, 9.76, 9.96, 10.13, 9.99, 10.02, 9.95, 10.05,
        10.09, 10.09, 10.22, 10.26, 10.33, 10.13, 10.03, 9.97, 10.01, 10.28,
        10.22, 10.60, 10.88, 11.15, 11.13, 11.26, 11.04, 10.89, 10.71, 10.96,
        10.86, 10.62, 10.46, 10.38, 10.65, 10.76, 10.80, 10.96, 10.97, 11.10,
        10.98, 11.32, 11.33, 11.40, 11.23, 11.18, 11.19, 11.26, 11.41, 11.40,
        11.43, 11.21, 11.03, 11.14, 11.40, 11.62, 11.58, 11.47, 11.67, 12.31,
        12.36, 12.52, 12.76, ]),

    'close': np.asarray([ 11.13, 11.30, 11.59, 11.71, 11.80, 11.80, 12.07, 12.14,
        12.04, 12.02, 12.34, 12.61, 12.59, 12.66, 12.82, 12.93, 12.79, 12.21,
        12.29, 12.42, 12.33, 12.26, 12.79, 12.96, 12.88, 12.84, 12.69, 12.44,
        12.54, 12.48, 12.38, 12.74, 12.75, 12.53, 12.28, 12.40, 12.23, 12.30,
        12.25, 12.38, 12.66, 12.72, 12.46, 12.09, 12.24, 12.46, 12.58, 12.43,
        12.70, 12.88, 12.90, 12.51, 12.63, 12.54, 12.57, 12.32, 12.32, 12.48,
        12.32, 12.32, 12.50, 12.48, 12.62, 12.64, 12.51, 12.47, 12.22, 11.79,
        11.91, 12.07, 11.92, 11.88, 11.91, 11.79, 11.66, 11.41, 11.35, 11.39,
        11.73, 11.87, 11.60, 11.28, 11.23, 11.10, 10.92, 10.67, 10.66, 10.61,
        10.69, 10.71, 10.58, 10.32, 10.15, 10.16, 10.01, 10.01, 10.20, 10.19,
        10.41, 10.59, 10.60, 10.84, 10.66, 10.56, 10.12, 10.04, 10.19, 10.57,
        10.55, 10.66, 10.45, 10.50, 10.30, 10.41, 10.35, 10.34, 10.56, 10.65,
        10.27, 10.19, 10.01, 10.01, 10.02, 10.09, 9.59, 9.39, 9.60, 9.57, 9.50,
        9.45, 9.35, 9.33, 9.13, 9.27, 9.26, 9.34, 9.38, 9.35, 9.21, 9.17, 9.06,
        8.97, 8.96, 9.00, 9.10, 9.24, 9.04, 8.92, 9.09, 9.15, 9.31, 9.35, 9.34,
        9.35, 9.40, 9.44, 9.49, 9.59, 9.63, 9.63, 9.53, 9.49, 9.45, 9.49, 9.39,
        9.34, 9.32, 9.31, 9.34, 9.41, 9.57, 9.92, 10.14, 10.11, 10.15, 10.21,
        10.34, 10.53, 10.39, 10.42, 10.59, 10.44, 10.40, 10.32, 10.09, 10.01,
        10.02, 9.86, 9.93, 9.79, 9.94, 10.11, 10.16, 10.05, 10.10, 9.98, 10.14,
        10.12, 10.22, 10.30, 10.41, 10.43, 10.18, 10.17, 10.00, 10.17, 10.39,
        10.36, 11.16, 11.25, 11.17, 11.25, 11.42, 11.06, 10.90, 10.93, 10.97,
        11.00, 10.67, 10.57, 10.50, 10.83, 10.85, 10.92, 11.10, 11.11, 11.10,
        11.25, 11.53, 11.45, 11.41, 11.31, 11.31, 11.24, 11.48, 11.47, 11.49,
        11.47, 11.27, 11.10, 11.39, 11.67, 11.73, 11.77, 11.86, 12.40, 12.79,
        12.76, 12.87, 12.95, ]),

    'volume': np.asarray([ 45709900, 79725200, 67877500, 59840700, 53981500,
        121750600, 63806000, 48687700, 46366700, 44398400, 47102700, 70894200,
        43705700, 49379700, 45768400, 54021600, 75470700, 142155300, 57752600,
        46412100, 71669000, 48347600, 78851200, 46363300, 39413500, 35352500,
        52290500, 52505500, 34474400, 39627900, 38174800, 49164400, 30778000,
        38409800, 43326000, 36747600, 31399300, 38703400, 30789000, 62093700,
        68262000, 49063500, 28433700, 57374500, 28440900, 37099100, 36159300,
        30275700, 42783600, 47578500, 55286600, 77119600, 52445700, 40214400,
        27521400, 50117100, 44755000, 26692200, 35070700, 41051700, 51039700,
        36381000, 43966900, 97034200, 51505000, 37939500, 42515300, 77370300,
        34724400, 26988800, 39675000, 31903500, 35981200, 32314000, 48169200,
        52631000, 31269200, 38615200, 45185400, 40889300, 83070300, 46156300,
        43959200, 48572900, 40238400, 53268400, 33235200, 46174500, 54501200,
        42526100, 36561300, 50225200, 41886500, 44321300, 49648900, 50572000,
        38134900, 44295700, 75647800, 45334100, 30430800, 43760600, 44592100,
        54297000, 68237000, 57305600, 38326200, 50458000, 33846100, 30811600,
        35811400, 35130800, 53471900, 37531800, 39442000, 27361000, 37155900,
        40810100, 40062800, 56427300, 44297600, 31871900, 33278900, 38648400,
        138138600, 63388600, 49629300, 31783900, 30355400, 37441600, 33516600,
        32028700, 55111000, 30248300, 28838200, 29510000, 31010000, 33615000,
        27968300, 33773800, 53519200, 44338200, 51798900, 67986800, 40958300,
        41360900, 65973000, 45326500, 38631400, 23819100, 43574500, 22630300,
        30909800, 19618800, 21122000, 21129500, 21308300, 34323700, 34533900,
        38923800, 26281100, 26965500, 23537700, 19574600, 22754200, 23084400,
        26115700, 16459400, 28029200, 37965000, 40608800, 67996400, 60617000,
        43381300, 28165300, 28046500, 50920200, 55934300, 31922200, 34937000,
        42403000, 28755100, 35459800, 28557900, 36866300, 44362600, 25740900,
        44586300, 33445600, 63630000, 51023800, 46855500, 40693900, 25473900,
        38235700, 33951600, 39328700, 24108500, 26466500, 32788400, 29346300,
        44041700, 40493000, 39149700, 32476500, 49339800, 59290900, 43485500,
        137960900, 88770100, 53399000, 37995000, 51232200, 56674900, 45948800,
        40703600, 25723100, 33342900, 45664700, 48879800, 45346200, 39359100,
        34739800, 21181700, 16032200, 26831700, 37610000, 38496900, 57289300,
        41329600, 47746300, 37760200, 33152400, 31065800, 38404500, 26025200,
        36326900, 31099900, 35443200, 36933500, 46983300, 61810400, 54884700,
        47750100, 94489300, 91734900, 140331900, 108315100, 95668600, 106908900 ]),
    }

series = np.array([ 91.50, 94.81, 94.38, 95.09, 93.78, 94.62, 92.53, 92.75,
     90.31, 92.47, 96.12, 97.25, 98.50, 89.88, 91.00, 92.81, 89.16, 89.34,
     91.62, 89.88, 88.38, 87.62, 84.78, 83.00, 83.50, 81.38, 84.44, 89.25,
     86.38, 86.25, 85.25, 87.12, 85.81, 88.97, 88.47, 86.88, 86.81, 84.88,
     84.19, 83.88, 83.38, 85.50, 89.19, 89.44, 91.09, 90.75, 91.44, 89.00,
     91.00, 90.50, 89.03, 88.81, 84.28, 83.50, 82.69, 84.75, 85.66, 86.19,
     88.94, 89.28, 88.62, 88.50, 91.97, 91.50, 93.25, 93.50, 93.16, 91.72,
     90.00, 89.69, 88.88, 85.19, 83.38, 84.88, 85.94, 97.25, 99.88, 104.94,
     106.00, 102.50, 102.41, 104.59, 106.12, 106.00, 106.06, 104.62, 108.62,
     109.31, 110.50, 112.75, 123.00, 119.62, 118.75, 119.25, 117.94, 116.44,
     115.19, 111.88, 110.59, 118.12, 116.00, 116.00, 112.00, 113.75, 112.94,
     116.00, 120.50, 116.62, 117.00, 115.25, 114.31, 115.50, 115.87, 120.69,
     120.19, 120.75, 124.75, 123.37, 122.94, 122.56, 123.12, 122.56, 124.62,
     129.25, 131.00, 132.25, 131.00, 132.81, 134.00, 137.38, 137.81, 137.88,
     137.25, 136.31, 136.25, 134.63, 128.25, 129.00, 123.87, 124.81, 123.00,
     126.25, 128.38, 125.37, 125.69, 122.25, 119.37, 118.50, 123.19, 123.50,
     122.19, 119.31, 123.31, 121.12, 123.37, 127.37, 128.50, 123.87, 122.94,
     121.75, 124.44, 122.00, 122.37, 122.94, 124.00, 123.19, 124.56, 127.25,
     125.87, 128.86, 132.00, 130.75, 134.75, 135.00, 132.38, 133.31, 131.94,
     130.00, 125.37, 130.13, 127.12, 125.19, 122.00, 125.00, 123.00, 123.50,
     120.06, 121.00, 117.75, 119.87, 122.00, 119.19, 116.37, 113.50, 114.25,
     110.00, 105.06, 107.00, 107.87, 107.00, 107.12, 107.00, 91.00, 93.94,
     93.87, 95.50, 93.00, 94.94, 98.25, 96.75, 94.81, 94.37, 91.56, 90.25,
     93.94, 93.62, 97.00, 95.00, 95.87, 94.06, 94.62, 93.75, 98.00, 103.94,
     107.87, 106.06, 104.50, 105.00, 104.19, 103.06, 103.42, 105.27, 111.87,
     116.00, 116.62, 118.28, 113.37, 109.00, 109.70, 109.25, 107.00, 109.19,
     110.00, 109.20, 110.12, 108.00, 108.62, 109.75, 109.81, 109.00, 108.75,
     107.87 ])

def assert_np_arrays_equal(expected, got):
    for i, value in enumerate(expected):
        if np.isnan(value):
            assert_true(np.isnan(got[i]))
        else:
            assert_equal(value, got[i])

def assert_np_arrays_not_equal(expected, got):
    ''' Verifies expected and got have the same number of leading nan fields,
    followed by different floats.
    '''
    nans = []
    equals = []
    for i, value in enumerate(expected):
        if np.isnan(value):
            assert_true(np.isnan(got[i]))
            nans.append(value)
        else:
            try:
                assert_not_equal(value, got[i])
            except AssertionError:
                equals.append(got[i])
    if len(equals) == len(expected[len(nans):]):
        raise AssertionError('Arrays were equal.')
    elif equals:
        print 'Arrays had %i/%i equivalent values.' % (len(equals), len(expected[len(nans):]))
