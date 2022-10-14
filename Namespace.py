class mobile:
    fp='yes'
    @classmethod
    def is_fp(cls):
        print('finger print:', cls.fp)
realme=mobile()
redmi=mobile()
geek=mobile()

print('class fp:',mobile.fp)
print('realme:',realme.fp)
print('redmi:',redmi.fp)
print('geek:',geek.fp)
print()
mobile.fp='no'
print('class fp:',mobile.fp)
print('realme:',realme.fp)
print('redmi:',redmi.fp)
print('geek:',geek.fp)
print()
realme.fp='not wprking'
print('class fp:',mobile.fp)
print('realme:',realme.fp)
print('redmi:',redmi.fp)
print('geek:',geek.fp)
print()


