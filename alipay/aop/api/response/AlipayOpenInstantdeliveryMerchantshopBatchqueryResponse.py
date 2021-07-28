#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MerchantShopDTO import MerchantShopDTO


class AlipayOpenInstantdeliveryMerchantshopBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenInstantdeliveryMerchantshopBatchqueryResponse, self).__init__()
        self._page_no = None
        self._page_size = None
        self._records = None
        self._total_no = None

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
    def records(self):
        return self._records

    @records.setter
    def records(self, value):
        if isinstance(value, list):
            self._records = list()
            for i in value:
                if isinstance(i, MerchantShopDTO):
                    self._records.append(i)
                else:
                    self._records.append(MerchantShopDTO.from_alipay_dict(i))
    @property
    def total_no(self):
        return self._total_no

    @total_no.setter
    def total_no(self, value):
        self._total_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenInstantdeliveryMerchantshopBatchqueryResponse, self).parse_response_content(response_content)
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'records' in response:
            self.records = response['records']
        if 'total_no' in response:
            self.total_no = response['total_no']
