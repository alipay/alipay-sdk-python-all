#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ISVLogSync(object):

    def __init__(self):
        self._application = None
        self._error_code = None
        self._error_msg = None
        self._exception_stack_trace = None
        self._execution_millis = None
        self._interface_name = None
        self._success = None
        self._sync_type = None
        self._timestamp = None

    @property
    def application(self):
        return self._application

    @application.setter
    def application(self, value):
        self._application = value
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
    def exception_stack_trace(self):
        return self._exception_stack_trace

    @exception_stack_trace.setter
    def exception_stack_trace(self, value):
        self._exception_stack_trace = value
    @property
    def execution_millis(self):
        return self._execution_millis

    @execution_millis.setter
    def execution_millis(self, value):
        self._execution_millis = value
    @property
    def interface_name(self):
        return self._interface_name

    @interface_name.setter
    def interface_name(self, value):
        self._interface_name = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def sync_type(self):
        return self._sync_type

    @sync_type.setter
    def sync_type(self, value):
        self._sync_type = value
    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = value


    def to_alipay_dict(self):
        params = dict()
        if self.application:
            if hasattr(self.application, 'to_alipay_dict'):
                params['application'] = self.application.to_alipay_dict()
            else:
                params['application'] = self.application
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
        if self.exception_stack_trace:
            if hasattr(self.exception_stack_trace, 'to_alipay_dict'):
                params['exception_stack_trace'] = self.exception_stack_trace.to_alipay_dict()
            else:
                params['exception_stack_trace'] = self.exception_stack_trace
        if self.execution_millis:
            if hasattr(self.execution_millis, 'to_alipay_dict'):
                params['execution_millis'] = self.execution_millis.to_alipay_dict()
            else:
                params['execution_millis'] = self.execution_millis
        if self.interface_name:
            if hasattr(self.interface_name, 'to_alipay_dict'):
                params['interface_name'] = self.interface_name.to_alipay_dict()
            else:
                params['interface_name'] = self.interface_name
        if self.success:
            if hasattr(self.success, 'to_alipay_dict'):
                params['success'] = self.success.to_alipay_dict()
            else:
                params['success'] = self.success
        if self.sync_type:
            if hasattr(self.sync_type, 'to_alipay_dict'):
                params['sync_type'] = self.sync_type.to_alipay_dict()
            else:
                params['sync_type'] = self.sync_type
        if self.timestamp:
            if hasattr(self.timestamp, 'to_alipay_dict'):
                params['timestamp'] = self.timestamp.to_alipay_dict()
            else:
                params['timestamp'] = self.timestamp
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ISVLogSync()
        if 'application' in d:
            o.application = d['application']
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'error_msg' in d:
            o.error_msg = d['error_msg']
        if 'exception_stack_trace' in d:
            o.exception_stack_trace = d['exception_stack_trace']
        if 'execution_millis' in d:
            o.execution_millis = d['execution_millis']
        if 'interface_name' in d:
            o.interface_name = d['interface_name']
        if 'success' in d:
            o.success = d['success']
        if 'sync_type' in d:
            o.sync_type = d['sync_type']
        if 'timestamp' in d:
            o.timestamp = d['timestamp']
        return o


