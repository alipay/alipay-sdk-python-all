#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsFreightflowTradereconApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsFreightflowTradereconApplyResponse, self).__init__()
        self._download_url = None
        self._result_date = None

    @property
    def download_url(self):
        return self._download_url

    @download_url.setter
    def download_url(self, value):
        self._download_url = value
    @property
    def result_date(self):
        return self._result_date

    @result_date.setter
    def result_date(self, value):
        self._result_date = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsFreightflowTradereconApplyResponse, self).parse_response_content(response_content)
        if 'download_url' in response:
            self.download_url = response['download_url']
        if 'result_date' in response:
            self.result_date = response['result_date']
