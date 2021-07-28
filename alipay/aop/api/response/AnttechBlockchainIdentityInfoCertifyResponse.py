#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainIdentityInfoCertifyResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainIdentityInfoCertifyResponse, self).__init__()
        self._acc_id = None
        self._code = None
        self._customer_id = None
        self._did = None
        self._pass = None
        self._req_msg_id = None
        self._success = None
        self._sys_err_code = None
        self._sys_err_msg = None

    @property
    def acc_id(self):
        return self._acc_id

    @acc_id.setter
    def acc_id(self, value):
        self._acc_id = value
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def did(self):
        return self._did

    @did.setter
    def did(self, value):
        self._did = value
    @property
    def pass(self):
        return self._pass

    @pass.setter
    def pass(self, value):
        self._pass = value
    @property
    def req_msg_id(self):
        return self._req_msg_id

    @req_msg_id.setter
    def req_msg_id(self, value):
        self._req_msg_id = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def sys_err_code(self):
        return self._sys_err_code

    @sys_err_code.setter
    def sys_err_code(self, value):
        self._sys_err_code = value
    @property
    def sys_err_msg(self):
        return self._sys_err_msg

    @sys_err_msg.setter
    def sys_err_msg(self, value):
        self._sys_err_msg = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainIdentityInfoCertifyResponse, self).parse_response_content(response_content)
        if 'acc_id' in response:
            self.acc_id = response['acc_id']
        if 'code' in response:
            self.code = response['code']
        if 'customer_id' in response:
            self.customer_id = response['customer_id']
        if 'did' in response:
            self.did = response['did']
        if 'pass' in response:
            self.pass = response['pass']
        if 'req_msg_id' in response:
            self.req_msg_id = response['req_msg_id']
        if 'success' in response:
            self.success = response['success']
        if 'sys_err_code' in response:
            self.sys_err_code = response['sys_err_code']
        if 'sys_err_msg' in response:
            self.sys_err_msg = response['sys_err_msg']
