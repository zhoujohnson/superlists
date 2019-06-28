#coding=utf8
import hashlib
def sign_md5(param,secret="c24619ed7fef02a0ae16328146bca5f97cc6493957a2137b"):
	t = []
	#将参数放入列表中
	for i in param:
		t.append(i)
		t.sort()
	m = ""
	#将参数组合成需要的模式
	for j in t:
		m = m + j + param[j]
	sign_str = secret + m + secret
	m = hashlib.md5()
	m.update(sign_str)
	return m.hexdigest()
