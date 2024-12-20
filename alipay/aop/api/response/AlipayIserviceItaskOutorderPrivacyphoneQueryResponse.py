#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceItaskOutorderPrivacyphoneQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceItaskOutorderPrivacyphoneQueryResponse, self).__init__()
        self._current_expire_time = None
        self._privacy_bind_phone = None

    @property
    def current_expire_time(self):
        return self._current_expire_time

    @current_expire_time.setter
    def current_expire_time(self, value):
        self._current_expire_time = value
    @property
    def privacy_bind_phone(self):
        return self._privacy_bind_phone

    @privacy_bind_phone.setter
    def privacy_bind_phone(self, value):
        self._privacy_bind_phone = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceItaskOutorderPrivacyphoneQueryResponse, self).parse_response_content(response_content)
        if 'current_expire_time' in response:
            self.current_expire_time = response['current_expire_time']
        if 'privacy_bind_phone' in response:
            self.privacy_bind_phone = response['privacy_bind_phone']
