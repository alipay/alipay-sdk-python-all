#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineSmddVisitLimitQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineSmddVisitLimitQueryResponse, self).__init__()
        self._limit = None
        self._limit_msg = None
        self._limit_type = None

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, value):
        self._limit = value
    @property
    def limit_msg(self):
        return self._limit_msg

    @limit_msg.setter
    def limit_msg(self, value):
        self._limit_msg = value
    @property
    def limit_type(self):
        return self._limit_type

    @limit_type.setter
    def limit_type(self, value):
        self._limit_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineSmddVisitLimitQueryResponse, self).parse_response_content(response_content)
        if 'limit' in response:
            self.limit = response['limit']
        if 'limit_msg' in response:
            self.limit_msg = response['limit_msg']
        if 'limit_type' in response:
            self.limit_type = response['limit_type']
