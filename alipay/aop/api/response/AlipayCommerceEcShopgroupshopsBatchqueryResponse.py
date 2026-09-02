#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SelfShopGroupShopDetail import SelfShopGroupShopDetail


class AlipayCommerceEcShopgroupshopsBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcShopgroupshopsBatchqueryResponse, self).__init__()
        self._page_no = None
        self._page_size = None
        self._shop_list = None
        self._total_num = None
        self._total_page = None

    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
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
                if isinstance(i, SelfShopGroupShopDetail):
                    self._shop_list.append(i)
                else:
                    self._shop_list.append(SelfShopGroupShopDetail.from_alipay_dict(i))
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value
    @property
    def total_page(self):
        return self._total_page

    @total_page.setter
    def total_page(self, value):
        self._total_page = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcShopgroupshopsBatchqueryResponse, self).parse_response_content(response_content)
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'shop_list' in response:
            self.shop_list = response['shop_list']
        if 'total_num' in response:
            self.total_num = response['total_num']
        if 'total_page' in response:
            self.total_page = response['total_page']
