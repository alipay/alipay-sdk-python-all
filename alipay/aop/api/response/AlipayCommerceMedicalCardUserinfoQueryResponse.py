#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalCardUserinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalCardUserinfoQueryResponse, self).__init__()
        self._medical_card_id = None
        self._user_cert_no = None
        self._user_cert_type = None
        self._username = None

    @property
    def medical_card_id(self):
        return self._medical_card_id

    @medical_card_id.setter
    def medical_card_id(self, value):
        self._medical_card_id = value
    @property
    def user_cert_no(self):
        return self._user_cert_no

    @user_cert_no.setter
    def user_cert_no(self, value):
        self._user_cert_no = value
    @property
    def user_cert_type(self):
        return self._user_cert_type

    @user_cert_type.setter
    def user_cert_type(self, value):
        self._user_cert_type = value
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalCardUserinfoQueryResponse, self).parse_response_content(response_content)
        if 'medical_card_id' in response:
            self.medical_card_id = response['medical_card_id']
        if 'user_cert_no' in response:
            self.user_cert_no = response['user_cert_no']
        if 'user_cert_type' in response:
            self.user_cert_type = response['user_cert_type']
        if 'username' in response:
            self.username = response['username']
