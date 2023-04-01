#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SupervisionBillInfo import SupervisionBillInfo


class AlipayEbppIndustrySupervisionBillBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustrySupervisionBillBatchqueryResponse, self).__init__()
        self._bill_list = None
        self._page_index = None
        self._page_size = None

    @property
    def bill_list(self):
        return self._bill_list

    @bill_list.setter
    def bill_list(self, value):
        if isinstance(value, list):
            self._bill_list = list()
            for i in value:
                if isinstance(i, SupervisionBillInfo):
                    self._bill_list.append(i)
                else:
                    self._bill_list.append(SupervisionBillInfo.from_alipay_dict(i))
    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustrySupervisionBillBatchqueryResponse, self).parse_response_content(response_content)
        if 'bill_list' in response:
            self.bill_list = response['bill_list']
        if 'page_index' in response:
            self.page_index = response['page_index']
        if 'page_size' in response:
            self.page_size = response['page_size']
