import requests
from django.shortcuts import render


def search_songs(request):
    if "query" in request.GET:
        query = request.GET.get("query")

        # Example API call to JioSaavn (replace with actual API endpoint)
        api_url = (
            f"https://jiosaavn-api-privatecvc2.vercel.app/search/songs?query={query}"
        )
        response = requests.get(api_url)

        if response.status_code == 200:
            song_data = response.json()
            # print(data)
            return render(
                request, "music/results.html", {"songs": song_data["data"]["results"]}
            )
        else:
            return render(
                request, "music/results.html", {"error": "API request failed"}
            )

    return render(request, "music/search.html")
