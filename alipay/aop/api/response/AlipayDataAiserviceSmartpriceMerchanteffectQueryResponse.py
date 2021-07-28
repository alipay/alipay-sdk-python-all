#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MerchantEffectQueryResult import MerchantEffectQueryResult


class AlipayDataAiserviceSmartpriceMerchanteffectQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataAiserviceSmartpriceMerchanteffectQueryResponse, self).__init__()
        self._result = None
        self._unit_id = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, list):
            self._result = list()
            for i in value:
                if isinstance(i, MerchantEffectQueryResult):
                    self._result.append(i)
                else:
                    self._result.append(MerchantEffectQueryResult.from_alipay_dict(i))
    @property
    def unit_id(self):
        return self._unit_id

    @unit_id.setter
    def unit_id(self, value):
        self._unit_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataAiserviceSmartpriceMerchanteffectQueryResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
        if 'unit_id' in response:
            self.unit_id = response['unit_id']
