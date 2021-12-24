#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpDossierCourtassessPrecreateModel(object):

    def __init__(self):
        self._derived_from = None
        self._scene_code = None
        self._user_id = None

    @property
    def derived_from(self):
        return self._derived_from

    @derived_from.setter
    def derived_from(self, value):
        self._derived_from = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.derived_from:
            if hasattr(self.derived_from, 'to_alipay_dict'):
                params['derived_from'] = self.derived_from.to_alipay_dict()
            else:
                params['derived_from'] = self.derived_from
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpDossierCourtassessPrecreateModel()
        if 'derived_from' in d:
            o.derived_from = d['derived_from']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


