from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})

# created a function (def) called post_list that takes request 
# and return a function render that will render (put together) our template blog/post_list.html
