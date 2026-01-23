#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportTrafficshareCrowdSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTrafficshareCrowdSyncResponse, self).__init__()
        self._phone_number_list = None

    @property
    def phone_number_list(self):
        return self._phone_number_list

    @phone_number_list.setter
    def phone_number_list(self, value):
        if isinstance(value, list):
            self._phone_number_list = list()
            for i in value:
                self._phone_number_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTrafficshareCrowdSyncResponse, self).parse_response_content(response_content)
        if 'phone_number_list' in response:
            self.phone_number_list = response['phone_number_list']
