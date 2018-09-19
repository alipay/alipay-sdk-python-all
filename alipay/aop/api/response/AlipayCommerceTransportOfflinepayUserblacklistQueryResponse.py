#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportOfflinepayUserblacklistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportOfflinepayUserblacklistQueryResponse, self).__init__()
        self._black_list = None

    @property
    def black_list(self):
        return self._black_list

    @black_list.setter
    def black_list(self, value):
        if isinstance(value, list):
            self._black_list = list()
            for i in value:
                self._black_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportOfflinepayUserblacklistQueryResponse, self).parse_response_content(response_content)
        if 'black_list' in response:
            self.black_list = response['black_list']
