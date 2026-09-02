#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneSimplestPolicyApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneSimplestPolicyApplyResponse, self).__init__()
        self._policy_no = None
        self._pre_order_id = None

    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def pre_order_id(self):
        return self._pre_order_id

    @pre_order_id.setter
    def pre_order_id(self, value):
        self._pre_order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneSimplestPolicyApplyResponse, self).parse_response_content(response_content)
        if 'policy_no' in response:
            self.policy_no = response['policy_no']
        if 'pre_order_id' in response:
            self.pre_order_id = response['pre_order_id']
