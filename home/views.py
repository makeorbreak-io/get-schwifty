from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from home.forms import q1Form, q2Form, q3Form, q4Form, q5Form, q6Form, q7Form, q8Form, q9Form, q10Form, q11Form, q12Form, q13Form, q14Form

import pickle
from sklearn import tree
import numpy as np

from geopy.geocoders import Nominatim
geolocator = Nominatim()


# Create your views here.

class HomeView(TemplateView):
	template_name = 'home/home.html'
	template_name2 = 'home/mapa.html'
	cityArray=[]

	def get(self, request):

		mapDisplay="display:none;"

		form = q1Form()
		form2 = q2Form()
		form3 = q3Form()
		form4 = q4Form()
		form5 = q5Form()
		form6 = q6Form()
		form7 = q7Form()
		form8 = q8Form()
		form9 = q9Form()
		form10 = q10Form()
		form11 = q11Form()
		form12 = q12Form()
		form13 = q13Form()
		form14 = q14Form()
		cityArray=[]
		return render(request, self.template_name, {'form':form, 'form2':form2, 'form3':form3, 'form4':form4, 'form5':form5, 'form6':form6,'form7':form7,'form8':form8,'form9':form9,'form10':form10,'form11':form11,'form12':form12,'form13':form13,'form14':form14,'cityArray':cityArray, 'mapDisplay':mapDisplay})

	def post(self, request):
		form = q1Form(request.POST)
		form2 = q2Form(request.POST)
		form3 = q3Form(request.POST)
		form4 = q4Form(request.POST)
		form5 = q5Form(request.POST)
		form6 = q6Form(request.POST)
		form7 = q7Form(request.POST)
		form8 = q8Form(request.POST)
		form9 = q9Form(request.POST)
		form10 = q10Form(request.POST)
		form11 = q11Form(request.POST)
		form12 = q12Form(request.POST)
		form13 = q13Form(request.POST)
		form14 = q14Form(request.POST)
		q1=''
		q2=''
		q3 = ''
		q4 = ''
		q5 = ''
		q6 = ''
		q7 = ''
		q8 = ''
		q9 = ''
		q10 = ''
		q11 = ''
		q12 = ''
		q13 = ''
		q14 = ''
		if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid() and form6.is_valid() and form7.is_valid() and form8.is_valid() and form9.is_valid() and form10.is_valid() and form11.is_valid() and form12.is_valid() and form13.is_valid() and form14.is_valid():
			q1 = form.cleaned_data.get('q1')
			q2 = form2.cleaned_data.get('q2')
			q3 = form3.cleaned_data.get('q3')
			q4 = form4.cleaned_data.get('q4')
			q5 = form5.cleaned_data.get('q5')
			q6 = form6.cleaned_data.get('q6')
			q7 = form7.cleaned_data.get('q7')
			q8 = form8.cleaned_data.get('q8')
			q9 = form9.cleaned_data.get('q9')
			q10 = form10.cleaned_data.get('q10')
			q11 = form11.cleaned_data.get('q11')
			q12 = form12.cleaned_data.get('q12')
			q13 = form13.cleaned_data.get('q13')
			q14 = form14.cleaned_data.get('q14')

			answers = [q1, q2, q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14]

			# filename = 'answers.sav'
			# pickle.dump(answers, open(filename, 'wb'))

			def convertList(index, size):
				temp=[2]*size
				for i in range(1,size+1):
					if str(i) in answers[5]:
						temp[i-1]=1;
				return temp

			def unwrap(answers):
				output=[]
				output.extend(list(map(int,answers[0:5])))
				output.extend(convertList(5,12))
				output.extend(convertList(6,8))
				output.extend(convertList(7,5))
				output.append(int(answers[8]))
				output.extend(convertList(9,11))
				output.append(int(answers[10]))
				output.append(int(answers[11]))
				output.extend(convertList(12,5))
				output.append(int(answers[13]))
				return output

			out_ex=unwrap(answers)
			out_ex = np.array(out_ex)

			names = open('target_names.csv')
			target_names=[]
			for line in names:
				line = line.strip()
				line = line.split(';')[:]
				target_names.append(line)

			names.close()
			target_names=target_names[1:]

			nova_target_names=[]
			for target in target_names:
				target = target[0] + ' ' + target[1]
				nova_target_names.append(target)

			###############################################

			filename = 'finalized_model.sav'


			loaded_model = pickle.load(open(filename, 'rb'))

			cityArray=[]

			for index in range(0,10):
				result = int(loaded_model[index].predict([out_ex]))
				
				destino = nova_target_names[result]

				nick = destino[0:3]

				locTmp = geolocator.geocode(destino)
				tempCity=Destino(nick,destino,locTmp.latitude,locTmp.longitude)
				if tempCity not in cityArray :
					cityArray.append([repr(tempCity.name),tempCity.lat,tempCity.lng])

			
			mapDisplay="""display:block;" onload="$('html, body').animate({
    scrollTop: $('#map').offset().top}, 1000);"""

		args = {'form':form, 'form2':form2, 'form3':form3,'form4':form4, 'form5':form5,'form6':form6,'form7':form7,'form8':form8,'form9':form9,'form10':form10,'form11':form11,'form12':form12,'form13':form13,'form14':form14,'q1':q1, 'q2':q2, 'q3':q3, 'q4':q4, 'q5':q5, 'q6':q6, 'q7':q7, 'q8':q8, 'q9':q9, 'q10':q10, 'q11':q11, 'q12':q12, 'q13':q13, 'q14':q14, 'cityArray':cityArray, 'destino':destino, 'mapDisplay':mapDisplay}
		return render(request, self.template_name2, args)


class Destino():
	def __init__(self, key, name, lat, lng):
		self.key  = key
		self.name = name
		self.lat  = lat
		self.lng  = lng

class Train(TemplateView):
	"""docstring for ClassName"""
	template_name3='home/train.html'

	def get(self, request):
		
		form = q1Form()
		form2 = q2Form()
		form3 = q3Form()
		form4 = q4Form()
		form5 = q5Form()
		form6 = q6Form()
		form7 = q7Form()
		form8 = q8Form()
		form9 = q9Form()
		form10 = q10Form()
		form11 = q11Form()
		form12 = q12Form()
		form13 = q13Form()
		form14 = q14Form()
		cityArray=[]
		return render(request, self.template_name3, {'form':form, 'form2':form2, 'form3':form3, 'form4':form4, 'form5':form5, 'form6':form6,'form7':form7,'form8':form8,'form9':form9,'form10':form10,'form11':form11,'form12':form12,'form13':form13,'form14':form14})