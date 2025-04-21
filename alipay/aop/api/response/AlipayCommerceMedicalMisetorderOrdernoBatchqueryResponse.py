#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalMisetorderOrdernoBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalMisetorderOrdernoBatchqueryResponse, self).__init__()
        self._data = None
        self._has_more = None
        self._page_no = None
        self._page_size = None
        self._total_count = None
        self._total_pages = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                self._data.append(i)
    @property
    def has_more(self):
        return self._has_more

    @has_more.setter
    def has_more(self, value):
        self._has_more = value
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
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, value):
        self._total_pages = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalMisetorderOrdernoBatchqueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'has_more' in response:
            self.has_more = response['has_more']
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_count' in response:
            self.total_count = response['total_count']
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
