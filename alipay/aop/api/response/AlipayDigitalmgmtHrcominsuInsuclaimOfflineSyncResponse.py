#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDigitalmgmtHrcominsuInsuclaimOfflineSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtHrcominsuInsuclaimOfflineSyncResponse, self).__init__()
        self._report_no_list = None

    @property
    def report_no_list(self):
        return self._report_no_list

    @report_no_list.setter
    def report_no_list(self, value):
        if isinstance(value, list):
            self._report_no_list = list()
            for i in value:
                self._report_no_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtHrcominsuInsuclaimOfflineSyncResponse, self).parse_response_content(response_content)
        if 'report_no_list' in response:
            self.report_no_list = response['report_no_list']
