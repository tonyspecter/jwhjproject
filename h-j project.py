tot_head=int(input('몇명인가요?  '))

print('명단을 파악하겠습니다')
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
print(public_money_dict)
#공급지불액 편차 계산
contribution=int(sum/tot_head)
public_money_deviation=public_money_dict.copy()
for i in public_money_dict:
    public_money_deviation[i]-=contribution
#
print('공금 일부를 공제 받아야 하는 인원을 조사하겠습니다')
de_head=int(input())

if de_head>0 :
    print('공제금을 조사하겠습니다\n이름 금액 :')
    de_dict = {}
    deduction_sum=0
    for i in range(de_head) :
        name,deduction=input().split()
        charge=public_money_deviation.get(name)
        deduction_sum+=deduction
        new_charge=charge+deduction





