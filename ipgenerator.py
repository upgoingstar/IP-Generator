import sys	
print "\n +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
print " |.|/|i|p|g|e|n|e|r|a|t|o|r|.|p|y|"
print " +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
if (len(sys.argv) > 2):
	print "\nUsage:	ipgenerator.py [OPTIONS] \n\n--safeips	All public IP Addresses, excluding those which are reserved\n		for specific purposes. (This option can be used to scan the \n		whole internet following safe practices). \n--unsafeIPs	All public IP Addresses, including those which are reserved\n		for specific purposes.	All reserved IP Addresses. \n--allprivate	All the Private IP Addresses including APIPA and Loopback IPs. \n--allprivaten	All the Private IP Addresses excluding APIPA and Loopback IPs. \n--loopback	The whole 127.0.0.0/24 series. \n--apipa		IPs belonging to APIPA series (169.254.X.X). \n--a10		IPs belonging to 10.X.X.X series. \n--b172		IPs belonging to 172.16.X.X series. \n--c192		IPs belonging to 192.168.X.X series\n--classA	All Class A Ip Addresses\n--classB	All class B IP Addresses\n--classC	All Class C IP addresses.\n--classD	All Class D IP addresses.\n--classE	All Class E IP addresses.\n--help		This awesome help in more detailed manner."
else:
	if (sys.argv[1] == "--reserved"):
		for q in range(0,255):
			for r in range(0,255):
				for s in range(0,255):
					ip = "10." + str(q) + "." + str(r) + "." + str(s)
					print ip
		for q in range(0,255):
			for r in range(0,255):
				for s in range(0,255):
					ip = "127." + str(q) + "." + str(r) + "." + str(s)
					print ip
		for q in range(64,127):
			for r in range(0,255):
				for s in range(0,255):
					ip = "100." + str(q) + "." + str(r) + "." + str(s)
					print ip
		for r in range(0,255):
			for s in range(0,255):
				ip = "169.254." + str(r) + "." + str(s)
				print ip
		for q in range(16,31):
			for r in range(0,255):
				for s in range(0,255):
					ip = "172." + str(q) + "." + str(r) + "." + str(s)
					print ip
		for s in range(0,255):
			ip = "192.0.0." + str(s)
			print ip
		for s in range(0,255):
			ip = "192.0.2." + str(s)
			print ip
		for s in range(0,255):
			ip = "192.88.99." + str(s)
			print ip	
		for r in range(0,255):
			for s in range(0,255):
				ip = "192.168." + str(r) + "." + str(s)
				print ip
		for r in range(0,255):
			for s in range(0,255):
				ip = "192.18." + str(r) + "." + str(s)
				print ip
		for r in range(0,255):
			for s in range(0,255):
				ip = "192.19." + str(r) + "." + str(s)
				print ip
		for s in range(0,255):
			ip = "192.51.100" + str(s)
			print ip
		for r in range(0,255):
			for s in range(0,255):
				ip = "203.113." + str(r) + "." + str(s)
				print ip
				
				

	if (sys.argv[1] == "--allprivate"):
		for q in range(0,255):
			for r in range(0,255):
				for s in range(0,255):
					ip = "10." + str(q) + "." + str(r) + "." + str(s)
					print ip
		for q in range(16,31):
			for r in range(0,255):
				for s in range(0,255):
					ip = "172." + str(q) + "." + str(r) + "." + str(s)
					print ip
		for r in range(0,255):
			for s in range(0,255):
				ip = "192.168." + str(r) + "." + str(s)
				print ip
	
	if (sys.argv[1] == "--allprivaten"):
		for q in range(0,255):
			for r in range(0,255):
				for s in range(0,255):
					ip = "10." + str(q) + "." + str(r) + "." + str(s)
					print ip
		for q in range(16,31):
			for r in range(0,255):
				for s in range(0,255):
					ip = "172." + str(q) + "." + str(r) + "." + str(s)
					print ip
		for r in range(0,255):
			for s in range(0,255):
				ip = "192.168." + str(r) + "." + str(s)
				print ip
		for r in range(0,255):
			for s in range(0,255):
				ip = "169.254." + str(r) + "." + str(s)
				print ip
		for q in range(0,255):
			for r in range(0,255):
				for s in range(0,255):
					ip = "127." + str(q) + "." + str(r) + "." + str(s)
					print ip
					
	if (sys.argv[1] == "--safeips"):
		for p in xrange(1,255):
			#print str(p) + "." + str(q) + "." + str(r) + "." + str(s) 
			for q in xrange(0,255):
				#print str(p) + "." + str(q) + "." + str(r) + "." + str(s)
				for r in xrange(0,255):
					#print str(p) + "." + str(q) + "." + str(r) + "." + str(s)
					for s in xrange(0,255):
						ip = str(p) + "." + str(q) + "." + str(r) + "." + str(s)
						if (p==10 or p==127):
							#Private IP and Loopback IP
							ip = "null"
						elif (p == 100 and q >= 64 and q <= 127):
							#Shared Address Space
							ip = "null"
						elif (p == 169 and q == 254):
							# APIPA
							ip = "null"
						elif (p == 172 and q >= 16 and q <= 31):
							#Private IP  172.16.0.0 - 172.31.255.255 
							ip = "null"
						elif (p == 192 and q == 0 and r == 0):
							#192.0.0.0/24        # RFC6890: IETF Protocol Assignments
							ip = "null"
						elif (p == 192 and q == 0 and r == 2):
							#192.0.2.0/24        # RFC5737: Documentation (TEST-NET-1)
							ip = "null"
						elif (p == 192 and q == 88 and r == 99):
							#192.88.99.0/24      # RFC3068: 6to4 Relay Anycast
							ip = "null"
						elif (p == 192 and q == 168):
							#RFC1918: Private-Use
							ip = "null"
						elif (p == 192 and q == 18):
							# RFC2544: Benchmarking
							ip = "null"
						elif (p == 192 and q == 19):
							# RFC2544: Benchmarking
							ip = "null"
						elif (p == 192 and q == 51 and r == 100):
							# RFC5737: Documentation (TEST-NET-2)
							ip = "null"
						elif (p == 203 and r == 113):
							# RFC5737: Documentation (TEST-NET-2)
							ip = "null"
						elif (p >= 224):
							# RFC5737: Reserved D & E
							ip = "null"
						if (ip != "null"):
							print ip
							
	if (sys.argv[1] == "--a10"):
		for q in range(0,255):
			for r in range(0,255):
				for s in range(0,255):
					ip = "10." + str(q) + "." + str(r) + "." + str(s)
					print ip
	
	if (sys.argv[1] == "--b172"):
		for q in range(16,31):
			for r in range(0,255):
				for s in range(0,255):
					ip = "172." + str(q) + "." + str(r) + "." + str(s)
					print ip
	
	if (sys.argv[1] == "--c192"):
		for r in range(0,255):
			for s in range(0,255):
				ip = "192.168." + str(r) + "." + str(s)
				print ip

	if (sys.argv[1] == "--loopback"):
		for q in range(0,255):
			for r in range(0,255):
				for s in range(0,255):
					ip = "127." + str(q) + "." + str(r) + "." + str(s)
					print ip
	
	if (sys.argv[1] == "--apipa"):
		for r in range(0,255):
			for s in range(0,255):
				ip = "169.254." + str(r) + "." + str(s)
				print ip
		
	if (sys.argv[1] == "--unsafeips"):
		for p in xrange(1,255):
			#print str(p) + "." + str(q) + "." + str(r) + "." + str(s) 
			for q in xrange(0,255):
				#print str(p) + "." + str(q) + "." + str(r) + "." + str(s)
				for r in xrange(0,255):
					#print str(p) + "." + str(q) + "." + str(r) + "." + str(s)
					for s in xrange(0,255):
						ip = str(p) + "." + str(q) + "." + str(r) + "." + str(s)
						if (p==10 or p==127):
							#Private IP and Loopback IP
							ip = "null"
						elif (p == 169 and q == 254):
							# APIPA
							ip = "null"
						elif (p == 172 and q >= 16 and q <= 31):
							#Private IP  172.16.0.0 - 172.31.255.255 
							ip = "null"
						elif (p == 192 and q == 168):
							#RFC1918: Private-Use
							ip = "null"
						if (ip != "null"):
							print ip
		
	
	if (sys.argv[1] == "--classA"):
		for p in xrange(1,126):
			for q in xrange(0,255):
				#print str(p) + "." + str(q) + "." + str(r) + "." + str(s)
				for r in xrange(0,255):
					#print str(p) + "." + str(q) + "." + str(r) + "." + str(s)
					for s in xrange(0,255):
						ip = str(p) + "." + str(q) + "." + str(r) + "." + str(s)
						print ip

	if (sys.argv[1] == "--classB"):
		for p in xrange(128,191):
			for q in xrange(0,255):
				#print str(p) + "." + str(q) + "." + str(r) + "." + str(s)
				for r in xrange(0,255):
					#print str(p) + "." + str(q) + "." + str(r) + "." + str(s)
					for s in xrange(0,255):
						ip = str(p) + "." + str(q) + "." + str(r) + "." + str(s)
						print ip

	if (sys.argv[1] == "--classC"):
		for p in xrange(192,223):
			for q in xrange(0,255):
				#print str(p) + "." + str(q) + "." + str(r) + "." + str(s)
				for r in xrange(0,255):
					#print str(p) + "." + str(q) + "." + str(r) + "." + str(s)
					for s in xrange(0,255):
						ip = str(p) + "." + str(q) + "." + str(r) + "." + str(s)
						print ip

	if (sys.argv[1] == "--classD"):
		for p in xrange(223,239):
			for q in xrange(0,255):
				#print str(p) + "." + str(q) + "." + str(r) + "." + str(s)
				for r in xrange(0,255):
					#print str(p) + "." + str(q) + "." + str(r) + "." + str(s)
					for s in xrange(0,255):
						ip = str(p) + "." + str(q) + "." + str(r) + "." + str(s)
						print ip

	if (sys.argv[1] == "--classE"):
		for p in xrange(239,255):
			for q in xrange(0,255):
				#print str(p) + "." + str(q) + "." + str(r) + "." + str(s)
				for r in xrange(0,255):
					#print str(p) + "." + str(q) + "." + str(r) + "." + str(s)
					for s in xrange(0,255):
						ip = str(p) + "." + str(q) + "." + str(r) + "." + str(s)
						print ip
						
	if (sys.argv[1] != "--safeips" and sys.argv[1] != "--unsafeips" and sys.argv[1] != "--allprivaten" and sys.argv[1] != "--allprivate" and sys.argv[1] != "--classA" and sys.argv[1] != "--classB" and sys.argv[1] != "--classC" and sys.argv[1] != "--classD" and sys.argv[1] != "--classE" and sys.argv[1] != "--a10" and sys.argv[1] != "--b172" and sys.argv[1] != "--c192" and sys.argv[1] != "--apipa" and sys.argv[1] != "--loopback" or sys.argv[1]=="-h"):
		print "\nUsage:	ipgenerator.py [OPTIONS] \n\n--safeips	All public IP Addresses, excluding those which are reserved\n		for specific purposes. (This option can be used to scan the \n		whole internet following safe practices). \n--unsafeIPs	All public IP Addresses, including those which are reserved\n		for specific purposes.	All reserved IP Addresses. \n--allprivate	All the Private IP Addresses including APIPA and Loopback IPs. \n--allprivaten	All the Private IP Addresses excluding APIPA and Loopback IPs. \n--loopback	The whole 127.0.0.0/24 series. \n--apipa		IPs belonging to APIPA series (169.254.X.X). \n--a10		IPs belonging to 10.X.X.X series. \n--b172		IPs belonging to 172.16.X.X series. \n--c192		IPs belonging to 192.168.X.X series\n--classA	All Class A Ip Addresses\n--classB	All class B IP Addresses\n--classC	All Class C IP addresses.\n--classD	All Class D IP addresses.\n--classE	All Class E IP addresses.\n--help		This awesome help in more detailed manner.\n\n Read more at http://google.com"

