#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskRiskscanSingleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskRiskscanSingleQueryResponse, self).__init__()
        self._scan_result_data = None

    @property
    def scan_result_data(self):
        return self._scan_result_data

    @scan_result_data.setter
    def scan_result_data(self, value):
        self._scan_result_data = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskRiskscanSingleQueryResponse, self).parse_response_content(response_content)
        if 'scan_result_data' in response:
            self.scan_result_data = response['scan_result_data']
