#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserInfoInnerQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserInfoInnerQueryResponse, self).__init__()
        self._binded_mobile = None
        self._email = None
        self._email_logon_id = None
        self._havana_id = None
        self._inst_type = None
        self._is_enable_payment = None
        self._is_forbidden_withdraw = None
        self._mobile_logon_id = None
        self._user_id = None
        self._user_status = None
        self._zid = None

    @property
    def binded_mobile(self):
        return self._binded_mobile

    @binded_mobile.setter
    def binded_mobile(self, value):
        self._binded_mobile = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def email_logon_id(self):
        return self._email_logon_id

    @email_logon_id.setter
    def email_logon_id(self, value):
        self._email_logon_id = value
    @property
    def havana_id(self):
        return self._havana_id

    @havana_id.setter
    def havana_id(self, value):
        self._havana_id = value
    @property
    def inst_type(self):
        return self._inst_type

    @inst_type.setter
    def inst_type(self, value):
        self._inst_type = value
    @property
    def is_enable_payment(self):
        return self._is_enable_payment

    @is_enable_payment.setter
    def is_enable_payment(self, value):
        self._is_enable_payment = value
    @property
    def is_forbidden_withdraw(self):
        return self._is_forbidden_withdraw

    @is_forbidden_withdraw.setter
    def is_forbidden_withdraw(self, value):
        self._is_forbidden_withdraw = value
    @property
    def mobile_logon_id(self):
        return self._mobile_logon_id

    @mobile_logon_id.setter
    def mobile_logon_id(self, value):
        self._mobile_logon_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_status(self):
        return self._user_status

    @user_status.setter
    def user_status(self, value):
        self._user_status = value
    @property
    def zid(self):
        return self._zid

    @zid.setter
    def zid(self, value):
        self._zid = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserInfoInnerQueryResponse, self).parse_response_content(response_content)
        if 'binded_mobile' in response:
            self.binded_mobile = response['binded_mobile']
        if 'email' in response:
            self.email = response['email']
        if 'email_logon_id' in response:
            self.email_logon_id = response['email_logon_id']
        if 'havana_id' in response:
            self.havana_id = response['havana_id']
        if 'inst_type' in response:
            self.inst_type = response['inst_type']
        if 'is_enable_payment' in response:
            self.is_enable_payment = response['is_enable_payment']
        if 'is_forbidden_withdraw' in response:
            self.is_forbidden_withdraw = response['is_forbidden_withdraw']
        if 'mobile_logon_id' in response:
            self.mobile_logon_id = response['mobile_logon_id']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'user_status' in response:
            self.user_status = response['user_status']
        if 'zid' in response:
            self.zid = response['zid']
