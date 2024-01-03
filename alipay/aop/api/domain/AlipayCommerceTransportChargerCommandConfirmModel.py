#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportChargerCommandConfirmModel(object):

    def __init__(self):
        self._command_result = None
        self._command_serial_number = None

    @property
    def command_result(self):
        return self._command_result

    @command_result.setter
    def command_result(self, value):
        self._command_result = value
    @property
    def command_serial_number(self):
        return self._command_serial_number

    @command_serial_number.setter
    def command_serial_number(self, value):
        self._command_serial_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.command_result:
            if hasattr(self.command_result, 'to_alipay_dict'):
                params['command_result'] = self.command_result.to_alipay_dict()
            else:
                params['command_result'] = self.command_result
        if self.command_serial_number:
            if hasattr(self.command_serial_number, 'to_alipay_dict'):
                params['command_serial_number'] = self.command_serial_number.to_alipay_dict()
            else:
                params['command_serial_number'] = self.command_serial_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportChargerCommandConfirmModel()
        if 'command_result' in d:
            o.command_result = d['command_result']
        if 'command_serial_number' in d:
            o.command_serial_number = d['command_serial_number']
        return o


