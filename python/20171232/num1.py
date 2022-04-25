numbers= [273, 103, 5, 32, 65, 72, 800, 99]

int_odd  =0
int_even =0

for i in numbers:
    if(i %2==1):
        
        int_odd += i
    else:
        
        
        int_even += i
        


print('짝수의 합  %d , 홀수의 합 %d 개  '  %( int_even ,int_odd )  )