#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InstitutionBasicInfo import InstitutionBasicInfo


class AlipayEbppInvoiceInstitutionPageinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceInstitutionPageinfoQueryResponse, self).__init__()
        self._institution_basic_info_list = None
        self._page_num = None
        self._page_size = None
        self._total_page_count = None

    @property
    def institution_basic_info_list(self):
        return self._institution_basic_info_list

    @institution_basic_info_list.setter
    def institution_basic_info_list(self, value):
        if isinstance(value, list):
            self._institution_basic_info_list = list()
            for i in value:
                if isinstance(i, InstitutionBasicInfo):
                    self._institution_basic_info_list.append(i)
                else:
                    self._institution_basic_info_list.append(InstitutionBasicInfo.from_alipay_dict(i))
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
        response = super(AlipayEbppInvoiceInstitutionPageinfoQueryResponse, self).parse_response_content(response_content)
        if 'institution_basic_info_list' in response:
            self.institution_basic_info_list = response['institution_basic_info_list']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_page_count' in response:
            self.total_page_count = response['total_page_count']
