#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceDecorationPolicystatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceDecorationPolicystatusQueryResponse, self).__init__()
        self._order_no = None
        self._policy_status = None

    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def policy_status(self):
        return self._policy_status

    @policy_status.setter
    def policy_status(self, value):
        self._policy_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceDecorationPolicystatusQueryResponse, self).parse_response_content(response_content)
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'policy_status' in response:
            self.policy_status = response['policy_status']
