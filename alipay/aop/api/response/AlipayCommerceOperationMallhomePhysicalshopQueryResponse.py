#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PhysicalShopInfo import PhysicalShopInfo


class AlipayCommerceOperationMallhomePhysicalshopQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationMallhomePhysicalshopQueryResponse, self).__init__()
        self._page_num = None
        self._page_size = None
        self._physical_shop_list = None
        self._total = None

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
    def physical_shop_list(self):
        return self._physical_shop_list

    @physical_shop_list.setter
    def physical_shop_list(self, value):
        if isinstance(value, list):
            self._physical_shop_list = list()
            for i in value:
                if isinstance(i, PhysicalShopInfo):
                    self._physical_shop_list.append(i)
                else:
                    self._physical_shop_list.append(PhysicalShopInfo.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationMallhomePhysicalshopQueryResponse, self).parse_response_content(response_content)
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'physical_shop_list' in response:
            self.physical_shop_list = response['physical_shop_list']
        if 'total' in response:
            self.total = response['total']
