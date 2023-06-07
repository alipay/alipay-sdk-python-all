#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceCcmSwItemSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmSwItemSyncResponse, self).__init__()
        self._syn_id = None

    @property
    def syn_id(self):
        return self._syn_id

    @syn_id.setter
    def syn_id(self, value):
        self._syn_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmSwItemSyncResponse, self).parse_response_content(response_content)
        if 'syn_id' in response:
            self.syn_id = response['syn_id']
