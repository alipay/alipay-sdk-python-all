#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ManjiantTest(object):

    def __init__(self):
        self._open_id = None
        self._open_id_json = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def open_id_json(self):
        return self._open_id_json

    @open_id_json.setter
    def open_id_json(self, value):
        self._open_id_json = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.open_id_json:
            if hasattr(self.open_id_json, 'to_alipay_dict'):
                params['open_id_json'] = self.open_id_json.to_alipay_dict()
            else:
                params['open_id_json'] = self.open_id_json
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
        o = ManjiantTest()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'open_id_json' in d:
            o.open_id_json = d['open_id_json']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


