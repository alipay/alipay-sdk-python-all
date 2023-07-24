#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskMiniprogramVerifyidentityConfirmModel(object):

    def __init__(self):
        self._biz_id = None
        self._scene_code = None
        self._verify_token = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def verify_token(self):
        return self._verify_token

    @verify_token.setter
    def verify_token(self, value):
        self._verify_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.verify_token:
            if hasattr(self.verify_token, 'to_alipay_dict'):
                params['verify_token'] = self.verify_token.to_alipay_dict()
            else:
                params['verify_token'] = self.verify_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskMiniprogramVerifyidentityConfirmModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'verify_token' in d:
            o.verify_token = d['verify_token']
        return o


