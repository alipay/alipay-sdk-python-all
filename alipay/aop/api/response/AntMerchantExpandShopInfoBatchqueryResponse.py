#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ShopPageQueryDetailVO import ShopPageQueryDetailVO


class AntMerchantExpandShopInfoBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandShopInfoBatchqueryResponse, self).__init__()
        self._page_num = None
        self._page_size = None
        self._shop_infos = None
        self._total_pages = None
        self._total_size = None

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
    def shop_infos(self):
        return self._shop_infos

    @shop_infos.setter
    def shop_infos(self, value):
        if isinstance(value, list):
            self._shop_infos = list()
            for i in value:
                if isinstance(i, ShopPageQueryDetailVO):
                    self._shop_infos.append(i)
                else:
                    self._shop_infos.append(ShopPageQueryDetailVO.from_alipay_dict(i))
    @property
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, value):
        self._total_pages = value
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandShopInfoBatchqueryResponse, self).parse_response_content(response_content)
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'shop_infos' in response:
            self.shop_infos = response['shop_infos']
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
        if 'total_size' in response:
            self.total_size = response['total_size']
