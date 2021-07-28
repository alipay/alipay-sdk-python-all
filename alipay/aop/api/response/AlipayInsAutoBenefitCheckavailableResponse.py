#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FrequencyRuleDetail import FrequencyRuleDetail


class AlipayInsAutoBenefitCheckavailableResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsAutoBenefitCheckavailableResponse, self).__init__()
        self._available = None
        self._frequency_rule_detail = None
        self._reason = None

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):
        self._available = value
    @property
    def frequency_rule_detail(self):
        return self._frequency_rule_detail

    @frequency_rule_detail.setter
    def frequency_rule_detail(self, value):
        if isinstance(value, FrequencyRuleDetail):
            self._frequency_rule_detail = value
        else:
            self._frequency_rule_detail = FrequencyRuleDetail.from_alipay_dict(value)
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsAutoBenefitCheckavailableResponse, self).parse_response_content(response_content)
        if 'available' in response:
            self.available = response['available']
        if 'frequency_rule_detail' in response:
            self.frequency_rule_detail = response['frequency_rule_detail']
        if 'reason' in response:
            self.reason = response['reason']
