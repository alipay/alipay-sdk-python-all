#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OrderInfoDTO import OrderInfoDTO


class AlipayMerchantShopcodeApplyorderBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantShopcodeApplyorderBatchqueryResponse, self).__init__()
        self._cur_page_no = None
        self._order_list = None
        self._page_size = None
        self._total_items = None
        self._total_pages = None

    @property
    def cur_page_no(self):
        return self._cur_page_no

    @cur_page_no.setter
    def cur_page_no(self, value):
        self._cur_page_no = value
    @property
    def order_list(self):
        return self._order_list

    @order_list.setter
    def order_list(self, value):
        if isinstance(value, list):
            self._order_list = list()
            for i in value:
                if isinstance(i, OrderInfoDTO):
                    self._order_list.append(i)
                else:
                    self._order_list.append(OrderInfoDTO.from_alipay_dict(i))
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_items(self):
        return self._total_items

    @total_items.setter
    def total_items(self, value):
        self._total_items = value
    @property
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, value):
        self._total_pages = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantShopcodeApplyorderBatchqueryResponse, self).parse_response_content(response_content)
        if 'cur_page_no' in response:
            self.cur_page_no = response['cur_page_no']
        if 'order_list' in response:
            self.order_list = response['order_list']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_items' in response:
            self.total_items = response['total_items']
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
