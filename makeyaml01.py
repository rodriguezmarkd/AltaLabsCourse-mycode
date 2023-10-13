#!/usr/bin/python3

import yaml

def main():
    hitchhikers = [{'name':'Zaphod Beeblebrox', 'species':'Betelgeusian'},{'name':'Arthur Dent','species':'Human'}]

    print(hitchhikers)

    with open("galaxyguide.yaml","w") as zfile:
        yaml.dump(hitchhikers, zfile)
    yamlstring = yaml.dump(hitchhikers)
    print(yamlstring)
if __name__ == "__main__":
    main()
