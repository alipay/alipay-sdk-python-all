#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ScheduleWorkStatItem(object):

    def __init__(self):
        self._all_miles_sts = None
        self._all_trip_sts = None
        self._down_chain_cnt = None
        self._invalid_miles_sts = None
        self._invalid_trip_sts = None
        self._line_id = None
        self._opt_type = None
        self._up_chain_cnt = None
        self._valid_miles_sts = None
        self._valid_trip_sts = None
        self._wait_time_sts = None
        self._work_time_sts = None

    @property
    def all_miles_sts(self):
        return self._all_miles_sts

    @all_miles_sts.setter
    def all_miles_sts(self, value):
        self._all_miles_sts = value
    @property
    def all_trip_sts(self):
        return self._all_trip_sts

    @all_trip_sts.setter
    def all_trip_sts(self, value):
        self._all_trip_sts = value
    @property
    def down_chain_cnt(self):
        return self._down_chain_cnt

    @down_chain_cnt.setter
    def down_chain_cnt(self, value):
        self._down_chain_cnt = value
    @property
    def invalid_miles_sts(self):
        return self._invalid_miles_sts

    @invalid_miles_sts.setter
    def invalid_miles_sts(self, value):
        self._invalid_miles_sts = value
    @property
    def invalid_trip_sts(self):
        return self._invalid_trip_sts

    @invalid_trip_sts.setter
    def invalid_trip_sts(self, value):
        self._invalid_trip_sts = value
    @property
    def line_id(self):
        return self._line_id

    @line_id.setter
    def line_id(self, value):
        self._line_id = value
    @property
    def opt_type(self):
        return self._opt_type

    @opt_type.setter
    def opt_type(self, value):
        self._opt_type = value
    @property
    def up_chain_cnt(self):
        return self._up_chain_cnt

    @up_chain_cnt.setter
    def up_chain_cnt(self, value):
        self._up_chain_cnt = value
    @property
    def valid_miles_sts(self):
        return self._valid_miles_sts

    @valid_miles_sts.setter
    def valid_miles_sts(self, value):
        self._valid_miles_sts = value
    @property
    def valid_trip_sts(self):
        return self._valid_trip_sts

    @valid_trip_sts.setter
    def valid_trip_sts(self, value):
        self._valid_trip_sts = value
    @property
    def wait_time_sts(self):
        return self._wait_time_sts

    @wait_time_sts.setter
    def wait_time_sts(self, value):
        self._wait_time_sts = value
    @property
    def work_time_sts(self):
        return self._work_time_sts

    @work_time_sts.setter
    def work_time_sts(self, value):
        self._work_time_sts = value


    def to_alipay_dict(self):
        params = dict()
        if self.all_miles_sts:
            if hasattr(self.all_miles_sts, 'to_alipay_dict'):
                params['all_miles_sts'] = self.all_miles_sts.to_alipay_dict()
            else:
                params['all_miles_sts'] = self.all_miles_sts
        if self.all_trip_sts:
            if hasattr(self.all_trip_sts, 'to_alipay_dict'):
                params['all_trip_sts'] = self.all_trip_sts.to_alipay_dict()
            else:
                params['all_trip_sts'] = self.all_trip_sts
        if self.down_chain_cnt:
            if hasattr(self.down_chain_cnt, 'to_alipay_dict'):
                params['down_chain_cnt'] = self.down_chain_cnt.to_alipay_dict()
            else:
                params['down_chain_cnt'] = self.down_chain_cnt
        if self.invalid_miles_sts:
            if hasattr(self.invalid_miles_sts, 'to_alipay_dict'):
                params['invalid_miles_sts'] = self.invalid_miles_sts.to_alipay_dict()
            else:
                params['invalid_miles_sts'] = self.invalid_miles_sts
        if self.invalid_trip_sts:
            if hasattr(self.invalid_trip_sts, 'to_alipay_dict'):
                params['invalid_trip_sts'] = self.invalid_trip_sts.to_alipay_dict()
            else:
                params['invalid_trip_sts'] = self.invalid_trip_sts
        if self.line_id:
            if hasattr(self.line_id, 'to_alipay_dict'):
                params['line_id'] = self.line_id.to_alipay_dict()
            else:
                params['line_id'] = self.line_id
        if self.opt_type:
            if hasattr(self.opt_type, 'to_alipay_dict'):
                params['opt_type'] = self.opt_type.to_alipay_dict()
            else:
                params['opt_type'] = self.opt_type
        if self.up_chain_cnt:
            if hasattr(self.up_chain_cnt, 'to_alipay_dict'):
                params['up_chain_cnt'] = self.up_chain_cnt.to_alipay_dict()
            else:
                params['up_chain_cnt'] = self.up_chain_cnt
        if self.valid_miles_sts:
            if hasattr(self.valid_miles_sts, 'to_alipay_dict'):
                params['valid_miles_sts'] = self.valid_miles_sts.to_alipay_dict()
            else:
                params['valid_miles_sts'] = self.valid_miles_sts
        if self.valid_trip_sts:
            if hasattr(self.valid_trip_sts, 'to_alipay_dict'):
                params['valid_trip_sts'] = self.valid_trip_sts.to_alipay_dict()
            else:
                params['valid_trip_sts'] = self.valid_trip_sts
        if self.wait_time_sts:
            if hasattr(self.wait_time_sts, 'to_alipay_dict'):
                params['wait_time_sts'] = self.wait_time_sts.to_alipay_dict()
            else:
                params['wait_time_sts'] = self.wait_time_sts
        if self.work_time_sts:
            if hasattr(self.work_time_sts, 'to_alipay_dict'):
                params['work_time_sts'] = self.work_time_sts.to_alipay_dict()
            else:
                params['work_time_sts'] = self.work_time_sts
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ScheduleWorkStatItem()
        if 'all_miles_sts' in d:
            o.all_miles_sts = d['all_miles_sts']
        if 'all_trip_sts' in d:
            o.all_trip_sts = d['all_trip_sts']
        if 'down_chain_cnt' in d:
            o.down_chain_cnt = d['down_chain_cnt']
        if 'invalid_miles_sts' in d:
            o.invalid_miles_sts = d['invalid_miles_sts']
        if 'invalid_trip_sts' in d:
            o.invalid_trip_sts = d['invalid_trip_sts']
        if 'line_id' in d:
            o.line_id = d['line_id']
        if 'opt_type' in d:
            o.opt_type = d['opt_type']
        if 'up_chain_cnt' in d:
            o.up_chain_cnt = d['up_chain_cnt']
        if 'valid_miles_sts' in d:
            o.valid_miles_sts = d['valid_miles_sts']
        if 'valid_trip_sts' in d:
            o.valid_trip_sts = d['valid_trip_sts']
        if 'wait_time_sts' in d:
            o.wait_time_sts = d['wait_time_sts']
        if 'work_time_sts' in d:
            o.work_time_sts = d['work_time_sts']
        return o


