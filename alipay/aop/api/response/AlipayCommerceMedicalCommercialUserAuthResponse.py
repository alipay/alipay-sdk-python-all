#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalCommercialUserAuthResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalCommercialUserAuthResponse, self).__init__()
        self._open_id = None
        self._staff_user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def staff_user_id(self):
        return self._staff_user_id

    @staff_user_id.setter
    def staff_user_id(self, value):
        self._staff_user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalCommercialUserAuthResponse, self).parse_response_content(response_content)
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'staff_user_id' in response:
            self.staff_user_id = response['staff_user_id']
