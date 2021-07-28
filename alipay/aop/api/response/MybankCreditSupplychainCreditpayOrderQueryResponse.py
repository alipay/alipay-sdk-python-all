#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OrderVO import OrderVO


class MybankCreditSupplychainCreditpayOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainCreditpayOrderQueryResponse, self).__init__()
        self._items_per_page = None
        self._next_page = None
        self._order_vo_list = None
        self._page = None

    @property
    def items_per_page(self):
        return self._items_per_page

    @items_per_page.setter
    def items_per_page(self, value):
        self._items_per_page = value
    @property
    def next_page(self):
        return self._next_page

    @next_page.setter
    def next_page(self, value):
        self._next_page = value
    @property
    def order_vo_list(self):
        return self._order_vo_list

    @order_vo_list.setter
    def order_vo_list(self, value):
        if isinstance(value, list):
            self._order_vo_list = list()
            for i in value:
                if isinstance(i, OrderVO):
                    self._order_vo_list.append(i)
                else:
                    self._order_vo_list.append(OrderVO.from_alipay_dict(i))
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        if isinstance(value, list):
            self._page = list()
            for i in value:
                self._page.append(i)

    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainCreditpayOrderQueryResponse, self).parse_response_content(response_content)
        if 'items_per_page' in response:
            self.items_per_page = response['items_per_page']
        if 'next_page' in response:
            self.next_page = response['next_page']
        if 'order_vo_list' in response:
            self.order_vo_list = response['order_vo_list']
        if 'page' in response:
            self.page = response['page']
