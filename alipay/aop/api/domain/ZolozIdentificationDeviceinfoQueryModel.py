#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZolozIdentificationDeviceinfoQueryModel(object):

    def __init__(self):
        self._apdid_token = None
        self._biz_id = None
        self._terminal_type = None

    @property
    def apdid_token(self):
        return self._apdid_token

    @apdid_token.setter
    def apdid_token(self, value):
        self._apdid_token = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def terminal_type(self):
        return self._terminal_type

    @terminal_type.setter
    def terminal_type(self, value):
        self._terminal_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.apdid_token:
            if hasattr(self.apdid_token, 'to_alipay_dict'):
                params['apdid_token'] = self.apdid_token.to_alipay_dict()
            else:
                params['apdid_token'] = self.apdid_token
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.terminal_type:
            if hasattr(self.terminal_type, 'to_alipay_dict'):
                params['terminal_type'] = self.terminal_type.to_alipay_dict()
            else:
                params['terminal_type'] = self.terminal_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZolozIdentificationDeviceinfoQueryModel()
        if 'apdid_token' in d:
            o.apdid_token = d['apdid_token']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'terminal_type' in d:
            o.terminal_type = d['terminal_type']
        return o


