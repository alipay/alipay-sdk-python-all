#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Data import Data


class AlipayMobilePublicFollowListResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMobilePublicFollowListResponse, self).__init__()
        self._code = None
        self._count = None
        self._data = None
        self._next_alipay_user_id = None
        self._next_user_id = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, Data):
            self._data = value
        else:
            self._data = Data.from_alipay_dict(value)
    @property
    def next_alipay_user_id(self):
        return self._next_alipay_user_id

    @next_alipay_user_id.setter
    def next_alipay_user_id(self, value):
        self._next_alipay_user_id = value
    @property
    def next_user_id(self):
        return self._next_user_id

    @next_user_id.setter
    def next_user_id(self, value):
        self._next_user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMobilePublicFollowListResponse, self).parse_response_content(response_content)
        if 'code' in response:
            self.code = response['code']
        if 'count' in response:
            self.count = response['count']
        if 'data' in response:
            self.data = response['data']
        if 'next_alipay_user_id' in response:
            self.next_alipay_user_id = response['next_alipay_user_id']
        if 'next_user_id' in response:
            self.next_user_id = response['next_user_id']
