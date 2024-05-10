import requests

# Fetch the content of the URL
url = "https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/configtg.txt"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if the request was unsuccessful
except requests.exceptions.RequestException as e:
    print(f"An error occurred while fetching the URL: {e}")
else:
    content = response.text

    # Separate the subscriptions based on the v2ray type
    subscriptions = content.splitlines()
    vmess = [s for s in subscriptions if s.startswith('vmess://')]
    vless = [s for s in subscriptions if s.startswith('vless://')]
    trojan = [s for s in subscriptions if s.startswith('trojan://')]
    ss = [s for s in subscriptions if s.startswith('ss://')]
    socks = [s for s in subscriptions if s.startswith('socks://')]
    hysteria2 = [s for s in subscriptions if s.startswith('hysteria2://')]
    hy2 = [s for s in subscriptions if s.startswith('hy2://')]
    tuic = [s for s in subscriptions if s.startswith('tuic://')]
    hysteria = [s for s in subscriptions if s.startswith('hysteria://')]
    naive = [s for s in subscriptions if s.startswith('naive+')]

    # Write the results to separate files
    with open('python/vmess', 'w') as f:
        f.write('\n'.join(vmess))
    with open('python/vless', 'w') as f:
        f.write('\n'.join(vless))
    with open('python/trojan', 'w') as f:
        f.write('\n'.join(trojan))
    with open('python/ss', 'w') as f:
        f.write('\n'.join(ss))
    with open('python/socks', 'w') as f:
        f.write('\n'.join(socks))
    with open('python/hysteria2', 'w') as f:
        f.write('\n'.join(hysteria2))
    with open('python/hy2', 'w') as f:
        f.write('\n'.join(hy2))
    with open('python/tuic', 'w') as f:
        f.write('\n'.join(tuic))
    with open('python/hysteria', 'w') as f:
        f.write('\n'.join(hysteria))
    with open('python/naive', 'w') as f:
        f.write('\n'.join(naive))





                
