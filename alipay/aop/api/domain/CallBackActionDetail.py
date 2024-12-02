#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CallBackMessageDetail import CallBackMessageDetail


class CallBackActionDetail(object):

    def __init__(self):
        self._action_driver_code = None
        self._call_back_time = None
        self._message_detail = None
        self._message_type = None

    @property
    def action_driver_code(self):
        return self._action_driver_code

    @action_driver_code.setter
    def action_driver_code(self, value):
        self._action_driver_code = value
    @property
    def call_back_time(self):
        return self._call_back_time

    @call_back_time.setter
    def call_back_time(self, value):
        self._call_back_time = value
    @property
    def message_detail(self):
        return self._message_detail

    @message_detail.setter
    def message_detail(self, value):
        if isinstance(value, CallBackMessageDetail):
            self._message_detail = value
        else:
            self._message_detail = CallBackMessageDetail.from_alipay_dict(value)
    @property
    def message_type(self):
        return self._message_type

    @message_type.setter
    def message_type(self, value):
        self._message_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_driver_code:
            if hasattr(self.action_driver_code, 'to_alipay_dict'):
                params['action_driver_code'] = self.action_driver_code.to_alipay_dict()
            else:
                params['action_driver_code'] = self.action_driver_code
        if self.call_back_time:
            if hasattr(self.call_back_time, 'to_alipay_dict'):
                params['call_back_time'] = self.call_back_time.to_alipay_dict()
            else:
                params['call_back_time'] = self.call_back_time
        if self.message_detail:
            if hasattr(self.message_detail, 'to_alipay_dict'):
                params['message_detail'] = self.message_detail.to_alipay_dict()
            else:
                params['message_detail'] = self.message_detail
        if self.message_type:
            if hasattr(self.message_type, 'to_alipay_dict'):
                params['message_type'] = self.message_type.to_alipay_dict()
            else:
                params['message_type'] = self.message_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CallBackActionDetail()
        if 'action_driver_code' in d:
            o.action_driver_code = d['action_driver_code']
        if 'call_back_time' in d:
            o.call_back_time = d['call_back_time']
        if 'message_detail' in d:
            o.message_detail = d['message_detail']
        if 'message_type' in d:
            o.message_type = d['message_type']
        return o


