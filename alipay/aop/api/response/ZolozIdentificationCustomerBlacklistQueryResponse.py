#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZolozIdentificationCustomerBlacklistQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZolozIdentificationCustomerBlacklistQueryResponse, self).__init__()
        self._detail_reason = None
        self._expire_time = None
        self._in_black_list = None

    @property
    def detail_reason(self):
        return self._detail_reason

    @detail_reason.setter
    def detail_reason(self, value):
        self._detail_reason = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def in_black_list(self):
        return self._in_black_list

    @in_black_list.setter
    def in_black_list(self, value):
        self._in_black_list = value

    def parse_response_content(self, response_content):
        response = super(ZolozIdentificationCustomerBlacklistQueryResponse, self).parse_response_content(response_content)
        if 'detail_reason' in response:
            self.detail_reason = response['detail_reason']
        if 'expire_time' in response:
            self.expire_time = response['expire_time']
        if 'in_black_list' in response:
            self.in_black_list = response['in_black_list']
