import csv
mylist=[]
dicta={}
dictb={}
prob_attra={}
prob_attrb={}
proba=0
probb=0
with open("clean_data.csv","rb") as file1:
	mylist=csv.reader(file1)
	takelist = list(mylist)

def iter_data(list1):
	classa=0
	classb=0
        #proba=0
        #robb=0
	for i in list1:
		templist = []
		for j in i:
			#templist.append(j)
			#print j
			if (i[-1]=="1"):
				classa+=1
				if(j not in dicta):
					dicta[j]=1
					templist.append(j)
				elif (j not in templist):
					dicta[j]+=1
			else:
				classb+=1
				if(j not in dictb):
					dictb[j]=1
					templist.append(j)
				elif (j not in templist):
					dictb[j]+=1
	#print dicta
	#print "  CLASS A ",classa
    #    print "  CLASS B ",classb
	#print "----------------------------------------------------------------------------------------"
	#print dictb
	proba=calc_prob(classa,classb)
	probb=calc_prob(classb,classa)
	#print proba
	#print probb
	for i in dicta.keys():
	    	prob_attra[i]=calc_prob1(dicta[i],classa)
	#print prob_attra
	for i in dictb.keys():
	    	prob_attrb[i]=calc_prob1(dictb[i],classb)
	#print prob_attrb
def test_prob(list1):
	pa=0
	pb=0
	acc=0
	for i in list1:
		for x in range(len(i)-1):
			if(i[x] in dicta.keys()):
				pa*=prob_attra[i[x]]
			if(i[x] in dictb.keys()):
				pb*=prob_attrb[i[x]]
		pa*=proba
		pb*=probb
		if(pa>pb):
			if(i[len(i)-1]=="1"):
				acc+=1
		else:
			if(i[len(i)-1]!="1"):
				acc+=1
        print "ACC ",acc
	print float(acc)/len(list1)


def calc_prob(a,b):
	return float(a)/(a+b)
def calc_prob1(a,b):
	return float(a)/b
bigattr=[]
attr=[]
for x in takelist:
	z=x[0].split(" ")
	z.append(x[1])
	attr.append(z)
	attr.append(x[1])
	bigattr.append(z)

        attr=[]
#print bigattr
iter_data(bigattr)

test_prob(bigattr[0:1000])
