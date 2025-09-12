#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditLoanHonorBindApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanHonorBindApplyResponse, self).__init__()
        self._access = None
        self._alipay_user_id = None
        self._credit_consult_serial_no = None
        self._exempt_verify = None
        self._fail_code = None
        self._fail_reason = None
        self._open_id = None
        self._refuse_control_time = None
        self._refuse_msg_data = None
        self._verify_url = None

    @property
    def access(self):
        return self._access

    @access.setter
    def access(self, value):
        self._access = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def credit_consult_serial_no(self):
        return self._credit_consult_serial_no

    @credit_consult_serial_no.setter
    def credit_consult_serial_no(self, value):
        self._credit_consult_serial_no = value
    @property
    def exempt_verify(self):
        return self._exempt_verify

    @exempt_verify.setter
    def exempt_verify(self, value):
        self._exempt_verify = value
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
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def refuse_control_time(self):
        return self._refuse_control_time

    @refuse_control_time.setter
    def refuse_control_time(self, value):
        self._refuse_control_time = value
    @property
    def refuse_msg_data(self):
        return self._refuse_msg_data

    @refuse_msg_data.setter
    def refuse_msg_data(self, value):
        self._refuse_msg_data = value
    @property
    def verify_url(self):
        return self._verify_url

    @verify_url.setter
    def verify_url(self, value):
        self._verify_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanHonorBindApplyResponse, self).parse_response_content(response_content)
        if 'access' in response:
            self.access = response['access']
        if 'alipay_user_id' in response:
            self.alipay_user_id = response['alipay_user_id']
        if 'credit_consult_serial_no' in response:
            self.credit_consult_serial_no = response['credit_consult_serial_no']
        if 'exempt_verify' in response:
            self.exempt_verify = response['exempt_verify']
        if 'fail_code' in response:
            self.fail_code = response['fail_code']
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'refuse_control_time' in response:
            self.refuse_control_time = response['refuse_control_time']
        if 'refuse_msg_data' in response:
            self.refuse_msg_data = response['refuse_msg_data']
        if 'verify_url' in response:
            self.verify_url = response['verify_url']
