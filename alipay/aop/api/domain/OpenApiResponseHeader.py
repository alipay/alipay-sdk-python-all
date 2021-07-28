#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiResponseHeader(object):

    def __init__(self):
        self._conversation_id = None
        self._response_id = None
        self._status_code = None
        self._status_message = None
        self._sub_status_code = None

    @property
    def conversation_id(self):
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, value):
        self._conversation_id = value
    @property
    def response_id(self):
        return self._response_id

    @response_id.setter
    def response_id(self, value):
        self._response_id = value
    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, value):
        self._status_code = value
    @property
    def status_message(self):
        return self._status_message

    @status_message.setter
    def status_message(self, value):
        self._status_message = value
    @property
    def sub_status_code(self):
        return self._sub_status_code

    @sub_status_code.setter
    def sub_status_code(self, value):
        self._sub_status_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.conversation_id:
            if hasattr(self.conversation_id, 'to_alipay_dict'):
                params['conversation_id'] = self.conversation_id.to_alipay_dict()
            else:
                params['conversation_id'] = self.conversation_id
        if self.response_id:
            if hasattr(self.response_id, 'to_alipay_dict'):
                params['response_id'] = self.response_id.to_alipay_dict()
            else:
                params['response_id'] = self.response_id
        if self.status_code:
            if hasattr(self.status_code, 'to_alipay_dict'):
                params['status_code'] = self.status_code.to_alipay_dict()
            else:
                params['status_code'] = self.status_code
        if self.status_message:
            if hasattr(self.status_message, 'to_alipay_dict'):
                params['status_message'] = self.status_message.to_alipay_dict()
            else:
                params['status_message'] = self.status_message
        if self.sub_status_code:
            if hasattr(self.sub_status_code, 'to_alipay_dict'):
                params['sub_status_code'] = self.sub_status_code.to_alipay_dict()
            else:
                params['sub_status_code'] = self.sub_status_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiResponseHeader()
        if 'conversation_id' in d:
            o.conversation_id = d['conversation_id']
        if 'response_id' in d:
            o.response_id = d['response_id']
        if 'status_code' in d:
            o.status_code = d['status_code']
        if 'status_message' in d:
            o.status_message = d['status_message']
        if 'sub_status_code' in d:
            o.sub_status_code = d['sub_status_code']
        return o


