#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OperationList import OperationList


class AlipayCloudCloudbaseRedisOperationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseRedisOperationQueryResponse, self).__init__()
        self._data = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                if isinstance(i, OperationList):
                    self._data.append(i)
                else:
                    self._data.append(OperationList.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseRedisOperationQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
