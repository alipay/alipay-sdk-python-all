#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CropsComplexInfo import CropsComplexInfo


class AnttechBlockchainDefinDataserviceCropbaseBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainDefinDataserviceCropbaseBatchqueryResponse, self).__init__()
        self._data_list = None
        self._page_no = None
        self._page_size = None
        self._total = None

    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        if isinstance(value, list):
            self._data_list = list()
            for i in value:
                if isinstance(i, CropsComplexInfo):
                    self._data_list.append(i)
                else:
                    self._data_list.append(CropsComplexInfo.from_alipay_dict(i))
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
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainDefinDataserviceCropbaseBatchqueryResponse, self).parse_response_content(response_content)
        if 'data_list' in response:
            self.data_list = response['data_list']
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
