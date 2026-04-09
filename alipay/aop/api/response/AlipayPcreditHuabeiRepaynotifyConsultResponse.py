#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiRepaynotifyConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiRepaynotifyConsultResponse, self).__init__()
        self._consult_code = None
        self._do_call = None
        self._phone = None
        self._re_consult = None
        self._reason = None
        self._user_id = None
        self._user_open_id = None
        self._voice_code = None

    @property
    def consult_code(self):
        return self._consult_code

    @consult_code.setter
    def consult_code(self, value):
        self._consult_code = value
    @property
    def do_call(self):
        return self._do_call

    @do_call.setter
    def do_call(self, value):
        self._do_call = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def re_consult(self):
        return self._re_consult

    @re_consult.setter
    def re_consult(self, value):
        self._re_consult = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_open_id(self):
        return self._user_open_id

    @user_open_id.setter
    def user_open_id(self, value):
        self._user_open_id = value
    @property
    def voice_code(self):
        return self._voice_code

    @voice_code.setter
    def voice_code(self, value):
        self._voice_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiRepaynotifyConsultResponse, self).parse_response_content(response_content)
        if 'consult_code' in response:
            self.consult_code = response['consult_code']
        if 'do_call' in response:
            self.do_call = response['do_call']
        if 'phone' in response:
            self.phone = response['phone']
        if 're_consult' in response:
            self.re_consult = response['re_consult']
        if 'reason' in response:
            self.reason = response['reason']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'user_open_id' in response:
            self.user_open_id = response['user_open_id']
        if 'voice_code' in response:
            self.voice_code = response['voice_code']
