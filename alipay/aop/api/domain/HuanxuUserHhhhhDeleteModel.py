#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HuanxuUserHhhhhDeleteModel(object):

    def __init__(self):
        self._aa = None
        self._add = None
        self._app_name = None
        self._dd = None
        self._mini_app_id = None

    @property
    def aa(self):
        return self._aa

    @aa.setter
    def aa(self, value):
        self._aa = value
    @property
    def add(self):
        return self._add

    @add.setter
    def add(self, value):
        self._add = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def dd(self):
        return self._dd

    @dd.setter
    def dd(self, value):
        self._dd = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.aa:
            if hasattr(self.aa, 'to_alipay_dict'):
                params['aa'] = self.aa.to_alipay_dict()
            else:
                params['aa'] = self.aa
        if self.add:
            if hasattr(self.add, 'to_alipay_dict'):
                params['add'] = self.add.to_alipay_dict()
            else:
                params['add'] = self.add
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.dd:
            if hasattr(self.dd, 'to_alipay_dict'):
                params['dd'] = self.dd.to_alipay_dict()
            else:
                params['dd'] = self.dd
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HuanxuUserHhhhhDeleteModel()
        if 'aa' in d:
            o.aa = d['aa']
        if 'add' in d:
            o.add = d['add']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'dd' in d:
            o.dd = d['dd']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        return o


