#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MerchantBaseInfoResponse import MerchantBaseInfoResponse


class AlipayFincoreComplianceRcassetscenterMerchantbaseinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFincoreComplianceRcassetscenterMerchantbaseinfoQueryResponse, self).__init__()
        self._merchant_base_info_list = None

    @property
    def merchant_base_info_list(self):
        return self._merchant_base_info_list

    @merchant_base_info_list.setter
    def merchant_base_info_list(self, value):
        if isinstance(value, list):
            self._merchant_base_info_list = list()
            for i in value:
                if isinstance(i, MerchantBaseInfoResponse):
                    self._merchant_base_info_list.append(i)
                else:
                    self._merchant_base_info_list.append(MerchantBaseInfoResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFincoreComplianceRcassetscenterMerchantbaseinfoQueryResponse, self).parse_response_content(response_content)
        if 'merchant_base_info_list' in response:
            self.merchant_base_info_list = response['merchant_base_info_list']
