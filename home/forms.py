from django import forms
from .models import Message, Visitor


class StyledModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(StyledModelForm, self).__init__(*args, **kwargs)
        for field in self.fields.itervalues():
            field.widget.attrs['placeholder'] = field.label.capitalize()
            field.widget.attrs['required'] = ''


class MessageForm(StyledModelForm):

    name = forms.CharField(required=True, label='name')
    email = forms.EmailField(required=True, label='email')

    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'content']

    def save(self):
        instance = super(MessageForm, self).save()

        post_data = self.clean()
        v, _ = Visitor.objects.update_or_create(
            email=post_data['email'],
            defaults={'name': post_data['name']})

        instance.visitor = v
        instance.save()

        return instance
