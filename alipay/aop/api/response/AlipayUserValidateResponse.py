#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserValidateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserValidateResponse, self).__init__()
        self._alipay_user_id = None
        self._certified = None
        self._real_name = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def certified(self):
        return self._certified

    @certified.setter
    def certified(self, value):
        self._certified = value
    @property
    def real_name(self):
        return self._real_name

    @real_name.setter
    def real_name(self, value):
        self._real_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserValidateResponse, self).parse_response_content(response_content)
        if 'alipay_user_id' in response:
            self.alipay_user_id = response['alipay_user_id']
        if 'certified' in response:
            self.certified = response['certified']
        if 'real_name' in response:
            self.real_name = response['real_name']
