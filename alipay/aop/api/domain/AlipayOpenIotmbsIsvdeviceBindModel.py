#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotmbsIsvdeviceBindModel(object):

    def __init__(self):
        self._device_category = None
        self._floor_num = None
        self._project_id = None
        self._room_num = None
        self._scene_type = None
        self._sn = None

    @property
    def device_category(self):
        return self._device_category

    @device_category.setter
    def device_category(self, value):
        self._device_category = value
    @property
    def floor_num(self):
        return self._floor_num

    @floor_num.setter
    def floor_num(self, value):
        self._floor_num = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def room_num(self):
        return self._room_num

    @room_num.setter
    def room_num(self, value):
        self._room_num = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_category:
            if hasattr(self.device_category, 'to_alipay_dict'):
                params['device_category'] = self.device_category.to_alipay_dict()
            else:
                params['device_category'] = self.device_category
        if self.floor_num:
            if hasattr(self.floor_num, 'to_alipay_dict'):
                params['floor_num'] = self.floor_num.to_alipay_dict()
            else:
                params['floor_num'] = self.floor_num
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.room_num:
            if hasattr(self.room_num, 'to_alipay_dict'):
                params['room_num'] = self.room_num.to_alipay_dict()
            else:
                params['room_num'] = self.room_num
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotmbsIsvdeviceBindModel()
        if 'device_category' in d:
            o.device_category = d['device_category']
        if 'floor_num' in d:
            o.floor_num = d['floor_num']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'room_num' in d:
            o.room_num = d['room_num']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        if 'sn' in d:
            o.sn = d['sn']
        return o


