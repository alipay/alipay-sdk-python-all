#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EcShopDetail import EcShopDetail


class AlipayCommerceEcShoppoolShopGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcShoppoolShopGetResponse, self).__init__()
        self._shop_info_list = None

    @property
    def shop_info_list(self):
        return self._shop_info_list

    @shop_info_list.setter
    def shop_info_list(self, value):
        if isinstance(value, list):
            self._shop_info_list = list()
            for i in value:
                if isinstance(i, EcShopDetail):
                    self._shop_info_list.append(i)
                else:
                    self._shop_info_list.append(EcShopDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcShoppoolShopGetResponse, self).parse_response_content(response_content)
        if 'shop_info_list' in response:
            self.shop_info_list = response['shop_info_list']
