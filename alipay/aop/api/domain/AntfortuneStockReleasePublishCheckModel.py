#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneStockReleasePublishCheckModel(object):

    def __init__(self):
        self._env = None
        self._inst_id = None
        self._tgz_name = None

    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def tgz_name(self):
        return self._tgz_name

    @tgz_name.setter
    def tgz_name(self, value):
        self._tgz_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.env:
            if hasattr(self.env, 'to_alipay_dict'):
                params['env'] = self.env.to_alipay_dict()
            else:
                params['env'] = self.env
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.tgz_name:
            if hasattr(self.tgz_name, 'to_alipay_dict'):
                params['tgz_name'] = self.tgz_name.to_alipay_dict()
            else:
                params['tgz_name'] = self.tgz_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneStockReleasePublishCheckModel()
        if 'env' in d:
            o.env = d['env']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'tgz_name' in d:
            o.tgz_name = d['tgz_name']
        return o


