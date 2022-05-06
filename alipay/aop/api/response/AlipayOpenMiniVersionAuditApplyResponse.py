#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniVersionAuditApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniVersionAuditApplyResponse, self).__init__()
        self._speed_up = None
        self._speed_up_memo = None

    @property
    def speed_up(self):
        return self._speed_up

    @speed_up.setter
    def speed_up(self, value):
        self._speed_up = value
    @property
    def speed_up_memo(self):
        return self._speed_up_memo

    @speed_up_memo.setter
    def speed_up_memo(self, value):
        self._speed_up_memo = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniVersionAuditApplyResponse, self).parse_response_content(response_content)
        if 'speed_up' in response:
            self.speed_up = response['speed_up']
        if 'speed_up_memo' in response:
            self.speed_up_memo = response['speed_up_memo']
