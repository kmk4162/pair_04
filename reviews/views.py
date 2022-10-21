from django.shortcuts import render, redirect
from .models import Comment, Review
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

# 글 및 댓글 보기 함수
def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    comment_form = CommentForm()
    comments = review.comment_set.all()
    context = {
        'review' : review,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'reviews/detail.html', context)

# 댓글 작성 함수
@login_required
def create_comment(request, review_pk):
    # 무슨 글인지 가져오고
    review = Review.objects.get(pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.save()
    return redirect('reviews:detail', review_pk)

# 댓글 삭제 함수
@login_required
def delete_comment(request, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if comment.user == request.user:
        comment.delete()
    return redirect('reviews:detail', review_pk) 