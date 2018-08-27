#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceDataSendModel(object):

    def __init__(self):
        self._channel = None
        self._op_code = None
        self._op_data = None
        self._scene_code = None
        self._scene_data = None
        self._target_id = None
        self._target_id_type = None
        self._version = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def op_code(self):
        return self._op_code

    @op_code.setter
    def op_code(self, value):
        self._op_code = value
    @property
    def op_data(self):
        return self._op_data

    @op_data.setter
    def op_data(self, value):
        self._op_data = value
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
    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.op_code:
            if hasattr(self.op_code, 'to_alipay_dict'):
                params['op_code'] = self.op_code.to_alipay_dict()
            else:
                params['op_code'] = self.op_code
        if self.op_data:
            if hasattr(self.op_data, 'to_alipay_dict'):
                params['op_data'] = self.op_data.to_alipay_dict()
            else:
                params['op_data'] = self.op_data
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
        if self.version:
            if hasattr(self.version, 'to_alipay_dict'):
                params['version'] = self.version.to_alipay_dict()
            else:
                params['version'] = self.version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceDataSendModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'op_code' in d:
            o.op_code = d['op_code']
        if 'op_data' in d:
            o.op_data = d['op_data']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'scene_data' in d:
            o.scene_data = d['scene_data']
        if 'target_id' in d:
            o.target_id = d['target_id']
        if 'target_id_type' in d:
            o.target_id_type = d['target_id_type']
        if 'version' in d:
            o.version = d['version']
        return o


