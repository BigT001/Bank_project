import signup
import signin

welcome = ("\nWelcome to padiPAY""\n\n\n")
message = ("The most reliable payment valut""\n\n\n")
optsignIN = ("Already a payPAID user? signIN" "\n\n\n")
optsignUP = ("New to payPADI? signUP\n")

print (welcome, message, optsignIN, optsignUP)

user_option = input("Enter an option (signIN or signUP): ")

if user_option.lower() == 'signin':
    print("Redirecting to sign-in page...")
    signin.padiUSER()

elif user_option.lower() == 'signup':
    print("Redirecting to sign-up page...")
    signup.newUSER()

else:
    print("Invalid choice. Please enter 'signin' or 'signup'.")