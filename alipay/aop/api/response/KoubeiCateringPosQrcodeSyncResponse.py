#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiCateringPosQrcodeSyncResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringPosQrcodeSyncResponse, self).__init__()
        self._desk_ids = None

    @property
    def desk_ids(self):
        return self._desk_ids

    @desk_ids.setter
    def desk_ids(self, value):
        if isinstance(value, list):
            self._desk_ids = list()
            for i in value:
                self._desk_ids.append(i)

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringPosQrcodeSyncResponse, self).parse_response_content(response_content)
        if 'desk_ids' in response:
            self.desk_ids = response['desk_ids']
