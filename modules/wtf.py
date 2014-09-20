from mod_base import*

class Wtf(Command):
    """Show definitions for common acronyms. Usage: wtf acronym."""

    def init(self):
        self.acronyms = {
            'rom': 'Read-Only Memory',
            'edi': 'Electronic Data Interchange',
            'osi': 'Open Systems Interconnection',
            'mp3': 'MPEG-1 Audio Layer-3',
            'dvd+rw': 'Digital Versatile Disk Rewritable',
            'llc': 'Logical link control',
            'alu': 'Arithmetic Logic Unit',
            'osd': 'On Screen Display',
            'itu-t': 'ITU Telecommunication Standardization Sector',
            'gbic': 'Gigabit interface converter',
            'smm': 'Social Media Marketing',
            'aup': 'Acceptable Use Policy',
            'gigo': 'Garbage In, Garbage Out',
            'vlb': 'VESA Local Bus',
            'vle': 'Virtual Learning Environment',
            'risc': 'Reduced Instruction Set Computing',
            'hdtv': 'High Definition Televsion',
            'icann': 'Internet Corporation For Assigned Names and Numbers',
            'voip': 'Voice Over Internet Protocol',
            'gui': 'Graphical User Interface',
            'olap': 'Online Analytical Processing',
            'cms': 'Content Management System',
            'ups': 'Uninterruptible Power Supply',
            'pmu': 'Power Management Unit',
            'tcp/ip': 'Transmission control protocol',
            'pum': 'Potentially Unwanted Modification',
            'nbma': 'Non-broadcast multiple-access network',
            'nrzi': 'Non-Return-to-Zero Inverted',
            'ssid': 'Service Set Identifier',
            'jpeg': 'Joint Photographic Experts Group',
            'led': 'Light-Emitting Diode',
            'hdmi': 'High-Definition Multimedia Interface',
            'rdram': 'Rambus Dynamic Random Access Memory',
            'wais': 'Wide Area Information Server',
            'ctp': 'Composite Theoretical Performance',
            'ctr': 'Click-Through Rate',
            'cmyk': 'Cyan Magenta Yellow Black',
            'rdf': 'Resource Description Framework',
            'drm': 'Digital Rights Management',
            'jre': 'Java Runtime Environment',
            'iana': 'Internet Assigned Numbers Authority',
            'dvd+r': 'Digital Versatile Disc Recordable',
            'pci-x': 'Peripheral Component Interconnect Extended',
            'apu': 'Accelerated Processing Unit',
            'ips': 'Intrusion Prevention System',
            'api': 'Application Program Interface',
            'ipx': 'Internetwork Packet Exchange',
            'rup': 'Rational Unified Process',
            'vlsm': 'Cariable-length subnet masking',
            'usb': 'Universal Serial Bus',
            'zif': 'Zero Insertion Force',
            'https': 'HyperText Transport Protocol Secure',
            'iis': 'Internet Information Services',
            'uddi': 'Universal Description Discovery and Integration',
            'oop': 'Object-Oriented Programming',
            'vpn': 'Virtual Private Network',
            'vpi': 'Virtual Path Identifier',
            'des': 'Data Encryption Standard',
            'cat': 'Category 5 cable',
            'cisc': 'Complex Instruction Set Computing',
            'cad': 'Computer-Aided Design',
            'atm': 'Asynchronous Transfer Mode',
            'smtp': 'Simple Mail Transfer Protocol',
            'uat': 'User Acceptance Testing',
            'slip': 'Serial Line Internet Protocol',
            'sip': 'Session Initiation Protocol',
            'fpu': 'Floating Point Unit',
            'sata': 'Serial Advanced Technology Attachment',
            'lamp': 'Linux, Apache, MySQL, and PHP',
            'xhtml': 'Extensible Hypertext Markup Language',
            'pppoe': 'Point-to-Point Protocol over Ethernet',
            'css': 'Cascading Style Sheet',
            'lan': 'Local Area Network',
            'faq': 'Frequently Asked Questions',
            'sna': 'IBM Systems Network Architecture',
            'vlan': 'Virtual local area network',
            'mac': 'Address Media Access Control Address',
            'internic': 'Internet Network Information Center',
            'eof': 'End of frame',
            'man': 'Metropolitan area network',
            'ospf': 'Open Shortest Path First',
            'hfs': 'Hierarchical File System',
            'so': '-DIMM Small Outline Dual In-Line Memory Module',
            'scsi': 'Small Computer System Interface',
            'sd': 'Secure Digital',
            'ppc': 'Pay Per Click',
            'fifo': 'First In, First Out',
            'ttl': 'Time To Live',
            'pcmcia': 'Personal Computer Memory Card International Association',
            'wddm': 'Windows Display Driver Model',
            'cli': 'Command-line interpreter',
            'pci': 'Peripheral Component Interconnect',
            'pcm': 'Pulse-code modulation',
            'pcb': 'Printed Circuit Board',
            'pram': 'Parameter Random Access Memory',
            'eup': 'Enterprise Unified Process',
            'dac': 'Digital-to-Analog Converter',
            'ddr2': 'Double Data Rate 2',
            'ddr3': 'Double Data Rate Type 3',
            'fios': 'Fiber Optic Service',
            'noc': 'Network Operations Center',
            'daw': 'Digital Audio Workstation',
            'srgb': 'Standard Red Green Blue',
            'bsod': 'Blue Screen of Death',
            'dvd-ram': 'Digital Versatile Disc Random Access Memory',
            'odbc': 'Open Database Connectivity',
            'oui': 'Organizationally Unique Identifier',
            'mdi': 'Medium Dependent Interface',
            'mdf': 'Main distribution frame',
            'http': 'Hypertext Transfer Protocol',
            'ftp': 'File Transfer Protocol',
            'vci': 'Virtual Channel Identifier',
            'sms': 'Short Message Service',
            'dsl': 'Digital Subscriber Line',
            'sdlc': 'Synchronous Data Link Control',
            'dhcp': 'Dynamic Host Configuration Protocol',
            'smb': 'Server Message Block',
            'rll': 'Run length limited',
            'asp': 'Active Server Page or Application Service Provider',
            'ecc': 'Error Correction Code',
            'mms': 'Multimedia Messaging Service',
            'oasis': 'Organization for the Advancement of Structured Information Standards',
            'wi-fi': 'Wireless Fidelity',
            'pup': 'Potentially Unwanted Program',
            'bash': 'Bourne-Again Shell',
            'midi': 'Musical Instrument Digital Interface',
            'isp': 'Internet Service Provider',
            'iso': 'International Organization for Standardization',
            'lte': 'Long Term Evolution',
            'isa': 'Industry Standard Architecture',
            'cdma': 'Code Division Multiple Access',
            'bios': 'Basic Input/Output System',
            'cd-r': 'Compact Disc Recordable',
            'mamp': 'Mac OS X, Apache, MySQL, and PHP',
            'pots': 'Plain old telephone service',
            'dfs': 'Distributed File System',
            'ata': 'Advanced Technology Attachment',
            'nvram': 'Non-Volatile Random Access Memory',
            'gpu': 'Graphics Processing Unit',
            'gps': 'Global Positioning System',
            'udp': 'User Datagram Protocol',
            'tft': 'Thin-Film Transistor',
            'png': 'Portable Network Graphic',
            'rss': 'RDF Site Summary',
            'serp': 'Search Engine Results Page',
            'mbps': 'Megabits Per Second',
            'dte': 'Data terminal equipment',
            'dtd': 'Document Type Definition',
            'stp': 'Spanning tree protocol',
            'wins': 'Windows Internet Name Service',
            'lapf': 'Frame relay',
            'dslam': 'Digital Subscriber Line Access Multiplexer',
            'san': 'Storage Area Network',
            'ram': 'Random Access Memory',
            'sdram': 'Synchronous Dynamic Random Access Memory',
            'mib': 'Management information base',
            'vga': 'Video Graphics Array',
            'mis': 'Management Information System',
            'soap': 'Simple Object Access Protocol',
            'jsf': 'JavaServer Faces',
            'fcs': 'Frame check sequence',
            'sfp': 'Small form-factor pluggable transceiver',
            'bss': 'Basic service set',
            'mpeg': 'Moving Picture Experts Group',
            'jsp': 'Java Server Page',
            'fddi': 'Fiber Distributed Data Interface',
            'url': 'Uniform Resource Locator',
            'uri': 'Uniform Resource Identifier',
            'cps': 'Classroom Performance System',
            'qbe': 'Query By Example',
            'lpi': 'Lines Per Inch',
            'irq': 'Interrupt Request',
            'dos': 'Disk Operating System',
            'rte': 'Runtime Environment',
            'rtf': 'Rich Text Format',
            'ugc': 'User Generated Content',
            'cdn': 'Content Delivery Network',
            'rtp': 'Real-time Transport Protocol',
            'xml': 'Extensible Markup Language',
            'ldap': 'Lightweight Directory Access Protocol',
            'iec': 'International Organization for Standardization',
            'ocr': 'Optical Character Recognition',
            'xmp': 'Extensible Metadata Platform',
            'pop3': 'Post Office Protocol',
            'ssl': 'Secure Sockets Layer',
            'ssh': 'Secure Shell',
            'dv': 'Digital Video',
            'ssd': 'Solid State Drive',
            'i/o': 'Input/Output',
            'aes': 'Advanced Encryption Standard',
            'crt': 'Cathode Ray Tube',
            'ietf': 'Internet Engineering Task Force',
            'rfc': 'Request for Comments',
            'crc': 'Cyclical redundancy checking',
            'dpi': 'Dots Per Inch',
            'crm': 'Customer Relationship Management',
            'arp': 'Address Resolution Protocol',
            'isdn': 'Integrated Services Digital Network',
            'dvd-r': 'Digital Versatile Disc Recordable',
            'radius': 'Remote Authentication Dial In User Service',
            'nui': 'Natural User Interface',
            'seo': 'Search Engine Optimization',
            'dlc': 'Downloadable Content',
            'ieee': 'Institute of Electrical and Electronics Engineers',
            'dll': 'Dynamic Link Library',
            'ppga': 'Plastic Pin Grid Array',
            'irc': 'Internet Relay Chat',
            'nntp': 'Network News Transfer Protocol',
            'lun': 'Logical Unit Number',
            'xslt': 'Extensible Style Sheet Language Transformation',
            'sram': 'Static Random Access Memory',
            'vfat': 'Virtual File Allocation Table',
            'p2p': 'Peer To Peer',
            'vram': 'Video Random Access Memory',
            'gbps': 'Gigabits Per Second',
            'pdu': 'Protocol data unit',
            'slarp': 'Serial Line Address Resolution Protocol',
            'unc': 'Universal Naming Convention',
            'cd-rw': 'Compact Disc Re-Writable',
            'jfs': 'Journaled File System',
            'pdf': 'Portable Document Format',
            'tftp': 'Trivial File Transfer Protocol',
            'pda': 'Personal Digital Assistant',
            'cc': 'Carbon Copy',
            'vdsl': 'Very High Bit Rate Digital Subscriber Line',
            'pop': 'Point of presence',
            'cd': 'Compact Disc',
            'pon': 'Passive Optical Network',
            'rpc': 'Remote Procedure Call',
            'guid': 'Globally Unique Identifier',
            'rpm': 'Revenue Per 1,000 Impressions',
            'dcim': 'Digital Camera IMages',
            'twain': 'Toolkit Without An Informative Name',
            'pc': 'Personal Computer',
            'json': 'JavaScript Object Notation',
            'basic': "Beginner's All-purpose Symbolic Instruction Code",
            'blob': 'Binary Large Object',
            'lifo': 'Last In, First Out',
            'mca': 'Micro Channel Architecture',
            'nrz': 'Non-return-to-zero',
            'bmp': 'Bitmap',
            'imap': 'Internet Message Access Protocol',
            'hdv': 'High-Definition Video',
            'manet': 'Mobile Ad Hoc Network',
            'aix': 'Advanced Interactive Executive',
            'mpls': 'Multiprotocol Label Switching',
            'eia': 'Electronic Industries Alliance',
            'eigrp': 'Enhanced Interior Gateway Routing Protocol',
            'hdd': 'Hard Disk Drive',
            'sli': 'Scalable Link Interface',
            'sla': 'Software License or Service Level Agreement',
            'vc': 'Virtual circuit',
            'ip': 'Internet Protocol',
            'it': 'Information Technology',
            'rip': 'Routing Information Protocol',
            'im': 'Instant Message',
            'ivr': 'Interactive Voice Response',
            'ascii': 'American Standard Code for Information Interchange',
            'pap': 'Password authentication protocol',
            'pat': 'Port address translation',
            'filo': 'First In, Last Out',
            'iscsi': 'Internet Small Computer Systems Interface',
            'pptp': 'Point-to-Point Tunneling Protocol',
            'html': 'Hypertext Markup Language',
            'cmos': 'Complementary Metal Oxide Semiconductor',
            'raid': 'Redundant Array of Independent Disks',
            'nic': 'Network Interface Card',
            'rfid': 'Radio-Frequency Identification',
            'dbms': 'Database Management System',
            'dimm': 'Dual In-Line Memory Module',
            'mips': 'Million Instructions Per Second',
            'php': 'PHP Hypertext Preprocessor',
            'wpa': 'Wi-Fi Protected Access',
            'eps': 'Encapsulated PostScript',
            'ccd': 'Charged Coupled Device',
            'flops': 'Floating Point Operations Per Second',
            'clob': 'Character Large Object',
            'aiff': 'Audio Interchange File Format',
            'tcp': '/IP  Transmission Control Protocol/Internet Protocol',
            'hdlc': 'High-Level Data Link Control',
            'dvd-rw': 'Digital Versatile Disk Rewritable',
            'simm': 'Single In-Line Memory Module',
            'sku': 'Stock Keeping Unit',
            'adf': 'Automatic Document Feeder',
            'rgb': 'Red Green Blue',
            'wep': 'Wired Equivalent Privacy',
            'cdfs': 'Compact Disc File System',
            'adc': 'Analog-to-Digital Converter',
            'snap': 'Subnetwork Access Protocol',
            'smart': 'Self-Monitoring Analysis And Reporting Technology',
            'lcd': 'Liquid Crystal Display',
            'vdu': 'Visual Display Unit',
            'www': 'World Wide Web',
            'ole': 'Object Linking and Embedding',
            'kde': 'K Desktop Environment',
            'sdsl': 'Symmetric Digital Subscriber Line',
            'rstp': 'Spanning Tree Protocol#Rapid Spanning Tree Protocol .28RSTP.29',
            'exif': 'Exchangeable Image File Format',
            'ddr': 'Double Data Rate',
            'saas': 'Software as a Service',
            'icf': 'Internet Connection Firewall',
            'ptt': 'Public Telephone and Telegraph',
            'prom': 'Programmable Read-Only Memory',
            'ddl': 'Data Definition Language',
            'ics': 'Internet Connection Sharing',
            'uml': 'Unified Modeling Language',
            'ict': 'Information and Communication Technologies',
            'cgi': 'Common Gateway Interface',
            'hsf': 'Heat Sink and Fan',
            'tdm': 'Time-division multiplexing',
            'dce': 'Data communications equipment',
            's-http': 'Secure Hypertext Transfer Protocol',
            'oem': 'Original Equipment Manufacturer',
            'post': 'Power On Self Test',
            'netbios': 'Network Basic Input/Output System',
            'y2k': 'Year 2000',
            'ack': 'Acknowledgment (Transmission Control Protocol)',
            'ids': 'Intrusion Detection System',
            'acl': 'Access Control List',
            'bgp': 'Border Gateway Protocol',
            'rarp': 'Reverse Address Resolution Protocol',
            'fcc': 'Federal Communications Commission',
            'idf': 'Intermediate distribution frame',
            'ide': 'Integrated Device Electronics or Integrated Development Environment',
            'kbps': 'Kilobit per second',
            'soa': 'Service Oriented Architecture',
            'tiff': 'Tagged Image File Format',
            'ppi': 'Pixels Per Inch',
            'wamp': 'Windows, Apache, MySQL, and PHP',
            'tofu': 'Trust On First Use',
            'ppm': 'Pages Per Minute',
            'ppl': 'Pay Per Lead',
            'pps': 'Pay Per Sale',
            'ppp': 'Point to Point Protocol',
            'nsp': 'Network Service Provider',
            'mbr': 'Master Boot Record',
            'wan': 'Wide Area Network',
            'w3c': 'World Wide Web Consortium',
            'gis': 'Geographic Information Systems',
            'snmp': 'Simple Network Management Protocol',
            'gif': 'Graphics Interchange Format',
            'eha': 'Ethernet Hardware Address',
            'dns': 'Domain Name System',
            'is-is': 'Intermediate System to Intermediate System',
            'cpl': 'Cost Per Lead',
            'cidr': 'Classless Inter-Domain Routing',
            'icmp': 'Internet Control Message Protocol',
            'sdk': 'Software Development Kit',
            'dma': 'Direct Memory Access',
            'utf': 'Unicode Transformation Format',
            'mtu': 'Maximum Transmission Unit',
            'cir': 'Committed Information Rate',
            'utp': 'Unshielded twisted pair',
            'cpa': 'Cost Per Action',
            'pim': 'Personal Information Manager',
            'chap': 'Challenge-handshake authentication protocol',
            'adsl': 'Asymmetric Digital Subscriber Line',
            'dec(obs.)': 'Digital Equipment Corporation',
            'upnp': 'Universal Plug and Play',
            'crc-16-ccitt': 'Cyclical redundancy checking',
            'nac': 'Network Access Control',
            'ps/2': 'Personal System/2',
            'igp': 'Integrated Graphics Processor',
            'pvst': 'Per-VLAN Spanning Tree',
            'nat': 'Network Address Translation',
            'tia': 'Telecommunications Industry Association',
            'vrml': 'Virtual Reality Modeling Language',
            'ccitt': 'ITU Telecommunication Standardization Sector',
            'kvm': 'Switch  Keyboard, Video, and Mouse Switch',
            'ansi': 'American National Standards Institute',
            'sql': 'Structured Query Language',
            'dram': 'Dynamic Random Access Memory',
            'ess': 'Extended Service Set',
            'fsb': 'Frontside Bus',
            'ntfs': 'New Technology File System',
            'dvi': 'Digital Video Interface',
            'cpm': 'Cost Per 1,000 Impressions',
            'dvd': 'Digital Versatile Disc',
            'cd-rom': 'Compact Disc Read-Only Memory',
            'cpc': 'Cost Per Click',
            'eide': 'Enhanced Integrated Drive Electronics',
            'cpe': 'Customer premises equipment',
            'bcc': 'Blind Carbon Copy',
            'agp': 'Accelerated Graphics Port',
            'cpu': 'Central Processing Unit',
            'dvr': 'Digital Video Recorder'
        }

    def run(self, win, user, data, caller=None):
        args = Args(data)
        if args.Empty():
            key = args[0].lower()
            if key in self.acronyms.keys():
                win.Send(self.acronyms[key])
            else:
                win.Send("sorry, I don't know that one. try this: http://en.wikipedia.org/wiki/" + args[0])
        else:
            win.Send("please provide an acronym. i know " + str(len(self.acronyms)) + " of them.")

module = {
    "class": Wtf,
    "type": MOD_COMMAND,
    "level": 0,
}
