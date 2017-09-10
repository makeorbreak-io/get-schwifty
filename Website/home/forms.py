from django import forms

class q1Form(forms.Form):
	CHOICES = ((1,'North-American'),
		(2,'Latin-American'),
		(3,'European'),
		(4,'Arabic'),
		(5, 'Asian'),
		(6, 'African'))
	q1 = forms.ChoiceField(choices=CHOICES, label = '', widget=forms.Select(attrs = {'class':'form-control'}))


class q2Form(forms.Form):
	CHOICES = ((1,'< 1 week'),
		(2,'1-2 weeks'),
		(3,'> 2 weeks'),)
	q2 = forms.ChoiceField(choices=CHOICES, label = '', widget=forms.Select(attrs = {'class':'form-control'}))

class q3Form(forms.Form):
	CHOICES = ((1,'Plane'),
		(2,'Car'),
		(3,'Train'),
		(4,'Boat'))
	q3 = forms.ChoiceField(choices=CHOICES, label = '', widget=forms.Select(attrs = {'class':'form-control'}))

class q4Form(forms.Form):
	CHOICES = ((1,'Socialism (Democracy)'),
		(2,'Communism (Democracy)'),
		(3,'Social-Democrat (Democracy)'),
		(4,'Any Democracy'),
		(5, 'Dictatorship'),
		(6, 'War Zone'),
		(7, 'Monarchy'))
	q4 = forms.ChoiceField(choices=CHOICES, label = '', widget=forms.Select(attrs = {'class':'form-control'}))

class q5Form(forms.Form):
	CHOICES = ((1,'Catholicism'),
		(2,'Protestant'),
		(3,'Judaism'),
		(4, 'Islam'),
		(5, 'Hinduism'),
		(6, 'Buddhism'),
		(7, 'Pagan'),
		(8, 'Indifferent'))
	q5 = forms.ChoiceField(choices=CHOICES, label = '', widget=forms.Select(attrs = {'class':'form-control'}))

class q6Form(forms.Form):
	CHOICES = ((1,'City Sightseeing'),
		(2, 'Shopping'),
		(3, 'Hiking'),
		(4, 'Sport events'),
		(5, 'Historic exploration'),
		(6, 'Nature Photography'),
		(7, 'City Photography'),
		(8, 'Clubbing'),
		(9,'Gambling'),
		(10, 'Art gallery visiting'),
		(11, 'Beach'),
		(12, 'Safari'))
	q6 = forms.MultipleChoiceField(choices=CHOICES, label = '', widget=forms.CheckboxSelectMultiple(attrs = {'class':'form-group'}))

class q7Form(forms.Form):
	CHOICES = ((1,'Legal Marijuana'),
		(2, 'Free entrance at Museums'),
		(3, 'Amusement parks'),
		(4, 'LGBT friendly'),
		(5, 'Green spaces'),
		(6, 'Art and Architecture'),
		(7, 'Agriculture'),
		(8, 'Casinos'))

	q7 = forms.MultipleChoiceField(choices=CHOICES, label = '', widget=forms.CheckboxSelectMultiple(attrs = {'class':'form-group'}))

class q8Form(forms.Form):
	CHOICES = ((1,'Hostel'),
		(2, 'Camping'),
		(3, 'Hotel'),
		(4, 'CouchSurfing'),
		(5, 'Airbnb/Renting'))

	q8 = forms.MultipleChoiceField(choices=CHOICES, label = '', widget=forms.CheckboxSelectMultiple(attrs = {'class':'form-group'}))

class q9Form(forms.Form):
	CHOICES = ((1,'Low'),
		(2,'Medium'),
		(3,'High'))

	q9 = forms.ChoiceField(choices=CHOICES, label = '', widget=forms.Select(attrs = {'class':'form-control'}))

class q10Form(forms.Form):
	CHOICES = ((1,'English friendly'),
		(2, 'Portuguese'),
		(3, 'Spanish'),
		(4, 'French'),
		(5, 'German'),
		(6, 'Mandarin'),
		(7, 'Italian'),
		(8, 'Russian'),
		(9, 'Danish'),
		(10, 'Arabic'),
		(11, 'Japanese'))

	q10 = forms.MultipleChoiceField(choices=CHOICES, label = '', widget=forms.CheckboxSelectMultiple(attrs = {'class':'form-group'}))

class q11Form(forms.Form):
	CHOICES = ((1,'Mediterranean food'),
		(2, 'Spicy food'),
		(3, 'Fast food'),
		(4, 'Umami flavoured'),
		(5, 'Tropical food'),
		(6, 'Fish'))

	q11 = forms.ChoiceField(choices=CHOICES, label = '', widget=forms.Select(attrs = {'class':'form-control'}))

class q12Form(forms.Form):
	CHOICES = ((1,'< 4.5'),
		(2, '4.5 - 5.5'),
		(3, '5.5 - 6.5'),
		(4, '> 6.5'))

	q12 = forms.ChoiceField(choices=CHOICES, label = '', widget=forms.Select(attrs = {'class':'form-control'}))

class q13Form(forms.Form):
	CHOICES = ((1,'Metro'),
		(2, 'Train'),
		(3, 'Uber'),
		(4, 'Bike'),
		(5, 'Walk'))

	q13 = forms.MultipleChoiceField(choices=CHOICES, label = '', widget=forms.CheckboxSelectMultiple(attrs = {'class':'form-group'}))

class q14Form(forms.Form):
	CHOICES = ((1,'River'),
		(2,'Mountains'),
		(3,'WaterFalls'),
		(4, 'Volcanoes'),
		(5, 'Desert'),
		(6, 'Plain'))

	q14 = forms.ChoiceField(choices=CHOICES, label = '', widget=forms.Select(attrs = {'class':'form-control'}))