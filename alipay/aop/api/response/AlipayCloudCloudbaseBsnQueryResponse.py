#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AliyunBSN import AliyunBSN


class AlipayCloudCloudbaseBsnQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseBsnQueryResponse, self).__init__()
        self._bsns = None
        self._page_index = None
        self._page_size = None
        self._total = None

    @property
    def bsns(self):
        return self._bsns

    @bsns.setter
    def bsns(self, value):
        if isinstance(value, list):
            self._bsns = list()
            for i in value:
                if isinstance(i, AliyunBSN):
                    self._bsns.append(i)
                else:
                    self._bsns.append(AliyunBSN.from_alipay_dict(i))
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
        response = super(AlipayCloudCloudbaseBsnQueryResponse, self).parse_response_content(response_content)
        if 'bsns' in response:
            self.bsns = response['bsns']
        if 'page_index' in response:
            self.page_index = response['page_index']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
