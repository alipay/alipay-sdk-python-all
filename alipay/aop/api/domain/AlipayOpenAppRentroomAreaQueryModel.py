#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppRentroomAreaQueryModel(object):

    def __init__(self):
        self._area_id = None
        self._out_area_id = None

    @property
    def area_id(self):
        return self._area_id

    @area_id.setter
    def area_id(self, value):
        self._area_id = value
    @property
    def out_area_id(self):
        return self._out_area_id

    @out_area_id.setter
    def out_area_id(self, value):
        self._out_area_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_id:
            if hasattr(self.area_id, 'to_alipay_dict'):
                params['area_id'] = self.area_id.to_alipay_dict()
            else:
                params['area_id'] = self.area_id
        if self.out_area_id:
            if hasattr(self.out_area_id, 'to_alipay_dict'):
                params['out_area_id'] = self.out_area_id.to_alipay_dict()
            else:
                params['out_area_id'] = self.out_area_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppRentroomAreaQueryModel()
        if 'area_id' in d:
            o.area_id = d['area_id']
        if 'out_area_id' in d:
            o.out_area_id = d['out_area_id']
        return o


