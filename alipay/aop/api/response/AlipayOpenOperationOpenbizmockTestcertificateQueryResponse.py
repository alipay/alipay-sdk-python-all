#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenOperationOpenbizmockTestcertificateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenOperationOpenbizmockTestcertificateQueryResponse, self).__init__()
        self._result = None
        self._result_openid = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def result_openid(self):
        return self._result_openid

    @result_openid.setter
    def result_openid(self, value):
        self._result_openid = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenOperationOpenbizmockTestcertificateQueryResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
        if 'result_openid' in response:
            self.result_openid = response['result_openid']
