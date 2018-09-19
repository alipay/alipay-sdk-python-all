#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class McardNotifyMessage(object):

    def __init__(self):
        self._change_reason = None
        self._ext_info = None
        self._message_type = None

    @property
    def change_reason(self):
        return self._change_reason

    @change_reason.setter
    def change_reason(self, value):
        self._change_reason = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def message_type(self):
        return self._message_type

    @message_type.setter
    def message_type(self, value):
        self._message_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.change_reason:
            if hasattr(self.change_reason, 'to_alipay_dict'):
                params['change_reason'] = self.change_reason.to_alipay_dict()
            else:
                params['change_reason'] = self.change_reason
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
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
        o = McardNotifyMessage()
        if 'change_reason' in d:
            o.change_reason = d['change_reason']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'message_type' in d:
            o.message_type = d['message_type']
        return o


