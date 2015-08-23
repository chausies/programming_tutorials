def get_running_list():
  """
  Returns a running list function, where you can add elements and get a
  running list of all elements that've been added.

  Example
  -------
  >>> running_list = get_running_list()
  >>> running_list(1)
  [1]
  >>> running_list(2)
  [1, 2]
  >>> running_list(3)
  [1, 2, 3]
  >>> running_list("hello world")
  [1, 2, 3, 'hello world']
  """
  my_list = []
  def running_list(x):
    """
    Adds x to a running list and returns the running list so far.
    """
    my_list.append(x)
    return my_list
  return running_list


def get_running_avger(T = 10):
  """
  Returns a running average function that returns the average of the last
  `T` items that've been given to it. Initially, the last `T` items it starts
  out with are 0's.
  >>> running_avg = get_running_avger()
  >>> running_avg(1)
  0.1
  >>> running_avg(9)
  1.0
  >>> for i in range(10):
  ...   if i==9:
  ...     print running_avg(i)
  ...   else: 
  ...     _ = running_avg(i)
  4.5
  """
  hist = [0]*T
  def running_avg(x):
    i = 1
    while i < T: 
      hist[i-1] = hist[i]
      i = i + 1
    hist[-1] = x
    return sum(hist)/10.0
  return running_avg
