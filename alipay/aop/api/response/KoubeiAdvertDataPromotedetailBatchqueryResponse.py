#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PromoteDetailModel import PromoteDetailModel


class KoubeiAdvertDataPromotedetailBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiAdvertDataPromotedetailBatchqueryResponse, self).__init__()
        self._data = None
        self._page_index = None
        self._page_size = None
        self._total_count = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                if isinstance(i, PromoteDetailModel):
                    self._data.append(i)
                else:
                    self._data.append(PromoteDetailModel.from_alipay_dict(i))
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
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(KoubeiAdvertDataPromotedetailBatchqueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'page_index' in response:
            self.page_index = response['page_index']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_count' in response:
            self.total_count = response['total_count']
