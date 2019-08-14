#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsAutoUserOilQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsAutoUserOilQueryResponse, self).__init__()
        self._accum_oil = None
        self._current_oil = None
        self._total_oil = None
        self._unpick_oil = None
        self._use_oil = None

    @property
    def accum_oil(self):
        return self._accum_oil

    @accum_oil.setter
    def accum_oil(self, value):
        self._accum_oil = value
    @property
    def current_oil(self):
        return self._current_oil

    @current_oil.setter
    def current_oil(self, value):
        self._current_oil = value
    @property
    def total_oil(self):
        return self._total_oil

    @total_oil.setter
    def total_oil(self, value):
        self._total_oil = value
    @property
    def unpick_oil(self):
        return self._unpick_oil

    @unpick_oil.setter
    def unpick_oil(self, value):
        self._unpick_oil = value
    @property
    def use_oil(self):
        return self._use_oil

    @use_oil.setter
    def use_oil(self, value):
        self._use_oil = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsAutoUserOilQueryResponse, self).parse_response_content(response_content)
        if 'accum_oil' in response:
            self.accum_oil = response['accum_oil']
        if 'current_oil' in response:
            self.current_oil = response['current_oil']
        if 'total_oil' in response:
            self.total_oil = response['total_oil']
        if 'unpick_oil' in response:
            self.unpick_oil = response['unpick_oil']
        if 'use_oil' in response:
            self.use_oil = response['use_oil']
