text=input('Text: ')
herfler={}
for herf in text:
    if(herf in herfler):
        herfler[herf]+=1
    else:
        herfler[herf]=1

for herf,say in herfler.items():
    print(f'{herf}-in sayi:{say}')
