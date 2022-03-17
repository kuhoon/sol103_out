import os

# from IPython.display import HTML as html_print
from pyNastran.bdf.bdf import BDF, CaseControlDeck
model = BDF()


E = 72397.0
G = 27000.0
nu = 0.32
rho = 0.0000000000000001
mat = model.add_mat1(1, E, G, nu, rho)


model.add_grid(1, [1299.18, 0.00, 0.00])
model.add_grid(2, [1299.18, 416.47, 0.00])
model.add_grid(3, [1299.18, 832.94, 0.00])
model.add_grid(4, [1299.13, 1191.88, 0.00])
model.add_grid(5, [1299.08, 1550.81, 0.00])
model.add_grid(6, [1299.04, 1909.75, 0.00])
model.add_grid(7, [1298.99, 2268.69, 0.00])
model.add_grid(8, [1298.94, 2627.62, 0.00])
model.add_grid(9, [1298.87, 3117.08, 0.00])
model.add_grid(10, [1283.52, 3459.95, 0.00])
model.add_grid(11, [1268.17, 3802.81, 0.00])
model.add_grid(12, [1252.82, 4145.68, 0.00])
model.add_grid(13, [1237.46, 4488.548, 0.00])
model.add_grid(14, [1222.11, 4831.41, 0.00])
model.add_grid(15, [1206.76, 5174.28, 0.00])
model.add_grid(16, [1191.41, 5517.15, 0.00])
model.add_grid(17, [1176.06, 5860.01, 0.00])
model.add_grid(18, [1160.71, 6202.88, 0.00])
model.add_grid(19, [1145.35, 6545.75, 0.00])
model.add_grid(20, [1130.00, 6888.61, 0.00])
model.add_grid(21, [1114.65, 7231.48, 0.00])
model.add_grid(22, [1099.30, 7574.347, 0.00])
model.add_grid(23, [1083.95, 7917.21, 0.00])
model.add_grid(24, [1068.95, 8252.11, 0.00])
model.add_grid(25, [1053.96, 8587.00, 0.00])
model.add_grid(100, [-234.5, 2627.6, 0.00])
model.add_grid(101, [748.5, 2627.6, 0.00])


model.add_conm2(1, 1, 0.01400159)
model.add_conm2(2, 2, 0.02484664)
model.add_conm2(3, 3, 0.02546982)
model.add_conm2(4, 4, 0.01906899)
model.add_conm2(5, 5, 0.01796483)
model.add_conm2(6, 6, 0.01694792)
model.add_conm2(7, 7, 0.0160897)
model.add_conm2(8, 8, 0.04461853)
model.add_conm2(9, 9, 0.01657169)
model.add_conm2(10, 10, 0.01297902)
model.add_conm2(11, 11, 0.01210256)
model.add_conm2(12, 12, 0.01126236)
model.add_conm2(13, 13, 0.01045264)
model.add_conm2(14, 14, 0.009674809)
model.add_conm2(15, 15, 0.008933798)
model.add_conm2(16, 16, 0.008255062)
model.add_conm2(17, 17, 0.007709694)
model.add_conm2(18, 18, 0.007193918)
model.add_conm2(19, 19, 0.006732572)
model.add_conm2(20, 20, 0.006313959)
model.add_conm2(21, 21, 0.005904836)
model.add_conm2(22, 22, 0.005501775)
model.add_conm2(23, 23, 0.005051136)
model.add_conm2(24, 24, 0.004619121)
model.add_conm2(25, 25, 0.002293105)
model.add_conm2(100, 100, 0.3344)
model.add_conm2(101, 101, 0.1368)


# ctrl+d = 해당 줄 복사, ctrl+/ = 주석처리, shift + d / = 여러줄, ctrl shift alt j = 전체변환


mid = 1
model.add_pbeam(1, mid, [0.0], ['YES'], [12157.813], [331910581.134], [1100289834.703], [0], [609701318.281])
model.add_pbeam(2, mid, [0.0], ['YES'], [10738.436], [292133317.129], [980814110.442], [0], [551800270.525])
model.add_pbeam(3, mid, [0.0], ['YES'], [9486.486], [256666420.008], [870458062.477], [0], [491798910.37])
model.add_pbeam(4, mid, [0.0], ['YES'], [8417.469], [225684368.908], [774617325.51], [0], [437545561.434])
model.add_pbeam(5, mid, [0.0], ['YES'], [7433.996], [197541294.719], [685692114.531], [0], [386832287.536])
model.add_pbeam(6, mid, [0.0], ['YES'], [6556.182], [172905479.58], [604906685.344], [0], [339997895.31])
model.add_pbeam(7, mid, [0.0], ['YES'], [6015.555], [159584565.071], [552319696.44], [0], [310479741.099])
model.add_pbeam(8, mid, [0.0], ['YES'], [5311.215], [138852997.883], [502848069.473], [0], [289387811.644])
model.add_pbeam(9, mid, [0.0], ['YES'], [4495.576], [109520827.96], [428137909.155], [0], [249312309.056])
model.add_pbeam(10, mid, [0.0], ['YES'], [3988.313], [88030296.155], [354443867.032], [0], [201764914.256])
model.add_pbeam(11, mid, [0.0], ['YES'], [3517.323], [69823922.577], [292514855.646], [0], [162737100.172])
model.add_pbeam(12, mid, [0.0], ['YES'], [3072.426], [54488518.815], [239049732.809], [0], [129663523.628])
model.add_pbeam(13, mid, [0.0], ['YES'], [2651.958], [41721704.689], [192719113.392], [0], [101405553.857])
model.add_pbeam(14, mid, [0.0], ['YES'], [2259.093], [31267342.772], [153078238.419], [0], [77619163.804])
model.add_pbeam(15, mid, [0.0], ['YES'], [1906.941], [22915567.125], [121158013.375], [0], [58391418.906])
model.add_pbeam(16, mid, [0.0], ['YES'], [1658.027], [17298826.431], [98600004.307], [0], [45156443.361])
model.add_pbeam(17, mid, [0.0], ['YES'], [1488.02], [13578314.084], [81924788.27], [0], [36162938.141])
model.add_pbeam(18, mid, [0.0], ['YES'], [1350.313], [10657902.697], [68289709.411], [0], [28882784.857])
model.add_pbeam(19, mid, [0.0], ['YES'], [1260.435], [8542308.215], [57794500.388], [0], [23465170.158])
model.add_pbeam(20, mid, [0.0], ['YES'], [1190.88], [6883323.444], [49065659.953], [0], [19175800.061])
model.add_pbeam(21, mid, [0.0], ['YES'], [1121.95], [5474488.548], [41303328.649], [0], [15507330.722])
model.add_pbeam(22, mid, [0.0], ['YES'], [1053.605], [4289548.871], [34439256.93], [0], [12393714.736])
model.add_pbeam(23, mid, [0.0], ['YES'], [986.596], [3313860.021], [28472032.705], [0], [9798457.689])
model.add_pbeam(24, mid, [0.0], ['YES'], [920.852], [2519174.587], [23315700.227], [0], [7654888.444])


model.add_cbeam(1, 1, [1, 2], [], 100)
model.add_cbeam(2, 2, [2, 3], [], 100)
model.add_cbeam(3, 3, [3, 4], [], 100)
model.add_cbeam(4, 4, [4, 5], [], 100)
model.add_cbeam(5, 5, [5, 6], [], 100)
model.add_cbeam(6, 6, [6, 7], [], 100)
model.add_cbeam(7, 7, [7, 8], [], 100)
model.add_cbeam(8, 8, [8, 9], [], 100)
model.add_cbeam(9, 9, [9, 10], [], 100)
model.add_cbeam(10, 10, [10, 11], [], 100)
model.add_cbeam(11, 11, [11, 12], [], 100)
model.add_cbeam(12, 12, [12, 13], [], 100)
model.add_cbeam(13, 13, [13, 14], [], 100)
model.add_cbeam(14, 14, [14, 15], [], 100)
model.add_cbeam(15, 15, [15, 16], [], 100)
model.add_cbeam(16, 16, [16, 17], [], 100)
model.add_cbeam(17, 17, [17, 18], [], 100)
model.add_cbeam(18, 18, [18, 19], [], 100)
model.add_cbeam(19, 19, [19, 20], [], 100)
model.add_cbeam(20, 20, [20, 21], [], 100)
model.add_cbeam(21, 21, [21, 22], [], 100)
model.add_cbeam(22, 22, [22, 23], [], 100)
model.add_cbeam(23, 23, [23, 24], [], 100)
model.add_cbeam(24, 24, [24, 25], [], 100)


spc_id = 50
model.add_spc1(spc_id, '123456', [1])


model.add_rbe2(51, 8, '123456', [100])
model.add_rbe2(52, 8, '123456', [101])


eigrl = model.add_eigrl(10, nd=10)
model.sol = 103  # start=103
cc = CaseControlDeck([
    'SUBCASE 1',
    'SUBTITLE = Default',
    'METHOD = 10',
    'SPC = %s' % spc_id,
    'VECTOR(SORT1,REAL)=ALL',
    'SPCFORCES(SORT1, REAL) = ALL',
    'BEGIN BULK'
])
model.case_control_deck = cc
model.validate()

bdf_filename_out = os.path.join('sol103_OUT.bdf')
model.write_bdf(bdf_filename_out, enddata=True)
print(bdf_filename_out)

print('----------------------------------------------------------------------------------------------------')
