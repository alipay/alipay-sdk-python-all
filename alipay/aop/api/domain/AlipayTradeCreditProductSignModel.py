#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiValidStrategy import OpenApiValidStrategy


class AlipayTradeCreditProductSignModel(object):

    def __init__(self):
        self._ext_info = None
        self._scene_code = None
        self._user_id = None
        self._valid_strategy = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def valid_strategy(self):
        return self._valid_strategy

    @valid_strategy.setter
    def valid_strategy(self, value):
        if isinstance(value, OpenApiValidStrategy):
            self._valid_strategy = value
        else:
            self._valid_strategy = OpenApiValidStrategy.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.valid_strategy:
            if hasattr(self.valid_strategy, 'to_alipay_dict'):
                params['valid_strategy'] = self.valid_strategy.to_alipay_dict()
            else:
                params['valid_strategy'] = self.valid_strategy
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeCreditProductSignModel()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'valid_strategy' in d:
            o.valid_strategy = d['valid_strategy']
        return o


