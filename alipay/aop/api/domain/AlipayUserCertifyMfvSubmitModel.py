#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserCertifyMfvSubmitModel(object):

    def __init__(self):
        self._execute_type = None
        self._out_biz_order_no = None
        self._out_biz_type = None
        self._params = None
        self._scene_id = None

    @property
    def execute_type(self):
        return self._execute_type

    @execute_type.setter
    def execute_type(self, value):
        self._execute_type = value
    @property
    def out_biz_order_no(self):
        return self._out_biz_order_no

    @out_biz_order_no.setter
    def out_biz_order_no(self, value):
        self._out_biz_order_no = value
    @property
    def out_biz_type(self):
        return self._out_biz_type

    @out_biz_type.setter
    def out_biz_type(self, value):
        self._out_biz_type = value
    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value
    @property
    def scene_id(self):
        return self._scene_id

    @scene_id.setter
    def scene_id(self, value):
        self._scene_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.execute_type:
            if hasattr(self.execute_type, 'to_alipay_dict'):
                params['execute_type'] = self.execute_type.to_alipay_dict()
            else:
                params['execute_type'] = self.execute_type
        if self.out_biz_order_no:
            if hasattr(self.out_biz_order_no, 'to_alipay_dict'):
                params['out_biz_order_no'] = self.out_biz_order_no.to_alipay_dict()
            else:
                params['out_biz_order_no'] = self.out_biz_order_no
        if self.out_biz_type:
            if hasattr(self.out_biz_type, 'to_alipay_dict'):
                params['out_biz_type'] = self.out_biz_type.to_alipay_dict()
            else:
                params['out_biz_type'] = self.out_biz_type
        if self.params:
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
        if self.scene_id:
            if hasattr(self.scene_id, 'to_alipay_dict'):
                params['scene_id'] = self.scene_id.to_alipay_dict()
            else:
                params['scene_id'] = self.scene_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserCertifyMfvSubmitModel()
        if 'execute_type' in d:
            o.execute_type = d['execute_type']
        if 'out_biz_order_no' in d:
            o.out_biz_order_no = d['out_biz_order_no']
        if 'out_biz_type' in d:
            o.out_biz_type = d['out_biz_type']
        if 'params' in d:
            o.params = d['params']
        if 'scene_id' in d:
            o.scene_id = d['scene_id']
        return o


