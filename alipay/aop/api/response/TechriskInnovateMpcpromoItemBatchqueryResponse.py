#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MpcItemVO import MpcItemVO


class TechriskInnovateMpcpromoItemBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(TechriskInnovateMpcpromoItemBatchqueryResponse, self).__init__()
        self._item_list = None
        self._page_num = None
        self._page_size = None
        self._shop_name = None
        self._total = None

    @property
    def item_list(self):
        return self._item_list

    @item_list.setter
    def item_list(self, value):
        if isinstance(value, MpcItemVO):
            self._item_list = value
        else:
            self._item_list = MpcItemVO.from_alipay_dict(value)
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
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(TechriskInnovateMpcpromoItemBatchqueryResponse, self).parse_response_content(response_content)
        if 'item_list' in response:
            self.item_list = response['item_list']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'shop_name' in response:
            self.shop_name = response['shop_name']
        if 'total' in response:
            self.total = response['total']
