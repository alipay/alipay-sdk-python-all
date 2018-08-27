#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPointBalanceGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPointBalanceGetResponse, self).__init__()
        self._point_amount = None

    @property
    def point_amount(self):
        return self._point_amount

    @point_amount.setter
    def point_amount(self, value):
        self._point_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayPointBalanceGetResponse, self).parse_response_content(response_content)
        if 'point_amount' in response:
            self.point_amount = response['point_amount']
