#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserSportshealthAccountFreezeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserSportshealthAccountFreezeResponse, self).__init__()
        self._pay_order_no = None

    @property
    def pay_order_no(self):
        return self._pay_order_no

    @pay_order_no.setter
    def pay_order_no(self, value):
        self._pay_order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserSportshealthAccountFreezeResponse, self).parse_response_content(response_content)
        if 'pay_order_no' in response:
            self.pay_order_no = response['pay_order_no']
