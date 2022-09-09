#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VehicleCommand(object):

    def __init__(self):
        self._command_desc = None
        self._command_result = None
        self._command_seq_no = None
        self._command_timestamp = None
        self._command_type = None
        self._command_value = None

    @property
    def command_desc(self):
        return self._command_desc

    @command_desc.setter
    def command_desc(self, value):
        self._command_desc = value
    @property
    def command_result(self):
        return self._command_result

    @command_result.setter
    def command_result(self, value):
        self._command_result = value
    @property
    def command_seq_no(self):
        return self._command_seq_no

    @command_seq_no.setter
    def command_seq_no(self, value):
        self._command_seq_no = value
    @property
    def command_timestamp(self):
        return self._command_timestamp

    @command_timestamp.setter
    def command_timestamp(self, value):
        self._command_timestamp = value
    @property
    def command_type(self):
        return self._command_type

    @command_type.setter
    def command_type(self, value):
        self._command_type = value
    @property
    def command_value(self):
        return self._command_value

    @command_value.setter
    def command_value(self, value):
        self._command_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.command_desc:
            if hasattr(self.command_desc, 'to_alipay_dict'):
                params['command_desc'] = self.command_desc.to_alipay_dict()
            else:
                params['command_desc'] = self.command_desc
        if self.command_result:
            if hasattr(self.command_result, 'to_alipay_dict'):
                params['command_result'] = self.command_result.to_alipay_dict()
            else:
                params['command_result'] = self.command_result
        if self.command_seq_no:
            if hasattr(self.command_seq_no, 'to_alipay_dict'):
                params['command_seq_no'] = self.command_seq_no.to_alipay_dict()
            else:
                params['command_seq_no'] = self.command_seq_no
        if self.command_timestamp:
            if hasattr(self.command_timestamp, 'to_alipay_dict'):
                params['command_timestamp'] = self.command_timestamp.to_alipay_dict()
            else:
                params['command_timestamp'] = self.command_timestamp
        if self.command_type:
            if hasattr(self.command_type, 'to_alipay_dict'):
                params['command_type'] = self.command_type.to_alipay_dict()
            else:
                params['command_type'] = self.command_type
        if self.command_value:
            if hasattr(self.command_value, 'to_alipay_dict'):
                params['command_value'] = self.command_value.to_alipay_dict()
            else:
                params['command_value'] = self.command_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VehicleCommand()
        if 'command_desc' in d:
            o.command_desc = d['command_desc']
        if 'command_result' in d:
            o.command_result = d['command_result']
        if 'command_seq_no' in d:
            o.command_seq_no = d['command_seq_no']
        if 'command_timestamp' in d:
            o.command_timestamp = d['command_timestamp']
        if 'command_type' in d:
            o.command_type = d['command_type']
        if 'command_value' in d:
            o.command_value = d['command_value']
        return o


