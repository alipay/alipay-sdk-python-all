#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CorsDomain import CorsDomain


class AlipayCloudCloudbaseHttpaccessCorsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseHttpaccessCorsQueryResponse, self).__init__()
        self._cors = None
        self._page_index = None
        self._page_size = None
        self._total = None

    @property
    def cors(self):
        return self._cors

    @cors.setter
    def cors(self, value):
        if isinstance(value, list):
            self._cors = list()
            for i in value:
                if isinstance(i, CorsDomain):
                    self._cors.append(i)
                else:
                    self._cors.append(CorsDomain.from_alipay_dict(i))
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
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseHttpaccessCorsQueryResponse, self).parse_response_content(response_content)
        if 'cors' in response:
            self.cors = response['cors']
        if 'page_index' in response:
            self.page_index = response['page_index']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
