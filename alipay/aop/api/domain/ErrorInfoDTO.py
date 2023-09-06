#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ErrorInfoDTO(object):

    def __init__(self):
        self._contact_user_id = None
        self._error_code = None
        self._error_message = None

    @property
    def contact_user_id(self):
        return self._contact_user_id

    @contact_user_id.setter
    def contact_user_id(self, value):
        self._contact_user_id = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.contact_user_id:
            if hasattr(self.contact_user_id, 'to_alipay_dict'):
                params['contact_user_id'] = self.contact_user_id.to_alipay_dict()
            else:
                params['contact_user_id'] = self.contact_user_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ErrorInfoDTO()
        if 'contact_user_id' in d:
            o.contact_user_id = d['contact_user_id']
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'error_message' in d:
            o.error_message = d['error_message']
        return o


