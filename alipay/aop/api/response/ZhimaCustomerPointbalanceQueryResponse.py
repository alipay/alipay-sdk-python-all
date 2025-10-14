#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerPointbalanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerPointbalanceQueryResponse, self).__init__()
        self._point_balance = None

    @property
    def point_balance(self):
        return self._point_balance

    @point_balance.setter
    def point_balance(self, value):
        self._point_balance = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerPointbalanceQueryResponse, self).parse_response_content(response_content)
        if 'point_balance' in response:
            self.point_balance = response['point_balance']
