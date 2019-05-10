import mechanicalsoup

BASE_URL = 'https://ci.chromium.org'
IMPORT_URL = BASE_URL + '/p/infra/builders/luci.infra.cron/wpt-importer?limit=200'
EXPORT_URL = BASE_URL + '/p/infra/builders/luci.infra.cron/wpt-exporter?limit=200'


def scrape_buildbot(url):
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(url)
    rows = browser.get_current_page().select('div.main table.info tr')

    builds = []
    recent_failures = 0
    last_success = None
    # Skip the table header.
    for row in rows[1:]:
        columns = row.select('td')

        time = columns[0].get_text().strip()
        duration = columns[1].get_text().strip()
        # revision
        result = columns[3].get_text().strip()
        build = BASE_URL + columns[4].a['href']
        info = columns[5].get_text().strip()
        if result == 'Success':
            last_success = last_success or time
        else:
            if not last_success:
                recent_failures += 1

        builds.append({
            'time': time,
            'duration': duration,
            'result': result,
            'build': build,
            'info': info
        })

    result = {
        'last_success': last_success,
        'recent_failures': recent_failures,
        'builds': builds,
    }

    return result


def import_status():
    return scrape_buildbot(IMPORT_URL)


def export_status():
    return scrape_buildbot(EXPORT_URL)
