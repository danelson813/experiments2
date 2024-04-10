from helpers.selenium_template import get_soup
import pandas as pd

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
filename = "data/text_html.txt"

soup = get_soup(url, True, filename)
if soup:
    title = soup.select_one('head title').text.strip()
    print(f'title is: {title}')
else:
    print('there is a problem')

# parse the soup
movies = soup.select('li.ipc-metadata-list-summary-item')

results = []
for movie in movies:
    try:
        title = movie.select_one('h3').text.replace(',', '')
    except:
        title = 'unkown'
    try:
        year = movie.select_one('span.sc-b0691f29-8.ilsLEX.cli-title-metadata-item').text
    except:
        year = 'unknown'
    try:
        running_time = movie.select('span.sc-b0691f29-8.ilsLEX.cli-title-metadata-item')[1].text
    except:
        running_time = "unknown"
    try:
        rating = movie.select('span.sc-b0691f29-8.ilsLEX.cli-title-metadata-item')[2].text
    except:
        rating = 'unknown'
    try:
        star_rating = movie.select_one('span.ipc-rating-star')['aria-label']
    except:
        star_rating = "unknown"

    result = {
        'title': title,
        'year': year,
        'running_time': running_time,
        'rating': rating,
        'star_rating': star_rating
    }
    results.append(result)

df = pd.DataFrame(results)
df.to_csv('data/results.csv', index=False)