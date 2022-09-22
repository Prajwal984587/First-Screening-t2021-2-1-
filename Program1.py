class calculator:
  def cal_op(self,a,b,operation):
    match operation:
      case 'addition':
        return a+b
      case 'subtraction':
        return a-b
      case 'multiplication':
        return a*b
      case 'division':
        return a/b
      case_:
        return 'choose correct operation'
cl=calculator()
a=int(input())
b=int(input())
operator=input()
print(cl.cal_op(a,b,operation))
