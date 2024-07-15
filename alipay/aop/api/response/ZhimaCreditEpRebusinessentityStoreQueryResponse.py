#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RebusinessEntityRelation import RebusinessEntityRelation


class ZhimaCreditEpRebusinessentityStoreQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpRebusinessentityStoreQueryResponse, self).__init__()
        self._data = None
        self._platform_id = None
        self._store_id = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, RebusinessEntityRelation):
            self._data = value
        else:
            self._data = RebusinessEntityRelation.from_alipay_dict(value)
    @property
    def platform_id(self):
        return self._platform_id

    @platform_id.setter
    def platform_id(self, value):
        self._platform_id = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpRebusinessentityStoreQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'platform_id' in response:
            self.platform_id = response['platform_id']
        if 'store_id' in response:
            self.store_id = response['store_id']
