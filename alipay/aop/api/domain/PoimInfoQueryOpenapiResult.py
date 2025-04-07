#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PoimAddressQueryOpenapiResult import PoimAddressQueryOpenapiResult


class PoimInfoQueryOpenapiResult(object):

    def __init__(self):
        self._area_info = None
        self._poim_id = None
        self._poim_name = None
        self._scenic_id = None

    @property
    def area_info(self):
        return self._area_info

    @area_info.setter
    def area_info(self, value):
        if isinstance(value, PoimAddressQueryOpenapiResult):
            self._area_info = value
        else:
            self._area_info = PoimAddressQueryOpenapiResult.from_alipay_dict(value)
    @property
    def poim_id(self):
        return self._poim_id

    @poim_id.setter
    def poim_id(self, value):
        self._poim_id = value
    @property
    def poim_name(self):
        return self._poim_name

    @poim_name.setter
    def poim_name(self, value):
        self._poim_name = value
    @property
    def scenic_id(self):
        return self._scenic_id

    @scenic_id.setter
    def scenic_id(self, value):
        self._scenic_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_info:
            if hasattr(self.area_info, 'to_alipay_dict'):
                params['area_info'] = self.area_info.to_alipay_dict()
            else:
                params['area_info'] = self.area_info
        if self.poim_id:
            if hasattr(self.poim_id, 'to_alipay_dict'):
                params['poim_id'] = self.poim_id.to_alipay_dict()
            else:
                params['poim_id'] = self.poim_id
        if self.poim_name:
            if hasattr(self.poim_name, 'to_alipay_dict'):
                params['poim_name'] = self.poim_name.to_alipay_dict()
            else:
                params['poim_name'] = self.poim_name
        if self.scenic_id:
            if hasattr(self.scenic_id, 'to_alipay_dict'):
                params['scenic_id'] = self.scenic_id.to_alipay_dict()
            else:
                params['scenic_id'] = self.scenic_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PoimInfoQueryOpenapiResult()
        if 'area_info' in d:
            o.area_info = d['area_info']
        if 'poim_id' in d:
            o.poim_id = d['poim_id']
        if 'poim_name' in d:
            o.poim_name = d['poim_name']
        if 'scenic_id' in d:
            o.scenic_id = d['scenic_id']
        return o


