#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IsvBizOpenOrderFailReason import IsvBizOpenOrderFailReason


class AntMerchantExpandBizaccessOrderCheckResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandBizaccessOrderCheckResponse, self).__init__()
        self._fail_reasons = None

    @property
    def fail_reasons(self):
        return self._fail_reasons

    @fail_reasons.setter
    def fail_reasons(self, value):
        if isinstance(value, list):
            self._fail_reasons = list()
            for i in value:
                if isinstance(i, IsvBizOpenOrderFailReason):
                    self._fail_reasons.append(i)
                else:
                    self._fail_reasons.append(IsvBizOpenOrderFailReason.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandBizaccessOrderCheckResponse, self).parse_response_content(response_content)
        if 'fail_reasons' in response:
            self.fail_reasons = response['fail_reasons']
