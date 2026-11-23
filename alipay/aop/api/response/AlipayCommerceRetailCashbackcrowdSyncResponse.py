#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRetailCashbackcrowdSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRetailCashbackcrowdSyncResponse, self).__init__()
        self._accepted = None

    @property
    def accepted(self):
        return self._accepted

    @accepted.setter
    def accepted(self, value):
        self._accepted = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRetailCashbackcrowdSyncResponse, self).parse_response_content(response_content)
        if 'accepted' in response:
            self.accepted = response['accepted']
