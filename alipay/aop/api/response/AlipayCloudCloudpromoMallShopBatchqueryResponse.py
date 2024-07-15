#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ShopVO import ShopVO


class AlipayCloudCloudpromoMallShopBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoMallShopBatchqueryResponse, self).__init__()
        self._page_num = None
        self._page_size = None
        self._shop_list = None
        self._total_count = None

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
    def shop_list(self):
        return self._shop_list

    @shop_list.setter
    def shop_list(self, value):
        if isinstance(value, list):
            self._shop_list = list()
            for i in value:
                if isinstance(i, ShopVO):
                    self._shop_list.append(i)
                else:
                    self._shop_list.append(ShopVO.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoMallShopBatchqueryResponse, self).parse_response_content(response_content)
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'shop_list' in response:
            self.shop_list = response['shop_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
