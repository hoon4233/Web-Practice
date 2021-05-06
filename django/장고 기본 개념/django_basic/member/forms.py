from django import forms
from .models import BoardMember
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label = '사용자 이름',
    error_messages = {'required':'아이디를 입력하세요!'}
    )
    password = forms.CharField(widget = forms.PasswordInput, label = '비밀번호',
    error_messages = {'required':'비밀번호를 입력하세요!'}
    )

    def clean(self):
        clean_data = super().clean()
        username = clean_data.get('username')
        password = clean_data.get('password')

        if username and password :
            try :
                member = BoardMember.objects.get(username = username)

                if not check_password(password, member.password):
                    self.add_error('password','비밀번호가 다릅니다.')
                else :
                    self.user_id = member.id

            except BoardMember.DoesNotExist:
                self.add_error('username', '없는 회원입니다.')
                return
