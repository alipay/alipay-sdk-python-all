#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OrderItem import OrderItem


class AlipayOpenServicemarketOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenServicemarketOrderQueryResponse, self).__init__()
        self._commodity_id = None
        self._current_page = None
        self._order_items = None
        self._specifications = None
        self._status = None
        self._total_size = None

    @property
    def commodity_id(self):
        return self._commodity_id

    @commodity_id.setter
    def commodity_id(self, value):
        self._commodity_id = value
    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def order_items(self):
        return self._order_items

    @order_items.setter
    def order_items(self, value):
        if isinstance(value, list):
            self._order_items = list()
            for i in value:
                if isinstance(i, OrderItem):
                    self._order_items.append(i)
                else:
                    self._order_items.append(OrderItem.from_alipay_dict(i))
    @property
    def specifications(self):
        return self._specifications

    @specifications.setter
    def specifications(self, value):
        self._specifications = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenServicemarketOrderQueryResponse, self).parse_response_content(response_content)
        if 'commodity_id' in response:
            self.commodity_id = response['commodity_id']
        if 'current_page' in response:
            self.current_page = response['current_page']
        if 'order_items' in response:
            self.order_items = response['order_items']
        if 'specifications' in response:
            self.specifications = response['specifications']
        if 'status' in response:
            self.status = response['status']
        if 'total_size' in response:
            self.total_size = response['total_size']
