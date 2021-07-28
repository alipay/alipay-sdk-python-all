#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.StoreOrderDTO import StoreOrderDTO


class AntMerchantOrderStoreBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantOrderStoreBatchqueryResponse, self).__init__()
        self._has_more = None
        self._order_list = None
        self._page_no = None
        self._page_size = None
        self._total = None

    @property
    def has_more(self):
        return self._has_more

    @has_more.setter
    def has_more(self, value):
        self._has_more = value
    @property
    def order_list(self):
        return self._order_list

    @order_list.setter
    def order_list(self, value):
        if isinstance(value, list):
            self._order_list = list()
            for i in value:
                if isinstance(i, StoreOrderDTO):
                    self._order_list.append(i)
                else:
                    self._order_list.append(StoreOrderDTO.from_alipay_dict(i))
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
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantOrderStoreBatchqueryResponse, self).parse_response_content(response_content)
        if 'has_more' in response:
            self.has_more = response['has_more']
        if 'order_list' in response:
            self.order_list = response['order_list']
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
