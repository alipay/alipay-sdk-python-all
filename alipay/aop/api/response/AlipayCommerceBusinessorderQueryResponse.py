#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceBusinessorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceBusinessorderQueryResponse, self).__init__()
        self._record_detail = None

    @property
    def record_detail(self):
        return self._record_detail

    @record_detail.setter
    def record_detail(self, value):
        self._record_detail = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceBusinessorderQueryResponse, self).parse_response_content(response_content)
        if 'record_detail' in response:
            self.record_detail = response['record_detail']
