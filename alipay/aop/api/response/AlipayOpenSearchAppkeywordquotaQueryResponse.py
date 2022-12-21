#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSearchAppkeywordquotaQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSearchAppkeywordquotaQueryResponse, self).__init__()
        self._quota_num = None

    @property
    def quota_num(self):
        return self._quota_num

    @quota_num.setter
    def quota_num(self, value):
        self._quota_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSearchAppkeywordquotaQueryResponse, self).parse_response_content(response_content)
        if 'quota_num' in response:
            self.quota_num = response['quota_num']
