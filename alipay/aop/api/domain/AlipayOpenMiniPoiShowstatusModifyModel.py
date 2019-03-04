#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniPoiShowstatusModifyModel(object):

    def __init__(self):
        self._poi_id = None
        self._show_status = None

    @property
    def poi_id(self):
        return self._poi_id

    @poi_id.setter
    def poi_id(self, value):
        self._poi_id = value
    @property
    def show_status(self):
        return self._show_status

    @show_status.setter
    def show_status(self, value):
        self._show_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.poi_id:
            if hasattr(self.poi_id, 'to_alipay_dict'):
                params['poi_id'] = self.poi_id.to_alipay_dict()
            else:
                params['poi_id'] = self.poi_id
        if self.show_status:
            if hasattr(self.show_status, 'to_alipay_dict'):
                params['show_status'] = self.show_status.to_alipay_dict()
            else:
                params['show_status'] = self.show_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniPoiShowstatusModifyModel()
        if 'poi_id' in d:
            o.poi_id = d['poi_id']
        if 'show_status' in d:
            o.show_status = d['show_status']
        return o


