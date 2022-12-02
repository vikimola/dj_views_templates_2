from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello(request):
    num_visits = request.session.get("num_visits", 0) + 1
    request.session["num_visits"] = num_visits
    resp = HttpResponse(f"Number of times visited: {num_visits}.")
    if num_visits > 2:
        del request.session["num_visits"]
    return resp


def cookie(request):
    cookie = request.COOKIES.get('c', None)
    resp = HttpResponse(f"Currently, the 'c' cookie values is '{cookie}'.")
    if cookie:
        resp.set_cookie("c", int(cookie) + 1)
    else:
        resp.set_cookie("c", 36)
    resp.set_cookie("cecil", 60, max_age=1000)
    return resp

    # template = "hw_sesh/cookie.html"
    # resp = render(request, template)
    # resp.set_cookie(key="c", value="36", max_age=60)
    # return resp
