#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MyObjectDdd import MyObjectDdd


class AlipayOpenEchoSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenEchoSendResponse, self).__init__()
        self._obj = None
        self._out_a = None
        self._out_b = None
        self._out_c = None
        self._out_d = None
        self._word = None

    @property
    def obj(self):
        return self._obj

    @obj.setter
    def obj(self, value):
        if isinstance(value, MyObjectDdd):
            self._obj = value
        else:
            self._obj = MyObjectDdd.from_alipay_dict(value)
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
    def out_c(self):
        return self._out_c

    @out_c.setter
    def out_c(self, value):
        self._out_c = value
    @property
    def out_d(self):
        return self._out_d

    @out_d.setter
    def out_d(self, value):
        self._out_d = value
    @property
    def word(self):
        return self._word

    @word.setter
    def word(self, value):
        self._word = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenEchoSendResponse, self).parse_response_content(response_content)
        if 'obj' in response:
            self.obj = response['obj']
        if 'out_a' in response:
            self.out_a = response['out_a']
        if 'out_b' in response:
            self.out_b = response['out_b']
        if 'out_c' in response:
            self.out_c = response['out_c']
        if 'out_d' in response:
            self.out_d = response['out_d']
        if 'word' in response:
            self.word = response['word']
