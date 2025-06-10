#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderCoilWorkreporturlQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderCoilWorkreporturlQueryResponse, self).__init__()
        self._report_date = None
        self._report_file_url = None

    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value
    @property
    def report_file_url(self):
        return self._report_file_url

    @report_file_url.setter
    def report_file_url(self, value):
        self._report_file_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderCoilWorkreporturlQueryResponse, self).parse_response_content(response_content)
        if 'report_date' in response:
            self.report_date = response['report_date']
        if 'report_file_url' in response:
            self.report_file_url = response['report_file_url']
