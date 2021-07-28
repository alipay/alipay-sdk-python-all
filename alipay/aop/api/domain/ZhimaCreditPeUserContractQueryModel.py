#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditPeUserContractQueryModel(object):

    def __init__(self):
        self._credit_scene = None
        self._user_id = None

    @property
    def credit_scene(self):
        return self._credit_scene

    @credit_scene.setter
    def credit_scene(self, value):
        self._credit_scene = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.credit_scene:
            if hasattr(self.credit_scene, 'to_alipay_dict'):
                params['credit_scene'] = self.credit_scene.to_alipay_dict()
            else:
                params['credit_scene'] = self.credit_scene
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
        o = ZhimaCreditPeUserContractQueryModel()
        if 'credit_scene' in d:
            o.credit_scene = d['credit_scene']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


