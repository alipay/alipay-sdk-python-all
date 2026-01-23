#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RoomDetailInfo(object):

    def __init__(self):
        self._area = None
        self._bed_desc = None
        self._capacity = None
        self._floor = None

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value
    @property
    def bed_desc(self):
        return self._bed_desc

    @bed_desc.setter
    def bed_desc(self, value):
        self._bed_desc = value
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value
    @property
    def floor(self):
        return self._floor

    @floor.setter
    def floor(self, value):
        self._floor = value


    def to_alipay_dict(self):
        params = dict()
        if self.area:
            if hasattr(self.area, 'to_alipay_dict'):
                params['area'] = self.area.to_alipay_dict()
            else:
                params['area'] = self.area
        if self.bed_desc:
            if hasattr(self.bed_desc, 'to_alipay_dict'):
                params['bed_desc'] = self.bed_desc.to_alipay_dict()
            else:
                params['bed_desc'] = self.bed_desc
        if self.capacity:
            if hasattr(self.capacity, 'to_alipay_dict'):
                params['capacity'] = self.capacity.to_alipay_dict()
            else:
                params['capacity'] = self.capacity
        if self.floor:
            if hasattr(self.floor, 'to_alipay_dict'):
                params['floor'] = self.floor.to_alipay_dict()
            else:
                params['floor'] = self.floor
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RoomDetailInfo()
        if 'area' in d:
            o.area = d['area']
        if 'bed_desc' in d:
            o.bed_desc = d['bed_desc']
        if 'capacity' in d:
            o.capacity = d['capacity']
        if 'floor' in d:
            o.floor = d['floor']
        return o


