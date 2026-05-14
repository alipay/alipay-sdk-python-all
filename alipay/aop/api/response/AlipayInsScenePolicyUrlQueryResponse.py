#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsScenePolicyUrlQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsScenePolicyUrlQueryResponse, self).__init__()
        self._expiration = None
        self._policy_url = None

    @property
    def expiration(self):
        return self._expiration

    @expiration.setter
    def expiration(self, value):
        self._expiration = value
    @property
    def policy_url(self):
        return self._policy_url

    @policy_url.setter
    def policy_url(self, value):
        self._policy_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsScenePolicyUrlQueryResponse, self).parse_response_content(response_content)
        if 'expiration' in response:
            self.expiration = response['expiration']
        if 'policy_url' in response:
            self.policy_url = response['policy_url']
