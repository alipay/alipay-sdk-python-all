#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportVehicleownerTransdataSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportVehicleownerTransdataSyncResponse, self).__init__()
        self._excute_lines = None
        self._result = None

    @property
    def excute_lines(self):
        return self._excute_lines

    @excute_lines.setter
    def excute_lines(self, value):
        self._excute_lines = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportVehicleownerTransdataSyncResponse, self).parse_response_content(response_content)
        if 'excute_lines' in response:
            self.excute_lines = response['excute_lines']
        if 'result' in response:
            self.result = response['result']
