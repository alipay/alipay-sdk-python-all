#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataIotdataBaiCargocountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataIotdataBaiCargocountQueryResponse, self).__init__()
        self._storage_detail = None
        self._storage_num = None

    @property
    def storage_detail(self):
        return self._storage_detail

    @storage_detail.setter
    def storage_detail(self, value):
        self._storage_detail = value
    @property
    def storage_num(self):
        return self._storage_num

    @storage_num.setter
    def storage_num(self, value):
        self._storage_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataIotdataBaiCargocountQueryResponse, self).parse_response_content(response_content)
        if 'storage_detail' in response:
            self.storage_detail = response['storage_detail']
        if 'storage_num' in response:
            self.storage_num = response['storage_num']
