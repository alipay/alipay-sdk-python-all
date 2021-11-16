#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.StandardVoucherOpenApiVO import StandardVoucherOpenApiVO


class AlipayBossFncGffundStandardvoucherBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossFncGffundStandardvoucherBatchqueryResponse, self).__init__()
        self._cur_page = None
        self._page_size = None
        self._standard_voucher_list = None
        self._success = None
        self._total_items = None
        self._total_pages = None

    @property
    def cur_page(self):
        return self._cur_page

    @cur_page.setter
    def cur_page(self, value):
        self._cur_page = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def standard_voucher_list(self):
        return self._standard_voucher_list

    @standard_voucher_list.setter
    def standard_voucher_list(self, value):
        if isinstance(value, list):
            self._standard_voucher_list = list()
            for i in value:
                if isinstance(i, StandardVoucherOpenApiVO):
                    self._standard_voucher_list.append(i)
                else:
                    self._standard_voucher_list.append(StandardVoucherOpenApiVO.from_alipay_dict(i))
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
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
        response = super(AlipayBossFncGffundStandardvoucherBatchqueryResponse, self).parse_response_content(response_content)
        if 'cur_page' in response:
            self.cur_page = response['cur_page']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'standard_voucher_list' in response:
            self.standard_voucher_list = response['standard_voucher_list']
        if 'success' in response:
            self.success = response['success']
        if 'total_items' in response:
            self.total_items = response['total_items']
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
