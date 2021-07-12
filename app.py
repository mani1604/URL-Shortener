from flask import Flask, request, redirect
from shorten import UrlShortener


app = Flask(__name__)
url_data = dict()
sh = UrlShortener()
domain = 'http://localhost:8080/'
start_id = 1000000000


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
    for data in url_data:
        print(data_to_check)
        print(url_data[data])
        if data_to_check == url_data[data]:
            actual_url = data
            break

    if actual_url:
        return redirect(actual_url)

    return '<h2>No such URL found</h2>'


def get_id():
    end_id = start_id + len(url_data)

    return end_id


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)