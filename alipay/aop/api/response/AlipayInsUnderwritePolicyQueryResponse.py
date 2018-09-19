#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsPolicy import InsPolicy


class AlipayInsUnderwritePolicyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsUnderwritePolicyQueryResponse, self).__init__()
        self._policy = None

    @property
    def policy(self):
        return self._policy

    @policy.setter
    def policy(self, value):
        if isinstance(value, InsPolicy):
            self._policy = value
        else:
            self._policy = InsPolicy.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayInsUnderwritePolicyQueryResponse, self).parse_response_content(response_content)
        if 'policy' in response:
            self.policy = response['policy']
