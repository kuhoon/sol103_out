# ctrl+d = 해당 줄 복사, ctrl+/ = 주석처리, shift + d / = 여러줄, ctrl shift alt j = 전체변환

import os

# from IPython.display import HTML as html_print
from pyNastran.bdf.bdf import BDF, CaseControlDeck
model = BDF()

E = 72397.0
G = 27000.0
nu = 0.32
rho = 0.0000000000000001
mat = model.add_mat1(1, E, G, nu, rho)

# open node.dat file_Wing
with open("nodes.dat") as datFile:
    idList1 = [data.split()[0] for data in datFile]
with open("nodes.dat") as datFile:
    xValueList1 = [data.split()[1] for data in datFile]
with open("nodes.dat") as datFile:
    yValueList1 = [data.split()[2] for data in datFile]
with open("nodes.dat") as datFile:
    zValueList1 = [data.split()[3] for data in datFile]

# open mass_conc.dat file_Main Engine, Landing Gear
with open("mass_conc.dat") as datFile:
    idList2 = [data.split()[0] for data in datFile]
with open("mass_conc.dat") as datFile:
    xValueList2 = [data.split()[2] for data in datFile]
with open("mass_conc.dat") as datFile:
    yValueList2 = [data.split()[3] for data in datFile]
with open("mass_conc.dat") as datFile:
    zValueList2 = [data.split()[4] for data in datFile]
with open("mass_conc.dat") as datFile:
    conm2List1 = [data.split()[1] for data in datFile]
with open("mass_conc.dat") as datFile:
    Mlump1 = [data.split()[5] for data in datFile]

# open mass_lump.dat file_Wing
with open("mass_lump.dat") as datFile:
    conm2List2 = [data.split()[0] for data in datFile]
with open("mass_lump.dat") as datFile:
    Mlump2 = [data.split()[2] for data in datFile]

# delete column name
del idList1[0]
del xValueList1[0]
del yValueList1[0]
del zValueList1[0]
del idList2[0]
del xValueList2[0]
del yValueList2[0]
del zValueList2[0]

# delete column name
del conm2List1[0]
del Mlump1[0]
del conm2List2[0]
del Mlump2[0]

# grad list merge
idList = idList1 + idList2
xValueList = xValueList1 + xValueList2
yValueList = yValueList1 + yValueList2
zValueList = zValueList1 + zValueList2

# conm2 list merge
conm2List = conm2List1 + conm2List2
Mlump = Mlump1 + Mlump2

# insert model.add_grid(id_no, x, y, z)
for i, x, y, z in zip(idList, xValueList, yValueList, zValueList):
    model.add_grid(int(i), [float(x), float(y), float(z)])

# insert model.add_grid(id_no, x, y, z)
for j, i, m in zip(conm2List, idList, Mlump):
    model.add_conm2(int(j), int(i), float(m))





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

bdf_filename_out = os.path.join('sol103_OUT2.bdf')
model.write_bdf(bdf_filename_out, enddata=True)
print(bdf_filename_out)

print('----------------------------------------------------------------------------------------------------')
