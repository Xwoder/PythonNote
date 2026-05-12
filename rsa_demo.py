import math

# ==========
# 1. 选择两个小素数 p, q
# ==========
p = 5
q = 11
print(f"p = {p}")
print(f"q = {q}")

# 检查：p 和 q 是否为素数
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

assert is_prime(p), "p 不是素数"
assert is_prime(q), "q 不是素数"
assert p != q, "p 和 q 不能相同"

print("p, q 是素数 ✔")

# ==========
# 2. 计算 n
# ==========
n = p * q
print("n =", n)

# ==========
# 3. 计算欧拉函数 φ(n)
# ==========
phi_n = (p - 1) * (q - 1)
print("φ(n) =", phi_n)

# ==========
# 4. 选择公钥指数 e
# ==========
e = 3

# 检查条件
assert 1 < e < phi_n, "e 不在合法范围内"
assert math.gcd(e, phi_n) == 1, "e 与 φ(n) 不互素"

print("e 合法 ✔")

# ==========
# 5. 计算私钥指数 d
#    e * d ≡ 1 (mod φ(n))
# ==========
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    raise ValueError("不存在模逆")

d = mod_inverse(e, phi_n)
print("d =", d)

# 再次检查
assert (e * d) % phi_n == 1, "d 不是 e 的模逆"
print("d 校验通过 ✔")

# ==========
# 6. 公钥 & 私钥
# ==========
public_key = (n, e)
private_key = (n, d)

print("公钥 =", public_key)
print("私钥 =", private_key)

# ==========
# 7. 选择明文 m
# ==========
m = 7

# 检查明文范围
assert 0 < m < n, "明文 m 必须满足 0 < m < n"
print("明文 m 合法 ✔")

# ==========
# 8. 加密
# c = m^e mod n
# ==========
c = pow(m, e, n)
print("密文 c =", c)

# ==========
# 9. 解密
# m' = c^d mod n
# ==========
m_decrypted = pow(c, d, n)
print("解密结果 m' =", m_decrypted)

# ==========
# 10. 最终验证
# ==========
assert m == m_decrypted, "解密失败"
print("RSA 加密/解密成功 ✔")
