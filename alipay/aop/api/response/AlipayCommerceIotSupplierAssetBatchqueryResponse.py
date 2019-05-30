#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SupplierAssetResponse import SupplierAssetResponse


class AlipayCommerceIotSupplierAssetBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotSupplierAssetBatchqueryResponse, self).__init__()
        self._cur_page_num = None
        self._page_size = None
        self._result_list = None
        self._total_page = None
        self._total_size = None

    @property
    def cur_page_num(self):
        return self._cur_page_num

    @cur_page_num.setter
    def cur_page_num(self, value):
        self._cur_page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def result_list(self):
        return self._result_list

    @result_list.setter
    def result_list(self, value):
        if isinstance(value, list):
            self._result_list = list()
            for i in value:
                if isinstance(i, SupplierAssetResponse):
                    self._result_list.append(i)
                else:
                    self._result_list.append(SupplierAssetResponse.from_alipay_dict(i))
    @property
    def total_page(self):
        return self._total_page

    @total_page.setter
    def total_page(self, value):
        self._total_page = value
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotSupplierAssetBatchqueryResponse, self).parse_response_content(response_content)
        if 'cur_page_num' in response:
            self.cur_page_num = response['cur_page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'result_list' in response:
            self.result_list = response['result_list']
        if 'total_page' in response:
            self.total_page = response['total_page']
        if 'total_size' in response:
            self.total_size = response['total_size']
