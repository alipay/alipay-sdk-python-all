#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpReportQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpReportQueryResponse, self).__init__()
        self._report_url = None

    @property
    def report_url(self):
        return self._report_url

    @report_url.setter
    def report_url(self, value):
        self._report_url = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpReportQueryResponse, self).parse_response_content(response_content)
        if 'report_url' in response:
            self.report_url = response['report_url']
