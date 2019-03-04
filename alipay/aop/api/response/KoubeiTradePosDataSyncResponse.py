#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiTradePosDataSyncResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiTradePosDataSyncResponse, self).__init__()
        self._ext_infos = None

    @property
    def ext_infos(self):
        return self._ext_infos

    @ext_infos.setter
    def ext_infos(self, value):
        self._ext_infos = value

    def parse_response_content(self, response_content):
        response = super(KoubeiTradePosDataSyncResponse, self).parse_response_content(response_content)
        if 'ext_infos' in response:
            self.ext_infos = response['ext_infos']
