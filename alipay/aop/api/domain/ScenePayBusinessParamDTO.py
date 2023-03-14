#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ScenePayBusinessParamDTO(object):

    def __init__(self):
        self._mall_cell_id = None
        self._mall_cell_type = None
        self._mall_id = None
        self._mall_pid = None
        self._real_store_id = None

    @property
    def mall_cell_id(self):
        return self._mall_cell_id

    @mall_cell_id.setter
    def mall_cell_id(self, value):
        self._mall_cell_id = value
    @property
    def mall_cell_type(self):
        return self._mall_cell_type

    @mall_cell_type.setter
    def mall_cell_type(self, value):
        self._mall_cell_type = value
    @property
    def mall_id(self):
        return self._mall_id

    @mall_id.setter
    def mall_id(self, value):
        self._mall_id = value
    @property
    def mall_pid(self):
        return self._mall_pid

    @mall_pid.setter
    def mall_pid(self, value):
        self._mall_pid = value
    @property
    def real_store_id(self):
        return self._real_store_id

    @real_store_id.setter
    def real_store_id(self, value):
        self._real_store_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.mall_cell_id:
            if hasattr(self.mall_cell_id, 'to_alipay_dict'):
                params['mall_cell_id'] = self.mall_cell_id.to_alipay_dict()
            else:
                params['mall_cell_id'] = self.mall_cell_id
        if self.mall_cell_type:
            if hasattr(self.mall_cell_type, 'to_alipay_dict'):
                params['mall_cell_type'] = self.mall_cell_type.to_alipay_dict()
            else:
                params['mall_cell_type'] = self.mall_cell_type
        if self.mall_id:
            if hasattr(self.mall_id, 'to_alipay_dict'):
                params['mall_id'] = self.mall_id.to_alipay_dict()
            else:
                params['mall_id'] = self.mall_id
        if self.mall_pid:
            if hasattr(self.mall_pid, 'to_alipay_dict'):
                params['mall_pid'] = self.mall_pid.to_alipay_dict()
            else:
                params['mall_pid'] = self.mall_pid
        if self.real_store_id:
            if hasattr(self.real_store_id, 'to_alipay_dict'):
                params['real_store_id'] = self.real_store_id.to_alipay_dict()
            else:
                params['real_store_id'] = self.real_store_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ScenePayBusinessParamDTO()
        if 'mall_cell_id' in d:
            o.mall_cell_id = d['mall_cell_id']
        if 'mall_cell_type' in d:
            o.mall_cell_type = d['mall_cell_type']
        if 'mall_id' in d:
            o.mall_id = d['mall_id']
        if 'mall_pid' in d:
            o.mall_pid = d['mall_pid']
        if 'real_store_id' in d:
            o.real_store_id = d['real_store_id']
        return o


