#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DefaultDeliverAddress import DefaultDeliverAddress


class AlipayUserAddressDefaultaddressQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAddressDefaultaddressQueryResponse, self).__init__()
        self._default_address = None

    @property
    def default_address(self):
        return self._default_address

    @default_address.setter
    def default_address(self, value):
        if isinstance(value, DefaultDeliverAddress):
            self._default_address = value
        else:
            self._default_address = DefaultDeliverAddress.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayUserAddressDefaultaddressQueryResponse, self).parse_response_content(response_content)
        if 'default_address' in response:
            self.default_address = response['default_address']
