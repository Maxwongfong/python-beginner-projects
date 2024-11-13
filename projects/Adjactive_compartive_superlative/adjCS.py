from nltk.corpus import wordnet
import nltk
import re
import json

nltk.download("wordnet", quiet=True)

#Load irregular adjectives from a JSON file
with open("irregular_adjectives.json", "r") as f:
    IRREGULAR_ADJECTIVES = json.load(f)


def get_comp_sup(adjs):
    comp_sup = []

    for adj in adjs:
        synsets = wordnet.synsets(adj, pos=wordnet.ADJ)
        #print(synsets)
        if synsets:
            for syn in synsets:
            #print(syn)
                comp_forms = [lemma.name().replace("_", " ") for lemma in syn.lemmas()]
                #print('synlemmas',syn.lemmas())
                #print('a',comp_forms)
                #print(len(comp_forms))
                if len(comp_forms) >= 2:

                    comp_form = comp_forms[1]
                    #print('b',comp_forms)
                else:
                    comp_form = get_comparative_form(adj)
                if len(comp_forms) >= 3:
                    superl_form = comp_forms[2]
                    #print('c',comp_forms)
                else:
                    superl_form = get_superlative_form(adj)
                comp_sup.append((adj, comp_form, superl_form))
        else:
            comp_sup.append((adj, get_comparative_form(adj), get_superlative_form(adj)))

    #seen = set()
    unique_comp_sup = []
    for item in comp_sup:
        if item not in unique_comp_sup:
            unique_comp_sup.append(item)
            #seen.add(item)
        #else:
            #continue
    #comp_sup = unique_comp_sup
    return unique_comp_sup


def get_comparative_form(adj):
    if adj in IRREGULAR_ADJECTIVES:
        return IRREGULAR_ADJECTIVES[adj][0]
    elif re.match(r"^[aeiou][a-z]*$", adj):
        return adj + "er"
    else:
        return "more " + adj


def get_superlative_form(adj):
    if adj in IRREGULAR_ADJECTIVES:
        return IRREGULAR_ADJECTIVES[adj][1]
    elif re.match(r"^[aeiou][a-z]*$", adj):
        return adj + "est"
    else:
        return "most " + adj


def main():
    adjs = input("Enter a list of adjectives (comma-separated): ").split(",")
    adjs = [adj.strip() for adj in adjs]
    #print('d',adjs)
    unique_comp_sup = get_comp_sup(adjs)


    print("\nAdjective\tComparative\tSuperlative")
    print("------------------------------------------")
    for adj, c, s in unique_comp_sup:
        #while i<len(comp_sup):
        #    comp_sup
        print(f"{adj}\t\t{c}\t\t{s}")


if __name__ == "__main__":
    main()
