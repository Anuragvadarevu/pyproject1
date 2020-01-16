



value=[]
while True:

	value1=(input('enter the value: '))

	
	if value1=="E":
		print('EXIT')

		exit()
	
	list_of_fact=[]	
	value1=int(value1)
		
	
	for n in range(1,value1+1):
		if value1%n==0:
			list_of_fact.append(n)
				
	x=len(list_of_fact)
	print('the factors of value',list_of_fact)
	if x<10:
		print('This is too less - Good Bye')
		print('Program Ends ')
	if x>10:
		r=list_of_fact[x-1]
		s=list_of_fact[x-2]
		t=list_of_fact[x-3]
		
				
		avg=[]
		avg.append(t)
		avg.append(r)
		avg.append(s)
		print('the highest 3 factors ',r,s,t)
		print(sum(avg)/len(avg))
	
	
	

	


	
		   
			
	


			







		   
		
     




	
	
	

	

		
	    
	

	

