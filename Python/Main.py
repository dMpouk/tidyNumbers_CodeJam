#Solution for Tidy Numbers, both Small and Large input
#Mpoukouvalas Dimitris

def find_tidy(num):
    i = 0
    count = 0
    flag = False
    while i < (len(num) - 1):
        if num[i] > num[i+1]:
            if count == i and flag is True:
                temp_str = str(int(num[0]) - 1)
                temp_str += '9' * (len(num) - 1)
            else:
                new_digit = str(int(num[i-count]) - 1)
                temp_str = num[:i-count] + str(new_digit) + ('9' * (len(num) - ((i-count)+1)))
            return temp_str
        elif num[i] == num[i+1]:
            count += 1     #count continuous same digits
            flag = True
        else:
            count = 0
        i += 1

    return num

#Selection of input
choice = input("For which input you want a solution? (Small or Large)\n")
if choice.upper() == "SMALL":
    #for small.in
    fr = open('B-small-practice.in', 'r')
    fw = open('B-small-output.out', 'w')
elif choice.upper() == "LARGE":
    #for large.in
    fr = open('B-large-practice.in', 'r')
    fw = open('B-large-output.out', 'w')
else:
    print("Choose one input")
# --- end of selection ---

t = int(fr.readline())

for cases in range(t):
    num = fr.readline()
    result = find_tidy(num.strip())
    fw.write('Case #{case}: {res} \n'.format(case=cases + 1, res=result.lstrip('0')))