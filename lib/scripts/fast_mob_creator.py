#hoa
for i in range(81):
    print "elif prop_i=="+str(1261+i)+": \n\tmob_image = \"actor"+str(102+i)+"\""
print "\n"
#image
for i in range(137):
    print "\t\"actor"+str(i)+"_0\":DATA_IMAGES_ACTORS+\"actor"+str(i)+"_0.gif\",\\"
    print "\t\"actor"+str(i)+"_1\":DATA_IMAGES_ACTORS+\"actor"+str(i)+"_1.gif\",\\"
print "\n"
#mapeditor
for i in range(81):
    print("elif itemTexture=="+str(1261+i)+":")
    print("\tif light==0: tex = \"actor"+str(102+i)+"_0\"")
    print("\telse: tex = \"actor"+str(102+i)+"_1\"")
print "\n"
#mapeditor
for i in range(83):
    print("\t\t   [\"actor"+str(102+i)+"_0\","+str(1261+i)+"],\\")