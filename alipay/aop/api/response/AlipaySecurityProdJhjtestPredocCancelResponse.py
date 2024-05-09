#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.JhjTestNew import JhjTestNew


class AlipaySecurityProdJhjtestPredocCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdJhjtestPredocCancelResponse, self).__init__()
        self._out_a = None
        self._out_b = None
        self._out_com = None

    @property
    def out_a(self):
        return self._out_a

    @out_a.setter
    def out_a(self, value):
        self._out_a = value
    @property
    def out_b(self):
        return self._out_b

    @out_b.setter
    def out_b(self, value):
        self._out_b = value
    @property
    def out_com(self):
        return self._out_com

    @out_com.setter
    def out_com(self, value):
        if isinstance(value, JhjTestNew):
            self._out_com = value
        else:
            self._out_com = JhjTestNew.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdJhjtestPredocCancelResponse, self).parse_response_content(response_content)
        if 'out_a' in response:
            self.out_a = response['out_a']
        if 'out_b' in response:
            self.out_b = response['out_b']
        if 'out_com' in response:
            self.out_com = response['out_com']
