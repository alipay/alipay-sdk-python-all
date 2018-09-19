#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AlipayOfflinePayMasterKey import AlipayOfflinePayMasterKey


class AlipayCommerceTransportOfflinepayKeyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportOfflinepayKeyQueryResponse, self).__init__()
        self._keys = None

    @property
    def keys(self):
        return self._keys

    @keys.setter
    def keys(self, value):
        if isinstance(value, list):
            self._keys = list()
            for i in value:
                if isinstance(i, AlipayOfflinePayMasterKey):
                    self._keys.append(i)
                else:
                    self._keys.append(AlipayOfflinePayMasterKey.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportOfflinepayKeyQueryResponse, self).parse_response_content(response_content)
        if 'keys' in response:
            self.keys = response['keys']
