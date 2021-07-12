from flask import Flask, request, redirect
from shorten import UrlShortener
from utils import write_to_json, read_json
from pathlib import Path


app = Flask(__name__)
sh = UrlShortener()
domain = 'http://localhost:5000/'
start_id = 1000000000
url_data_file = 'data.json'
if Path(url_data_file).exists():
    url_data = read_json(url_data_file)
else:
    url_data = dict()


@app.route("/", methods=['GET', 'POST'])
def get_long_url():
    long_url = request.args.get("long_url", "")
    if long_url:
        if long_url in url_data:
            url_id = url_data[long_url][0]
            short_url = url_data[long_url][1]
        else:
            url_id = get_id()
            short_url = sh.shorten(url_id)
            short_url = domain + short_url
            url_data[long_url] = [url_id, short_url]
            write_to_json(url_data, url_data_file)
    else:
        short_url = ''
        url_id = ''

    return (
        """<form action="" method="get">
                Long URL: <input type="text" name="long_url">
                <input type="submit" value="Shorten it!">
            </form>"""
        + "Short URL: "
        + short_url
        + "\nID: "
        + str(url_id)
    )


@app.route('/<string:short_url>')
def url_redirect(short_url):
    actual_url = None
    url_id = sh.un_shorten(short_url)
    short_url = domain + short_url
    data_to_check = [url_id, short_url]
    url_data_from_file = read_json(url_data_file)
    for data in url_data_from_file:
        if data_to_check == url_data_from_file[data]:
            actual_url = data
            break

    if actual_url:
        return redirect(actual_url)

    return '<h2>No such URL found</h2>'


def get_id():
    if Path(url_data_file).exists():
        url_data_from_file = read_json(url_data_file)
    else:
        url_data_from_file = {}

    end_id = start_id + len(url_data_from_file)

    return end_id


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)