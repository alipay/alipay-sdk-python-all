#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExternalBillInfoResult import ExternalBillInfoResult


class AlipayEbppMerchantExternalbillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppMerchantExternalbillQueryResponse, self).__init__()
        self._external_bill_list = None
        self._page_number = None
        self._page_size = None
        self._total_count = None

    @property
    def external_bill_list(self):
        return self._external_bill_list

    @external_bill_list.setter
    def external_bill_list(self, value):
        if isinstance(value, list):
            self._external_bill_list = list()
            for i in value:
                if isinstance(i, ExternalBillInfoResult):
                    self._external_bill_list.append(i)
                else:
                    self._external_bill_list.append(ExternalBillInfoResult.from_alipay_dict(i))
    @property
    def page_number(self):
        return self._page_number

    @page_number.setter
    def page_number(self, value):
        self._page_number = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppMerchantExternalbillQueryResponse, self).parse_response_content(response_content)
        if 'external_bill_list' in response:
            self.external_bill_list = response['external_bill_list']
        if 'page_number' in response:
            self.page_number = response['page_number']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_count' in response:
            self.total_count = response['total_count']
