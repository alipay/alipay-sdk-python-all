#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderExpoCoilBindModel(object):

    def __init__(self):
        self._activity_code = None
        self._coil_no = None
        self._jump_url = None
        self._scene_name = None
        self._solution_code = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def coil_no(self):
        return self._coil_no

    @coil_no.setter
    def coil_no(self, value):
        self._coil_no = value
    @property
    def jump_url(self):
        return self._jump_url

    @jump_url.setter
    def jump_url(self, value):
        self._jump_url = value
    @property
    def scene_name(self):
        return self._scene_name

    @scene_name.setter
    def scene_name(self, value):
        self._scene_name = value
    @property
    def solution_code(self):
        return self._solution_code

    @solution_code.setter
    def solution_code(self, value):
        self._solution_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_code:
            if hasattr(self.activity_code, 'to_alipay_dict'):
                params['activity_code'] = self.activity_code.to_alipay_dict()
            else:
                params['activity_code'] = self.activity_code
        if self.coil_no:
            if hasattr(self.coil_no, 'to_alipay_dict'):
                params['coil_no'] = self.coil_no.to_alipay_dict()
            else:
                params['coil_no'] = self.coil_no
        if self.jump_url:
            if hasattr(self.jump_url, 'to_alipay_dict'):
                params['jump_url'] = self.jump_url.to_alipay_dict()
            else:
                params['jump_url'] = self.jump_url
        if self.scene_name:
            if hasattr(self.scene_name, 'to_alipay_dict'):
                params['scene_name'] = self.scene_name.to_alipay_dict()
            else:
                params['scene_name'] = self.scene_name
        if self.solution_code:
            if hasattr(self.solution_code, 'to_alipay_dict'):
                params['solution_code'] = self.solution_code.to_alipay_dict()
            else:
                params['solution_code'] = self.solution_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderExpoCoilBindModel()
        if 'activity_code' in d:
            o.activity_code = d['activity_code']
        if 'coil_no' in d:
            o.coil_no = d['coil_no']
        if 'jump_url' in d:
            o.jump_url = d['jump_url']
        if 'scene_name' in d:
            o.scene_name = d['scene_name']
        if 'solution_code' in d:
            o.solution_code = d['solution_code']
        return o


