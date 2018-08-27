#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DishonorOrder import DishonorOrder


class AlipayFundTransDishonorQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransDishonorQueryResponse, self).__init__()
        self._dishonor_order_list = None
        self._items = None
        self._items_per_page = None
        self._page = None

    @property
    def dishonor_order_list(self):
        return self._dishonor_order_list

    @dishonor_order_list.setter
    def dishonor_order_list(self, value):
        if isinstance(value, list):
            self._dishonor_order_list = list()
            for i in value:
                if isinstance(i, DishonorOrder):
                    self._dishonor_order_list.append(i)
                else:
                    self._dishonor_order_list.append(DishonorOrder.from_alipay_dict(i))
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value
    @property
    def items_per_page(self):
        return self._items_per_page

    @items_per_page.setter
    def items_per_page(self, value):
        self._items_per_page = value
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransDishonorQueryResponse, self).parse_response_content(response_content)
        if 'dishonor_order_list' in response:
            self.dishonor_order_list = response['dishonor_order_list']
        if 'items' in response:
            self.items = response['items']
        if 'items_per_page' in response:
            self.items_per_page = response['items_per_page']
        if 'page' in response:
            self.page = response['page']
