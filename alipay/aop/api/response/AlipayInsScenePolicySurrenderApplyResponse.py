#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsScenePolicySurrenderApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsScenePolicySurrenderApplyResponse, self).__init__()
        self._policy_no = None

    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsScenePolicySurrenderApplyResponse, self).parse_response_content(response_content)
        if 'policy_no' in response:
            self.policy_no = response['policy_no']
