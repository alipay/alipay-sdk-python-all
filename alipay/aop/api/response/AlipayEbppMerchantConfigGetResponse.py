#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MerchantInstConfig import MerchantInstConfig


class AlipayEbppMerchantConfigGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppMerchantConfigGetResponse, self).__init__()
        self._inst_configs = None
        self._merchant_user_id = None

    @property
    def inst_configs(self):
        return self._inst_configs

    @inst_configs.setter
    def inst_configs(self, value):
        if isinstance(value, list):
            self._inst_configs = list()
            for i in value:
                if isinstance(i, MerchantInstConfig):
                    self._inst_configs.append(i)
                else:
                    self._inst_configs.append(MerchantInstConfig.from_alipay_dict(i))
    @property
    def merchant_user_id(self):
        return self._merchant_user_id

    @merchant_user_id.setter
    def merchant_user_id(self, value):
        self._merchant_user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppMerchantConfigGetResponse, self).parse_response_content(response_content)
        if 'inst_configs' in response:
            self.inst_configs = response['inst_configs']
        if 'merchant_user_id' in response:
            self.merchant_user_id = response['merchant_user_id']
