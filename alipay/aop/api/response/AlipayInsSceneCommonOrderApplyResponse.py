#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsOpenPolicyDigestDTO import InsOpenPolicyDigestDTO


class AlipayInsSceneCommonOrderApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneCommonOrderApplyResponse, self).__init__()
        self._policy = None

    @property
    def policy(self):
        return self._policy

    @policy.setter
    def policy(self, value):
        if isinstance(value, InsOpenPolicyDigestDTO):
            self._policy = value
        else:
            self._policy = InsOpenPolicyDigestDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneCommonOrderApplyResponse, self).parse_response_content(response_content)
        if 'policy' in response:
            self.policy = response['policy']
