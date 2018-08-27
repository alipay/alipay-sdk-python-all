#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZolozAuthenticationCustomerFacemanageCreateResponse(AlipayResponse):

    def __init__(self):
        super(ZolozAuthenticationCustomerFacemanageCreateResponse, self).__init__()
        self._result = None
        self._retcode = None
        self._retmessage = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def retcode(self):
        return self._retcode

    @retcode.setter
    def retcode(self, value):
        self._retcode = value
    @property
    def retmessage(self):
        return self._retmessage

    @retmessage.setter
    def retmessage(self, value):
        self._retmessage = value

    def parse_response_content(self, response_content):
        response = super(ZolozAuthenticationCustomerFacemanageCreateResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
        if 'retcode' in response:
            self.retcode = response['retcode']
        if 'retmessage' in response:
            self.retmessage = response['retmessage']
