cant = 30
pos = 51
item_id = 1296
obj = "big_constructionwall"
folder = "DATA_IMAGES_BUILDING_BIG"
filename = "tex.txt"
tofile = False
logic = 7

if tofile:
    a = open(filename,"w")
    for i in range(cant):
        a.write("  \""+obj+str(pos+i)+"_0\":PhotoImage(file="+folder+"+\""+obj+str(pos+i)+"_0.gif\"),\\\n")
        a.write("  \""+obj+str(pos+i)+"_1\":PhotoImage(file="+folder+"+\""+obj+str(pos+i)+"_1.gif\"),\\\n")
    a.write("\n")
    for i in range(cant):
        a.write("elif itemTexture == "+str(item_id+i)+":\n")
        a.write("\tif light==0: tex = \""+obj+str(pos+i)+"_0\"\n")
        a.write("\telse: tex = \""+obj+str(pos+i)+"_1\"\n")
    a.write("\n")
    a.close()

else:
    print "Textures:"
    for i in range(cant):
        print("\t\""+obj+str(pos+i)+"_0\":PhotoImage(file="+folder+"+\""+obj+str(pos+i)+"_0.gif\"),\\")
        print("\t\""+obj+str(pos+i)+"_1\":PhotoImage(file="+folder+"+\""+obj+str(pos+i)+"_1.gif\"),\\")
    print "\nAnalisys:"
    for i in range(cant):
        print("elif itemTexture == "+str(item_id+i)+":")
        print("\tif light==0: tex = \""+obj+str(pos+i)+"_0\"")
        print("\telse: tex = \""+obj+str(pos+i)+"_1\"")
    print "\nButtons:"
    for i in range(cant):
        print("[\""+obj+str(pos+i)+"_0\",\""+str(logic)+"-"+str(item_id+i)+"\",2],\\")