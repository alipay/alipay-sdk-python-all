#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SimpleShopInfo import SimpleShopInfo


class AntMerchantExpandShopBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandShopBatchqueryResponse, self).__init__()
        self._page_no = None
        self._page_size = None
        self._shops = None
        self._total_page = None
        self._total_size = None

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
    def shops(self):
        return self._shops

    @shops.setter
    def shops(self, value):
        if isinstance(value, list):
            self._shops = list()
            for i in value:
                if isinstance(i, SimpleShopInfo):
                    self._shops.append(i)
                else:
                    self._shops.append(SimpleShopInfo.from_alipay_dict(i))
    @property
    def total_page(self):
        return self._total_page

    @total_page.setter
    def total_page(self, value):
        self._total_page = value
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandShopBatchqueryResponse, self).parse_response_content(response_content)
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'shops' in response:
            self.shops = response['shops']
        if 'total_page' in response:
            self.total_page = response['total_page']
        if 'total_size' in response:
            self.total_size = response['total_size']
