import enum
class Countries(enum.Enum):
    Antartica = 672
    Afghanistan= 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244

user_input=input("Enter the member name: ")
print("Member name: ",Countries[user_input].name)
print("Member value: ",Countries[user_input].value)
