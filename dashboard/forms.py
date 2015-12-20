from django import forms
from .models import Snippet, SnippetPos


class StyledModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(StyledModelForm, self).__init__(*args, **kwargs)
        for field in self.fields.itervalues():
            field.widget.attrs['class'] = 'form-control'


class SnippetForm(StyledModelForm):

    POSITION_CHOICES = (('', '----------'),) + \
        tuple((sp.slug, sp.slug) for sp in SnippetPos.objects.all())

    position = forms.CharField(
        required=False,
        label='position',
        widget=forms.Select(
            attrs={'class': 'form-control'},
            choices=POSITION_CHOICES,
        ),
    )

    def __init__(self, *args, **kwargs):
        super(SnippetForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['rows'] = 25

    def save(self, *args, **kwargs):
        instance = super(SnippetForm, self).save(*args, **kwargs)

        original_snippet_pos_set = SnippetPos.objects.filter(snippet=instance)
        if len(original_snippet_pos_set) == 1:
            original_snippet_pos_set[0].snippet = None
            original_snippet_pos_set[0].save()

        position = self.clean().get('position', '')
        snippet_pos_set = SnippetPos.objects.filter(slug=position)
        if len(snippet_pos_set) == 1:
            snippet_pos_set[0].snippet = instance
            snippet_pos_set[0].save()

        return instance

    class Meta:
        model = Snippet
        fields = ['subject', 'content', 'position']
