#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataIotdataDataTotalQueryModel(object):

    def __init__(self):
        self._business_id = None
        self._end_time = None
        self._point_id = None
        self._start_time = None
        self._sub_biz_id = None

    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, value):
        self._business_id = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def point_id(self):
        return self._point_id

    @point_id.setter
    def point_id(self, value):
        self._point_id = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def sub_biz_id(self):
        return self._sub_biz_id

    @sub_biz_id.setter
    def sub_biz_id(self, value):
        self._sub_biz_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_id:
            if hasattr(self.business_id, 'to_alipay_dict'):
                params['business_id'] = self.business_id.to_alipay_dict()
            else:
                params['business_id'] = self.business_id
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.point_id:
            if hasattr(self.point_id, 'to_alipay_dict'):
                params['point_id'] = self.point_id.to_alipay_dict()
            else:
                params['point_id'] = self.point_id
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.sub_biz_id:
            if hasattr(self.sub_biz_id, 'to_alipay_dict'):
                params['sub_biz_id'] = self.sub_biz_id.to_alipay_dict()
            else:
                params['sub_biz_id'] = self.sub_biz_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataIotdataDataTotalQueryModel()
        if 'business_id' in d:
            o.business_id = d['business_id']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'point_id' in d:
            o.point_id = d['point_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'sub_biz_id' in d:
            o.sub_biz_id = d['sub_biz_id']
        return o


