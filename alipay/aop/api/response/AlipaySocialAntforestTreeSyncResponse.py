#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialAntforestTreeSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialAntforestTreeSyncResponse, self).__init__()
        self._synced = None

    @property
    def synced(self):
        return self._synced

    @synced.setter
    def synced(self, value):
        self._synced = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialAntforestTreeSyncResponse, self).parse_response_content(response_content)
        if 'synced' in response:
            self.synced = response['synced']
