from commity.commitly import Commitly

commitly = Commitly()

commitly.add(".")

msg = commitly.msg_commit()
print(msg)

commitly.save_msg_in_file(msg)

commitly.commit()