#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceDecorationPolicyCancelApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceDecorationPolicyCancelApplyResponse, self).__init__()
        self._inst_policy_no = None
        self._order_no = None
        self._out_order_no = None
        self._policy_no = None
        self._policy_status = None
        self._surrender_flow_no = None

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
    def surrender_flow_no(self):
        return self._surrender_flow_no

    @surrender_flow_no.setter
    def surrender_flow_no(self, value):
        self._surrender_flow_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceDecorationPolicyCancelApplyResponse, self).parse_response_content(response_content)
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
        if 'surrender_flow_no' in response:
            self.surrender_flow_no = response['surrender_flow_no']
