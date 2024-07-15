#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudFundAgreementQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudFundAgreementQueryResponse, self).__init__()
        self._agreement_no = None
        self._alipay_logon_id = None
        self._invalid_time = None
        self._personal_product_code = None
        self._pricipal_type = None
        self._sign_scene = None
        self._sign_time = None
        self._status = None
        self._third_party_type = None
        self._valid_time = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def alipay_logon_id(self):
        return self._alipay_logon_id

    @alipay_logon_id.setter
    def alipay_logon_id(self, value):
        self._alipay_logon_id = value
    @property
    def invalid_time(self):
        return self._invalid_time

    @invalid_time.setter
    def invalid_time(self, value):
        self._invalid_time = value
    @property
    def personal_product_code(self):
        return self._personal_product_code

    @personal_product_code.setter
    def personal_product_code(self, value):
        self._personal_product_code = value
    @property
    def pricipal_type(self):
        return self._pricipal_type

    @pricipal_type.setter
    def pricipal_type(self, value):
        self._pricipal_type = value
    @property
    def sign_scene(self):
        return self._sign_scene

    @sign_scene.setter
    def sign_scene(self, value):
        self._sign_scene = value
    @property
    def sign_time(self):
        return self._sign_time

    @sign_time.setter
    def sign_time(self, value):
        self._sign_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def third_party_type(self):
        return self._third_party_type

    @third_party_type.setter
    def third_party_type(self, value):
        self._third_party_type = value
    @property
    def valid_time(self):
        return self._valid_time

    @valid_time.setter
    def valid_time(self, value):
        self._valid_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudFundAgreementQueryResponse, self).parse_response_content(response_content)
        if 'agreement_no' in response:
            self.agreement_no = response['agreement_no']
        if 'alipay_logon_id' in response:
            self.alipay_logon_id = response['alipay_logon_id']
        if 'invalid_time' in response:
            self.invalid_time = response['invalid_time']
        if 'personal_product_code' in response:
            self.personal_product_code = response['personal_product_code']
        if 'pricipal_type' in response:
            self.pricipal_type = response['pricipal_type']
        if 'sign_scene' in response:
            self.sign_scene = response['sign_scene']
        if 'sign_time' in response:
            self.sign_time = response['sign_time']
        if 'status' in response:
            self.status = response['status']
        if 'third_party_type' in response:
            self.third_party_type = response['third_party_type']
        if 'valid_time' in response:
            self.valid_time = response['valid_time']
