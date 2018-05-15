def fav(name,place,food,superhero,editor,os):

 print('my name is %s' % name)
 print('my fav place is %s' % place)
 print('my fav food is %s' % food)
 print('my fav superhero is %s' % superhero)
 print('my fav editor is %s' % editor)
 print('my fav OS is %s' % os)

#fav('sid','Miami','sizziler','Dr Strange','Luis','macos')

fav_list=['sid','Miami','Sizzeler','Dr Strange','Luis','mac OS']
fav(*fav_list)

