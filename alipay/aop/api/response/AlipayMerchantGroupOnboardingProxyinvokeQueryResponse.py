#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantGroupOnboardingProxyinvokeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupOnboardingProxyinvokeQueryResponse, self).__init__()
        self._app_auth_token = None
        self._auth_app_id = None
        self._confirm_qr_code = None
        self._confirm_qr_code_img_url = None
        self._confirm_web_link = None
        self._fail_code = None
        self._fail_reason = None
        self._gmt_modified = None
        self._isv_pid = None
        self._leads_id = None
        self._merchant_pid = None
        self._status = None
        self._unique_biz_id = None

    @property
    def app_auth_token(self):
        return self._app_auth_token

    @app_auth_token.setter
    def app_auth_token(self, value):
        self._app_auth_token = value
    @property
    def auth_app_id(self):
        return self._auth_app_id

    @auth_app_id.setter
    def auth_app_id(self, value):
        self._auth_app_id = value
    @property
    def confirm_qr_code(self):
        return self._confirm_qr_code

    @confirm_qr_code.setter
    def confirm_qr_code(self, value):
        self._confirm_qr_code = value
    @property
    def confirm_qr_code_img_url(self):
        return self._confirm_qr_code_img_url

    @confirm_qr_code_img_url.setter
    def confirm_qr_code_img_url(self, value):
        self._confirm_qr_code_img_url = value
    @property
    def confirm_web_link(self):
        return self._confirm_web_link

    @confirm_web_link.setter
    def confirm_web_link(self, value):
        self._confirm_web_link = value
    @property
    def fail_code(self):
        return self._fail_code

    @fail_code.setter
    def fail_code(self, value):
        self._fail_code = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def leads_id(self):
        return self._leads_id

    @leads_id.setter
    def leads_id(self, value):
        self._leads_id = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def unique_biz_id(self):
        return self._unique_biz_id

    @unique_biz_id.setter
    def unique_biz_id(self, value):
        self._unique_biz_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupOnboardingProxyinvokeQueryResponse, self).parse_response_content(response_content)
        if 'app_auth_token' in response:
            self.app_auth_token = response['app_auth_token']
        if 'auth_app_id' in response:
            self.auth_app_id = response['auth_app_id']
        if 'confirm_qr_code' in response:
            self.confirm_qr_code = response['confirm_qr_code']
        if 'confirm_qr_code_img_url' in response:
            self.confirm_qr_code_img_url = response['confirm_qr_code_img_url']
        if 'confirm_web_link' in response:
            self.confirm_web_link = response['confirm_web_link']
        if 'fail_code' in response:
            self.fail_code = response['fail_code']
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'isv_pid' in response:
            self.isv_pid = response['isv_pid']
        if 'leads_id' in response:
            self.leads_id = response['leads_id']
        if 'merchant_pid' in response:
            self.merchant_pid = response['merchant_pid']
        if 'status' in response:
            self.status = response['status']
        if 'unique_biz_id' in response:
            self.unique_biz_id = response['unique_biz_id']
