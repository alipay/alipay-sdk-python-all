#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SubServiceKeyWordInfo import SubServiceKeyWordInfo


class AlipayOpenSearchSubservicekeywordBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSearchSubservicekeywordBatchqueryResponse, self).__init__()
        self._page_number = None
        self._page_size = None
        self._subservice_keyword_info = None
        self._total_count = None
        self._total_page_count = None

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
    def subservice_keyword_info(self):
        return self._subservice_keyword_info

    @subservice_keyword_info.setter
    def subservice_keyword_info(self, value):
        if isinstance(value, list):
            self._subservice_keyword_info = list()
            for i in value:
                if isinstance(i, SubServiceKeyWordInfo):
                    self._subservice_keyword_info.append(i)
                else:
                    self._subservice_keyword_info.append(SubServiceKeyWordInfo.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def total_page_count(self):
        return self._total_page_count

    @total_page_count.setter
    def total_page_count(self, value):
        self._total_page_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSearchSubservicekeywordBatchqueryResponse, self).parse_response_content(response_content)
        if 'page_number' in response:
            self.page_number = response['page_number']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'subservice_keyword_info' in response:
            self.subservice_keyword_info = response['subservice_keyword_info']
        if 'total_count' in response:
            self.total_count = response['total_count']
        if 'total_page_count' in response:
            self.total_page_count = response['total_page_count']
