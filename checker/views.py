# from django.shortcuts import render
# from .forms import PasswordForm
# import zxcvbn ## used to analyze the password strength

# # Create your views here.

# def password(request):
#     feedback = None ## initializing the 'feedback' variable as 'None' as it will be used to hold values later
#     if request.method == 'POST': 
#         form = PasswordForm(request.POST) ## 'form' creates an instanse 'PasswordForm' & populates 'PasswordForm' with the data it recives from the POST operation
#         if form.is_valid(): ## 'is_valid()' checks that if the data has been correctly filled in the form
#             password = form.cleaned_data['password'] ## extracts the password entered by the user in the form and 'cleaned_data[]' cleans the unwanted things like whitespaces, etc.
#             result = zxcvbn.zxcvbn(password)
#             feedback = {
#                 'score': result['score'], ## gives the password a score according to its strength
#                 'suggestions': result['feedback']['suggestions'],
#                 'warning': result['feedback']['warning']
#             }
#     else:
#         form = PasswordForm()
#     return render(request, 'password_checker.html', {'form': form, 'feedback': feedback})







from django.shortcuts import render
from .forms import PasswordForm
import zxcvbn

def password(request):
    feedback = None
    if request.method == 'POST':
        print("POST request received")  # Debugging line to confirm the request is POST
        form = PasswordForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # Debugging line to confirm form validation
            password = form.cleaned_data['password']  # Get cleaned password
            print(f"Password entered: {password}")  # Debugging line to check password
            result = zxcvbn.zxcvbn(password)  # Analyze password strength
            feedback = {
                'score': result['score'],
                'suggestions': result['feedback']['suggestions'],
                'warning': result['feedback']['warning']
            }
        else:
            print("Form is not valid")  # Debugging line to catch form validation errors
    else:
        print("GET request received")  # Debugging line for GET request
        form = PasswordForm()

    return render(request, 'password_checker.html', {'form': form, 'feedback': feedback})
