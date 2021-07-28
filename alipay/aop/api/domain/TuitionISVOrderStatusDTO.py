#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TuitionISVOrderStatusDTO(object):

    def __init__(self):
        self._error_code = None
        self._error_message = None
        self._status_code = None
        self._status_desc = None

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
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, value):
        self._status_code = value
    @property
    def status_desc(self):
        return self._status_desc

    @status_desc.setter
    def status_desc(self, value):
        self._status_desc = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.status_code:
            if hasattr(self.status_code, 'to_alipay_dict'):
                params['status_code'] = self.status_code.to_alipay_dict()
            else:
                params['status_code'] = self.status_code
        if self.status_desc:
            if hasattr(self.status_desc, 'to_alipay_dict'):
                params['status_desc'] = self.status_desc.to_alipay_dict()
            else:
                params['status_desc'] = self.status_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TuitionISVOrderStatusDTO()
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'error_message' in d:
            o.error_message = d['error_message']
        if 'status_code' in d:
            o.status_code = d['status_code']
        if 'status_desc' in d:
            o.status_desc = d['status_desc']
        return o


