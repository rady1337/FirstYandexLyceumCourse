lister = [9, 4, 5, 2, 8, 3]#  При данной функуции sorted, создается новый список,#  котороый явялется отсортированным списком lister, но список lister остается прежнимb = sorted(lister)print(b, 'видим, что появился наовый список под названием "b", а старый остался прежним')print(lister, 'листер остался прежним')#  А если мы напишем lister.sort(), то список lister изменится, станет остортированнымlister.sort()#  У нас остался тот же список, а новый не создавался, только уже имеющийся список изменилсяprint(lister, 'lister изменился и теперь он отсортирован, новый список не добавялся')