from django import forms

class FeedBackForm(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)
    bot_handler = forms.CharField(required=False,widget=forms.HiddenInput)
    # password = forms.CharField(label='Enter password',widget=forms.PasswordInput)
    # rpassword = forms.CharField(label='Re Enter password',widget=forms.PasswordInput)
    
    def clean(self):
        total_cleaned_data = super().clean()
        bot_handler_value = total_cleaned_data['bot_handler']
        if len(bot_handler_value)>0:
            raise forms.ValidationError('Request from bot cannot be submitted.')
        
    # def clean(self):
    #     total_cleaned_data = super().clean()
    #     pwd = total_cleaned_data['password']
    #     rpwd = total_cleaned_data['rpassword']
    #     if pwd != rpwd:
    #         raise forms.ValidationError('Entered password do not match')
        
    # def clean(self):
    #     print("Total form validation.")
    #     total_cleaned_data = super().clean()
    #     print("Validating name.")
    #     inputname = total_cleaned_data['name']
    #     if len(inputname) < 4:
    #         raise forms.ValidationError("The minimum number of characters in the name field should be 4.")
        
    #     print("Validating rollno.")
    #     inputrollno = total_cleaned_data['rollno']
    #     if inputrollno <= 0:
    #         raise forms.ValidationError("Roll no should be greater than 0")
        
    #     print("Validating email.")
    #     inputemail = total_cleaned_data['email']
    #     if inputemail[-10:] != '@gmail.com':
    #         raise forms.ValidationError("Email should be gmail.")
    
   