#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingDataMemberReportQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingDataMemberReportQueryResponse, self).__init__()
        self._report_data = None

    @property
    def report_data(self):
        return self._report_data

    @report_data.setter
    def report_data(self, value):
        self._report_data = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingDataMemberReportQueryResponse, self).parse_response_content(response_content)
        if 'report_data' in response:
            self.report_data = response['report_data']
