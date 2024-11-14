
from django.shortcuts import render, redirect
from .models import Question, Response, CreditScore


def questions_view(request):
    questions = Question.objects.all()
    return render(request, 'app/questions.html', {'questions': questions})


def submit_answers(request):
    if request.method == 'POST':
        user_id = request.user.id
        total_score = 0

        
        Response.objects.filter(user_id=user_id).delete()

        for question in Question.objects.all():
            response = request.POST.get(f'response_{question.id}')
            if response:
                score_mapping = {
                    'A': question.score_a,
                    'B': question.score_b,
                    'C': question.score_c,
                    'D': question.score_d
                }
                total_score += score_mapping[response]
                Response.objects.create(
                    user_id=user_id,
                    question=question,
                    selected_option=response
                )

        # Save the total score in the CreditScore model
        CreditScore.objects.create(user_id=user_id, score=total_score)

        return redirect('results')


def results_view(request):
    user_id = request.user.id
    responses = Response.objects.filter(user_id=user_id)
    total_score = sum([getattr(response.question, f"score_{response.selected_option.lower()}") for response in responses])
    return render(request, 'app/results.html', {'score': total_score})
