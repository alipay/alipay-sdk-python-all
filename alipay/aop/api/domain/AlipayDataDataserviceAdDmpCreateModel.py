#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdDmpCreateModel(object):

    def __init__(self):
        self._alipay_pid = None
        self._behavior_types = None
        self._biz_token = None
        self._crowd_id = None
        self._crowd_name = None
        self._data_type = None
        self._device_ids = None
        self._expiry_time = None
        self._if_end = None
        self._open_time = None
        self._operate_type = None
        self._principal_tag = None
        self._uuid = None

    @property
    def alipay_pid(self):
        return self._alipay_pid

    @alipay_pid.setter
    def alipay_pid(self, value):
        self._alipay_pid = value
    @property
    def behavior_types(self):
        return self._behavior_types

    @behavior_types.setter
    def behavior_types(self, value):
        if isinstance(value, list):
            self._behavior_types = list()
            for i in value:
                self._behavior_types.append(i)
    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def crowd_id(self):
        return self._crowd_id

    @crowd_id.setter
    def crowd_id(self, value):
        self._crowd_id = value
    @property
    def crowd_name(self):
        return self._crowd_name

    @crowd_name.setter
    def crowd_name(self, value):
        self._crowd_name = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def device_ids(self):
        return self._device_ids

    @device_ids.setter
    def device_ids(self, value):
        if isinstance(value, list):
            self._device_ids = list()
            for i in value:
                self._device_ids.append(i)
    @property
    def expiry_time(self):
        return self._expiry_time

    @expiry_time.setter
    def expiry_time(self, value):
        self._expiry_time = value
    @property
    def if_end(self):
        return self._if_end

    @if_end.setter
    def if_end(self, value):
        self._if_end = value
    @property
    def open_time(self):
        return self._open_time

    @open_time.setter
    def open_time(self, value):
        self._open_time = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def principal_tag(self):
        return self._principal_tag

    @principal_tag.setter
    def principal_tag(self, value):
        self._principal_tag = value
    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        self._uuid = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_pid:
            if hasattr(self.alipay_pid, 'to_alipay_dict'):
                params['alipay_pid'] = self.alipay_pid.to_alipay_dict()
            else:
                params['alipay_pid'] = self.alipay_pid
        if self.behavior_types:
            if isinstance(self.behavior_types, list):
                for i in range(0, len(self.behavior_types)):
                    element = self.behavior_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.behavior_types[i] = element.to_alipay_dict()
            if hasattr(self.behavior_types, 'to_alipay_dict'):
                params['behavior_types'] = self.behavior_types.to_alipay_dict()
            else:
                params['behavior_types'] = self.behavior_types
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.crowd_id:
            if hasattr(self.crowd_id, 'to_alipay_dict'):
                params['crowd_id'] = self.crowd_id.to_alipay_dict()
            else:
                params['crowd_id'] = self.crowd_id
        if self.crowd_name:
            if hasattr(self.crowd_name, 'to_alipay_dict'):
                params['crowd_name'] = self.crowd_name.to_alipay_dict()
            else:
                params['crowd_name'] = self.crowd_name
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.device_ids:
            if isinstance(self.device_ids, list):
                for i in range(0, len(self.device_ids)):
                    element = self.device_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.device_ids[i] = element.to_alipay_dict()
            if hasattr(self.device_ids, 'to_alipay_dict'):
                params['device_ids'] = self.device_ids.to_alipay_dict()
            else:
                params['device_ids'] = self.device_ids
        if self.expiry_time:
            if hasattr(self.expiry_time, 'to_alipay_dict'):
                params['expiry_time'] = self.expiry_time.to_alipay_dict()
            else:
                params['expiry_time'] = self.expiry_time
        if self.if_end:
            if hasattr(self.if_end, 'to_alipay_dict'):
                params['if_end'] = self.if_end.to_alipay_dict()
            else:
                params['if_end'] = self.if_end
        if self.open_time:
            if hasattr(self.open_time, 'to_alipay_dict'):
                params['open_time'] = self.open_time.to_alipay_dict()
            else:
                params['open_time'] = self.open_time
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.principal_tag:
            if hasattr(self.principal_tag, 'to_alipay_dict'):
                params['principal_tag'] = self.principal_tag.to_alipay_dict()
            else:
                params['principal_tag'] = self.principal_tag
        if self.uuid:
            if hasattr(self.uuid, 'to_alipay_dict'):
                params['uuid'] = self.uuid.to_alipay_dict()
            else:
                params['uuid'] = self.uuid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdDmpCreateModel()
        if 'alipay_pid' in d:
            o.alipay_pid = d['alipay_pid']
        if 'behavior_types' in d:
            o.behavior_types = d['behavior_types']
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'crowd_id' in d:
            o.crowd_id = d['crowd_id']
        if 'crowd_name' in d:
            o.crowd_name = d['crowd_name']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'device_ids' in d:
            o.device_ids = d['device_ids']
        if 'expiry_time' in d:
            o.expiry_time = d['expiry_time']
        if 'if_end' in d:
            o.if_end = d['if_end']
        if 'open_time' in d:
            o.open_time = d['open_time']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'principal_tag' in d:
            o.principal_tag = d['principal_tag']
        if 'uuid' in d:
            o.uuid = d['uuid']
        return o


