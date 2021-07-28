#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneInsserviceprodSerinfoSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneInsserviceprodSerinfoSyncResponse, self).__init__()
        self._ser_biz_no = None

    @property
    def ser_biz_no(self):
        return self._ser_biz_no

    @ser_biz_no.setter
    def ser_biz_no(self, value):
        self._ser_biz_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneInsserviceprodSerinfoSyncResponse, self).parse_response_content(response_content)
        if 'ser_biz_no' in response:
            self.ser_biz_no = response['ser_biz_no']
