#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppPdeductSignConfirmModel(object):

    def __init__(self):
        self._agent_channel = None
        self._agent_code = None
        self._bill_key = None
        self._charge_inst = None
        self._error_code = None
        self._error_message = None
        self._extend_field = None
        self._out_agreement_id = None
        self._pid = None
        self._serial_no = None
        self._sign_result = None
        self._user_id = None

    @property
    def agent_channel(self):
        return self._agent_channel

    @agent_channel.setter
    def agent_channel(self, value):
        self._agent_channel = value
    @property
    def agent_code(self):
        return self._agent_code

    @agent_code.setter
    def agent_code(self, value):
        self._agent_code = value
    @property
    def bill_key(self):
        return self._bill_key

    @bill_key.setter
    def bill_key(self, value):
        self._bill_key = value
    @property
    def charge_inst(self):
        return self._charge_inst

    @charge_inst.setter
    def charge_inst(self, value):
        self._charge_inst = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value
    @property
    def extend_field(self):
        return self._extend_field

    @extend_field.setter
    def extend_field(self, value):
        self._extend_field = value
    @property
    def out_agreement_id(self):
        return self._out_agreement_id

    @out_agreement_id.setter
    def out_agreement_id(self, value):
        self._out_agreement_id = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value
    @property
    def sign_result(self):
        return self._sign_result

    @sign_result.setter
    def sign_result(self, value):
        self._sign_result = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_channel:
            if hasattr(self.agent_channel, 'to_alipay_dict'):
                params['agent_channel'] = self.agent_channel.to_alipay_dict()
            else:
                params['agent_channel'] = self.agent_channel
        if self.agent_code:
            if hasattr(self.agent_code, 'to_alipay_dict'):
                params['agent_code'] = self.agent_code.to_alipay_dict()
            else:
                params['agent_code'] = self.agent_code
        if self.bill_key:
            if hasattr(self.bill_key, 'to_alipay_dict'):
                params['bill_key'] = self.bill_key.to_alipay_dict()
            else:
                params['bill_key'] = self.bill_key
        if self.charge_inst:
            if hasattr(self.charge_inst, 'to_alipay_dict'):
                params['charge_inst'] = self.charge_inst.to_alipay_dict()
            else:
                params['charge_inst'] = self.charge_inst
        if self.error_code:
            if hasattr(self.error_code, 'to_alipay_dict'):
                params['error_code'] = self.error_code.to_alipay_dict()
            else:
                params['error_code'] = self.error_code
        if self.error_message:
            if hasattr(self.error_message, 'to_alipay_dict'):
                params['error_message'] = self.error_message.to_alipay_dict()
            else:
                params['error_message'] = self.error_message
        if self.extend_field:
            if hasattr(self.extend_field, 'to_alipay_dict'):
                params['extend_field'] = self.extend_field.to_alipay_dict()
            else:
                params['extend_field'] = self.extend_field
        if self.out_agreement_id:
            if hasattr(self.out_agreement_id, 'to_alipay_dict'):
                params['out_agreement_id'] = self.out_agreement_id.to_alipay_dict()
            else:
                params['out_agreement_id'] = self.out_agreement_id
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.serial_no:
            if hasattr(self.serial_no, 'to_alipay_dict'):
                params['serial_no'] = self.serial_no.to_alipay_dict()
            else:
                params['serial_no'] = self.serial_no
        if self.sign_result:
            if hasattr(self.sign_result, 'to_alipay_dict'):
                params['sign_result'] = self.sign_result.to_alipay_dict()
            else:
                params['sign_result'] = self.sign_result
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppPdeductSignConfirmModel()
        if 'agent_channel' in d:
            o.agent_channel = d['agent_channel']
        if 'agent_code' in d:
            o.agent_code = d['agent_code']
        if 'bill_key' in d:
            o.bill_key = d['bill_key']
        if 'charge_inst' in d:
            o.charge_inst = d['charge_inst']
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'error_message' in d:
            o.error_message = d['error_message']
        if 'extend_field' in d:
            o.extend_field = d['extend_field']
        if 'out_agreement_id' in d:
            o.out_agreement_id = d['out_agreement_id']
        if 'pid' in d:
            o.pid = d['pid']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        if 'sign_result' in d:
            o.sign_result = d['sign_result']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


