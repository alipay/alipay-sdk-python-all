#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ItemInfoDetail import ItemInfoDetail


class AlipayCommerceMedicalItemListQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalItemListQueryResponse, self).__init__()
        self._item_info_list = None
        self._page_no = None
        self._page_size = None
        self._total = None

    @property
    def item_info_list(self):
        return self._item_info_list

    @item_info_list.setter
    def item_info_list(self, value):
        if isinstance(value, list):
            self._item_info_list = list()
            for i in value:
                if isinstance(i, ItemInfoDetail):
                    self._item_info_list.append(i)
                else:
                    self._item_info_list.append(ItemInfoDetail.from_alipay_dict(i))
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
        response = super(AlipayCommerceMedicalItemListQueryResponse, self).parse_response_content(response_content)
        if 'item_info_list' in response:
            self.item_info_list = response['item_info_list']
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
