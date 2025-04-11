from commitly import Commitly

commitly = Commitly()

commitly.add("test.py")

msg = commitly.msg_commit()
print(msg)

commitly.save_msg_in_file(msg)

commitly.commit()