#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialAntforestRewardCertifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialAntforestRewardCertifyResponse, self).__init__()
        self._has_reward = None

    @property
    def has_reward(self):
        return self._has_reward

    @has_reward.setter
    def has_reward(self, value):
        self._has_reward = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialAntforestRewardCertifyResponse, self).parse_response_content(response_content)
        if 'has_reward' in response:
            self.has_reward = response['has_reward']
