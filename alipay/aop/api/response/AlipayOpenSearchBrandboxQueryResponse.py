#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SearchBrandBoxInfo import SearchBrandBoxInfo


class AlipayOpenSearchBrandboxQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSearchBrandboxQueryResponse, self).__init__()
        self._data = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, SearchBrandBoxInfo):
            self._data = value
        else:
            self._data = SearchBrandBoxInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSearchBrandboxQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
