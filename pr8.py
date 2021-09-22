t=[7,7,8,8,8,8,9,10,10,6,6,6,7,7,7,12,12,12,12,11,11,9,9,9]
o=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
print(sum(t)/24)
print(max(t),'maximul tepereturii', min(t),'min temperaturii')
max=t.index(max(t))
print('ora',o[max])
min=t.index(min(t))
print('ora',o[min])