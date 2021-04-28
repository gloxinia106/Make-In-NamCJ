from datetime import date, timedelta
import math
import os

start = date(2019,8,26)
now = date.today()
total = 654
total_day = timedelta(days=total)
end = start + total_day
han_day = now - start
namun_day = end -now
persent = (han_day.days / total) * 100


print("="*7+"야발"+"="*7)
print("들어온날짜:" + str(start))
print("나의 전역일자:" +str(end))
print("%d일을 복무했고" %han_day.days)
print("%d일정도 남았습니다." %namun_day.days)
print("약 %d%%를 했습니다."%math.floor(persent))
print("="*18)

os.system('Pause')
