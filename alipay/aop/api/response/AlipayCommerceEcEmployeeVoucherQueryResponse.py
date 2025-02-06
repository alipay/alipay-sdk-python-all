#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VoucherInfoResponse import VoucherInfoResponse


class AlipayCommerceEcEmployeeVoucherQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcEmployeeVoucherQueryResponse, self).__init__()
        self._page_num = None
        self._page_size = None
        self._total_page_count = None
        self._voucher_info_list = None

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
    def total_page_count(self):
        return self._total_page_count

    @total_page_count.setter
    def total_page_count(self, value):
        self._total_page_count = value
    @property
    def voucher_info_list(self):
        return self._voucher_info_list

    @voucher_info_list.setter
    def voucher_info_list(self, value):
        if isinstance(value, VoucherInfoResponse):
            self._voucher_info_list = value
        else:
            self._voucher_info_list = VoucherInfoResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcEmployeeVoucherQueryResponse, self).parse_response_content(response_content)
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_page_count' in response:
            self.total_page_count = response['total_page_count']
        if 'voucher_info_list' in response:
            self.voucher_info_list = response['voucher_info_list']
