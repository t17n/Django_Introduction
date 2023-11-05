from django import forms

class HelloForm(forms.Form):
    data=[
        ('one', 'item 1'),
        ('two', 'item 2'),
        ('three', 'item 3'),
        ('four', 'item 4'),
        ('five', 'item 5'),
    ]
    choice = forms.MultipleChoiceField(label='radio', choices=data, widget=forms.SelectMultiple(attrs={'size': 6, 'class':'form-select'}))

    '''
    # 選択リスト
    data=[
        ('one', 'item 1'),
        ('two', 'item 2'),
        ('three', 'item 3'),
        ('four', 'item 4'),
        ('five', 'item 5'),
    ]
    choice = forms.ChoiceField(label='radio', choices=data, widget=forms.Select(attrs={'size': 5, 'class':'form-select'}))

    # ラジオボタン
    data=[
        ('one', 'radio 1'),
        ('two', 'radio 2'),
        ('three', 'radio 3')
    ]
    choice = forms.ChoiceField(label='radio', choices=data, widget=forms.RadioSelect())

    # プルダウン
    data=[
        ('one', 'item 1'), 
        ('two', 'item 2'), 
        ('three', 'item 3')
    ]
    choice = forms.ChoiceField(label='Choice', choices=data)
    
    # チェックボックス
    check = forms.NullBooleanField(label='Check')
    '''