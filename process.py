from threading import Thread
from .mommy import mommy
from .daddy import daddy
from .chan import chan
from .mod import mod
from .var import var
from .error import error

def process_file(FileName: str):
  if not FileName.endswith('.uwu'): raise ValueError('The file must end with a .uwu')
  with open(FileName, 'r') as f:
    file = f.read()
  operations = file.split('pwease')
  print(operations)
  for i in range(len(operations)):
    process_op(operations[i], i)

def process_op(op, num):
  if op.startswith('|'):
    t = Thread(target=process_top, args=(op, num))
    t.start()
    t.join()
  elif op.startswith(' comment'): 
    return
  elif op.startswith(' mommy'):
    mommy(op, num)
  elif op.startswith(' daddy'):
    daddy(op, num)
  elif op.startswith(' daddy-chan') or op.startswith(' mommy-chan'):
    chan(op, num)
  elif op.startswith(' mod'):
    mod(op, num)
  elif op.startswith(' var'):
    var(op, num)
  else:
    error(op, num, 'You made daddy/mommy angwy I don\'t know what that mean')

def process_top(op, num):
  return process_op(op[1:], num)
