#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniOrderExtInfoVO(object):

    def __init__(self):
        self._memo = None
        self._remark = None
        self._remark_color_flag = None

    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def remark_color_flag(self):
        return self._remark_color_flag

    @remark_color_flag.setter
    def remark_color_flag(self, value):
        self._remark_color_flag = value


    def to_alipay_dict(self):
        params = dict()
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.remark_color_flag:
            if hasattr(self.remark_color_flag, 'to_alipay_dict'):
                params['remark_color_flag'] = self.remark_color_flag.to_alipay_dict()
            else:
                params['remark_color_flag'] = self.remark_color_flag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniOrderExtInfoVO()
        if 'memo' in d:
            o.memo = d['memo']
        if 'remark' in d:
            o.remark = d['remark']
        if 'remark_color_flag' in d:
            o.remark_color_flag = d['remark_color_flag']
        return o


