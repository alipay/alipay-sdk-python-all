#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneInsserviceprodSerprivacyApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneInsserviceprodSerprivacyApplyResponse, self).__init__()
        self._bind_phone = None
        self._expired_time = None
        self._extension_no = None

    @property
    def bind_phone(self):
        return self._bind_phone

    @bind_phone.setter
    def bind_phone(self, value):
        self._bind_phone = value
    @property
    def expired_time(self):
        return self._expired_time

    @expired_time.setter
    def expired_time(self, value):
        self._expired_time = value
    @property
    def extension_no(self):
        return self._extension_no

    @extension_no.setter
    def extension_no(self, value):
        self._extension_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneInsserviceprodSerprivacyApplyResponse, self).parse_response_content(response_content)
        if 'bind_phone' in response:
            self.bind_phone = response['bind_phone']
        if 'expired_time' in response:
            self.expired_time = response['expired_time']
        if 'extension_no' in response:
            self.extension_no = response['extension_no']
