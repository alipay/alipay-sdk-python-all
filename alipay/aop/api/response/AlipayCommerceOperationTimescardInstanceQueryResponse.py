#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TimeCardInfo import TimeCardInfo


class AlipayCommerceOperationTimescardInstanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationTimescardInstanceQueryResponse, self).__init__()
        self._data = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, TimeCardInfo):
            self._data = value
        else:
            self._data = TimeCardInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationTimescardInstanceQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
