#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EcShop import EcShop


class AlipayCommerceEcBrandShopQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcBrandShopQueryResponse, self).__init__()
        self._page_num = None
        self._page_size = None
        self._shop_info_list = None
        self._total_page_count = None

    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def shop_info_list(self):
        return self._shop_info_list

    @shop_info_list.setter
    def shop_info_list(self, value):
        if isinstance(value, list):
            self._shop_info_list = list()
            for i in value:
                if isinstance(i, EcShop):
                    self._shop_info_list.append(i)
                else:
                    self._shop_info_list.append(EcShop.from_alipay_dict(i))
    @property
    def total_page_count(self):
        return self._total_page_count

    @total_page_count.setter
    def total_page_count(self, value):
        self._total_page_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcBrandShopQueryResponse, self).parse_response_content(response_content)
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'shop_info_list' in response:
            self.shop_info_list = response['shop_info_list']
        if 'total_page_count' in response:
            self.total_page_count = response['total_page_count']
