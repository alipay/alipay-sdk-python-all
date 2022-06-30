#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.YunTaskVoucherPackageInfo import YunTaskVoucherPackageInfo


class AlipayCommerceYuntaskSalegiftpackageQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceYuntaskSalegiftpackageQueryResponse, self).__init__()
        self._page = None
        self._page_size = None
        self._total_size = None
        self._voucher_package_infos = None

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
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
    def voucher_package_infos(self):
        return self._voucher_package_infos

    @voucher_package_infos.setter
    def voucher_package_infos(self, value):
        if isinstance(value, list):
            self._voucher_package_infos = list()
            for i in value:
                if isinstance(i, YunTaskVoucherPackageInfo):
                    self._voucher_package_infos.append(i)
                else:
                    self._voucher_package_infos.append(YunTaskVoucherPackageInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceYuntaskSalegiftpackageQueryResponse, self).parse_response_content(response_content)
        if 'page' in response:
            self.page = response['page']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_size' in response:
            self.total_size = response['total_size']
        if 'voucher_package_infos' in response:
            self.voucher_package_infos = response['voucher_package_infos']
