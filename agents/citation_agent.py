import requests

def fetch_citation_metadata(doi):
    headers = {"Accept": "application/vnd.citationstyles.csl+json"}
    url = f"https://doi.org/{doi}"
    try:
        res = requests.get(url, headers=headers)
        if res.ok:
            return res.json()
    except:
        return {}
