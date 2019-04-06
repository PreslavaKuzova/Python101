def reduce_file_path(path):
    lst = path.split('/')
    lst = [x for x in lst if x != '' and x != '.']
    for index, element in enumerate(lst):
        if element == '..':
            del lst[index -1]
    lst = [x for x in lst if x != '..']
    new_path = '/' + '/'.join(lst)

    print(new_path)

reduce_file_path("/srv/../")
# "/"
reduce_file_path("/srv/www/htdocs/wtf/")
# "/srv/www/htdocs/wtf"
reduce_file_path("/srv/www/htdocs/wtf")
# "/srv/www/htdocs/wtf"
reduce_file_path("/srv/./././././")
# "/srv"
reduce_file_path("/etc//wtf/")
# "/etc/wtf"
reduce_file_path("/etc/../etc/../etc/../")
# "/"
reduce_file_path("//////////////")
# "/"
reduce_file_path("/../")
# "/"
