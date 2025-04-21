#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAgentIsvCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAgentIsvCreateResponse, self).__init__()
        self._order_no = None

    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAgentIsvCreateResponse, self).parse_response_content(response_content)
        if 'order_no' in response:
            self.order_no = response['order_no']
