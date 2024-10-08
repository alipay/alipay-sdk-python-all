#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UnitTraffic(object):

    def __init__(self):
        self._crowd_id = None
        self._crowd_percent = None
        self._id_range = None
        self._unit_key = None

    @property
    def crowd_id(self):
        return self._crowd_id

    @crowd_id.setter
    def crowd_id(self, value):
        self._crowd_id = value
    @property
    def crowd_percent(self):
        return self._crowd_percent

    @crowd_percent.setter
    def crowd_percent(self, value):
        self._crowd_percent = value
    @property
    def id_range(self):
        return self._id_range

    @id_range.setter
    def id_range(self, value):
        self._id_range = value
    @property
    def unit_key(self):
        return self._unit_key

    @unit_key.setter
    def unit_key(self, value):
        self._unit_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_id:
            if hasattr(self.crowd_id, 'to_alipay_dict'):
                params['crowd_id'] = self.crowd_id.to_alipay_dict()
            else:
                params['crowd_id'] = self.crowd_id
        if self.crowd_percent:
            if hasattr(self.crowd_percent, 'to_alipay_dict'):
                params['crowd_percent'] = self.crowd_percent.to_alipay_dict()
            else:
                params['crowd_percent'] = self.crowd_percent
        if self.id_range:
            if hasattr(self.id_range, 'to_alipay_dict'):
                params['id_range'] = self.id_range.to_alipay_dict()
            else:
                params['id_range'] = self.id_range
        if self.unit_key:
            if hasattr(self.unit_key, 'to_alipay_dict'):
                params['unit_key'] = self.unit_key.to_alipay_dict()
            else:
                params['unit_key'] = self.unit_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UnitTraffic()
        if 'crowd_id' in d:
            o.crowd_id = d['crowd_id']
        if 'crowd_percent' in d:
            o.crowd_percent = d['crowd_percent']
        if 'id_range' in d:
            o.id_range = d['id_range']
        if 'unit_key' in d:
            o.unit_key = d['unit_key']
        return o


