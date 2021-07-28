#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneMobileScreenRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneMobileScreenRefundResponse, self).__init__()
        self._policy_no = None
        self._surrender_premium = None

    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def surrender_premium(self):
        return self._surrender_premium

    @surrender_premium.setter
    def surrender_premium(self, value):
        self._surrender_premium = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneMobileScreenRefundResponse, self).parse_response_content(response_content)
        if 'policy_no' in response:
            self.policy_no = response['policy_no']
        if 'surrender_premium' in response:
            self.surrender_premium = response['surrender_premium']
