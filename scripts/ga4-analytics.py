#!/usr/bin/env python3
"""GA4 Analytics overview for Mission Control dashboard."""
import json
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, DateRange, Metric, Dimension
from google.oauth2 import service_account

PROPERTY = 'properties/286245028'
CREDS_PATH = '/home/jonny/.openclaw/workspace/credentials/ga4-service-account.json'

def get_client():
    creds = service_account.Credentials.from_service_account_file(
        CREDS_PATH, scopes=['https://www.googleapis.com/auth/analytics.readonly']
    )
    return BetaAnalyticsDataClient(credentials=creds)

def run(client, dims, mets, start='7daysAgo'):
    r = client.run_report(RunReportRequest(
        property=PROPERTY,
        date_ranges=[DateRange(start_date=start, end_date='today')],
        dimensions=[Dimension(name=d) for d in dims],
        metrics=[Metric(name=m) for m in mets],
        limit=50,
    ))
    return [{'dimensions': [v.value for v in row.dimension_values],
             'metrics': [v.value for v in row.metric_values]} for row in r.rows]

def main():
    c = get_client()

    # 7-day daily overview
    daily = run(c, ['date'], ['sessions', 'totalUsers', 'newUsers', 'screenPageViews', 'averageSessionDuration', 'conversions'])

    # 30-day daily (for trend)
    monthly = run(c, ['date'], ['sessions', 'totalUsers'], start='30daysAgo')

    # Channel breakdown (7 days)
    channels = run(c, ['sessionDefaultChannelGroup'], ['sessions', 'totalUsers', 'newUsers', 'screenPageViews', 'conversions'])

    # Top pages (7 days)
    pages = run(c, ['pagePath'], ['screenPageViews', 'sessions', 'totalUsers'])

    # Device category (7 days)
    devices = run(c, ['deviceCategory'], ['sessions', 'totalUsers'])

    # Country (7 days)
    countries = run(c, ['country'], ['sessions', 'totalUsers'])

    # 7-day totals
    totals = run(c, [], ['sessions', 'totalUsers', 'newUsers', 'screenPageViews', 'averageSessionDuration', 'conversions'])

    # 30-day totals (for comparison)
    totals_30d = run(c, [], ['sessions', 'totalUsers', 'newUsers', 'screenPageViews'], start='30daysAgo')

    print(json.dumps({
        'daily': daily,
        'monthly': monthly,
        'channels': channels,
        'pages': pages,
        'devices': devices,
        'countries': countries,
        'totals': totals,
        'totals30d': totals_30d,
    }))

if __name__ == '__main__':
    main()
