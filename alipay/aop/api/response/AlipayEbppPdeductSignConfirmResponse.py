#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppPdeductSignConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppPdeductSignConfirmResponse, self).__init__()
        self._agreement_id = None
        self._alipay_sign_status = None
        self._rtn_flag = None
        self._rtn_msg = None
        self._serial_no = None

    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def alipay_sign_status(self):
        return self._alipay_sign_status

    @alipay_sign_status.setter
    def alipay_sign_status(self, value):
        self._alipay_sign_status = value
    @property
    def rtn_flag(self):
        return self._rtn_flag

    @rtn_flag.setter
    def rtn_flag(self, value):
        self._rtn_flag = value
    @property
    def rtn_msg(self):
        return self._rtn_msg

    @rtn_msg.setter
    def rtn_msg(self, value):
        self._rtn_msg = value
    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppPdeductSignConfirmResponse, self).parse_response_content(response_content)
        if 'agreement_id' in response:
            self.agreement_id = response['agreement_id']
        if 'alipay_sign_status' in response:
            self.alipay_sign_status = response['alipay_sign_status']
        if 'rtn_flag' in response:
            self.rtn_flag = response['rtn_flag']
        if 'rtn_msg' in response:
            self.rtn_msg = response['rtn_msg']
        if 'serial_no' in response:
            self.serial_no = response['serial_no']
