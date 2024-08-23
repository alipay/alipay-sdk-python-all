#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudpromoFaceCheckCreateModel(object):

    def __init__(self):
        self._biz_no = None
        self._custom_id = None
        self._env_data = None
        self._instance_id = None
        self._scene_type = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def custom_id(self):
        return self._custom_id

    @custom_id.setter
    def custom_id(self, value):
        self._custom_id = value
    @property
    def env_data(self):
        return self._env_data

    @env_data.setter
    def env_data(self, value):
        self._env_data = value
    @property
    def instance_id(self):
        return self._instance_id

    @instance_id.setter
    def instance_id(self, value):
        self._instance_id = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.custom_id:
            if hasattr(self.custom_id, 'to_alipay_dict'):
                params['custom_id'] = self.custom_id.to_alipay_dict()
            else:
                params['custom_id'] = self.custom_id
        if self.env_data:
            if hasattr(self.env_data, 'to_alipay_dict'):
                params['env_data'] = self.env_data.to_alipay_dict()
            else:
                params['env_data'] = self.env_data
        if self.instance_id:
            if hasattr(self.instance_id, 'to_alipay_dict'):
                params['instance_id'] = self.instance_id.to_alipay_dict()
            else:
                params['instance_id'] = self.instance_id
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoFaceCheckCreateModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'custom_id' in d:
            o.custom_id = d['custom_id']
        if 'env_data' in d:
            o.env_data = d['env_data']
        if 'instance_id' in d:
            o.instance_id = d['instance_id']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        return o


