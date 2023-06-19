#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OssObjectDetail import OssObjectDetail


class AlipayCloudCloudrunObjectstorageFilelistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudrunObjectstorageFilelistQueryResponse, self).__init__()
        self._next_token = None
        self._object_list = None
        self._page_size = None

    @property
    def next_token(self):
        return self._next_token

    @next_token.setter
    def next_token(self, value):
        self._next_token = value
    @property
    def object_list(self):
        return self._object_list

    @object_list.setter
    def object_list(self, value):
        if isinstance(value, list):
            self._object_list = list()
            for i in value:
                if isinstance(i, OssObjectDetail):
                    self._object_list.append(i)
                else:
                    self._object_list.append(OssObjectDetail.from_alipay_dict(i))
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudrunObjectstorageFilelistQueryResponse, self).parse_response_content(response_content)
        if 'next_token' in response:
            self.next_token = response['next_token']
        if 'object_list' in response:
            self.object_list = response['object_list']
        if 'page_size' in response:
            self.page_size = response['page_size']
