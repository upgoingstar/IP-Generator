IPGenerator.py
--------------

Wanted to scan a huge network? Intranet? Or may be Internet? But messed up with generating the list of IP addresses for specific address ranges. You can use this tool.
Ipgenerator.py  is basically a script to generate such kind of IP Addresses by just passing a simple switch. This is certainly a helpful script which will come handy when you are performing a specific set of operation (say scanning), on a range of IP Addresses. By using this script, you only need to take the output of this utility in a file, or may be in a variable and play around. Following is a brief description for using the script:

Usage:	ipgenerator.py 		[OPTIONS] --only one argument is required (which is mandatory). <br>
--reserved	this will print all the IP addresses which are reserved in some way, i.e. Shared Address Space, IETF Protocol Assignments, Private IP Addresses, Loopback, APIPA, Relay Anycast, Benchmarking, RFC5737: Documentation (TEST-NET-1), RFC5737: Documentation (TEST-NET-2), D and E Class IP Addresses.  

--safeips	all public IP Addresses, excluding those which are reserved. This was the option for which this tool was basically created. If you want to scan the whole internet, you can simply use this switch, and pass the output to your scanner. Doing this will exclude all the reserved IP addresses which will save your time as well as legal issues with your scanning.  

--allprivate			all the Private IP Addresses including APIPA and Loopback IPs. "  

--allprivaten			all the Private IP Addresses excluding APIPA and Loopback IPs. "  

--unsafeips	all public IP Addresses, including those which are reserved. So this basically gives all the IP addresses in public space.   

--a10	this will print all the private IP addresses which exist in Class A, i.e. 10.X.Y.Z series. 
--b172	this will print all the private IP Addresses which exist in Class B, i.e. 172.16.X.Y to 172.31.X.Y series.
--c192	this will print all the private IP Addresses which exist in Class C, i.e. 192.168.X.Y series.
--classA				all the IP addresses which may exist in class A.
--classB				all the IP addresses which may exist in class B.
--classC 			all the IP addresses which may exist in class C.
--classD				all the IP addresses which may exist in class D.
--classE				all the IP addresses which may exist in class E.
--help				see this help section.

Disclaimer: Yes, I know I am a bad programmer and the way I had written this is pathetic, but I was quite keen in getting the purpose solved. 
In case you have any suggestions, query, etc., feel free to reach me at:
Email: upgoingstaar@gmail.com
Twitter: @upgoingstar
