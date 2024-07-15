#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AnxinItemSellOrderDetailResponse import AnxinItemSellOrderDetailResponse


class AlipayOpenMiniOrderAnxinitemsellorderBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniOrderAnxinitemsellorderBatchqueryResponse, self).__init__()
        self._has_next_page = None
        self._order_list = None
        self._page_size = None
        self._page_token = None
        self._total = None

    @property
    def has_next_page(self):
        return self._has_next_page

    @has_next_page.setter
    def has_next_page(self, value):
        self._has_next_page = value
    @property
    def order_list(self):
        return self._order_list

    @order_list.setter
    def order_list(self, value):
        if isinstance(value, list):
            self._order_list = list()
            for i in value:
                if isinstance(i, AnxinItemSellOrderDetailResponse):
                    self._order_list.append(i)
                else:
                    self._order_list.append(AnxinItemSellOrderDetailResponse.from_alipay_dict(i))
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def page_token(self):
        return self._page_token

    @page_token.setter
    def page_token(self, value):
        self._page_token = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniOrderAnxinitemsellorderBatchqueryResponse, self).parse_response_content(response_content)
        if 'has_next_page' in response:
            self.has_next_page = response['has_next_page']
        if 'order_list' in response:
            self.order_list = response['order_list']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'page_token' in response:
            self.page_token = response['page_token']
        if 'total' in response:
            self.total = response['total']
