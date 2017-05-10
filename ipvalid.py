def validate(ip):
	flag = 0
	l = ip.split('.')
	for each in l:
		if int(each) > 255 or int(each)<0:
			flag=1
		elif not each.isdigit():
			flag=2
	if not l[-1].isdigit():  # for conditions like : 192.168.2. 
                flag=3
	count = ip.count('.') 
        if count!=3:             # for conditions like : 192.168
       		flag=3
	if flag==1:
		print "invalid ip -- value is greater than 255 or less than 0"
	elif flag==2:
		print "invalid ip -- characters apart from integers "
	elif flag==3:
		print "invalid ip -- incomplete ip"
	elif flag==0:
		print "valid ip"
		return 1
	

def subnet(mask,ip):
	start_addr=[] # to store the starting IP address
	last_addr = [] # to store the last IP address
	binary = [] # to hold the binary equivalent of IP
	l2=[] # to hold the mask 
	l3=[] # to hold the mask2
	mask_list=[] #refined mask storing
	mask_list2=[] 
	l = ip.split('.') #converting IP string to list with delim ='.'
	size = len(l)
	#converting IP to its binary eqvivalent
	for each in l:
		binary.append(bin(int(each))[2:].zfill(8))
	zeros = 32 - mask
	#generating mask 
	for i in range(mask):
		l2.append('1')
	for i in range(zeros):
		l2.extend('0')
	binary_mask = ''.join(l2)

	k=0
	while k<32: #refine storing mask string in list
		string = ''.join(l2[k:k+8])
		mask_list.append(string)
		k=k+8	
	#print "mask list : ",mask_list
	
	for i in range(0,size):
		start_addr.append(int(binary[i],2) & int(mask_list[i],2))
	print "starting address in the network :"
	print start_addr
	print "first usable network address is: "
	start_addr[-1]=start_addr[-1]+1
	first=''
        first = '.'.join(str(x) for x in start_addr)
	print first

	for i in range(mask):
       		l3.append('0')
        for i in range(zeros):
                l3.extend('1')
        k=0
        while k<32:
                string2 = ''.join(l3[k:k+8])
                mask_list2.append(string2)
                k=k+8
        
	for i in range(0,size):
		last_addr.append(int(binary[i],2) | int(mask_list2[i],2))
	print "Broadcast address of the network is : "
	print last_addr
	print "last usable addresss of the network is :"
	last_addr[-1]=last_addr[-1]-1
	last=''
	last = '.'.join(str(x) for x in last_addr)	
	print last


ip = raw_input("Enter the IP address for validation : ")
res = validate(ip)
if res == 1: # if only ip is valid ask subnet mask otherwise do not ask
	try:
		mask = int(raw_input("Enter subnet mask of the network : "))
	except:
		print" invalid entry of subnet mask."
subnet(mask,ip)
