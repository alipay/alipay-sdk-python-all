#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsOpenPolicyDigestDTO import InsOpenPolicyDigestDTO


class AlipayInsSceneEcommerceTradeeventSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneEcommerceTradeeventSyncResponse, self).__init__()
        self._policy_list = None

    @property
    def policy_list(self):
        return self._policy_list

    @policy_list.setter
    def policy_list(self, value):
        if isinstance(value, list):
            self._policy_list = list()
            for i in value:
                if isinstance(i, InsOpenPolicyDigestDTO):
                    self._policy_list.append(i)
                else:
                    self._policy_list.append(InsOpenPolicyDigestDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneEcommerceTradeeventSyncResponse, self).parse_response_content(response_content)
        if 'policy_list' in response:
            self.policy_list = response['policy_list']
