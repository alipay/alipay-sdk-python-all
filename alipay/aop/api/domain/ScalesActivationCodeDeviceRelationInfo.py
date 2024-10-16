#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ScalesActivationCodeDeviceRelationInfo(object):

    def __init__(self):
        self._activation_code = None
        self._bind_type = None
        self._biz_tid = None
        self._isv_tid = None
        self._operate_time = None
        self._relation_type = None
        self._white_operate_type = None

    @property
    def activation_code(self):
        return self._activation_code

    @activation_code.setter
    def activation_code(self, value):
        self._activation_code = value
    @property
    def bind_type(self):
        return self._bind_type

    @bind_type.setter
    def bind_type(self, value):
        self._bind_type = value
    @property
    def biz_tid(self):
        return self._biz_tid

    @biz_tid.setter
    def biz_tid(self, value):
        self._biz_tid = value
    @property
    def isv_tid(self):
        return self._isv_tid

    @isv_tid.setter
    def isv_tid(self, value):
        self._isv_tid = value
    @property
    def operate_time(self):
        return self._operate_time

    @operate_time.setter
    def operate_time(self, value):
        self._operate_time = value
    @property
    def relation_type(self):
        return self._relation_type

    @relation_type.setter
    def relation_type(self, value):
        self._relation_type = value
    @property
    def white_operate_type(self):
        return self._white_operate_type

    @white_operate_type.setter
    def white_operate_type(self, value):
        self._white_operate_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.activation_code:
            if hasattr(self.activation_code, 'to_alipay_dict'):
                params['activation_code'] = self.activation_code.to_alipay_dict()
            else:
                params['activation_code'] = self.activation_code
        if self.bind_type:
            if hasattr(self.bind_type, 'to_alipay_dict'):
                params['bind_type'] = self.bind_type.to_alipay_dict()
            else:
                params['bind_type'] = self.bind_type
        if self.biz_tid:
            if hasattr(self.biz_tid, 'to_alipay_dict'):
                params['biz_tid'] = self.biz_tid.to_alipay_dict()
            else:
                params['biz_tid'] = self.biz_tid
        if self.isv_tid:
            if hasattr(self.isv_tid, 'to_alipay_dict'):
                params['isv_tid'] = self.isv_tid.to_alipay_dict()
            else:
                params['isv_tid'] = self.isv_tid
        if self.operate_time:
            if hasattr(self.operate_time, 'to_alipay_dict'):
                params['operate_time'] = self.operate_time.to_alipay_dict()
            else:
                params['operate_time'] = self.operate_time
        if self.relation_type:
            if hasattr(self.relation_type, 'to_alipay_dict'):
                params['relation_type'] = self.relation_type.to_alipay_dict()
            else:
                params['relation_type'] = self.relation_type
        if self.white_operate_type:
            if hasattr(self.white_operate_type, 'to_alipay_dict'):
                params['white_operate_type'] = self.white_operate_type.to_alipay_dict()
            else:
                params['white_operate_type'] = self.white_operate_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ScalesActivationCodeDeviceRelationInfo()
        if 'activation_code' in d:
            o.activation_code = d['activation_code']
        if 'bind_type' in d:
            o.bind_type = d['bind_type']
        if 'biz_tid' in d:
            o.biz_tid = d['biz_tid']
        if 'isv_tid' in d:
            o.isv_tid = d['isv_tid']
        if 'operate_time' in d:
            o.operate_time = d['operate_time']
        if 'relation_type' in d:
            o.relation_type = d['relation_type']
        if 'white_operate_type' in d:
            o.white_operate_type = d['white_operate_type']
        return o


