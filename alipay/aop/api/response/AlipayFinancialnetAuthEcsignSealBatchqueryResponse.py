#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EcsignSealOpenVO import EcsignSealOpenVO


class AlipayFinancialnetAuthEcsignSealBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetAuthEcsignSealBatchqueryResponse, self).__init__()
        self._page_no = None
        self._page_size = None
        self._seal_list = None
        self._total_count = None

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
    def seal_list(self):
        return self._seal_list

    @seal_list.setter
    def seal_list(self, value):
        if isinstance(value, list):
            self._seal_list = list()
            for i in value:
                if isinstance(i, EcsignSealOpenVO):
                    self._seal_list.append(i)
                else:
                    self._seal_list.append(EcsignSealOpenVO.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayFinancialnetAuthEcsignSealBatchqueryResponse, self).parse_response_content(response_content)
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'seal_list' in response:
            self.seal_list = response['seal_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
