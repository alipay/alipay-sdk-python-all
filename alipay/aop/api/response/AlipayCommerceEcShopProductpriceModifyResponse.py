#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ShopProductPriceModifyResult import ShopProductPriceModifyResult
from alipay.aop.api.domain.ShopProductPriceModifyResult import ShopProductPriceModifyResult


class AlipayCommerceEcShopProductpriceModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcShopProductpriceModifyResponse, self).__init__()
        self._fail_list = None
        self._success_list = None

    @property
    def fail_list(self):
        return self._fail_list

    @fail_list.setter
    def fail_list(self, value):
        if isinstance(value, list):
            self._fail_list = list()
            for i in value:
                if isinstance(i, ShopProductPriceModifyResult):
                    self._fail_list.append(i)
                else:
                    self._fail_list.append(ShopProductPriceModifyResult.from_alipay_dict(i))
    @property
    def success_list(self):
        return self._success_list

    @success_list.setter
    def success_list(self, value):
        if isinstance(value, list):
            self._success_list = list()
            for i in value:
                if isinstance(i, ShopProductPriceModifyResult):
                    self._success_list.append(i)
                else:
                    self._success_list.append(ShopProductPriceModifyResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcShopProductpriceModifyResponse, self).parse_response_content(response_content)
        if 'fail_list' in response:
            self.fail_list = response['fail_list']
        if 'success_list' in response:
            self.success_list = response['success_list']
