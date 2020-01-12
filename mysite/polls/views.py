from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import get_object_or_404
# from django.template import loader
from .models import Question,Choice
from django.urls import reverse
# Create your views here.
# 编写视图
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'







# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # template =loader.get_template('polls/index.html')
#     context ={'latest_question_list':latest_question_list,}
#     # return HttpResponse(template.render(context, request))
#     return render(request,'polls/index.html',context)

# def detail(request,question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request,'polls/detail.html',{'question':question})
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request,'polls/detail.html',{'question':question})
#
#
# def results(request,question_id):
#     response = "You're looking at the result of question %s"
#     return HttpResponse(response% question_id)

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{'question':question,'error_message':"You didn't select a _choice"})

    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
#
# def results(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request,'polls/results.html',{'question':question})

