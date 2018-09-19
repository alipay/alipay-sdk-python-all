#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsUnderwriteMutualPolicyBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsUnderwriteMutualPolicyBatchqueryResponse, self).__init__()
        self._plan_no = None
        self._policy_nos = None

    @property
    def plan_no(self):
        return self._plan_no

    @plan_no.setter
    def plan_no(self, value):
        self._plan_no = value
    @property
    def policy_nos(self):
        return self._policy_nos

    @policy_nos.setter
    def policy_nos(self, value):
        if isinstance(value, list):
            self._policy_nos = list()
            for i in value:
                self._policy_nos.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayInsUnderwriteMutualPolicyBatchqueryResponse, self).parse_response_content(response_content)
        if 'plan_no' in response:
            self.plan_no = response['plan_no']
        if 'policy_nos' in response:
            self.policy_nos = response['policy_nos']
