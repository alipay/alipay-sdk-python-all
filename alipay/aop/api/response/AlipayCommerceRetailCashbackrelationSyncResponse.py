#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRetailCashbackrelationSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRetailCashbackrelationSyncResponse, self).__init__()
        self._affected_count = None

    @property
    def affected_count(self):
        return self._affected_count

    @affected_count.setter
    def affected_count(self, value):
        self._affected_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRetailCashbackrelationSyncResponse, self).parse_response_content(response_content)
        if 'affected_count' in response:
            self.affected_count = response['affected_count']
