#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VoucherPackageInfo import VoucherPackageInfo


class AlipayMarketingActivityVoucherpackageBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityVoucherpackageBatchqueryResponse, self).__init__()
        self._page_num = None
        self._page_size = None
        self._total_size = None
        self._voucher_package_info = None

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
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value
    @property
    def voucher_package_info(self):
        return self._voucher_package_info

    @voucher_package_info.setter
    def voucher_package_info(self, value):
        if isinstance(value, list):
            self._voucher_package_info = list()
            for i in value:
                if isinstance(i, VoucherPackageInfo):
                    self._voucher_package_info.append(i)
                else:
                    self._voucher_package_info.append(VoucherPackageInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingActivityVoucherpackageBatchqueryResponse, self).parse_response_content(response_content)
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_size' in response:
            self.total_size = response['total_size']
        if 'voucher_package_info' in response:
            self.voucher_package_info = response['voucher_package_info']
