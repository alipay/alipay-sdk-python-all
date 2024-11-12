#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BizOrderMessage(object):

    def __init__(self):
        self._biz_flow_id = None
        self._biz_value = None
        self._create_time = None
        self._message_id = None
        self._message_type = None

    @property
    def biz_flow_id(self):
        return self._biz_flow_id

    @biz_flow_id.setter
    def biz_flow_id(self, value):
        self._biz_flow_id = value
    @property
    def biz_value(self):
        return self._biz_value

    @biz_value.setter
    def biz_value(self, value):
        self._biz_value = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def message_id(self):
        return self._message_id

    @message_id.setter
    def message_id(self, value):
        self._message_id = value
    @property
    def message_type(self):
        return self._message_type

    @message_type.setter
    def message_type(self, value):
        self._message_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_flow_id:
            if hasattr(self.biz_flow_id, 'to_alipay_dict'):
                params['biz_flow_id'] = self.biz_flow_id.to_alipay_dict()
            else:
                params['biz_flow_id'] = self.biz_flow_id
        if self.biz_value:
            if hasattr(self.biz_value, 'to_alipay_dict'):
                params['biz_value'] = self.biz_value.to_alipay_dict()
            else:
                params['biz_value'] = self.biz_value
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.message_id:
            if hasattr(self.message_id, 'to_alipay_dict'):
                params['message_id'] = self.message_id.to_alipay_dict()
            else:
                params['message_id'] = self.message_id
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
        o = BizOrderMessage()
        if 'biz_flow_id' in d:
            o.biz_flow_id = d['biz_flow_id']
        if 'biz_value' in d:
            o.biz_value = d['biz_value']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'message_id' in d:
            o.message_id = d['message_id']
        if 'message_type' in d:
            o.message_type = d['message_type']
        return o


