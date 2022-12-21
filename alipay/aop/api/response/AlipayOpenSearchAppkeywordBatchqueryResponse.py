#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KeyWordInfo import KeyWordInfo


class AlipayOpenSearchAppkeywordBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSearchAppkeywordBatchqueryResponse, self).__init__()
        self._key_word_info = None
        self._page_number = None
        self._page_size = None
        self._total_count = None
        self._total_page_count = None

    @property
    def key_word_info(self):
        return self._key_word_info

    @key_word_info.setter
    def key_word_info(self, value):
        if isinstance(value, list):
            self._key_word_info = list()
            for i in value:
                if isinstance(i, KeyWordInfo):
                    self._key_word_info.append(i)
                else:
                    self._key_word_info.append(KeyWordInfo.from_alipay_dict(i))
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
        response = super(AlipayOpenSearchAppkeywordBatchqueryResponse, self).parse_response_content(response_content)
        if 'key_word_info' in response:
            self.key_word_info = response['key_word_info']
        if 'page_number' in response:
            self.page_number = response['page_number']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_count' in response:
            self.total_count = response['total_count']
        if 'total_page_count' in response:
            self.total_page_count = response['total_page_count']
