#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MerchantLimit import MerchantLimit
from alipay.aop.api.domain.JointAccountQuotaDTO import JointAccountQuotaDTO


class AlipayFundEnterprisepayRuleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundEnterprisepayRuleQueryResponse, self).__init__()
        self._merchant_limit = None
        self._quota_list = None

    @property
    def merchant_limit(self):
        return self._merchant_limit

    @merchant_limit.setter
    def merchant_limit(self, value):
        if isinstance(value, MerchantLimit):
            self._merchant_limit = value
        else:
            self._merchant_limit = MerchantLimit.from_alipay_dict(value)
    @property
    def quota_list(self):
        return self._quota_list

    @quota_list.setter
    def quota_list(self, value):
        if isinstance(value, list):
            self._quota_list = list()
            for i in value:
                if isinstance(i, JointAccountQuotaDTO):
                    self._quota_list.append(i)
                else:
                    self._quota_list.append(JointAccountQuotaDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFundEnterprisepayRuleQueryResponse, self).parse_response_content(response_content)
        if 'merchant_limit' in response:
            self.merchant_limit = response['merchant_limit']
        if 'quota_list' in response:
            self.quota_list = response['quota_list']
