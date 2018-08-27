#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAgreementSignEffectResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAgreementSignEffectResponse, self).__init__()
        self._agreement_no = None
        self._alipay_logon_id = None
        self._device_id = None
        self._external_agreement_no = None
        self._external_logon_id = None
        self._invalid_time = None
        self._personal_product_code = None
        self._pricipal_type = None
        self._principal_id = None
        self._sign_scene = None
        self._sign_time = None
        self._status = None
        self._third_party_type = None
        self._valid_time = None
        self._zm_open_id = None

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
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def external_agreement_no(self):
        return self._external_agreement_no

    @external_agreement_no.setter
    def external_agreement_no(self, value):
        self._external_agreement_no = value
    @property
    def external_logon_id(self):
        return self._external_logon_id

    @external_logon_id.setter
    def external_logon_id(self, value):
        self._external_logon_id = value
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
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
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
    @property
    def zm_open_id(self):
        return self._zm_open_id

    @zm_open_id.setter
    def zm_open_id(self, value):
        self._zm_open_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAgreementSignEffectResponse, self).parse_response_content(response_content)
        if 'agreement_no' in response:
            self.agreement_no = response['agreement_no']
        if 'alipay_logon_id' in response:
            self.alipay_logon_id = response['alipay_logon_id']
        if 'device_id' in response:
            self.device_id = response['device_id']
        if 'external_agreement_no' in response:
            self.external_agreement_no = response['external_agreement_no']
        if 'external_logon_id' in response:
            self.external_logon_id = response['external_logon_id']
        if 'invalid_time' in response:
            self.invalid_time = response['invalid_time']
        if 'personal_product_code' in response:
            self.personal_product_code = response['personal_product_code']
        if 'pricipal_type' in response:
            self.pricipal_type = response['pricipal_type']
        if 'principal_id' in response:
            self.principal_id = response['principal_id']
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
        if 'zm_open_id' in response:
            self.zm_open_id = response['zm_open_id']
