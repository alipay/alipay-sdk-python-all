#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoCmsCdataUploadModel(object):

    def __init__(self):
        self._attribute = None
        self._category = None
        self._exp_time = None
        self._merch_id = None
        self._op_data = None
        self._scene_data = None
        self._start_time = None
        self._syn = None
        self._t_v = None
        self._tamplate_id = None
        self._target_id = None

    @property
    def attribute(self):
        return self._attribute

    @attribute.setter
    def attribute(self, value):
        self._attribute = value
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def exp_time(self):
        return self._exp_time

    @exp_time.setter
    def exp_time(self, value):
        self._exp_time = value
    @property
    def merch_id(self):
        return self._merch_id

    @merch_id.setter
    def merch_id(self, value):
        self._merch_id = value
    @property
    def op_data(self):
        return self._op_data

    @op_data.setter
    def op_data(self, value):
        self._op_data = value
    @property
    def scene_data(self):
        return self._scene_data

    @scene_data.setter
    def scene_data(self, value):
        self._scene_data = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def syn(self):
        return self._syn

    @syn.setter
    def syn(self, value):
        self._syn = value
    @property
    def t_v(self):
        return self._t_v

    @t_v.setter
    def t_v(self, value):
        self._t_v = value
    @property
    def tamplate_id(self):
        return self._tamplate_id

    @tamplate_id.setter
    def tamplate_id(self, value):
        self._tamplate_id = value
    @property
    def target_id(self):
        return self._target_id

    @target_id.setter
    def target_id(self, value):
        self._target_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.attribute:
            if hasattr(self.attribute, 'to_alipay_dict'):
                params['attribute'] = self.attribute.to_alipay_dict()
            else:
                params['attribute'] = self.attribute
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.exp_time:
            if hasattr(self.exp_time, 'to_alipay_dict'):
                params['exp_time'] = self.exp_time.to_alipay_dict()
            else:
                params['exp_time'] = self.exp_time
        if self.merch_id:
            if hasattr(self.merch_id, 'to_alipay_dict'):
                params['merch_id'] = self.merch_id.to_alipay_dict()
            else:
                params['merch_id'] = self.merch_id
        if self.op_data:
            if hasattr(self.op_data, 'to_alipay_dict'):
                params['op_data'] = self.op_data.to_alipay_dict()
            else:
                params['op_data'] = self.op_data
        if self.scene_data:
            if hasattr(self.scene_data, 'to_alipay_dict'):
                params['scene_data'] = self.scene_data.to_alipay_dict()
            else:
                params['scene_data'] = self.scene_data
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.syn:
            if hasattr(self.syn, 'to_alipay_dict'):
                params['syn'] = self.syn.to_alipay_dict()
            else:
                params['syn'] = self.syn
        if self.t_v:
            if hasattr(self.t_v, 'to_alipay_dict'):
                params['t_v'] = self.t_v.to_alipay_dict()
            else:
                params['t_v'] = self.t_v
        if self.tamplate_id:
            if hasattr(self.tamplate_id, 'to_alipay_dict'):
                params['tamplate_id'] = self.tamplate_id.to_alipay_dict()
            else:
                params['tamplate_id'] = self.tamplate_id
        if self.target_id:
            if hasattr(self.target_id, 'to_alipay_dict'):
                params['target_id'] = self.target_id.to_alipay_dict()
            else:
                params['target_id'] = self.target_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoCmsCdataUploadModel()
        if 'attribute' in d:
            o.attribute = d['attribute']
        if 'category' in d:
            o.category = d['category']
        if 'exp_time' in d:
            o.exp_time = d['exp_time']
        if 'merch_id' in d:
            o.merch_id = d['merch_id']
        if 'op_data' in d:
            o.op_data = d['op_data']
        if 'scene_data' in d:
            o.scene_data = d['scene_data']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'syn' in d:
            o.syn = d['syn']
        if 't_v' in d:
            o.t_v = d['t_v']
        if 'tamplate_id' in d:
            o.tamplate_id = d['tamplate_id']
        if 'target_id' in d:
            o.target_id = d['target_id']
        return o


