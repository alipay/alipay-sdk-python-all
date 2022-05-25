#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceCcmSwSpuSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmSwSpuSyncResponse, self).__init__()
        self._spu_id = None

    @property
    def spu_id(self):
        return self._spu_id

    @spu_id.setter
    def spu_id(self, value):
        self._spu_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmSwSpuSyncResponse, self).parse_response_content(response_content)
        if 'spu_id' in response:
            self.spu_id = response['spu_id']
