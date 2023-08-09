![image](https://github.com/ParzivalHack/Proxy-Inspector/assets/82817793/de2b460b-1dd3-49ef-a5af-7f8da7b4d830)

# Proxy-Inspector
The Proxy Inspector is an advanced and feature-rich Python Command-Line Interface (CLI) tool meticulously engineered to provide comprehensive and accurate assessments of proxy validity and anonymity. Leveraging the robustness of Python, this tool sets itself apart from conventional proxy checkers, offering sophisticated functionalities that cater to the discerning needs of tech-savvy users.

Through its seamless integration with the "requests" library, the Proxy Inspector efficiently verifies the integrity of a user-provided list of proxies. Employing meticulous HTTP requests to the authoritative domain "https://httpbin.org/ip," it rigorously evaluates the responsiveness and legitimacy of each proxy. Proxies that successfully respond to the request are identified as valid, while those that fail to meet the criteria are swiftly excluded from further consideration.

Intriguingly, the Proxy Inspector goes beyond mere validity checks and delves into the realm of anonymity. With an astute analysis of the client IP address and the proxy IP address, it unearths crucial insights. When the client IP address diverges from the proxy IP address, the tool classifies the proxy as "anonymous," indicating its ability to shield the true identity of the client.

The Proxy Inspector stands as a testament to the capabilities of modern Python programming, exemplifying the sophistication and depth that can be achieved in developing tools for network analysis. Its clean and well-structured codebase ensures ease of maintenance and extensibility, while its comprehensive documentation empowers users with the knowledge to harness its capabilities effectively.

By empowering users with accurate and actionable data, the Proxy Inspector embodies the spirit of professionalism and precision, making it an indispensable tool for network administrators, cybersecurity experts, and developers seeking to navigate the intricate landscape of proxy verification.

# proxies.txt file

Along with the Proxy Inspector tool, a text file (.txt) is provided, comprising a substantial collection of more than 5000 proxies, available for testing purposes. While this file has not undergone exhaustive testing, it's nonetheless complete and offers a starting point for users to initiate their proxy verification process. This file serves as a valuable resource for users to expedite their evaluation of various proxies. 

It is essential to note that while the provided file is beneficial, users are encouraged to exercise caution and conduct their due diligence in verifying the authenticity and reliability of the proxies listed. 
For utmost control and flexibility, the file can and must be  customized to incorporate user-specific proxies for comprehensive and tailored testing (so if a user wants to test their own proxies, they must modify the proxies.txt and add them to the file).

# Download Prerequisites

* ```pip install requests```
* ```pip install colorama```

# Linux & Termux & MacOS

* ```git clone https://github.com/ParzivalHack/Proxy-Inspector```
* ```cd Proxy-Inspector```
* ```python proxyinspect.py```

# Windows
* Search in your pc the "Microsoft Store" and, once opened, search "Python" and install "Python 3.10".
* Just download (almost) ALL the files in this repository (the proxyinspect.py, the proxies.txt file and the run.bat file) and be sure to keep them all in the same directory on your pc (i suggest putting them on your Desktop).
* Double-click on the run.bat file to execute the tool.
* Once executed in cmd (and after modifying the proxies.txt file with your own proxies), just press ENTER to start the tool.

# License AGPL-3.0

Features of the GNU Affero General Public License (AGPL-3.0):

* Copyleft: Like the GPL, the AGPL-3.0 is a copyleft license. This means that if you modify or extend the software licensed under AGPL-3.0, you must distribute those modifications under the same license. This ensures that the source code remains open and accessible to everyone.

* Network Interaction: One key feature that distinguishes the AGPL-3.0 from the regular GPL is its "network interaction" clause. If you run a modified AGPL-licensed software on a server and provide access to it over a network, you must also make the modified source code available to the users who interact with that software over the network. This closes the so-called "application service provider (ASP) loophole" that exists in the regular GPL.

* Distribution and Use: AGPL-3.0 allows users to freely use, modify, and distribute the software, provided they comply with the license's terms, including the distribution of the source code for any changes.

* Compatibility: The AGPL-3.0 is not compatible with all other open-source licenses, particularly those that do not require derivative works to be distributed under the same license. If you use AGPL-3.0 code in your project, your project must be released under AGPL-3.0 or a compatible license.
