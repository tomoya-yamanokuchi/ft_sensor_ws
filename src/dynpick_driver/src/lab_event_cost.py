



n_Associate_Professor      = 1
n_Assistant_Professor      = 2
n_Doctoral_Course_Students = 9
n_master_valid             = 5



cost_Associate_Professor      = 1000
cost_Assistant_Professor      = 800
cost_Doctoral_Course_Students = 600
cost_master_valid             = 600


cost_total = 0
cost_total += n_Associate_Professor      * cost_Associate_Professor
cost_total += n_Assistant_Professor      * cost_Assistant_Professor
cost_total += n_Doctoral_Course_Students * cost_Doctoral_Course_Students
cost_total += n_master_valid             * cost_master_valid


n_Graduates       = 4
cost_per_Graduate = cost_total / n_Graduates

print("====================================")
print("          合計金額 = {:,}円".format(cost_total))
print("------------------------------------")
print("            卒業生 = {}人".format(n_Graduates))
print("  卒業生一人あたり = {:,}円".format(cost_per_Graduate))
print("====================================")