#IPGenerator.py

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  
| . | / | i | p | g | e | n | e | r | a | t | o | r | . | p | y |  
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  

Wanted to scan a huge network? Intranet? Or may be Internet? But messed up with generating the list of IP addresses for specific address ranges. You can use this tool.  

Ipgenerator.py  is basically a script to generate such kind of IP Addresses by just passing a simple switch. This is certainly a helpful script which will come handy when you are performing a specific set of operation (say scanning), on a range of IP Addresses. By using this script, you only need to take the output of this utility in a file, or may be in a variable and play around. Following is a brief description for using the script:

<dl>
  <dt>Usage:</dt>
  <dd>ipgenerator.py 		[OPTIONS] --only one argument is required (which is mandatory).</dd>

  <dt>--reserved</dt>
  <dd>this will print all the IP addresses which are reserved in some way, i.e. Shared Address Space, IETF Protocol Assignments, Private IP Addresses, Loopback, APIPA, Relay Anycast, Benchmarking, RFC5737: Documentation (TEST-NET-1), RFC5737: Documentation (TEST-NET-2), D and E Class IP Addresses.  </dd>


  <dt>--safeips </dt>
  <dd>all public IP Addresses, excluding those which are reserved. This was the option for which this tool was basically created. If you want to scan the whole internet, you can simply use this switch, and pass the output to your scanner. Doing this will exclude all the reserved IP addresses which will save your time as well as legal issues with your scanning. </dd>

  <dt>--allprivate</dt>
  <dd>all the Private IP Addresses including APIPA and Loopback IPs. </dd>

  <dt>--allpublic</dt>
  <dd>all the Private IP Addresses excluding APIPA and Loopback IPs. </dd>

  <dt>--unsafeips</dt>
  <dd>all public IP Addresses, including those which are reserved. So this basically gives all the IP addresses in public space. </dd>

  <dt>--a10</dt>
  <dd>this will print all the private IP addresses which exist in Class A, i.e. 10.X.Y.Z series. </dd>

  <dt>--b172</dt>
  <dd>this will print all the private IP Addresses which exist in Class B, i.e. 172.16.X.Y to 172.31.X.Y series.</dd>

  <dt>-c192</dt>
  <dd>this will print all the private IP Addresses which exist in Class C, i.e. 192.168.X.Y series.</dd>

 <dt>--classA</dt>
  <dd>all the IP addresses which may exist in class A.</dd>

 <dt>--classB	</dt>
  <dd>all the IP addresses which may exist in class B.</dd>

 <dt>--classC	</dt>
  <dd>all the IP addresses which may exist in class C.</dd>

 <dt>--classD	</dt>
  <dd>all the IP addresses which may exist in class D.</dd>

 <dt>--classE	</dt>
  <dd>all the IP addresses which may exist in class E.</dd>

 <dt>--help</dt>
  <dd>see the help section.</dd>

</dl>  

<b>Disclaimer:</b> Yes, I know I am a bad programmer and the way I had written this is pathetic, but I was quite keen in getting the purpose solved.  

In case you have any suggestions, query, etc., feel free to reach me at:  
<b>Email:</b> upgoingstaar@gmail.com  
<b>Twitter:</b> @upgoingstar



