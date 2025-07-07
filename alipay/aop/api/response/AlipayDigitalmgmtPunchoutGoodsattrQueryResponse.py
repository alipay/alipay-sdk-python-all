#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MallGoodsPrice import MallGoodsPrice


class AlipayDigitalmgmtPunchoutGoodsattrQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtPunchoutGoodsattrQueryResponse, self).__init__()
        self._page_num = None
        self._page_size = None
        self._price_list = None
        self._total = None

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
    def price_list(self):
        return self._price_list

    @price_list.setter
    def price_list(self, value):
        if isinstance(value, MallGoodsPrice):
            self._price_list = value
        else:
            self._price_list = MallGoodsPrice.from_alipay_dict(value)
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtPunchoutGoodsattrQueryResponse, self).parse_response_content(response_content)
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'price_list' in response:
            self.price_list = response['price_list']
        if 'total' in response:
            self.total = response['total']
