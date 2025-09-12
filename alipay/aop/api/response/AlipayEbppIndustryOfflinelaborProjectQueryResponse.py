#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OfflineLaborProjectJob import OfflineLaborProjectJob


class AlipayEbppIndustryOfflinelaborProjectQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryOfflinelaborProjectQueryResponse, self).__init__()
        self._page_num = None
        self._page_size = None
        self._record_list = None
        self._total = None
        self._total_page = None

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
    def record_list(self):
        return self._record_list

    @record_list.setter
    def record_list(self, value):
        if isinstance(value, list):
            self._record_list = list()
            for i in value:
                if isinstance(i, OfflineLaborProjectJob):
                    self._record_list.append(i)
                else:
                    self._record_list.append(OfflineLaborProjectJob.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value
    @property
    def total_page(self):
        return self._total_page

    @total_page.setter
    def total_page(self, value):
        self._total_page = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryOfflinelaborProjectQueryResponse, self).parse_response_content(response_content)
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'record_list' in response:
            self.record_list = response['record_list']
        if 'total' in response:
            self.total = response['total']
        if 'total_page' in response:
            self.total_page = response['total_page']
