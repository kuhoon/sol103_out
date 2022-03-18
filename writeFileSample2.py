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

# open elements.dat file_pbeam
with open("elements.dat") as datFile:
    pbeamList = [data.split()[0] for data in datFile]
with open("elements.dat") as datFile:
    areaList = [data.split()[3] for data in datFile]
with open("elements.dat") as datFile:
    i1List = [data.split()[4] for data in datFile]
with open("elements.dat") as datFile:
    i2List = [data.split()[5] for data in datFile]
with open("elements.dat") as datFile:
    jList = [data.split()[7] for data in datFile]
with open("elements.dat") as datFile:
    idFromList = [data.split()[1] for data in datFile]
with open("elements.dat") as datFile:
    idToList = [data.split()[2] for data in datFile]

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

# delete column name
del pbeamList[0]
del areaList[0]
del i1List[0]
del i2List[0]
del jList[0]
del idFromList[0]
del idToList[0]

# grad list merge
idList = idList1 + idList2
xValueList = xValueList1 + xValueList2
yValueList = yValueList1 + yValueList2
zValueList = zValueList1 + zValueList2

# conm2 list merge
conm2List = conm2List2 + conm2List1
Mlump = Mlump2 + Mlump1

# insert model.add_grid(id_no, x, y, z)
for i, x, y, z in zip(idList, xValueList, yValueList, zValueList):
    model.add_grid(int(i), [float(x), float(y), float(z)])

# insert model.add_conm2(id_conm2, id_no, Mlump)
for j, i, m in zip(conm2List, idList, Mlump):
    model.add_conm2(int(j), int(i), float(m))

# insert model.add_pbeam(id_pbeam, mid, x/xb, so, area, i1, i2, i12, j)
for p, a, i1, i2, j in zip(pbeamList, areaList, i1List, i2List, jList):
    model.add_pbeam(int(p), 1, [0.0], ['YES'], [float(a)], [float(i1)], [float(i2)], [0], [float(j)])

# insert model.add_cbeam
for p, idFrom, idTo in zip(pbeamList, idFromList, idToList):
    model.add_cbeam(int(p), int(p), [int(idFrom), int(idTo)], [], 100)

spc_id = 50
model.add_spc1(spc_id, '123456', [1])


model.add_rbe2(51, 8, '123456', [100])
model.add_rbe2(52, 8, '123456', [101])


eigrl = model.add_eigrl(10, nd=10) # how many want to mode
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
