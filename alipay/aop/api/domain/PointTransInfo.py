#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PointTransInfo(object):

    def __init__(self):
        self._op_time = None
        self._point = None
        self._remark = None
        self._trans_no = None
        self._trans_type = None

    @property
    def op_time(self):
        return self._op_time

    @op_time.setter
    def op_time(self, value):
        self._op_time = value
    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, value):
        self._point = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def trans_no(self):
        return self._trans_no

    @trans_no.setter
    def trans_no(self, value):
        self._trans_no = value
    @property
    def trans_type(self):
        return self._trans_type

    @trans_type.setter
    def trans_type(self, value):
        self._trans_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.op_time:
            if hasattr(self.op_time, 'to_alipay_dict'):
                params['op_time'] = self.op_time.to_alipay_dict()
            else:
                params['op_time'] = self.op_time
        if self.point:
            if hasattr(self.point, 'to_alipay_dict'):
                params['point'] = self.point.to_alipay_dict()
            else:
                params['point'] = self.point
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.trans_no:
            if hasattr(self.trans_no, 'to_alipay_dict'):
                params['trans_no'] = self.trans_no.to_alipay_dict()
            else:
                params['trans_no'] = self.trans_no
        if self.trans_type:
            if hasattr(self.trans_type, 'to_alipay_dict'):
                params['trans_type'] = self.trans_type.to_alipay_dict()
            else:
                params['trans_type'] = self.trans_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PointTransInfo()
        if 'op_time' in d:
            o.op_time = d['op_time']
        if 'point' in d:
            o.point = d['point']
        if 'remark' in d:
            o.remark = d['remark']
        if 'trans_no' in d:
            o.trans_no = d['trans_no']
        if 'trans_type' in d:
            o.trans_type = d['trans_type']
        return o


