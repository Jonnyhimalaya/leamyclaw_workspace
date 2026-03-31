#!/usr/bin/env python3
"""GA4 Marketing data for Mission Control dashboard."""
import json
import sys
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    RunReportRequest, DateRange, Metric, Dimension, FilterExpression, Filter
)
from google.oauth2 import service_account

PROPERTY = 'properties/286245028'
CREDS_PATH = '/home/jonny/.openclaw/workspace/credentials/ga4-service-account.json'

def get_client():
    creds = service_account.Credentials.from_service_account_file(
        CREDS_PATH, scopes=['https://www.googleapis.com/auth/analytics.readonly']
    )
    return BetaAnalyticsDataClient(credentials=creds)

def run_report(client, dims, mets, start='7daysAgo', filt_field=None, filt_value=None):
    kwargs = dict(
        property=PROPERTY,
        date_ranges=[DateRange(start_date=start, end_date='today')],
        dimensions=[Dimension(name=d) for d in dims],
        metrics=[Metric(name=m) for m in mets],
        limit=50,
    )
    if filt_field and filt_value:
        kwargs['dimension_filter'] = FilterExpression(
            filter=Filter(
                field_name=filt_field,
                string_filter=Filter.StringFilter(
                    match_type=Filter.StringFilter.MatchType.CONTAINS,
                    value=filt_value
                )
            )
        )
    r = client.run_report(RunReportRequest(**kwargs))
    return [
        {'dimensions': [v.value for v in row.dimension_values],
         'metrics': [v.value for v in row.metric_values]}
        for row in r.rows
    ]

def main():
    client = get_client()

    # 1. Channel breakdown
    channels = run_report(client,
        ['sessionDefaultChannelGroup'],
        ['sessions', 'totalUsers', 'newUsers', 'screenPageViews', 'conversions'])

    # 2. Paid landing pages
    landings = run_report(client,
        ['landingPage', 'sessionDefaultChannelGroup'],
        ['sessions', 'totalUsers'])

    # 3. Daily paid breakdown
    daily = run_report(client,
        ['date', 'sessionDefaultChannelGroup'],
        ['sessions', 'totalUsers', 'conversions'])

    # 4. Revision pages
    revision = run_report(client,
        ['pagePath'],
        ['screenPageViews', 'sessions', 'totalUsers'],
        filt_field='pagePath', filt_value='revision')

    print(json.dumps({
        'channels': channels,
        'landings': landings,
        'daily': daily,
        'revision': revision,
    }))

if __name__ == '__main__':
    main()
