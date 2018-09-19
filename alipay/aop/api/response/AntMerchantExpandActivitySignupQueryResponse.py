#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandActivitySignupQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandActivitySignupQueryResponse, self).__init__()
        self._desc = None
        self._pid = None
        self._status = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandActivitySignupQueryResponse, self).parse_response_content(response_content)
        if 'desc' in response:
            self.desc = response['desc']
        if 'pid' in response:
            self.pid = response['pid']
        if 'status' in response:
            self.status = response['status']
