from commitly.commitly import Commitly

commitly = Commitly()

commitly.add(".")

msg = commitly.generate_commit_message()
print(msg)

commitly.save_message_to_file(msg)

commitly.commit()