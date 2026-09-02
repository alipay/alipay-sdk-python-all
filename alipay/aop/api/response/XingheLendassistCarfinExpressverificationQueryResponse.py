#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class XingheLendassistCarfinExpressverificationQueryResponse(AlipayResponse):

    def __init__(self):
        super(XingheLendassistCarfinExpressverificationQueryResponse, self).__init__()
        self._completeness_check_result = None
        self._status = None

    @property
    def completeness_check_result(self):
        return self._completeness_check_result

    @completeness_check_result.setter
    def completeness_check_result(self, value):
        self._completeness_check_result = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(XingheLendassistCarfinExpressverificationQueryResponse, self).parse_response_content(response_content)
        if 'completeness_check_result' in response:
            self.completeness_check_result = response['completeness_check_result']
        if 'status' in response:
            self.status = response['status']
