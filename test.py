
def test():
    a=[1,2]
    a.pop()
    print a
    try:
        print 'here'
        1/0
        return
    finally:
        print 'there'
        
        
test()