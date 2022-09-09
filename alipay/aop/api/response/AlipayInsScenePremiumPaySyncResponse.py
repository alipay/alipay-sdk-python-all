#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsOpenPolicyDigestDTO import InsOpenPolicyDigestDTO


class AlipayInsScenePremiumPaySyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsScenePremiumPaySyncResponse, self).__init__()
        self._policy_digest = None

    @property
    def policy_digest(self):
        return self._policy_digest

    @policy_digest.setter
    def policy_digest(self, value):
        if isinstance(value, InsOpenPolicyDigestDTO):
            self._policy_digest = value
        else:
            self._policy_digest = InsOpenPolicyDigestDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayInsScenePremiumPaySyncResponse, self).parse_response_content(response_content)
        if 'policy_digest' in response:
            self.policy_digest = response['policy_digest']
