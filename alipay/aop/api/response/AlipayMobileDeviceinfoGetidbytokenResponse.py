#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMobileDeviceinfoGetidbytokenResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMobileDeviceinfoGetidbytokenResponse, self).__init__()
        self._apdid = None
        self._operateresult = None
        self._umid = None

    @property
    def apdid(self):
        return self._apdid

    @apdid.setter
    def apdid(self, value):
        self._apdid = value
    @property
    def operateresult(self):
        return self._operateresult

    @operateresult.setter
    def operateresult(self, value):
        self._operateresult = value
    @property
    def umid(self):
        return self._umid

    @umid.setter
    def umid(self, value):
        self._umid = value

    def parse_response_content(self, response_content):
        response = super(AlipayMobileDeviceinfoGetidbytokenResponse, self).parse_response_content(response_content)
        if 'apdid' in response:
            self.apdid = response['apdid']
        if 'operateresult' in response:
            self.operateresult = response['operateresult']
        if 'umid' in response:
            self.umid = response['umid']
