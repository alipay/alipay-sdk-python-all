#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationUserPointQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationUserPointQueryResponse, self).__init__()
        self._current_point = None
        self._total_point = None

    @property
    def current_point(self):
        return self._current_point

    @current_point.setter
    def current_point(self, value):
        self._current_point = value
    @property
    def total_point(self):
        return self._total_point

    @total_point.setter
    def total_point(self, value):
        self._total_point = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationUserPointQueryResponse, self).parse_response_content(response_content)
        if 'current_point' in response:
            self.current_point = response['current_point']
        if 'total_point' in response:
            self.total_point = response['total_point']
