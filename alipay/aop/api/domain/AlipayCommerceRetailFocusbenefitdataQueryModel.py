#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRetailFocusbenefitdataQueryModel(object):

    def __init__(self):
        self._area = None
        self._digest = None
        self._dt_list = None
        self._hh_list = None
        self._minute_time = None
        self._page_index = None
        self._page_size = None
        self._scene_code = None

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value
    @property
    def digest(self):
        return self._digest

    @digest.setter
    def digest(self, value):
        self._digest = value
    @property
    def dt_list(self):
        return self._dt_list

    @dt_list.setter
    def dt_list(self, value):
        self._dt_list = value
    @property
    def hh_list(self):
        return self._hh_list

    @hh_list.setter
    def hh_list(self, value):
        self._hh_list = value
    @property
    def minute_time(self):
        return self._minute_time

    @minute_time.setter
    def minute_time(self, value):
        self._minute_time = value
    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.area:
            if hasattr(self.area, 'to_alipay_dict'):
                params['area'] = self.area.to_alipay_dict()
            else:
                params['area'] = self.area
        if self.digest:
            if hasattr(self.digest, 'to_alipay_dict'):
                params['digest'] = self.digest.to_alipay_dict()
            else:
                params['digest'] = self.digest
        if self.dt_list:
            if hasattr(self.dt_list, 'to_alipay_dict'):
                params['dt_list'] = self.dt_list.to_alipay_dict()
            else:
                params['dt_list'] = self.dt_list
        if self.hh_list:
            if hasattr(self.hh_list, 'to_alipay_dict'):
                params['hh_list'] = self.hh_list.to_alipay_dict()
            else:
                params['hh_list'] = self.hh_list
        if self.minute_time:
            if hasattr(self.minute_time, 'to_alipay_dict'):
                params['minute_time'] = self.minute_time.to_alipay_dict()
            else:
                params['minute_time'] = self.minute_time
        if self.page_index:
            if hasattr(self.page_index, 'to_alipay_dict'):
                params['page_index'] = self.page_index.to_alipay_dict()
            else:
                params['page_index'] = self.page_index
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRetailFocusbenefitdataQueryModel()
        if 'area' in d:
            o.area = d['area']
        if 'digest' in d:
            o.digest = d['digest']
        if 'dt_list' in d:
            o.dt_list = d['dt_list']
        if 'hh_list' in d:
            o.hh_list = d['hh_list']
        if 'minute_time' in d:
            o.minute_time = d['minute_time']
        if 'page_index' in d:
            o.page_index = d['page_index']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


