from sys import stdind = {}frazes = stdin.readlines()for fraze in frazes:    fraze = fraze.strip()    type_fraze = fraze.split(': ')[1]    some_fraze = fraze.split(': ')[0]    if type_fraze in d:        if some_fraze not in d[type_fraze]:            old_frazes = d[type_fraze]            old_frazes = old_frazes + '; ' + some_fraze            d[type_fraze] = old_frazes    else:        d[type_fraze] = some_frazefor typ in d:    print(typ + ' - ' + d[typ])