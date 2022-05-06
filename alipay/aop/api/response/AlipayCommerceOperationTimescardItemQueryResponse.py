#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TimeCardItemInfo import TimeCardItemInfo


class AlipayCommerceOperationTimescardItemQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationTimescardItemQueryResponse, self).__init__()
        self._data = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, TimeCardItemInfo):
            self._data = value
        else:
            self._data = TimeCardItemInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationTimescardItemQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
