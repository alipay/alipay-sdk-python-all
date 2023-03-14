#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RcSmartCustomizeRuleResponse import RcSmartCustomizeRuleResponse


class AlipayFincoreComplianceRcservsmartCustomizeruleDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFincoreComplianceRcservsmartCustomizeruleDeleteResponse, self).__init__()
        self._rcsmart_common_response = None

    @property
    def rcsmart_common_response(self):
        return self._rcsmart_common_response

    @rcsmart_common_response.setter
    def rcsmart_common_response(self, value):
        if isinstance(value, RcSmartCustomizeRuleResponse):
            self._rcsmart_common_response = value
        else:
            self._rcsmart_common_response = RcSmartCustomizeRuleResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayFincoreComplianceRcservsmartCustomizeruleDeleteResponse, self).parse_response_content(response_content)
        if 'rcsmart_common_response' in response:
            self.rcsmart_common_response = response['rcsmart_common_response']
