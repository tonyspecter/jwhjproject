tot_head=int(input('몇명인가요?  '))

print('명단을 파악하겠습니다')
p_dic={}
name_list = []
for i in range(tot_head):
    name=input('이름: ')
    name_list.append(name)
public_money_dict=dict.fromkeys(name_list)


print('공금지불액을 조사하겠습니다')
for i in public_money_dict:
    paid_money=int(input('%s :' % i))
    public_money_dict[i]=paid_money

from collections import Counterunter
contribution=Counter(public_money_dict)
print(contribution)
