#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarRentcarUserdropoffSyncModel(object):

    def __init__(self):
        self._actual_drop_off_time = None
        self._driving_distance = None
        self._open_id = None
        self._out_order_no = None
        self._user_id = None

    @property
    def actual_drop_off_time(self):
        return self._actual_drop_off_time

    @actual_drop_off_time.setter
    def actual_drop_off_time(self, value):
        self._actual_drop_off_time = value
    @property
    def driving_distance(self):
        return self._driving_distance

    @driving_distance.setter
    def driving_distance(self, value):
        self._driving_distance = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_drop_off_time:
            if hasattr(self.actual_drop_off_time, 'to_alipay_dict'):
                params['actual_drop_off_time'] = self.actual_drop_off_time.to_alipay_dict()
            else:
                params['actual_drop_off_time'] = self.actual_drop_off_time
        if self.driving_distance:
            if hasattr(self.driving_distance, 'to_alipay_dict'):
                params['driving_distance'] = self.driving_distance.to_alipay_dict()
            else:
                params['driving_distance'] = self.driving_distance
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
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
        o = AlipayEcoMycarRentcarUserdropoffSyncModel()
        if 'actual_drop_off_time' in d:
            o.actual_drop_off_time = d['actual_drop_off_time']
        if 'driving_distance' in d:
            o.driving_distance = d['driving_distance']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


