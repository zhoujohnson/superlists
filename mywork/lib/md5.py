def md5(str):
    import hashlib
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()

if __name__ == "__main__":
    str = "methodglsx.common.account.loginapp_key48e5e13229b82c1b4e6e8c96151f0637v1.0.0channelandroidformatjsonaccount13267020113password111111timestamp2014-08-05 14:27:46"
    secret = "c24619ed7fef02a0ae16328146bca5f97cc6493957a2137b"
    print md5(secret+str+secret)