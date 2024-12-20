#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DTAgentExtInfo import DTAgentExtInfo
from alipay.aop.api.domain.DTAgentExtInfo import DTAgentExtInfo


class DTAgentSceneParam(object):

    def __init__(self):
        self._scene_biz_args = None
        self._scene_ext_info = None
        self._scene_name = None
        self._scene_user_id = None

    @property
    def scene_biz_args(self):
        return self._scene_biz_args

    @scene_biz_args.setter
    def scene_biz_args(self, value):
        if isinstance(value, list):
            self._scene_biz_args = list()
            for i in value:
                if isinstance(i, DTAgentExtInfo):
                    self._scene_biz_args.append(i)
                else:
                    self._scene_biz_args.append(DTAgentExtInfo.from_alipay_dict(i))
    @property
    def scene_ext_info(self):
        return self._scene_ext_info

    @scene_ext_info.setter
    def scene_ext_info(self, value):
        if isinstance(value, DTAgentExtInfo):
            self._scene_ext_info = value
        else:
            self._scene_ext_info = DTAgentExtInfo.from_alipay_dict(value)
    @property
    def scene_name(self):
        return self._scene_name

    @scene_name.setter
    def scene_name(self, value):
        self._scene_name = value
    @property
    def scene_user_id(self):
        return self._scene_user_id

    @scene_user_id.setter
    def scene_user_id(self, value):
        self._scene_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.scene_biz_args:
            if isinstance(self.scene_biz_args, list):
                for i in range(0, len(self.scene_biz_args)):
                    element = self.scene_biz_args[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.scene_biz_args[i] = element.to_alipay_dict()
            if hasattr(self.scene_biz_args, 'to_alipay_dict'):
                params['scene_biz_args'] = self.scene_biz_args.to_alipay_dict()
            else:
                params['scene_biz_args'] = self.scene_biz_args
        if self.scene_ext_info:
            if hasattr(self.scene_ext_info, 'to_alipay_dict'):
                params['scene_ext_info'] = self.scene_ext_info.to_alipay_dict()
            else:
                params['scene_ext_info'] = self.scene_ext_info
        if self.scene_name:
            if hasattr(self.scene_name, 'to_alipay_dict'):
                params['scene_name'] = self.scene_name.to_alipay_dict()
            else:
                params['scene_name'] = self.scene_name
        if self.scene_user_id:
            if hasattr(self.scene_user_id, 'to_alipay_dict'):
                params['scene_user_id'] = self.scene_user_id.to_alipay_dict()
            else:
                params['scene_user_id'] = self.scene_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DTAgentSceneParam()
        if 'scene_biz_args' in d:
            o.scene_biz_args = d['scene_biz_args']
        if 'scene_ext_info' in d:
            o.scene_ext_info = d['scene_ext_info']
        if 'scene_name' in d:
            o.scene_name = d['scene_name']
        if 'scene_user_id' in d:
            o.scene_user_id = d['scene_user_id']
        return o


