#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ItemSpuIdPair import ItemSpuIdPair


class AlipayOpenAppItemDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppItemDeleteResponse, self).__init__()
        self._records = None

    @property
    def records(self):
        return self._records

    @records.setter
    def records(self, value):
        if isinstance(value, list):
            self._records = list()
            for i in value:
                if isinstance(i, ItemSpuIdPair):
                    self._records.append(i)
                else:
                    self._records.append(ItemSpuIdPair.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppItemDeleteResponse, self).parse_response_content(response_content)
        if 'records' in response:
            self.records = response['records']
