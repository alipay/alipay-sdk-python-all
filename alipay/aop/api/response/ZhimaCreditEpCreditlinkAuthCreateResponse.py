#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpCreditlinkAuthCreateResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpCreditlinkAuthCreateResponse, self).__init__()
        self._biz_no = None
        self._expire_time = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpCreditlinkAuthCreateResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'expire_time' in response:
            self.expire_time = response['expire_time']
