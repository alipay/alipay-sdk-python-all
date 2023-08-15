#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MpcSceneQueryInfo(object):

    def __init__(self):
        self._goods_id = None
        self._last_operator = None
        self._position_code = None
        self._recomment_type = None
        self._scene_description = None
        self._scene_id = None
        self._scene_project_name = None
        self._status = None

    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        if isinstance(value, list):
            self._goods_id = list()
            for i in value:
                self._goods_id.append(i)
    @property
    def last_operator(self):
        return self._last_operator

    @last_operator.setter
    def last_operator(self, value):
        self._last_operator = value
    @property
    def position_code(self):
        return self._position_code

    @position_code.setter
    def position_code(self, value):
        self._position_code = value
    @property
    def recomment_type(self):
        return self._recomment_type

    @recomment_type.setter
    def recomment_type(self, value):
        self._recomment_type = value
    @property
    def scene_description(self):
        return self._scene_description

    @scene_description.setter
    def scene_description(self, value):
        self._scene_description = value
    @property
    def scene_id(self):
        return self._scene_id

    @scene_id.setter
    def scene_id(self, value):
        self._scene_id = value
    @property
    def scene_project_name(self):
        return self._scene_project_name

    @scene_project_name.setter
    def scene_project_name(self, value):
        self._scene_project_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_id:
            if isinstance(self.goods_id, list):
                for i in range(0, len(self.goods_id)):
                    element = self.goods_id[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_id[i] = element.to_alipay_dict()
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.last_operator:
            if hasattr(self.last_operator, 'to_alipay_dict'):
                params['last_operator'] = self.last_operator.to_alipay_dict()
            else:
                params['last_operator'] = self.last_operator
        if self.position_code:
            if hasattr(self.position_code, 'to_alipay_dict'):
                params['position_code'] = self.position_code.to_alipay_dict()
            else:
                params['position_code'] = self.position_code
        if self.recomment_type:
            if hasattr(self.recomment_type, 'to_alipay_dict'):
                params['recomment_type'] = self.recomment_type.to_alipay_dict()
            else:
                params['recomment_type'] = self.recomment_type
        if self.scene_description:
            if hasattr(self.scene_description, 'to_alipay_dict'):
                params['scene_description'] = self.scene_description.to_alipay_dict()
            else:
                params['scene_description'] = self.scene_description
        if self.scene_id:
            if hasattr(self.scene_id, 'to_alipay_dict'):
                params['scene_id'] = self.scene_id.to_alipay_dict()
            else:
                params['scene_id'] = self.scene_id
        if self.scene_project_name:
            if hasattr(self.scene_project_name, 'to_alipay_dict'):
                params['scene_project_name'] = self.scene_project_name.to_alipay_dict()
            else:
                params['scene_project_name'] = self.scene_project_name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MpcSceneQueryInfo()
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'last_operator' in d:
            o.last_operator = d['last_operator']
        if 'position_code' in d:
            o.position_code = d['position_code']
        if 'recomment_type' in d:
            o.recomment_type = d['recomment_type']
        if 'scene_description' in d:
            o.scene_description = d['scene_description']
        if 'scene_id' in d:
            o.scene_id = d['scene_id']
        if 'scene_project_name' in d:
            o.scene_project_name = d['scene_project_name']
        if 'status' in d:
            o.status = d['status']
        return o


