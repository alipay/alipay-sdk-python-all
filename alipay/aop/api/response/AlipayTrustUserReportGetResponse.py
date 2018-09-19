#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTrustUserReportGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTrustUserReportGetResponse, self).__init__()
        self._report = None

    @property
    def report(self):
        return self._report

    @report.setter
    def report(self, value):
        self._report = value

    def parse_response_content(self, response_content):
        response = super(AlipayTrustUserReportGetResponse, self).parse_response_content(response_content)
        if 'report' in response:
            self.report = response['report']
