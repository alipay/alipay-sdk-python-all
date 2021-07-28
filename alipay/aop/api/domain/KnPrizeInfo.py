#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KnPrizeInfo(object):

    def __init__(self):
        self._gmt_begin = None
        self._gmt_end = None
        self._prize_id = None
        self._prize_name = None
        self._prize_sub_type = None
        self._prize_type = None

    @property
    def gmt_begin(self):
        return self._gmt_begin

    @gmt_begin.setter
    def gmt_begin(self, value):
        self._gmt_begin = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value
    @property
    def prize_name(self):
        return self._prize_name

    @prize_name.setter
    def prize_name(self, value):
        self._prize_name = value
    @property
    def prize_sub_type(self):
        return self._prize_sub_type

    @prize_sub_type.setter
    def prize_sub_type(self, value):
        self._prize_sub_type = value
    @property
    def prize_type(self):
        return self._prize_type

    @prize_type.setter
    def prize_type(self, value):
        self._prize_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_begin:
            if hasattr(self.gmt_begin, 'to_alipay_dict'):
                params['gmt_begin'] = self.gmt_begin.to_alipay_dict()
            else:
                params['gmt_begin'] = self.gmt_begin
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        if self.prize_name:
            if hasattr(self.prize_name, 'to_alipay_dict'):
                params['prize_name'] = self.prize_name.to_alipay_dict()
            else:
                params['prize_name'] = self.prize_name
        if self.prize_sub_type:
            if hasattr(self.prize_sub_type, 'to_alipay_dict'):
                params['prize_sub_type'] = self.prize_sub_type.to_alipay_dict()
            else:
                params['prize_sub_type'] = self.prize_sub_type
        if self.prize_type:
            if hasattr(self.prize_type, 'to_alipay_dict'):
                params['prize_type'] = self.prize_type.to_alipay_dict()
            else:
                params['prize_type'] = self.prize_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KnPrizeInfo()
        if 'gmt_begin' in d:
            o.gmt_begin = d['gmt_begin']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'prize_name' in d:
            o.prize_name = d['prize_name']
        if 'prize_sub_type' in d:
            o.prize_sub_type = d['prize_sub_type']
        if 'prize_type' in d:
            o.prize_type = d['prize_type']
        return o


