#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PosStallModel(object):

    def __init__(self):
        self._sort = None
        self._stall_id = None
        self._stall_name = None

    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, value):
        self._sort = value
    @property
    def stall_id(self):
        return self._stall_id

    @stall_id.setter
    def stall_id(self, value):
        self._stall_id = value
    @property
    def stall_name(self):
        return self._stall_name

    @stall_name.setter
    def stall_name(self, value):
        self._stall_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.sort:
            if hasattr(self.sort, 'to_alipay_dict'):
                params['sort'] = self.sort.to_alipay_dict()
            else:
                params['sort'] = self.sort
        if self.stall_id:
            if hasattr(self.stall_id, 'to_alipay_dict'):
                params['stall_id'] = self.stall_id.to_alipay_dict()
            else:
                params['stall_id'] = self.stall_id
        if self.stall_name:
            if hasattr(self.stall_name, 'to_alipay_dict'):
                params['stall_name'] = self.stall_name.to_alipay_dict()
            else:
                params['stall_name'] = self.stall_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PosStallModel()
        if 'sort' in d:
            o.sort = d['sort']
        if 'stall_id' in d:
            o.stall_id = d['stall_id']
        if 'stall_name' in d:
            o.stall_name = d['stall_name']
        return o


