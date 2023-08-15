#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FqQrCodeExtendParams(object):

    def __init__(self):
        self._bind_type = None
        self._fq_num = None
        self._scene_tag = None

    @property
    def bind_type(self):
        return self._bind_type

    @bind_type.setter
    def bind_type(self, value):
        self._bind_type = value
    @property
    def fq_num(self):
        return self._fq_num

    @fq_num.setter
    def fq_num(self, value):
        self._fq_num = value
    @property
    def scene_tag(self):
        return self._scene_tag

    @scene_tag.setter
    def scene_tag(self, value):
        self._scene_tag = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_type:
            if hasattr(self.bind_type, 'to_alipay_dict'):
                params['bind_type'] = self.bind_type.to_alipay_dict()
            else:
                params['bind_type'] = self.bind_type
        if self.fq_num:
            if hasattr(self.fq_num, 'to_alipay_dict'):
                params['fq_num'] = self.fq_num.to_alipay_dict()
            else:
                params['fq_num'] = self.fq_num
        if self.scene_tag:
            if hasattr(self.scene_tag, 'to_alipay_dict'):
                params['scene_tag'] = self.scene_tag.to_alipay_dict()
            else:
                params['scene_tag'] = self.scene_tag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FqQrCodeExtendParams()
        if 'bind_type' in d:
            o.bind_type = d['bind_type']
        if 'fq_num' in d:
            o.fq_num = d['fq_num']
        if 'scene_tag' in d:
            o.scene_tag = d['scene_tag']
        return o


