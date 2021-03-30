tot_head=int(input('몇명인가요?  '))

print('명단을 파악하겠습니다')
p_dic={}
name_list = []
for i in range(tot_head):
    name=input('이름: ')
    name_list.append(name)
public_money_dict=dict.fromkeys(name_list)

#공금지불액 조사
print('공금지불액을 조사하겠습니다')
sum=0
for i in public_money_dict:
    paid_money=int(input('%s :' % i))
    sum+=paid_money
    public_money_dict[i]=paid_money

#공급지불액 편차 계산
contribution=int(sum/tot_head)
public_money_deviation=public_money_dict.copy()
for i in public_money_dict:
    public_money_deviation[i]-=contribution




