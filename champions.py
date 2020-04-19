import httpx

version = "10.6.1"

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

def get_champs_dict():
    r = httpx.get(f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json")

    champs = {}
	# Classify champion genders and map their champion id to name
    for champ in r.json()['data'].values():
        counts = word_count(champ['blurb'].lower())
        gender = "unknown"
        male_count = 0
        female_count = 0
        if "her" in counts:
            female_count += counts['her']
        if "she" in counts:
            female_count += counts['she']

        if "him" in counts:
            male_count += counts['him']
        if "he" in counts:
            male_count += counts['he']

        if female_count > male_count:
            gender = "female"
        elif male_count > female_count:
            gender = "male"

        champs.update({champ['key']: {"name": champ['id'], "gender": gender}})

    return champs

