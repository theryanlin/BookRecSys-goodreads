from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from .models import Book, Rank, WishList, Rating, Genre


genres = ["humor and comedy", "gay and lesbian", "cookbooks", "sports", "music", "business", "christian",
              "manga", "poetry", "graphic novels", "comics", "irituality", "self help", "art", "travel",
              "psychology", "religion", "memoir", "philosophy", "biography", "horror", "nonfiction",
              "paranormal", "chick lit", "crime", "history", "suspense", "thriller", "classics", "science",
              "mystery", "young adult", "romance", "fantasy", "contemporary", "fiction"]

most_popular = [1, 2, 4, 3, 5, 17, 20, 18, 23, 7, 24, 25, 21, 27, 13, 8, 16, 14, 28, 9]


def index(request, username):
    recommendation = Rank.objects.filter(user_id=username)[0]
    rec_list = recommendation.book_id
    rec_list = rec_list.split("   ")
    rec_list = [i.replace(" ", "") for i in rec_list]
    user_id = username
    read = Rating.objects.filter(user_id=user_id).order_by("rating")
    avg_rating = round(sum(i.rating for i in read) / len(read), 2)
    wish = WishList.objects.filter(user_id=user_id)
    book_list = []
    read_list = []
    wish_list = []
    favorite_tags = []

    # get read book list
    for i in range(len(read)):
        book_id = read[i].book_id
        book = Book.objects.get(_id=int(book_id))
        read_list.append(book)

    # get wish list
    for j in range(len(wish)):
        book_id = wish[j].book_id
        book = Book.objects.get(_id=int(book_id))
        wish_list.append(book)

    # get recommendation list
    for k in range(len(rec_list)):
        if len(read_list) < 10:
            rec_list = most_popular
        book = Book.objects.get(_id=int(rec_list[k]))
        if book not in read_list:
            goodread_id = book.book_id
            tags = Genre.objects.filter(goodreads_book_id=goodread_id)
            tags = [tag.genre for tag in tags]
            tag_list = []
            t = 0
            for i in range(len(genres)):
                if genres[i] in tags:
                    tag_list.append(genres[i])
                    t += 1
                if t == 3:
                    break
            book_list.append((book, tag_list))

    # get favarite tag list
    for q in range(len(read_list)):
        book_id = read_list[q].book_id
        genre_list = Genre.objects.filter(goodreads_book_id=book_id)
        genre_list = [genre.genre for genre in genre_list]
        for i in range(len(genres)):
            if genres[i] in genre_list and genres[i] not in favorite_tags:
                favorite_tags.append(genres[i])

    return render(request, 'index.html', {"username": user_id, "avg_rating": avg_rating, "rec_num": len(book_list),
                                          "read_num": len(read_list), "read_list": read_list[:5], "wish_list": wish_list[:5],
                                          "book_list": book_list, "favorite_tags": favorite_tags[:8]})


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if username == password:
            return HttpResponseRedirect('/index/{0}'.format(username))
        else:
            return render(request, "login.html")


class LogoutView(View):
    def get(self, request):
        return render(request, "login.html")