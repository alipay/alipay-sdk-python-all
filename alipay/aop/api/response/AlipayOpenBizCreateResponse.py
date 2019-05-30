#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GavintestNewonline import GavintestNewonline


class AlipayOpenBizCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenBizCreateResponse, self).__init__()
        self._a = None
        self._b = None
        self._c = None

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value
    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if isinstance(value, GavintestNewonline):
            self._b = value
        else:
            self._b = GavintestNewonline.from_alipay_dict(value)
    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        self._c = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenBizCreateResponse, self).parse_response_content(response_content)
        if 'a' in response:
            self.a = response['a']
        if 'b' in response:
            self.b = response['b']
        if 'c' in response:
            self.c = response['c']
