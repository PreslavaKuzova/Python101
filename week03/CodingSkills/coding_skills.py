import sys
import json 

def read_json():
    if (len(sys.argv) < 2):
        raise Exception("You must give the json file as a system argument!")

    with open (sys.argv[1], 'r') as f:
        data = json.load(f)
    return data

def checkKey(dict, key): 
    if key in dict.keys(): 
        return True 
    return False 

def coding_skills():
    data = read_json()
    dict_with_best_skills = {}
    dict_skill_level = {}
    for person in data.values():
        for personal_data in person:
            for skills in personal_data['skills']:
                if not checkKey(dict_with_best_skills, skills['name']):
                    dict_with_best_skills.update({skills['name'] : personal_data['first_name']+personal_data['last_name']})
                    dict_skill_level.update({skills['name'] : skills['level']})
                else:
                    if int(dict_skill_level.get(skills['name'])) < int(skills['level']):
                        dict_skill_level.update({skills['name'] : skills['level']})
                        dict_with_best_skills.update({skills['name'] : personal_data['first_name']+personal_data['last_name']})
    print(dict_with_best_skills)


coding_skills()