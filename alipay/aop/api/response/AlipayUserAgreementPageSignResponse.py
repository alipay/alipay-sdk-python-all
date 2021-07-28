#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAgreementPageSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAgreementPageSignResponse, self).__init__()
        self._agreement_no = None
        self._alipay_logon_id = None
        self._alipay_user_id = None
        self._credit_auth_mode = None
        self._external_agreement_no = None
        self._external_logon_id = None
        self._forex_eligible = None
        self._invalid_time = None
        self._personal_product_code = None
        self._sign_scene = None
        self._sign_time = None
        self._specified_sort_assets = None
        self._status = None
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
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def credit_auth_mode(self):
        return self._credit_auth_mode

    @credit_auth_mode.setter
    def credit_auth_mode(self, value):
        self._credit_auth_mode = value
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
    def forex_eligible(self):
        return self._forex_eligible

    @forex_eligible.setter
    def forex_eligible(self, value):
        self._forex_eligible = value
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
    def specified_sort_assets(self):
        return self._specified_sort_assets

    @specified_sort_assets.setter
    def specified_sort_assets(self, value):
        self._specified_sort_assets = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
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
        response = super(AlipayUserAgreementPageSignResponse, self).parse_response_content(response_content)
        if 'agreement_no' in response:
            self.agreement_no = response['agreement_no']
        if 'alipay_logon_id' in response:
            self.alipay_logon_id = response['alipay_logon_id']
        if 'alipay_user_id' in response:
            self.alipay_user_id = response['alipay_user_id']
        if 'credit_auth_mode' in response:
            self.credit_auth_mode = response['credit_auth_mode']
        if 'external_agreement_no' in response:
            self.external_agreement_no = response['external_agreement_no']
        if 'external_logon_id' in response:
            self.external_logon_id = response['external_logon_id']
        if 'forex_eligible' in response:
            self.forex_eligible = response['forex_eligible']
        if 'invalid_time' in response:
            self.invalid_time = response['invalid_time']
        if 'personal_product_code' in response:
            self.personal_product_code = response['personal_product_code']
        if 'sign_scene' in response:
            self.sign_scene = response['sign_scene']
        if 'sign_time' in response:
            self.sign_time = response['sign_time']
        if 'specified_sort_assets' in response:
            self.specified_sort_assets = response['specified_sort_assets']
        if 'status' in response:
            self.status = response['status']
        if 'valid_time' in response:
            self.valid_time = response['valid_time']
        if 'zm_open_id' in response:
            self.zm_open_id = response['zm_open_id']
