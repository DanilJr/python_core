def shorten_to_date(long_date):
    a=long_date.split()
    a.pop()
    b=' '.join(a)
    
    
    return  b.rstrip(',')