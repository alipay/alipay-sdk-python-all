#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataAntsycmCrowserviceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataAntsycmCrowserviceQueryResponse, self).__init__()
        self._service_type = None
        self._user_sign = None
        self._value = None

    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value
    @property
    def user_sign(self):
        return self._user_sign

    @user_sign.setter
    def user_sign(self, value):
        self._user_sign = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataAntsycmCrowserviceQueryResponse, self).parse_response_content(response_content)
        if 'service_type' in response:
            self.service_type = response['service_type']
        if 'user_sign' in response:
            self.user_sign = response['user_sign']
        if 'value' in response:
            self.value = response['value']
