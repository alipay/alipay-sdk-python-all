#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AlisisReport import AlisisReport


class KoubeiMarketingDataAlisisReportBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingDataAlisisReportBatchqueryResponse, self).__init__()
        self._report_list = None
        self._total_count = None

    @property
    def report_list(self):
        return self._report_list

    @report_list.setter
    def report_list(self, value):
        if isinstance(value, list):
            self._report_list = list()
            for i in value:
                if isinstance(i, AlisisReport):
                    self._report_list.append(i)
                else:
                    self._report_list.append(AlisisReport.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingDataAlisisReportBatchqueryResponse, self).parse_response_content(response_content)
        if 'report_list' in response:
            self.report_list = response['report_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
