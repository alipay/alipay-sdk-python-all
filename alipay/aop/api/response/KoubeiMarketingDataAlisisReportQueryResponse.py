#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AlisisReportRow import AlisisReportRow


class KoubeiMarketingDataAlisisReportQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingDataAlisisReportQueryResponse, self).__init__()
        self._report_data = None

    @property
    def report_data(self):
        return self._report_data

    @report_data.setter
    def report_data(self, value):
        if isinstance(value, list):
            self._report_data = list()
            for i in value:
                if isinstance(i, AlisisReportRow):
                    self._report_data.append(i)
                else:
                    self._report_data.append(AlisisReportRow.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingDataAlisisReportQueryResponse, self).parse_response_content(response_content)
        if 'report_data' in response:
            self.report_data = response['report_data']
