#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VoucherItem import VoucherItem


class AlipayMarketingCampaignUserVoucherBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignUserVoucherBatchqueryResponse, self).__init__()
        self._current_pages = None
        self._items_per_page = None
        self._total_items = None
        self._total_pages = None
        self._voucher_item_list = None

    @property
    def current_pages(self):
        return self._current_pages

    @current_pages.setter
    def current_pages(self, value):
        self._current_pages = value
    @property
    def items_per_page(self):
        return self._items_per_page

    @items_per_page.setter
    def items_per_page(self, value):
        self._items_per_page = value
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
    @property
    def voucher_item_list(self):
        return self._voucher_item_list

    @voucher_item_list.setter
    def voucher_item_list(self, value):
        if isinstance(value, list):
            self._voucher_item_list = list()
            for i in value:
                if isinstance(i, VoucherItem):
                    self._voucher_item_list.append(i)
                else:
                    self._voucher_item_list.append(VoucherItem.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignUserVoucherBatchqueryResponse, self).parse_response_content(response_content)
        if 'current_pages' in response:
            self.current_pages = response['current_pages']
        if 'items_per_page' in response:
            self.items_per_page = response['items_per_page']
        if 'total_items' in response:
            self.total_items = response['total_items']
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
        if 'voucher_item_list' in response:
            self.voucher_item_list = response['voucher_item_list']
