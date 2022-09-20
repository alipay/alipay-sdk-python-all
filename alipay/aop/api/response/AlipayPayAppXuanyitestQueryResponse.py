#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.JinyouTestFive import JinyouTestFive


class AlipayPayAppXuanyitestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayAppXuanyitestQueryResponse, self).__init__()
        self._f_3_f = None
        self._r_1_openid = None
        self._r_1_y = None
        self._r_2_n = None

    @property
    def f_3_f(self):
        return self._f_3_f

    @f_3_f.setter
    def f_3_f(self, value):
        if isinstance(value, JinyouTestFive):
            self._f_3_f = value
        else:
            self._f_3_f = JinyouTestFive.from_alipay_dict(value)
    @property
    def r_1_openid(self):
        return self._r_1_openid

    @r_1_openid.setter
    def r_1_openid(self, value):
        self._r_1_openid = value
    @property
    def r_1_y(self):
        return self._r_1_y

    @r_1_y.setter
    def r_1_y(self, value):
        self._r_1_y = value
    @property
    def r_2_n(self):
        return self._r_2_n

    @r_2_n.setter
    def r_2_n(self, value):
        self._r_2_n = value

    def parse_response_content(self, response_content):
        response = super(AlipayPayAppXuanyitestQueryResponse, self).parse_response_content(response_content)
        if 'f_3_f' in response:
            self.f_3_f = response['f_3_f']
        if 'r_1_openid' in response:
            self.r_1_openid = response['r_1_openid']
        if 'r_1_y' in response:
            self.r_1_y = response['r_1_y']
        if 'r_2_n' in response:
            self.r_2_n = response['r_2_n']
