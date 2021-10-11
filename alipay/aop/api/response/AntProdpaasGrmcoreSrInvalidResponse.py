#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntProdpaasGrmcoreSrInvalidResponse(AlipayResponse):

    def __init__(self):
        super(AntProdpaasGrmcoreSrInvalidResponse, self).__init__()
        self._flag = None
        self._suppliers = None

    @property
    def flag(self):
        return self._flag

    @flag.setter
    def flag(self, value):
        self._flag = value
    @property
    def suppliers(self):
        return self._suppliers

    @suppliers.setter
    def suppliers(self, value):
        if isinstance(value, list):
            self._suppliers = list()
            for i in value:
                self._suppliers.append(i)

    def parse_response_content(self, response_content):
        response = super(AntProdpaasGrmcoreSrInvalidResponse, self).parse_response_content(response_content)
        if 'flag' in response:
            self.flag = response['flag']
        if 'suppliers' in response:
            self.suppliers = response['suppliers']
