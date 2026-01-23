#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceDecorationPolicystatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceDecorationPolicystatusQueryResponse, self).__init__()
        self._inst_policy_no = None
        self._order_no = None
        self._out_order_no = None
        self._policy_no = None
        self._policy_status = None
        self._policy_url = None

    @property
    def inst_policy_no(self):
        return self._inst_policy_no

    @inst_policy_no.setter
    def inst_policy_no(self, value):
        self._inst_policy_no = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def policy_status(self):
        return self._policy_status

    @policy_status.setter
    def policy_status(self, value):
        self._policy_status = value
    @property
    def policy_url(self):
        return self._policy_url

    @policy_url.setter
    def policy_url(self, value):
        self._policy_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceDecorationPolicystatusQueryResponse, self).parse_response_content(response_content)
        if 'inst_policy_no' in response:
            self.inst_policy_no = response['inst_policy_no']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'policy_no' in response:
            self.policy_no = response['policy_no']
        if 'policy_status' in response:
            self.policy_status = response['policy_status']
        if 'policy_url' in response:
            self.policy_url = response['policy_url']
