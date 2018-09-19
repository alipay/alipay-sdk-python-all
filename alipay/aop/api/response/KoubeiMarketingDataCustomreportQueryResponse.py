#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ReportDataItem import ReportDataItem


class KoubeiMarketingDataCustomreportQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingDataCustomreportQueryResponse, self).__init__()
        self._count = None
        self._report_data = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def report_data(self):
        return self._report_data

    @report_data.setter
    def report_data(self, value):
        if isinstance(value, list):
            self._report_data = list()
            for i in value:
                if isinstance(i, ReportDataItem):
                    self._report_data.append(i)
                else:
                    self._report_data.append(ReportDataItem.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingDataCustomreportQueryResponse, self).parse_response_content(response_content)
        if 'count' in response:
            self.count = response['count']
        if 'report_data' in response:
            self.report_data = response['report_data']
