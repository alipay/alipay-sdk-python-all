#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AlipayPointDetail import AlipayPointDetail


class AlipayCommerceAcommunicationPointDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationPointDetailQueryResponse, self).__init__()
        self._data = None
        self._has_next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                if isinstance(i, AlipayPointDetail):
                    self._data.append(i)
                else:
                    self._data.append(AlipayPointDetail.from_alipay_dict(i))
    @property
    def has_next(self):
        return self._has_next

    @has_next.setter
    def has_next(self, value):
        self._has_next = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationPointDetailQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'has_next' in response:
            self.has_next = response['has_next']
