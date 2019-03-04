#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ShopOrderModifyResult import ShopOrderModifyResult


class KoubeiCateringConfigModifyResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringConfigModifyResponse, self).__init__()
        self._config_result_list = None

    @property
    def config_result_list(self):
        return self._config_result_list

    @config_result_list.setter
    def config_result_list(self, value):
        if isinstance(value, list):
            self._config_result_list = list()
            for i in value:
                if isinstance(i, ShopOrderModifyResult):
                    self._config_result_list.append(i)
                else:
                    self._config_result_list.append(ShopOrderModifyResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringConfigModifyResponse, self).parse_response_content(response_content)
        if 'config_result_list' in response:
            self.config_result_list = response['config_result_list']
