#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZolozAuthenticationCustomerFacemanageDeleteResponse(AlipayResponse):

    def __init__(self):
        super(ZolozAuthenticationCustomerFacemanageDeleteResponse, self).__init__()
        self._result = None
        self._retcode = None
        self._retcodesub = None
        self._retmessage = None
        self._retmessagesub = None

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
    def retcodesub(self):
        return self._retcodesub

    @retcodesub.setter
    def retcodesub(self, value):
        self._retcodesub = value
    @property
    def retmessage(self):
        return self._retmessage

    @retmessage.setter
    def retmessage(self, value):
        self._retmessage = value
    @property
    def retmessagesub(self):
        return self._retmessagesub

    @retmessagesub.setter
    def retmessagesub(self, value):
        self._retmessagesub = value

    def parse_response_content(self, response_content):
        response = super(ZolozAuthenticationCustomerFacemanageDeleteResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
        if 'retcode' in response:
            self.retcode = response['retcode']
        if 'retcodesub' in response:
            self.retcodesub = response['retcodesub']
        if 'retmessage' in response:
            self.retmessage = response['retmessage']
        if 'retmessagesub' in response:
            self.retmessagesub = response['retmessagesub']
