#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsClaimReport import InsClaimReport


class AlipayInsUnderwriteClaimReportQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsUnderwriteClaimReportQueryResponse, self).__init__()
        self._reports = None

    @property
    def reports(self):
        return self._reports

    @reports.setter
    def reports(self, value):
        if isinstance(value, list):
            self._reports = list()
            for i in value:
                if isinstance(i, InsClaimReport):
                    self._reports.append(i)
                else:
                    self._reports.append(InsClaimReport.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayInsUnderwriteClaimReportQueryResponse, self).parse_response_content(response_content)
        if 'reports' in response:
            self.reports = response['reports']
