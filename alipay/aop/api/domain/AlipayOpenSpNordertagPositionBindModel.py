#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpNordertagPositionBindModel(object):

    def __init__(self):
        self._cloi_no = None
        self._operate = None
        self._position_id = None

    @property
    def cloi_no(self):
        return self._cloi_no

    @cloi_no.setter
    def cloi_no(self, value):
        if isinstance(value, list):
            self._cloi_no = list()
            for i in value:
                self._cloi_no.append(i)
    @property
    def operate(self):
        return self._operate

    @operate.setter
    def operate(self, value):
        self._operate = value
    @property
    def position_id(self):
        return self._position_id

    @position_id.setter
    def position_id(self, value):
        self._position_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cloi_no:
            if isinstance(self.cloi_no, list):
                for i in range(0, len(self.cloi_no)):
                    element = self.cloi_no[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cloi_no[i] = element.to_alipay_dict()
            if hasattr(self.cloi_no, 'to_alipay_dict'):
                params['cloi_no'] = self.cloi_no.to_alipay_dict()
            else:
                params['cloi_no'] = self.cloi_no
        if self.operate:
            if hasattr(self.operate, 'to_alipay_dict'):
                params['operate'] = self.operate.to_alipay_dict()
            else:
                params['operate'] = self.operate
        if self.position_id:
            if hasattr(self.position_id, 'to_alipay_dict'):
                params['position_id'] = self.position_id.to_alipay_dict()
            else:
                params['position_id'] = self.position_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpNordertagPositionBindModel()
        if 'cloi_no' in d:
            o.cloi_no = d['cloi_no']
        if 'operate' in d:
            o.operate = d['operate']
        if 'position_id' in d:
            o.position_id = d['position_id']
        return o


