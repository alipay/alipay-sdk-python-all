#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceDataResultSendModel(object):

    def __init__(self):
        self._channel = None
        self._interface_version = None
        self._op_code = None
        self._result_code = None
        self._scene_code = None
        self._scene_data = None
        self._target_id = None
        self._target_id_type = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def interface_version(self):
        return self._interface_version

    @interface_version.setter
    def interface_version(self, value):
        self._interface_version = value
    @property
    def op_code(self):
        return self._op_code

    @op_code.setter
    def op_code(self, value):
        self._op_code = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def scene_data(self):
        return self._scene_data

    @scene_data.setter
    def scene_data(self, value):
        self._scene_data = value
    @property
    def target_id(self):
        return self._target_id

    @target_id.setter
    def target_id(self, value):
        self._target_id = value
    @property
    def target_id_type(self):
        return self._target_id_type

    @target_id_type.setter
    def target_id_type(self, value):
        self._target_id_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.interface_version:
            if hasattr(self.interface_version, 'to_alipay_dict'):
                params['interface_version'] = self.interface_version.to_alipay_dict()
            else:
                params['interface_version'] = self.interface_version
        if self.op_code:
            if hasattr(self.op_code, 'to_alipay_dict'):
                params['op_code'] = self.op_code.to_alipay_dict()
            else:
                params['op_code'] = self.op_code
        if self.result_code:
            if hasattr(self.result_code, 'to_alipay_dict'):
                params['result_code'] = self.result_code.to_alipay_dict()
            else:
                params['result_code'] = self.result_code
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.scene_data:
            if hasattr(self.scene_data, 'to_alipay_dict'):
                params['scene_data'] = self.scene_data.to_alipay_dict()
            else:
                params['scene_data'] = self.scene_data
        if self.target_id:
            if hasattr(self.target_id, 'to_alipay_dict'):
                params['target_id'] = self.target_id.to_alipay_dict()
            else:
                params['target_id'] = self.target_id
        if self.target_id_type:
            if hasattr(self.target_id_type, 'to_alipay_dict'):
                params['target_id_type'] = self.target_id_type.to_alipay_dict()
            else:
                params['target_id_type'] = self.target_id_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceDataResultSendModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'interface_version' in d:
            o.interface_version = d['interface_version']
        if 'op_code' in d:
            o.op_code = d['op_code']
        if 'result_code' in d:
            o.result_code = d['result_code']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'scene_data' in d:
            o.scene_data = d['scene_data']
        if 'target_id' in d:
            o.target_id = d['target_id']
        if 'target_id_type' in d:
            o.target_id_type = d['target_id_type']
        return o


