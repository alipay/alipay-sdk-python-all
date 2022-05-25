#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportCarbonDataQueryModel(object):

    def __init__(self):
        self._biz_date_end = None
        self._biz_date_start = None
        self._biz_scene = None
        self._city_code = None
        self._user_id = None

    @property
    def biz_date_end(self):
        return self._biz_date_end

    @biz_date_end.setter
    def biz_date_end(self, value):
        self._biz_date_end = value
    @property
    def biz_date_start(self):
        return self._biz_date_start

    @biz_date_start.setter
    def biz_date_start(self, value):
        self._biz_date_start = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_date_end:
            if hasattr(self.biz_date_end, 'to_alipay_dict'):
                params['biz_date_end'] = self.biz_date_end.to_alipay_dict()
            else:
                params['biz_date_end'] = self.biz_date_end
        if self.biz_date_start:
            if hasattr(self.biz_date_start, 'to_alipay_dict'):
                params['biz_date_start'] = self.biz_date_start.to_alipay_dict()
            else:
                params['biz_date_start'] = self.biz_date_start
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportCarbonDataQueryModel()
        if 'biz_date_end' in d:
            o.biz_date_end = d['biz_date_end']
        if 'biz_date_start' in d:
            o.biz_date_start = d['biz_date_start']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


