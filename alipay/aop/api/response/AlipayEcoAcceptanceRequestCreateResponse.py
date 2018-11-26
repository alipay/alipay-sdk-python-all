#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoAcceptanceRequestCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoAcceptanceRequestCreateResponse, self).__init__()
        self._request_id = None
        self._total_results = None

    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def total_results(self):
        return self._total_results

    @total_results.setter
    def total_results(self, value):
        self._total_results = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoAcceptanceRequestCreateResponse, self).parse_response_content(response_content)
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'total_results' in response:
            self.total_results = response['total_results']
