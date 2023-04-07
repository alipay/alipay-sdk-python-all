#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantIndirectRewardApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantIndirectRewardApplyResponse, self).__init__()
        self._result_code = None
        self._reward_code = None

    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def reward_code(self):
        return self._reward_code

    @reward_code.setter
    def reward_code(self, value):
        self._reward_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantIndirectRewardApplyResponse, self).parse_response_content(response_content)
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'reward_code' in response:
            self.reward_code = response['reward_code']
