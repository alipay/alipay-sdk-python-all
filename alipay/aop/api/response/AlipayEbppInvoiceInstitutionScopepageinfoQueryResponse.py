#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInvoiceInstitutionScopepageinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceInstitutionScopepageinfoQueryResponse, self).__init__()
        self._adapter_type = None
        self._onwer_open_id_list = None
        self._owner_id_list = None
        self._page_num = None
        self._page_size = None
        self._total_page_count = None

    @property
    def adapter_type(self):
        return self._adapter_type

    @adapter_type.setter
    def adapter_type(self, value):
        self._adapter_type = value
    @property
    def onwer_open_id_list(self):
        return self._onwer_open_id_list

    @onwer_open_id_list.setter
    def onwer_open_id_list(self, value):
        if isinstance(value, list):
            self._onwer_open_id_list = list()
            for i in value:
                self._onwer_open_id_list.append(i)
    @property
    def owner_id_list(self):
        return self._owner_id_list

    @owner_id_list.setter
    def owner_id_list(self, value):
        if isinstance(value, list):
            self._owner_id_list = list()
            for i in value:
                self._owner_id_list.append(i)
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
    def total_page_count(self):
        return self._total_page_count

    @total_page_count.setter
    def total_page_count(self, value):
        self._total_page_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceInstitutionScopepageinfoQueryResponse, self).parse_response_content(response_content)
        if 'adapter_type' in response:
            self.adapter_type = response['adapter_type']
        if 'onwer_open_id_list' in response:
            self.onwer_open_id_list = response['onwer_open_id_list']
        if 'owner_id_list' in response:
            self.owner_id_list = response['owner_id_list']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_page_count' in response:
            self.total_page_count = response['total_page_count']
