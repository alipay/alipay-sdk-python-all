#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainDefinInsuranceEpolicyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainDefinInsuranceEpolicyQueryResponse, self).__init__()
        self._policy_url = None

    @property
    def policy_url(self):
        return self._policy_url

    @policy_url.setter
    def policy_url(self, value):
        self._policy_url = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainDefinInsuranceEpolicyQueryResponse, self).parse_response_content(response_content)
        if 'policy_url' in response:
            self.policy_url = response['policy_url']
