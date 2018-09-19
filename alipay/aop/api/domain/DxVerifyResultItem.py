#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DxVerifyResultItem(object):

    def __init__(self):
        self._error_code = None
        self._error_msg = None
        self._input = None
        self._line = None
        self._output = None
        self._predict = None
        self._success = None
        self._trace = None

    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def input(self):
        return self._input

    @input.setter
    def input(self, value):
        self._input = value
    @property
    def line(self):
        return self._line

    @line.setter
    def line(self, value):
        self._line = value
    @property
    def output(self):
        return self._output

    @output.setter
    def output(self, value):
        self._output = value
    @property
    def predict(self):
        return self._predict

    @predict.setter
    def predict(self, value):
        self._predict = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def trace(self):
        return self._trace

    @trace.setter
    def trace(self, value):
        self._trace = value


    def to_alipay_dict(self):
        params = dict()
        if self.error_code:
            if hasattr(self.error_code, 'to_alipay_dict'):
                params['error_code'] = self.error_code.to_alipay_dict()
            else:
                params['error_code'] = self.error_code
        if self.error_msg:
            if hasattr(self.error_msg, 'to_alipay_dict'):
                params['error_msg'] = self.error_msg.to_alipay_dict()
            else:
                params['error_msg'] = self.error_msg
        if self.input:
            if hasattr(self.input, 'to_alipay_dict'):
                params['input'] = self.input.to_alipay_dict()
            else:
                params['input'] = self.input
        if self.line:
            if hasattr(self.line, 'to_alipay_dict'):
                params['line'] = self.line.to_alipay_dict()
            else:
                params['line'] = self.line
        if self.output:
            if hasattr(self.output, 'to_alipay_dict'):
                params['output'] = self.output.to_alipay_dict()
            else:
                params['output'] = self.output
        if self.predict:
            if hasattr(self.predict, 'to_alipay_dict'):
                params['predict'] = self.predict.to_alipay_dict()
            else:
                params['predict'] = self.predict
        if self.success:
            if hasattr(self.success, 'to_alipay_dict'):
                params['success'] = self.success.to_alipay_dict()
            else:
                params['success'] = self.success
        if self.trace:
            if hasattr(self.trace, 'to_alipay_dict'):
                params['trace'] = self.trace.to_alipay_dict()
            else:
                params['trace'] = self.trace
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DxVerifyResultItem()
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'error_msg' in d:
            o.error_msg = d['error_msg']
        if 'input' in d:
            o.input = d['input']
        if 'line' in d:
            o.line = d['line']
        if 'output' in d:
            o.output = d['output']
        if 'predict' in d:
            o.predict = d['predict']
        if 'success' in d:
            o.success = d['success']
        if 'trace' in d:
            o.trace = d['trace']
        return o


