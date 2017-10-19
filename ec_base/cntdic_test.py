
from ec_help import ec_cntdic as cntdic

cd = cntdic()

cd.add('a')
cd.add('b')
cd.add('b')
cd.add('c')
cd.add('c')
cd.add('c')
cd.add(7913)

print cd.by_cnt()
