import json
def read_data(argument):
    with open (argument, 'r') as f:
        data = json.load(f)
    return data


def main():
    data = read_data('data.json')
    for people in list(data.values()):
        for person in people:
            interests = ''
            for intr in person['interests']:
              interests += '<li>'+ intr + '</li>'           
            f = open(person['first_name'].lower() + '-' + person['last_name'].lower() + '.html', 'w')
            message = """
<!DOCTYPE html>
<html>
<head>
    <title>"""  + person['first_name'] + ' ' + person['last_name'] + """</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
    <h1 class="full-name">""" + person['first_name'] + ' ' + person['last_name'] + """</h1>
    <img class="avatar" src="avatars/""" + person['first_name'].lower() + """.png">
    <div class="base-info">
      <p>Age:""" + str(person['age']) + """</p>
      <p>Birth date:""" + str(person['birth_date']) + """</p>
      <p>Birth place:""" + person['birth_place'] + """</p>
      <p>Gender:""" + person['gender'] + """</p>
    </div>
    <div class="interests">
      <h2>Interests:</h2>
      <ul>""" + interests + """
      </ul>
    </div>
    <div class="skills">
    </div>
</body>
</html>
            """

            f.write(message)
            f.close()


if __name__ == '__main__':
    main()