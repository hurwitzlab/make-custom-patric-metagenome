# IPython log file

get_ipython().magic(u'logstate')
get_ipython().magic(u'logstate -o')
get_ipython().magic(u'logstop')
get_ipython().magic(u'ls ')
import os
file_in = open(args["file"],"r")
file_in = open("just-genome-and-accn.txt","r")
strain_to_accn={}
for line in file_in:
        line=line.rstrip('\n')
        cols=line.split(' ')
        accn=cols[0]
        strain=cols[1]
        strain_to_accn.update({strain:accn})
    
len(strain)
#[Out]# 6
len(strain_to_accn)
#[Out]# 15262
keys(strain_to_accn)
strain_to_accn.keys
#[Out]# <function keys>
strain_to_accn.keys()
#[Out]# ['717606.6',
#[Out]#  '1313.2378',
#[Out]#  '1203195.3',
#[Out]#  '756067.3',
#[Out]#  '403957.5',
#[Out]#  '1151323.4',
#[Out]#  '1639.166',
#[Out]#  '365046.3',
#[Out]#  '1229172.3',
#[Out]#  '1413430.3',
#[Out]#  '754774.3',
#[Out]#  '82654.3',
#[Out]#  '309807.25',
#[Out]#  '1262654.4',
#[Out]#  '1121101.3',
#[Out]#  '382638.14',
#[Out]#  '1208600.3',
#[Out]#  '1276220.3',
#[Out]#  '1182684.3',
#[Out]#  '243277.26',
#[Out]#  '1229204.3',
#[Out]#  '1111073.3',
#[Out]#  '1438708.3',
#[Out]#  '927655.4',
#[Out]#  '993047.3',
#[Out]#  '401472.3',
#[Out]#  '86106.3',
#[Out]#  '1515334.3',
#[Out]#  '868200.3',
#[Out]#  '998674.3',
#[Out]#  '889224.3',
#[Out]#  '1236952.3',
#[Out]#  '1168588.3',
#[Out]#  '1308978.3',
#[Out]#  '1049922.3',
#[Out]#  '191610.3',
#[Out]#  '596322.3',
#[Out]#  '1331256.3',
#[Out]#  '652.4',
#[Out]#  '1420917.4',
#[Out]#  '313589.5',
#[Out]#  '596153.4',
#[Out]#  '1470558.3',
#[Out]#  '1324967.4',
#[Out]#  '1123060.3',
#[Out]#  '1197174.4',
#[Out]#  '48291.4',
#[Out]#  '1283291.3',
#[Out]#  '1088544.3',
#[Out]#  '935845.3',
#[Out]#  '1463850.3',
#[Out]#  '1115632.3',
#[Out]#  '1410660.3',
#[Out]#  '1085623.3',
#[Out]#  '1047006.3',
#[Out]#  '76759.12',
#[Out]#  '469590.5',
#[Out]#  '1005043.3',
#[Out]#  '526997.3',
#[Out]#  '1294142.3',
#[Out]#  '1214121.5',
#[Out]#  '1248916.3',
#[Out]#  '1170562.3',
#[Out]#  '398261.3',
#[Out]#  '1266996.3',
#[Out]#  '1079455.4',
#[Out]#  '1074071.4',
#[Out]#  '1120950.3',
#[Out]#  '1279017.3',
#[Out]#  '1281273.3',
#[Out]#  '536231.5',
#[Out]#  '1408461.3',
#[Out]#  '1331262.3',
#[Out]#  '172088.3',
#[Out]#  '1188239.3',
#[Out]#  '436308.17',
#[Out]#  '888812.3',
#[Out]#  '1226335.3',
#[Out]#  '1130348.3',
#[Out]#  '1294266.3',
#[Out]#  '1196095.8',
#[Out]#  '1402806.3',
#[Out]#  '1444306.3',
#[Out]#  '1471481.3',
#[Out]#  '889487.3',
#[Out]#  '765869.4',
#[Out]#  '1392491.3',
#[Out]#  '1151193.3',
#[Out]#  '1461752.3',
#[Out]#  '123214.3',
#[Out]#  '1139219.4',
#[Out]#  '1220574.3',
#[Out]#  '1131272.3',
#[Out]#  '880633.7',
#[Out]#  '526987.3',
#[Out]#  '1541197.3',
#[Out]#  '85963.7',
#[Out]#  '351016.3',
#[Out]#  '335659.3',
#[Out]#  '309803.4',
#[Out]#  '1196421.3',
#[Out]#  '1311078.3',
#[Out]#  '1238220.3',
#[Out]#  '1095659.3',
#[Out]#  '1292021.4',
#[Out]#  '411471.5',
#[Out]#  '1122981.3',
#[Out]#  '1437612.3',
#[Out]#  '1345561.3',
#[Out]#  '879090.3',
#[Out]#  '1281263.3',
#[Out]#  '1260356.4',
#[Out]#  '33033.4',
#[Out]#  '153496.7',
#[Out]#  '1048808.3',
#[Out]#  '1338034.3',
#[Out]#  '1158604.4',
#[Out]#  '1402491.3',
#[Out]#  '665946.3',
#[Out]#  '1309807.3',
#[Out]#  '1094965.3',
#[Out]#  '1390077.3',
#[Out]#  '935705.3',
#[Out]#  '1204719.3',
#[Out]#  '1496690.4',
#[Out]#  '907491.3',
#[Out]#  '1203546.5',
#[Out]#  '1413410.3',
#[Out]#  '1240687.3',
#[Out]#  '565636.4',
#[Out]#  '195522.4',
#[Out]#  '1256203.3',
#[Out]#  '210.1338',
#[Out]#  '1204475.3',
#[Out]#  '756828.3',
#[Out]#  '1307438.3',
#[Out]#  '1428433.3',
#[Out]#  '888059.3',
#[Out]#  '1410830.3',
#[Out]#  '1313.4516',
#[Out]#  '333990.5',
#[Out]#  '1313.4512',
#[Out]#  '1185697.3',
#[Out]#  '1313291.3',
#[Out]#  '1208583.4',
#[Out]#  '1227461.3',
#[Out]#  '1276756.3',
#[Out]#  '749531.3',
#[Out]#  '1313.2968',
#[Out]#  '572478.10',
#[Out]#  '1428454.3',
#[Out]#  '1408449.4',
#[Out]#  '1471497.3',
#[Out]#  '1235441.3',
#[Out]#  '1294272.3',
#[Out]#  '1116032.3',
#[Out]#  '314266.4',
#[Out]#  '1161424.3',
#[Out]#  '1173023.4',
#[Out]#  '1281080.3',
#[Out]#  '1041826.3',
#[Out]#  '766761.3',
#[Out]#  '714083.8',
#[Out]#  '525271.4',
#[Out]#  '1136425.3',
#[Out]#  '1172179.3',
#[Out]#  '1235473.3',
#[Out]#  '1244142.4',
#[Out]#  '1399775.3',
#[Out]#  '1280694.3',
#[Out]#  '1157395.3',
#[Out]#  '861530.3',
#[Out]#  '399795.3',
#[Out]#  '1289387.3',
#[Out]#  '935848.3',
#[Out]#  '1188243.3',
#[Out]#  '1160286.3',
#[Out]#  '992059.3',
#[Out]#  '106370.16',
#[Out]#  '1261070.4',
#[Out]#  '1444057.3',
#[Out]#  '75379.4',
#[Out]#  '1203576.3',
#[Out]#  '391619.3',
#[Out]#  '1227483.3',
#[Out]#  '1524460.3',
#[Out]#  '1079986.3',
#[Out]#  '1287061.3',
#[Out]#  '561879.3',
#[Out]#  '1123070.3',
#[Out]#  '132474.8',
#[Out]#  '1040986.3',
#[Out]#  '751944.3',
#[Out]#  '451755.5',
#[Out]#  '1718.20',
#[Out]#  '1399796.3',
#[Out]#  '1074132.3',
#[Out]#  '132474.4',
#[Out]#  '132474.6',
#[Out]#  '374931.10',
#[Out]#  '1227493.4',
#[Out]#  '95614.3',
#[Out]#  '1495067.3',
#[Out]#  '1137258.3',
#[Out]#  '1112211.3',
#[Out]#  '1125971.3',
#[Out]#  '1105260.3',
#[Out]#  '1236501.3',
#[Out]#  '1232452.3',
#[Out]#  '273677.3',
#[Out]#  '2754.13',
#[Out]#  '1244096.3',
#[Out]#  '1181740.3',
#[Out]#  '1151419.3',
#[Out]#  '699263.3',
#[Out]#  '1147132.5',
#[Out]#  '1288494.3',
#[Out]#  '522492.3',
#[Out]#  '1236533.3',
#[Out]#  '1193095.6',
#[Out]#  '375286.7',
#[Out]#  '1116079.3',
#[Out]#  '1027374.10',
#[Out]#  '245012.3',
#[Out]#  '1309806.3',
#[Out]#  '111105.13',
#[Out]#  '111105.12',
#[Out]#  '111105.11',
#[Out]#  '111105.17',
#[Out]#  '1236490.3',
#[Out]#  '1126934.3',
#[Out]#  '111105.14',
#[Out]#  '1126893.3',
#[Out]#  '938457.3',
#[Out]#  '526989.3',
#[Out]#  '398767.5',
#[Out]#  '1313.2588',
#[Out]#  '1463888.3',
#[Out]#  '935563.3',
#[Out]#  '520999.6',
#[Out]#  '1121002.4',
#[Out]#  '1462527.3',
#[Out]#  '1134806.3',
#[Out]#  '1382367.3',
#[Out]#  '1121092.3',
#[Out]#  '1221293.3',
#[Out]#  '1232436.3',
#[Out]#  '1331240.3',
#[Out]#  '864570.3',
#[Out]#  '573066.3',
#[Out]#  '1117108.3',
#[Out]#  '999548.6',
#[Out]#  '1449088.3',
#[Out]#  '1234672.3',
#[Out]#  '1123347.4',
#[Out]#  '340102.8',
#[Out]#  '1229518.3',
#[Out]#  '1223498.3',
#[Out]#  '1127695.3',
#[Out]#  '1041156.3',
#[Out]#  '1122929.3',
#[Out]#  '868193.3',
#[Out]#  '1052848.3',
#[Out]#  '236097.3',
#[Out]#  '1304.156',
#[Out]#  '1202537.3',
#[Out]#  '349741.6',
#[Out]#  '749537.3',
#[Out]#  '555311.11',
#[Out]#  '1160719.4',
#[Out]#  '886877.3',
#[Out]#  '1035188.3',
#[Out]#  '1339306.3',
#[Out]#  '1258582.4',
#[Out]#  '1286279.3',
#[Out]#  '397287.3',
#[Out]#  '517418.5',
#[Out]#  '1439224.3',
#[Out]#  '1001592.3',
#[Out]#  '996854.3',
#[Out]#  '1451264.3',
#[Out]#  '107637.3',
#[Out]#  '1383064.3',
#[Out]#  '1446623.3',
#[Out]#  '651822.3',
#[Out]#  '913071.3',
#[Out]#  '227882.28',
#[Out]#  '596317.3',
#[Out]#  '1074889.3',
#[Out]#  '981540.3',
#[Out]#  '1344012.3',
#[Out]#  '1412591.3',
#[Out]#  '1385511.3',
#[Out]#  '1122158.3',
#[Out]#  '1283300.3',
#[Out]#  '1053223.3',
#[Out]#  '28447.4',
#[Out]#  '1237085.11',
#[Out]#  '935261.3',
#[Out]#  '667121.5',
#[Out]#  '1339341.3',
#[Out]#  '1357282.3',
#[Out]#  '1446660.3',
#[Out]#  '1439317.3',
#[Out]#  '476211.11',
#[Out]#  '1158172.3',
#[Out]#  '1210453.3',
#[Out]#  '1522072.3',
#[Out]#  '555088.4',
#[Out]#  '178901.10',
#[Out]#  '762966.3',
#[Out]#  '1307759.4',
#[Out]#  '1242864.3',
#[Out]#  '698964.3',
#[Out]#  '1446716.3',
#[Out]#  '1400797.3',
#[Out]#  '1144328.3',
#[Out]#  '86416.3',
#[Out]#  '1329909.3',
#[Out]#  '1116048.3',
#[Out]#  '1037908.3',
#[Out]#  '553175.3',
#[Out]#  '991983.4',
#[Out]#  '34073.10',
#[Out]#  '1158668.3',
#[Out]#  '983544.3',
#[Out]#  '1175313.3',
#[Out]#  '1471507.3',
#[Out]#  '935547.3',
#[Out]#  '1391468.3',
#[Out]#  '866790.3',
#[Out]#  '930.4',
#[Out]#  '434928.8',
#[Out]#  '1121126.5',
#[Out]#  '1121126.4',
#[Out]#  '40324.43',
#[Out]#  '1052829.3',
#[Out]#  '1121929.3',
#[Out]#  '1144316.3',
#[Out]#  '71421.8',
#[Out]#  '595.11',
#[Out]#  '1133596.3',
#[Out]#  '1427204.3',
#[Out]#  '556287.5',
#[Out]#  '1272954.3',
#[Out]#  '575606.3',
#[Out]#  '883163.3',
#[Out]#  '749525.3',
#[Out]#  '904294.3',
#[Out]#  '1137739.4',
#[Out]#  '1313.2709',
#[Out]#  '1329845.3',
#[Out]#  '1182685.3',
#[Out]#  '1095739.3',
#[Out]#  '1336205.3',
#[Out]#  '1005522.3',
#[Out]#  '1298608.3',
#[Out]#  '1384067.3',
#[Out]#  '562.2305',
#[Out]#  '909421.4',
#[Out]#  '1056816.3',
#[Out]#  '1384049.3',
#[Out]#  '1530186.3',
#[Out]#  '670.150',
#[Out]#  '1443104.3',
#[Out]#  '670.152',
#[Out]#  '317655.17',
#[Out]#  '1359.20',
#[Out]#  '1028806.3',
#[Out]#  '1049929.3',
#[Out]#  '670.159',
#[Out]#  '1451265.3',
#[Out]#  '293387.8',
#[Out]#  '1182699.3',
#[Out]#  '1453289.3',
#[Out]#  '562.2302',
#[Out]#  '657308.3',
#[Out]#  '428994.3',
#[Out]#  '1313.3970',
#[Out]#  '1121102.3',
#[Out]#  '1580.51',
#[Out]#  '1580.52',
#[Out]#  '1391496.3',
#[Out]#  '445336.4',
#[Out]#  '1414836.3',
#[Out]#  '1122170.4',
#[Out]#  '1138383.4',
#[Out]#  '1331216.3',
#[Out]#  '1408360.3',
#[Out]#  '537012.5',
#[Out]#  '1047073.3',
#[Out]#  '218493.5',
#[Out]#  '515621.3',
#[Out]#  '1302633.3',
#[Out]#  '1331660.3',
#[Out]#  '1214154.3',
#[Out]#  '189382.4',
#[Out]#  '387344.15',
#[Out]#  '1162282.3',
#[Out]#  '562.5414',
#[Out]#  '882083.3',
#[Out]#  '546262.4',
#[Out]#  '1002672.3',
#[Out]#  '1130300.3',
#[Out]#  '1341695.3',
#[Out]#  '754027.3',
#[Out]#  '563032.4',
#[Out]#  '111780.3',
#[Out]#  '562.5410',
#[Out]#  '1329377.3',
#[Out]#  '632.126',
#[Out]#  '1297799.3',
#[Out]#  '562.5278',
#[Out]#  '1215065.3',
#[Out]#  '1156935.5',
#[Out]#  '331109.4',
#[Out]#  '1095674.3',
#[Out]#  '1217715.3',
#[Out]#  '287.893',
#[Out]#  '1234368.3',
#[Out]#  '287.891',
#[Out]#  '287.890',
#[Out]#  '1367492.3',
#[Out]#  '1095729.3',
#[Out]#  '1104568.3',
#[Out]#  '1123497.3',
#[Out]#  '1448802.3',
#[Out]#  '1219064.3',
#[Out]#  '1151334.4',
#[Out]#  '584657.3',
#[Out]#  '497321.3',
#[Out]#  '1488.5',
#[Out]#  '1217709.3',
#[Out]#  '273075.10',
#[Out]#  '1005995.3',
#[Out]#  '888801.3',
#[Out]#  '246197.24',
#[Out]#  '1432547.3',
#[Out]#  '1112258.4',
#[Out]#  '33934.3',
#[Out]#  '1412478.3',
#[Out]#  '991791.3',
#[Out]#  '665571.4',
#[Out]#  '1169248.3',
#[Out]#  '498848.5',
#[Out]#  '1339228.3',
#[Out]#  '305.46',
#[Out]#  '1235440.3',
#[Out]#  '935549.4',
#[Out]#  '1386089.3',
#[Out]#  '1245601.3',
#[Out]#  '1561217.3',
#[Out]#  '548477.4',
#[Out]#  '1439319.3',
#[Out]#  '1448717.3',
#[Out]#  '761193.3',
#[Out]#  '1438748.3',
#[Out]#  '1131935.3',
#[Out]#  '868170.3',
#[Out]#  '1449069.3',
#[Out]#  '1317122.7',
#[Out]#  '1123075.3',
#[Out]#  '1313.3512',
#[Out]#  '937450.3',
#[Out]#  '1274985.3',
#[Out]#  '562.5361',
#[Out]#  '1137265.3',
#[Out]#  '1313.2179',
#[Out]#  '889220.3',
#[Out]#  '374927.4',
#[Out]#  '1104580.4',
#[Out]#  '1463875.3',
#[Out]#  '1402966.3',
#[Out]#  '1232673.3',
#[Out]#  '132474.20',
#[Out]#  '132474.21',
#[Out]#  '1306162.3',
#[Out]#  '1392.87',
#[Out]#  '1304865.3',
#[Out]#  '797114.5',
#[Out]#  '1499967.3',
#[Out]#  '1310734.3',
#[Out]#  '1444242.3',
#[Out]#  '1342299.3',
#[Out]#  '1278971.3',
#[Out]#  '1347368.3',
#[Out]#  '1410664.3',
#[Out]#  '1121922.3',
#[Out]#  '644968.4',
#[Out]#  '1050617.5',
#[Out]#  '1354301.3',
#[Out]#  '940285.3',
#[Out]#  '1078505.3',
#[Out]#  '718220.3',
#[Out]#  '662480.6',
#[Out]#  '1202768.4',
#[Out]#  '1049912.3',
#[Out]#  '1111454.3',
#[Out]#  '1408416.3',
#[Out]#  '1338009.3',
#[Out]#  '1217628.3',
#[Out]#  '1203190.3',
#[Out]#  '1313.2394',
#[Out]#  '1187956.3',
#[Out]#  '1280001.3',
#[Out]#  '872326.3',
#[Out]#  '1159076.3',
#[Out]#  '1345524.3',
#[Out]#  '549.16',
#[Out]#  '1256204.3',
#[Out]#  '1158552.3',
#[Out]#  '1005410.3',
#[Out]#  '651.3',
#[Out]#  '1531961.3',
#[Out]#  '763034.3',
#[Out]#  '1338015.4',
#[Out]#  '1408428.3',
#[Out]#  '1229780.4',
#[Out]#  '1260361.4',
#[Out]#  '171693.3',
#[Out]#  '1046625.3',
#[Out]#  '1076588.3',
#[Out]#  '862964.3',
#[Out]#  '1033806.13',
#[Out]#  '67256.3',
#[Out]#  '50743.3',
#[Out]#  '495036.3',
#[Out]#  '533240.4',
#[Out]#  '1306409.3',
#[Out]#  '1294271.3',
#[Out]#  '910040.3',
#[Out]#  '1094558.3',
#[Out]#  '1121938.3',
#[Out]#  '572546.12',
#[Out]#  '1104566.3',
#[Out]#  '471821.5',
#[Out]#  '1455608.3',
#[Out]#  '1120919.3',
#[Out]#  '1437602.3',
#[Out]#  '233412.5',
#[Out]#  '1408420.3',
#[Out]#  '1046598.4',
#[Out]#  '1418243.3',
#[Out]#  '1410767.3',
#[Out]#  '311458.9',
#[Out]#  '1138919.3',
#[Out]#  '1453495.3',
#[Out]#  '1393718.3',
#[Out]#  '139.70',
#[Out]#  '1397527.3',
#[Out]#  '658612.3',
#[Out]#  '1201037.3',
#[Out]#  '1280953.3',
#[Out]#  '1310114.3',
#[Out]#  '269798.16',
#[Out]#  '1123294.3',
#[Out]#  '1400155.3',
#[Out]#  '1265510.3',
#[Out]#  '1132496.5',
#[Out]#  '1165940.3',
#[Out]#  '1076524.3',
#[Out]#  '1122613.3',
#[Out]#  '1313298.4',
#[Out]#  '1107311.3',
#[Out]#  '1227358.4',
#[Out]#  '1074054.3',
#[Out]#  '1326980.6',
#[Out]#  '990271.3',
#[Out]#  '352165.3',
#[Out]#  '447456.3',
#[Out]#  '1384065.3',
#[Out]#  '768726.4',
#[Out]#  '1212766.3',
#[Out]#  '1224163.3',
#[Out]#  '742727.4',
#[Out]#  '316.77',
#[Out]#  '243261.3',
#[Out]#  '1169246.3',
#[Out]#  '1232451.3',
#[Out]#  '136273.5',
#[Out]#  '1410653.3',
#[Out]#  '550685.3',
#[Out]#  '1451188.3',
#[Out]#  '760856.3',
#[Out]#  '96765.3',
#[Out]#  '1391912.3',
#[Out]#  '1355022.5',
#[Out]#  '1054217.5',
#[Out]#  '1248724.3',
#[Out]#  '1122603.3',
#[Out]#  '1400149.3',
#[Out]#  '708248.3',
#[Out]#  '1117409.3',
#[Out]#  '1298894.3',
#[Out]#  '1235793.3',
#[Out]#  '525283.3',
#[Out]#  '1123368.4',
#[Out]#  '314277.4',
#[Out]#  '1151308.3',
#[Out]#  '626095.4',
#[Out]#  '868164.3',
#[Out]#  '1117317.3',
#[Out]#  '1145171.3',
#[Out]#  '443143.4',
#[Out]#  '360094.4',
#[Out]#  '1406866.3',
#[Out]#  '411486.3',
#[Out]#  '1225203.3',
#[Out]#  '754089.3',
#[Out]#  '749510.3',
#[Out]#  '67287.3',
#[Out]#  '243275.7',
#[Out]#  '387662.10',
#[Out]#  '1471521.3',
#[Out]#  '1517681.3',
#[Out]#  '1443897.3',
#[Out]#  '1158183.3',
#[Out]#  '1116178.3',
#[Out]#  '1423688.3',
#[Out]#  '1156986.4',
#[Out]#  '390874.12',
#[Out]#  '1151261.4',
#[Out]#  '927703.3',
#[Out]#  '1324269.3',
#[Out]#  '1380408.3',
#[Out]#  '1444166.3',
#[Out]#  '1214206.3',
#[Out]#  '1302425.3',
#[Out]#  '1504981.3',
#[Out]#  '1408457.3',
#[Out]#  '1347393.3',
#[Out]#  '868190.3',
#[Out]#  '1047059.3',
#[Out]#  '670.80',
#[Out]#  '247639.3',
#[Out]#  '287.1248',
#[Out]#  '1236548.3',
#[Out]#  '1214222.3',
#[Out]#  '1116232.3',
#[Out]#  '562.5066',
#[Out]#  '1463908.3',
#[Out]#  '1284393.3',
#[Out]#  '1343071.3',
#[Out]#  '1005552.4',
#[Out]#  '1073366.3',
#[Out]#  '1314958.3',
#[Out]#  '714315.3',
#[Out]#  '1365661.3',
#[Out]#  '1138925.3',
#[Out]#  '1121100.7',
#[Out]#  '1409678.3',
#[Out]#  '1579316.3',
#[Out]#  '457429.3',
#[Out]#  '1471492.3',
#[Out]#  '1311574.3',
#[Out]#  '629262.5',
#[Out]#  '1485007.3',
#[Out]#  '1181777.3',
#[Out]#  '1203553.3',
#[Out]#  '1298864.3',
#[Out]#  '1281064.3',
#[Out]#  '1151368.4',
#[Out]#  '929563.3',
#[Out]#  '765910.4',
#[Out]#  '407976.7',
#[Out]#  '1111735.3',
#[Out]#  '687914.3',
#[Out]#  '614083.3',
#[Out]#  '1121862.3',
#[Out]#  '1357289.4',
#[Out]#  '1071073.3',
#[Out]#  '1503925.3',
#[Out]#  '1123274.3',
#[Out]#  '871963.5',
#[Out]#  '686660.3',
#[Out]#  '1131290.3',
#[Out]#  '1391994.3',
#[Out]#  '1396.147',
#[Out]#  '1340435.4',
#[Out]#  '1400520.3',
#[Out]#  '1396.141',
#[Out]#  '46429.4',
#[Out]#  '1312921.3',
#[Out]#  '1347420.3',
#[Out]#  '405566.6',
#[Out]#  '1396.149',
#[Out]#  '867904.9',
#[Out]#  '1444052.3',
#[Out]#  '545534.3',
#[Out]#  '857109.4',
#[Out]#  '1151061.3',
#[Out]#  '765698.3',
#[Out]#  '1031288.3',
#[Out]#  '1214177.3',
#[Out]#  '1384040.4',
#[Out]#  '1265738.3',
#[Out]#  '1266738.3',
#[Out]#  '1450515.3',
#[Out]#  '1444131.3',
#[Out]#  '1308956.3',
#[Out]#  '1211112.3',
#[Out]#  '1380387.3',
#[Out]#  '1399144.3',
#[Out]#  '1281129.3',
#[Out]#  '1236528.3',
#[Out]#  '1134837.3',
#[Out]#  '376619.10',
#[Out]#  '1263868.3',
#[Out]#  '908341.3',
#[Out]#  '907263.3',
#[Out]#  '914129.3',
#[Out]#  '340189.4',
#[Out]#  '996805.3',
#[Out]#  '656519.3',
#[Out]#  '1217659.3',
#[Out]#  '1206737.4',
#[Out]#  '478005.5',
#[Out]#  '269797.17',
#[Out]#  '657323.3',
#[Out]#  '412965.8',
#[Out]#  '446468.6',
#[Out]#  '670.47',
#[Out]#  '981383.3',
#[Out]#  '903915.3',
#[Out]#  '1266914.3',
#[Out]#  '1157459.3',
#[Out]#  '1408250.3',
#[Out]#  '529122.4',
#[Out]#  '1380355.4',
#[Out]#  '1405.9',
#[Out]#  '1397698.3',
#[Out]#  '38312.3',
#[Out]#  '857143.3',
#[Out]#  '857115.3',
#[Out]#  '1221522.3',
#[Out]#  '1151344.4',
#[Out]#  '1125723.3',
#[Out]#  '550540.3',
#[Out]#  '1402545.3',
#[Out]#  '1422717.3',
#[Out]#  '321846.3',
#[Out]#  '992000.3',
#[Out]#  '1151120.3',
#[Out]#  '287.958',
#[Out]#  '716928.3',
#[Out]#  '888807.3',
#[Out]#  '1265647.3',
#[Out]#  '1388750.3',
#[Out]#  '1053181.3',
#[Out]#  '1214152.3',
#[Out]#  '948563.3',
#[Out]#  '1206745.3',
#[Out]#  '574750.3',
#[Out]#  '1053177.3',
#[Out]#  '1473546.3',
#[Out]#  '139.69',
#[Out]#  '1506995.3',
#[Out]#  '1409765.3',
#[Out]#  '882800.3',
#[Out]#  '1144333.3',
#[Out]#  '1194708.3',
#[Out]#  '1161415.3',
#[Out]#  '1156841.3',
#[Out]#  '680649.3',
#[Out]#  '622637.3',
#[Out]#  '1355374.3',
#[Out]#  '1357292.3',
#[Out]#  '891398.4',
#[Out]#  '1334627.3',
#[Out]#  '906888.9',
#[Out]#  '906888.8',
#[Out]#  '882084.3',
#[Out]#  '906888.7',
#[Out]#  '906888.6',
#[Out]#  '906888.5',
#[Out]#  '1445607.3',
#[Out]#  '670.148',
#[Out]#  '1154792.3',
#[Out]#  '1385856.3',
#[Out]#  '1089443.3',
#[Out]#  '889214.3',
#[Out]#  '1095694.3',
#[Out]#  '1333564.3',
#[Out]#  '1390360.3',
#[Out]#  '904778.3',
#[Out]#  '575611.3',
#[Out]#  '883156.3',
#[Out]#  '469608.3',
#[Out]#  '35802.52',
#[Out]#  '167879.5',
#[Out]#  '82374.4',
#[Out]#  '1339326.3',
#[Out]#  '272134.4',
#[Out]#  '1446585.3',
#[Out]#  '1299326.3',
#[Out]#  '1333511.3',
#[Out]#  '1177179.3',
#[Out]#  '548470.3',
#[Out]#  '1124992.3',
#[Out]#  '1433287.3',
#[Out]#  '596312.3',
#[Out]#  '1154807.3',
#[Out]#  '1236483.3',
#[Out]#  '585502.3',
#[Out]#  '1275974.3',
#[Out]#  '1147787.3',
#[Out]#  '1288293.3',
#[Out]#  '993517.3',
#[Out]#  '1120952.3',
#[Out]#  '563194.3',
#[Out]#  '1536771.3',
#[Out]#  '1138892.3',
#[Out]#  '1313.3688',
#[Out]#  '311424.5',
#[Out]#  '1136138.3',
#[Out]#  '330214.5',
#[Out]#  '1233950.5',
#[Out]#  '1046966.3',
#[Out]#  '470.623',
#[Out]#  '470.628',
#[Out]#  '1313.3668',
#[Out]#  '1009418.3',
#[Out]#  '1281191.3',
#[Out]#  '1434156.3',
#[Out]#  '1408271.3',
#[Out]#  '1511133.3',
#[Out]#  '1310602.3',
#[Out]#  '565034.3',
#[Out]#  '419610.10',
#[Out]#  '1539066.3',
#[Out]#  '657314.3',
#[Out]#  '631454.5',
#[Out]#  '1134799.3',
#[Out]#  '1158536.3',
#[Out]#  '1365007.3',
#[Out]#  '1219581.3',
#[Out]#  '97137.3',
#[Out]#  '1402213.3',
#[Out]#  '1310779.3',
#[Out]#  '1213457.3',
#[Out]#  '1217672.3',
#[Out]#  '1208922.3',
#[Out]#  '1587524.6',
#[Out]#  '1550401.3',
#[Out]#  '1215086.3',
#[Out]#  '1313.3664',
#[Out]#  '1212545.3',
#[Out]#  '1448856.3',
#[Out]#  '487796.3',
#[Out]#  '1158167.3',
#[Out]#  '1238444.3',
#[Out]#  '1280698.3',
#[Out]#  '553571.3',
#[Out]#  '1205681.4',
#[Out]#  '1005430.3',
#[Out]#  '883166.5',
#[Out]#  '1444182.3',
#[Out]#  '562.5486',
#[Out]#  '471852.6',
#[Out]#  '453363.4',
#[Out]#  '1350366.3',
#[Out]#  '1433291.3',
#[Out]#  '999422.3',
#[Out]#  '1310700.3',
#[Out]#  '1217660.3',
#[Out]#  '984233.3',
#[Out]#  '500153.3',
#[Out]#  '1211777.3',
#[Out]#  '1304877.3',
#[Out]#  '59196.3',
#[Out]#  '1211847.5',
#[Out]#  '670.178',
#[Out]#  '1094489.3',
#[Out]#  '1122128.3',
#[Out]#  '1000939.3',
#[Out]#  '670.173',
#[Out]#  '670.174',
#[Out]#  '670.175',
#[Out]#  '1313.3952',
#[Out]#  '1232392.6',
#[Out]#  '1391478.3',
#[Out]#  '1435356.3',
#[Out]#  '985008.3',
#[Out]#  '1006004.4',
#[Out]#  '882856.4',
#[Out]#  '1256198.3',
#[Out]#  '562.5475',
#[Out]#  '562.5474',
#[Out]#  '1418441.3',
#[Out]#  '562.5478',
#[Out]#  '1218598.3',
#[Out]#  '1499107.3',
#[Out]#  '1217668.3',
#[Out]#  '371196.3',
#[Out]#  '883158.3',
#[Out]#  '290633.11',
#[Out]#  '992088.3',
#[Out]#  '1157430.3',
#[Out]#  '63737.11',
#[Out]#  '1416753.3',
#[Out]#  '548.34',
#[Out]#  '1123021.3',
#[Out]#  '1400138.3',
#[Out]#  '644076.3',
#[Out]#  '1463834.3',
#[Out]#  '1413540.3',
#[Out]#  '158189.3',
#[Out]#  '384.6',
#[Out]#  '1224144.3',
#[Out]#  '1210907.3',
#[Out]#  '1123013.3',
#[Out]#  '563037.3',
#[Out]#  '1281116.3',
#[Out]#  '562.5216',
#[Out]#  '760795.3',
#[Out]#  '562.5213',
#[Out]#  '562.5212',
#[Out]#  '562.5211',
#[Out]#  '1279009.4',
#[Out]#  '1159057.3',
#[Out]#  '1463851.3',
#[Out]#  '910049.3',
#[Out]#  '1112204.3',
#[Out]#  '1403347.3',
#[Out]#  '1450449.3',
#[Out]#  '562.5218',
#[Out]#  '1471445.3',
#[Out]#  '1281779.3',
#[Out]#  '287.1089',
#[Out]#  '1223566.3',
#[Out]#  '287.1082',
#[Out]#  '784613.4',
#[Out]#  '550682.3',
#[Out]#  '1281196.3',
#[Out]#  '929556.3',
#[Out]#  '1049937.3',
#[Out]#  '692420.6',
#[Out]#  '553973.6',
#[Out]#  '1194706.3',
#[Out]#  '1327991.3',
#[Out]#  '1310938.3',
#[Out]#  '1072571.3',
#[Out]#  '709797.3',
#[Out]#  '1357270.3',
#[Out]#  '287.439',
#[Out]#  '1221996.3',
#[Out]#  '1519439.3',
#[Out]#  '1127744.3',
#[Out]#  '1104614.3',
#[Out]#  '648996.5',
#[Out]#  '1169245.3',
#[Out]#  '888743.3',
#[Out]#  '394503.7',
#[Out]#  '95616.4',
#[Out]#  '1444085.3',
#[Out]#  '1169279.3',
#[Out]#  '1049978.3',
#[Out]#  '315405.3',
#[Out]#  '54388.6',
#[Out]#  '1444198.3',
#[Out]#  '1284702.4',
#[Out]#  '1281120.3',
#[Out]#  '1458466.5',
#[Out]#  '1408471.3',
#[Out]#  '1291000.3',
#[Out]#  '1471451.3',
#[Out]#  '1121030.3',
#[Out]#  '1116230.3',
#[Out]#  '590062.3',
#[Out]#  '451707.4',
#[Out]#  '1313.3577',
#[Out]#  '1328375.3',
#[Out]#  '511051.3',
#[Out]#  '997886.3',
#[Out]#  '1150612.3',
#[Out]#  '451640.5',
#[Out]#  '915059.3',
#[Out]#  '1120934.3',
#[Out]#  '1313.2628',
#[Out]#  '1121278.3',
#[Out]#  '1406859.3',
#[Out]#  '1392.69',
#[Out]#  '1457250.4',
#[Out]#  '913338.3',
#[Out]#  '1531429.3',
#[Out]#  '1004951.3',
#[Out]#  '697282.3',
#[Out]#  '1181724.3',
#[Out]#  '1415162.4',
#[Out]#  '1145118.3',
#[Out]#  '1157679.3',
#[Out]#  '1479651.3',
#[Out]#  '981212.3',
#[Out]#  '1302650.3',
#[Out]#  '1528098.3',
#[Out]#  '1134413.3',
#[Out]#  '1128180.3',
#[Out]#  '340177.11',
#[Out]#  '1256996.3',
#[Out]#  '1224749.3',
#[Out]#  ...]
strain_to_accn.keys()[1]
#[Out]# '1313.2378'
strain_to_accn.get('1313.2378')
#[Out]# 'accn|ERS021097.6807_2_3.39'
get_ipython().magic(u'pwd ')
#[Out]# u'/gsfs1/rsgrps/bhurwitz/scottdaniel/make-custom-patric-metagenome/data'
file_in.name
#[Out]# 'just-genome-and-accn.txt'
strain_to_accn.get('441769.6')
#[Out]# 'accn|NZ_ABFU01000066'
for line in file_in:
        line=line.rstrip('\n')
        cols=line.split(' ')
        accn=cols[0]
        strain=cols[1]
        strain_to_accn.setdefault(strain,[])
    strain_to_accn[strain].append(accn)
    
for line in file_in:
    line=line.rstrip('\n')
    cols=line.split(' ')
    accn=cols[0]
    strain=cols[1]
    strain_to_accn.setdefault(strain,[])
    strain_to_accn[strain].append(accn)
    
len(strain_to_accn
)
#[Out]# 15262
strain_to_accn.get('441769.6')
#[Out]# 'accn|NZ_ABFU01000066'
get_ipython().magic(u'rm (strain_to_accn)')
strain_to_accn={}
len(strain_to_accn)
#[Out]# 0
for line in file_in:
    line=line.rstrip('\n')
    cols=line.split(' ')
    accn=cols[0]
    strain=cols[1]
    strain_to_accn.setdefault(strain,[])
    strain_to_accn[strain].append(accn)
    
len(strain_to_accn)
#[Out]# 0
strain
#[Out]# '1765.6'
accn
#[Out]# 'accn|1765.6.con.44'
get_ipython().magic(u'ls ()')
objects()
dir()
#[Out]# ['In',
#[Out]#  'Out',
#[Out]#  '_',
#[Out]#  '_11',
#[Out]#  '_12',
#[Out]#  '_14',
#[Out]#  '_15',
#[Out]#  '_16',
#[Out]#  '_17',
#[Out]#  '_18',
#[Out]#  '_19',
#[Out]#  '_20',
#[Out]#  '_23',
#[Out]#  '_24',
#[Out]#  '_27',
#[Out]#  '_29',
#[Out]#  '_30',
#[Out]#  '_31',
#[Out]#  '__',
#[Out]#  '___',
#[Out]#  '__builtin__',
#[Out]#  '__builtins__',
#[Out]#  '__doc__',
#[Out]#  '__name__',
#[Out]#  '__package__',
#[Out]#  '_dh',
#[Out]#  '_exit_code',
#[Out]#  '_i',
#[Out]#  '_i1',
#[Out]#  '_i10',
#[Out]#  '_i11',
#[Out]#  '_i12',
#[Out]#  '_i13',
#[Out]#  '_i14',
#[Out]#  '_i15',
#[Out]#  '_i16',
#[Out]#  '_i17',
#[Out]#  '_i18',
#[Out]#  '_i19',
#[Out]#  '_i2',
#[Out]#  '_i20',
#[Out]#  '_i21',
#[Out]#  '_i22',
#[Out]#  '_i23',
#[Out]#  '_i24',
#[Out]#  '_i25',
#[Out]#  '_i26',
#[Out]#  '_i27',
#[Out]#  '_i28',
#[Out]#  '_i29',
#[Out]#  '_i3',
#[Out]#  '_i30',
#[Out]#  '_i31',
#[Out]#  '_i32',
#[Out]#  '_i33',
#[Out]#  '_i34',
#[Out]#  '_i4',
#[Out]#  '_i5',
#[Out]#  '_i6',
#[Out]#  '_i7',
#[Out]#  '_i8',
#[Out]#  '_i9',
#[Out]#  '_ih',
#[Out]#  '_ii',
#[Out]#  '_iii',
#[Out]#  '_oh',
#[Out]#  '_sh',
#[Out]#  'accn',
#[Out]#  'cols',
#[Out]#  'exit',
#[Out]#  'file_in',
#[Out]#  'get_ipython',
#[Out]#  'line',
#[Out]#  'os',
#[Out]#  'quit',
#[Out]#  'strain',
#[Out]#  'strain_to_accn']
file_in
#[Out]# <open file 'just-genome-and-accn.txt', mode 'r' at 0x2b60a2f9b810>
head just-genome-and-accn.txt
file_in.flush
#[Out]# <function flush>
file_in.flush()
file_in.seek()
file_in.seek(0)
file_in.tell()
#[Out]# 0
file_in.flush()
file_in.tell()
#[Out]# 0
for line in file_in:
    line=line.rstrip('\n')
    cols=line.split(' ')
    accn=cols[0]
    strain=cols[1]
    strain_to_accn.setdefault(strain,[])
    strain_to_accn[strain].append(accn)
    
len(strain_to_accn)
#[Out]# 15262
strain_to_accn.get('441769.6')
#[Out]# ['accn|NZ_ABFU01000005',
#[Out]#  'accn|NZ_ABFU01000006',
#[Out]#  'accn|NZ_ABFU01000007',
#[Out]#  'accn|NZ_ABFU01000010',
#[Out]#  'accn|NZ_ABFU01000011',
#[Out]#  'accn|NZ_ABFU01000013',
#[Out]#  'accn|NZ_ABFU01000015',
#[Out]#  'accn|NZ_ABFU01000016',
#[Out]#  'accn|NZ_ABFU01000017',
#[Out]#  'accn|NZ_ABFU01000018',
#[Out]#  'accn|NZ_ABFU01000021',
#[Out]#  'accn|NZ_ABFU01000024',
#[Out]#  'accn|NZ_ABFU01000026',
#[Out]#  'accn|NZ_ABFU01000028',
#[Out]#  'accn|NZ_ABFU01000029',
#[Out]#  'accn|NZ_ABFU01000030',
#[Out]#  'accn|NZ_ABFU01000033',
#[Out]#  'accn|NZ_ABFU01000035',
#[Out]#  'accn|NZ_ABFU01000042',
#[Out]#  'accn|NZ_ABFU01000043',
#[Out]#  'accn|NZ_ABFU01000045',
#[Out]#  'accn|NZ_ABFU01000046',
#[Out]#  'accn|NZ_ABFU01000047',
#[Out]#  'accn|NZ_ABFU01000051',
#[Out]#  'accn|NZ_ABFU01000055',
#[Out]#  'accn|NZ_ABFU01000060',
#[Out]#  'accn|NZ_ABFU01000063',
#[Out]#  'accn|NZ_ABFU01000064',
#[Out]#  'accn|NZ_ABFU01000066']
from Bio import SeqIO
strain_to_accn[1]
strain_to_accn{1}
strain_to_accn.keys[1]
strain_to_accn.key[1]
strain_to_accn.keys
#[Out]# <function keys>
strain_to_accn.keys()
#[Out]# ['717606.6',
#[Out]#  '1313.2378',
#[Out]#  '1203195.3',
#[Ou[Out]#  '1457250.4',
#[Out]#  ...]
strain_to_accn.keys()[1]
#[Out]# '1313.2378'
strain_to_accn.keys(1)
strain_to_accn.keys()[1]
#[Out]# '1313.2378'
genome_name=join(strain_to_accn.keys()[1],'.fna')
genome_name=strain_to_accn.keys()[1] + '.fna'
genome_name
#[Out]# '1313.2378.fna'
exit()
