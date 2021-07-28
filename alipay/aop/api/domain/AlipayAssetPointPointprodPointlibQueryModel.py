#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAssetPointPointprodPointlibQueryModel(object):

    def __init__(self):
        self._point_lib_id = None

    @property
    def point_lib_id(self):
        return self._point_lib_id

    @point_lib_id.setter
    def point_lib_id(self, value):
        self._point_lib_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.point_lib_id:
            if hasattr(self.point_lib_id, 'to_alipay_dict'):
                params['point_lib_id'] = self.point_lib_id.to_alipay_dict()
            else:
                params['point_lib_id'] = self.point_lib_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAssetPointPointprodPointlibQueryModel()
        if 'point_lib_id' in d:
            o.point_lib_id = d['point_lib_id']
        return o


