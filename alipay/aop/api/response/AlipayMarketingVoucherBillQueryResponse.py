#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VoucherBill import VoucherBill


class AlipayMarketingVoucherBillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingVoucherBillQueryResponse, self).__init__()
        self._current_page = None
        self._items_per_page = None
        self._total_items = None
        self._total_pages = None
        self._voucher_bills = None

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
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
    def voucher_bills(self):
        return self._voucher_bills

    @voucher_bills.setter
    def voucher_bills(self, value):
        if isinstance(value, list):
            self._voucher_bills = list()
            for i in value:
                if isinstance(i, VoucherBill):
                    self._voucher_bills.append(i)
                else:
                    self._voucher_bills.append(VoucherBill.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingVoucherBillQueryResponse, self).parse_response_content(response_content)
        if 'current_page' in response:
            self.current_page = response['current_page']
        if 'items_per_page' in response:
            self.items_per_page = response['items_per_page']
        if 'total_items' in response:
            self.total_items = response['total_items']
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
        if 'voucher_bills' in response:
            self.voucher_bills = response['voucher_bills']
