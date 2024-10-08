#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AxfMerchantConfig import AxfMerchantConfig


class AlipayCommerceMerchantcardConfigBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMerchantcardConfigBatchqueryResponse, self).__init__()
        self._axf_merchant_config_list = None

    @property
    def axf_merchant_config_list(self):
        return self._axf_merchant_config_list

    @axf_merchant_config_list.setter
    def axf_merchant_config_list(self, value):
        if isinstance(value, list):
            self._axf_merchant_config_list = list()
            for i in value:
                if isinstance(i, AxfMerchantConfig):
                    self._axf_merchant_config_list.append(i)
                else:
                    self._axf_merchant_config_list.append(AxfMerchantConfig.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMerchantcardConfigBatchqueryResponse, self).parse_response_content(response_content)
        if 'axf_merchant_config_list' in response:
            self.axf_merchant_config_list = response['axf_merchant_config_list']
