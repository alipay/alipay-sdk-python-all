#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AuthorizeLifeApp(object):

    def __init__(self):
        self._life_app_id = None
        self._life_app_name = None

    @property
    def life_app_id(self):
        return self._life_app_id

    @life_app_id.setter
    def life_app_id(self, value):
        self._life_app_id = value
    @property
    def life_app_name(self):
        return self._life_app_name

    @life_app_name.setter
    def life_app_name(self, value):
        self._life_app_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.life_app_id:
            if hasattr(self.life_app_id, 'to_alipay_dict'):
                params['life_app_id'] = self.life_app_id.to_alipay_dict()
            else:
                params['life_app_id'] = self.life_app_id
        if self.life_app_name:
            if hasattr(self.life_app_name, 'to_alipay_dict'):
                params['life_app_name'] = self.life_app_name.to_alipay_dict()
            else:
                params['life_app_name'] = self.life_app_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AuthorizeLifeApp()
        if 'life_app_id' in d:
            o.life_app_id = d['life_app_id']
        if 'life_app_name' in d:
            o.life_app_name = d['life_app_name']
        return o


