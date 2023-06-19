#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PrePayOperationInfoViewData import PrePayOperationInfoViewData


class PrePayOperationInfo(object):

    def __init__(self):
        self._scene_code = None
        self._view_data = None

    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def view_data(self):
        return self._view_data

    @view_data.setter
    def view_data(self, value):
        if isinstance(value, PrePayOperationInfoViewData):
            self._view_data = value
        else:
            self._view_data = PrePayOperationInfoViewData.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.view_data:
            if hasattr(self.view_data, 'to_alipay_dict'):
                params['view_data'] = self.view_data.to_alipay_dict()
            else:
                params['view_data'] = self.view_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrePayOperationInfo()
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'view_data' in d:
            o.view_data = d['view_data']
        return o


