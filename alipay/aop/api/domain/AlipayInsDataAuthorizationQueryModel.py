#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsDataAuthorizationQueryModel(object):

    def __init__(self):
        self._auth_biz_no = None
        self._inst_id = None
        self._scene_code = None

    @property
    def auth_biz_no(self):
        return self._auth_biz_no

    @auth_biz_no.setter
    def auth_biz_no(self, value):
        self._auth_biz_no = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_biz_no:
            if hasattr(self.auth_biz_no, 'to_alipay_dict'):
                params['auth_biz_no'] = self.auth_biz_no.to_alipay_dict()
            else:
                params['auth_biz_no'] = self.auth_biz_no
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsDataAuthorizationQueryModel()
        if 'auth_biz_no' in d:
            o.auth_biz_no = d['auth_biz_no']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


