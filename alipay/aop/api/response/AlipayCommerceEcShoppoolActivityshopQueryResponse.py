#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EcShopDetail import EcShopDetail


class AlipayCommerceEcShoppoolActivityshopQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcShoppoolActivityshopQueryResponse, self).__init__()
        self._shop_info_list = None
        self._total_num = None

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
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcShoppoolActivityshopQueryResponse, self).parse_response_content(response_content)
        if 'shop_info_list' in response:
            self.shop_info_list = response['shop_info_list']
        if 'total_num' in response:
            self.total_num = response['total_num']
