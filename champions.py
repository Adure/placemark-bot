import httpx

version = "10.6.1"

def get_champs_dict():
    r = httpx.get(f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json")

    champs = {}
    for champ in r.json()['data'].values():
        dictVal = champs.update({champ['key']: champ['id']})

    return champs

