#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ItemQueryResponse import ItemQueryResponse


class KoubeiItemBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiItemBatchqueryResponse, self).__init__()
        self._current_page_no = None
        self._item_infos = None
        self._page_size = None
        self._total_items = None
        self._total_page_no = None

    @property
    def current_page_no(self):
        return self._current_page_no

    @current_page_no.setter
    def current_page_no(self, value):
        self._current_page_no = value
    @property
    def item_infos(self):
        return self._item_infos

    @item_infos.setter
    def item_infos(self, value):
        if isinstance(value, list):
            self._item_infos = list()
            for i in value:
                if isinstance(i, ItemQueryResponse):
                    self._item_infos.append(i)
                else:
                    self._item_infos.append(ItemQueryResponse.from_alipay_dict(i))
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
    def total_page_no(self):
        return self._total_page_no

    @total_page_no.setter
    def total_page_no(self, value):
        self._total_page_no = value

    def parse_response_content(self, response_content):
        response = super(KoubeiItemBatchqueryResponse, self).parse_response_content(response_content)
        if 'current_page_no' in response:
            self.current_page_no = response['current_page_no']
        if 'item_infos' in response:
            self.item_infos = response['item_infos']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_items' in response:
            self.total_items = response['total_items']
        if 'total_page_no' in response:
            self.total_page_no = response['total_page_no']
