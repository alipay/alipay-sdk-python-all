#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.JinyoutestopenidThree import JinyoutestopenidThree


class ZhimaCreditEpMinitipsdeliveryQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpMinitipsdeliveryQueryResponse, self).__init__()
        self._c = None
        self._jkjp = None

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        self._c = value
    @property
    def jkjp(self):
        return self._jkjp

    @jkjp.setter
    def jkjp(self, value):
        if isinstance(value, JinyoutestopenidThree):
            self._jkjp = value
        else:
            self._jkjp = JinyoutestopenidThree.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpMinitipsdeliveryQueryResponse, self).parse_response_content(response_content)
        if 'c' in response:
            self.c = response['c']
        if 'jkjp' in response:
            self.jkjp = response['jkjp']
