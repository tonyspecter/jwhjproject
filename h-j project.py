tot_head=int(input('몇명인가요?  '))

print('명단을 파악하겠습니다')
name_list = []
for i in range(tot_head):
    name=input('이름: ')
    name_list.append(name)
public_money_dict=dict.fromkeys(name_list)

#공금지불액 조사
print('공금지불액을 조사하겠습니다')
public_sum=0
for i in public_money_dict:
    paid_money=int(input('%s :' % i))
    public_sum+=paid_money
    public_money_dict[i]=paid_money
print(public_money_dict)
#공급지불액 편차 계산
contribution=int(public_sum / tot_head)
public_money_deviation=public_money_dict.copy()
for i in public_money_dict:
    public_money_deviation[i]-=contribution
#
print('공금 일부를 공제 받아야 하는 인원수을 조사하겠습니다')
de_head=int(input())

if de_head>0 :
    print('공제금을 조사하겠습니다\n이름 금액 :')
    de_dict = {}
    deduction_sum=0
    for i in range(de_head) :
        name,deduction=input().split()
        deduction=int(deduction)
        charge=public_money_deviation[name]
        new_charge=charge+deduction
        public_money_deviation[name]=new_charge
        for p in range(tot_head) :
            if p==name_list.index(name) :
                pass
            else :
                public_money_deviation[name_list[p]]-=deduction/(tot_head-1)

        deduction_sum += deduction
    if deduction_sum>public_sum :
        error
    print(public_money_deviation)







