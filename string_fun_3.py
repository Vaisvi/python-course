# find and index are exactly same, but find is used to
msg = 'Brandon Sanderson is an American author of epic fantasy and science function'
author_idx = msg.find('author')
print('author word start at',author_idx)

# normal version
and_idx = msg.find('and')
print('and word start at',and_idx)

# with tricky hack
and_idx = msg.find('and ')
print('and word start at',and_idx)

# with start position
and_idx = msg.find('and',10)
print('and word start at',and_idx)

# reverse
author_idx = msg.rfind('author')
print('author word start at',author_idx)

