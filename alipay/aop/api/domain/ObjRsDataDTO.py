#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RsData import RsData


class ObjRsDataDTO(object):

    def __init__(self):
        self._obj_dim_key = None
        self._rs_data = None

    @property
    def obj_dim_key(self):
        return self._obj_dim_key

    @obj_dim_key.setter
    def obj_dim_key(self, value):
        self._obj_dim_key = value
    @property
    def rs_data(self):
        return self._rs_data

    @rs_data.setter
    def rs_data(self, value):
        if isinstance(value, RsData):
            self._rs_data = value
        else:
            self._rs_data = RsData.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.obj_dim_key:
            if hasattr(self.obj_dim_key, 'to_alipay_dict'):
                params['obj_dim_key'] = self.obj_dim_key.to_alipay_dict()
            else:
                params['obj_dim_key'] = self.obj_dim_key
        if self.rs_data:
            if hasattr(self.rs_data, 'to_alipay_dict'):
                params['rs_data'] = self.rs_data.to_alipay_dict()
            else:
                params['rs_data'] = self.rs_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ObjRsDataDTO()
        if 'obj_dim_key' in d:
            o.obj_dim_key = d['obj_dim_key']
        if 'rs_data' in d:
            o.rs_data = d['rs_data']
        return o


