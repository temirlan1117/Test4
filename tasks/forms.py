from django import forms

from tasks.models import Category, Task


class SearchForm(forms.Form):
    search = forms.CharField(required=False, max_length=100, widget=forms.TextInput(
        attrs={
        'placeholder': "Введите текст для поиска",
        'class': 'form-control'}))

    task = forms.ModelMultipleChoiceField(required=False,
                                    queryset=Task.objects.all(),
                                    widget=forms.CheckboxSelectMultiple,)
    orderings = (
        ("category", "По категориям"),
        ("-category", "По категориям в обратном порядке"),
    )
    ordering = forms.ChoiceField(
        required=False,
        choices=orderings,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class TaskForm(forms.Form):
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        description = cleaned_data.get('description')


        if title and description and title.lower == description.lower():
            raise forms.ValidationError('Заголовок и контент не должны совпадать')
        else:
            return cleaned_data

class TaskForm2(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category']
