#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotMdeviceprodDeviceInitializeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotMdeviceprodDeviceInitializeResponse, self).__init__()
        self._biz_tid = None

    @property
    def biz_tid(self):
        return self._biz_tid

    @biz_tid.setter
    def biz_tid(self, value):
        self._biz_tid = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotMdeviceprodDeviceInitializeResponse, self).parse_response_content(response_content)
        if 'biz_tid' in response:
            self.biz_tid = response['biz_tid']
