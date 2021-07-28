#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignSelfActivityQueryModel(object):

    def __init__(self):
        self._activity_id = None
        self._need_use_scope_info = None
        self._scene_code = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def need_use_scope_info(self):
        return self._need_use_scope_info

    @need_use_scope_info.setter
    def need_use_scope_info(self, value):
        if isinstance(value, list):
            self._need_use_scope_info = list()
            for i in value:
                self._need_use_scope_info.append(i)
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        if isinstance(value, list):
            self._scene_code = list()
            for i in value:
                self._scene_code.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.need_use_scope_info:
            if isinstance(self.need_use_scope_info, list):
                for i in range(0, len(self.need_use_scope_info)):
                    element = self.need_use_scope_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.need_use_scope_info[i] = element.to_alipay_dict()
            if hasattr(self.need_use_scope_info, 'to_alipay_dict'):
                params['need_use_scope_info'] = self.need_use_scope_info.to_alipay_dict()
            else:
                params['need_use_scope_info'] = self.need_use_scope_info
        if self.scene_code:
            if isinstance(self.scene_code, list):
                for i in range(0, len(self.scene_code)):
                    element = self.scene_code[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.scene_code[i] = element.to_alipay_dict()
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignSelfActivityQueryModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'need_use_scope_info' in d:
            o.need_use_scope_info = d['need_use_scope_info']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


