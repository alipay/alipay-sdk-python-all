#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicOdpsCrowdSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicOdpsCrowdSyncResponse, self).__init__()
        self._biz_no = None
        self._crowd_id = None
        self._dmp_id = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def crowd_id(self):
        return self._crowd_id

    @crowd_id.setter
    def crowd_id(self, value):
        self._crowd_id = value
    @property
    def dmp_id(self):
        return self._dmp_id

    @dmp_id.setter
    def dmp_id(self, value):
        self._dmp_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicOdpsCrowdSyncResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'crowd_id' in response:
            self.crowd_id = response['crowd_id']
        if 'dmp_id' in response:
            self.dmp_id = response['dmp_id']
