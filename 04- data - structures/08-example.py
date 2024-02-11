# nice_things = ['coffee', 'cheese', 'crackers', 'tea']
# for thing in nice_things:
#   print(f' I does not like  {thing} ')


def notifyme(f, args=None, kwargs=None):
 def logged(*args, **kwargs):
  print(f.__name__, ' called with', args, 'and', kwargs)
 return f(*args, **kwargs)
 return logged
@notifyme
def square(x):
 return x * x
res = square(25)