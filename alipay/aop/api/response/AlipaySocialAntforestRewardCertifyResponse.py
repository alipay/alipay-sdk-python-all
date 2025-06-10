#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialAntforestRewardCertifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialAntforestRewardCertifyResponse, self).__init__()
        self._cert_id = None
        self._cert_name = None
        self._has_reward = None

    @property
    def cert_id(self):
        return self._cert_id

    @cert_id.setter
    def cert_id(self, value):
        self._cert_id = value
    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def has_reward(self):
        return self._has_reward

    @has_reward.setter
    def has_reward(self, value):
        self._has_reward = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialAntforestRewardCertifyResponse, self).parse_response_content(response_content)
        if 'cert_id' in response:
            self.cert_id = response['cert_id']
        if 'cert_name' in response:
            self.cert_name = response['cert_name']
        if 'has_reward' in response:
            self.has_reward = response['has_reward']
