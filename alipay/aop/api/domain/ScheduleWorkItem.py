#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ScheduleWorkItem(object):

    def __init__(self):
        self._all_miles = None
        self._all_trip_cnt = None
        self._chain_num = None
        self._invalid_miles = None
        self._invalid_trip_cnt = None
        self._line_id = None
        self._opt_type = None
        self._shift_id = None
        self._trip_chain = None
        self._valid_miles = None
        self._valid_trip_cnt = None
        self._wait_time = None
        self._work_endtime = None
        self._work_id = None
        self._work_starttime = None
        self._work_time = None

    @property
    def all_miles(self):
        return self._all_miles

    @all_miles.setter
    def all_miles(self, value):
        self._all_miles = value
    @property
    def all_trip_cnt(self):
        return self._all_trip_cnt

    @all_trip_cnt.setter
    def all_trip_cnt(self, value):
        self._all_trip_cnt = value
    @property
    def chain_num(self):
        return self._chain_num

    @chain_num.setter
    def chain_num(self, value):
        self._chain_num = value
    @property
    def invalid_miles(self):
        return self._invalid_miles

    @invalid_miles.setter
    def invalid_miles(self, value):
        self._invalid_miles = value
    @property
    def invalid_trip_cnt(self):
        return self._invalid_trip_cnt

    @invalid_trip_cnt.setter
    def invalid_trip_cnt(self, value):
        self._invalid_trip_cnt = value
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
    def shift_id(self):
        return self._shift_id

    @shift_id.setter
    def shift_id(self, value):
        self._shift_id = value
    @property
    def trip_chain(self):
        return self._trip_chain

    @trip_chain.setter
    def trip_chain(self, value):
        self._trip_chain = value
    @property
    def valid_miles(self):
        return self._valid_miles

    @valid_miles.setter
    def valid_miles(self, value):
        self._valid_miles = value
    @property
    def valid_trip_cnt(self):
        return self._valid_trip_cnt

    @valid_trip_cnt.setter
    def valid_trip_cnt(self, value):
        self._valid_trip_cnt = value
    @property
    def wait_time(self):
        return self._wait_time

    @wait_time.setter
    def wait_time(self, value):
        self._wait_time = value
    @property
    def work_endtime(self):
        return self._work_endtime

    @work_endtime.setter
    def work_endtime(self, value):
        self._work_endtime = value
    @property
    def work_id(self):
        return self._work_id

    @work_id.setter
    def work_id(self, value):
        self._work_id = value
    @property
    def work_starttime(self):
        return self._work_starttime

    @work_starttime.setter
    def work_starttime(self, value):
        self._work_starttime = value
    @property
    def work_time(self):
        return self._work_time

    @work_time.setter
    def work_time(self, value):
        self._work_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.all_miles:
            if hasattr(self.all_miles, 'to_alipay_dict'):
                params['all_miles'] = self.all_miles.to_alipay_dict()
            else:
                params['all_miles'] = self.all_miles
        if self.all_trip_cnt:
            if hasattr(self.all_trip_cnt, 'to_alipay_dict'):
                params['all_trip_cnt'] = self.all_trip_cnt.to_alipay_dict()
            else:
                params['all_trip_cnt'] = self.all_trip_cnt
        if self.chain_num:
            if hasattr(self.chain_num, 'to_alipay_dict'):
                params['chain_num'] = self.chain_num.to_alipay_dict()
            else:
                params['chain_num'] = self.chain_num
        if self.invalid_miles:
            if hasattr(self.invalid_miles, 'to_alipay_dict'):
                params['invalid_miles'] = self.invalid_miles.to_alipay_dict()
            else:
                params['invalid_miles'] = self.invalid_miles
        if self.invalid_trip_cnt:
            if hasattr(self.invalid_trip_cnt, 'to_alipay_dict'):
                params['invalid_trip_cnt'] = self.invalid_trip_cnt.to_alipay_dict()
            else:
                params['invalid_trip_cnt'] = self.invalid_trip_cnt
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
        if self.shift_id:
            if hasattr(self.shift_id, 'to_alipay_dict'):
                params['shift_id'] = self.shift_id.to_alipay_dict()
            else:
                params['shift_id'] = self.shift_id
        if self.trip_chain:
            if hasattr(self.trip_chain, 'to_alipay_dict'):
                params['trip_chain'] = self.trip_chain.to_alipay_dict()
            else:
                params['trip_chain'] = self.trip_chain
        if self.valid_miles:
            if hasattr(self.valid_miles, 'to_alipay_dict'):
                params['valid_miles'] = self.valid_miles.to_alipay_dict()
            else:
                params['valid_miles'] = self.valid_miles
        if self.valid_trip_cnt:
            if hasattr(self.valid_trip_cnt, 'to_alipay_dict'):
                params['valid_trip_cnt'] = self.valid_trip_cnt.to_alipay_dict()
            else:
                params['valid_trip_cnt'] = self.valid_trip_cnt
        if self.wait_time:
            if hasattr(self.wait_time, 'to_alipay_dict'):
                params['wait_time'] = self.wait_time.to_alipay_dict()
            else:
                params['wait_time'] = self.wait_time
        if self.work_endtime:
            if hasattr(self.work_endtime, 'to_alipay_dict'):
                params['work_endtime'] = self.work_endtime.to_alipay_dict()
            else:
                params['work_endtime'] = self.work_endtime
        if self.work_id:
            if hasattr(self.work_id, 'to_alipay_dict'):
                params['work_id'] = self.work_id.to_alipay_dict()
            else:
                params['work_id'] = self.work_id
        if self.work_starttime:
            if hasattr(self.work_starttime, 'to_alipay_dict'):
                params['work_starttime'] = self.work_starttime.to_alipay_dict()
            else:
                params['work_starttime'] = self.work_starttime
        if self.work_time:
            if hasattr(self.work_time, 'to_alipay_dict'):
                params['work_time'] = self.work_time.to_alipay_dict()
            else:
                params['work_time'] = self.work_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ScheduleWorkItem()
        if 'all_miles' in d:
            o.all_miles = d['all_miles']
        if 'all_trip_cnt' in d:
            o.all_trip_cnt = d['all_trip_cnt']
        if 'chain_num' in d:
            o.chain_num = d['chain_num']
        if 'invalid_miles' in d:
            o.invalid_miles = d['invalid_miles']
        if 'invalid_trip_cnt' in d:
            o.invalid_trip_cnt = d['invalid_trip_cnt']
        if 'line_id' in d:
            o.line_id = d['line_id']
        if 'opt_type' in d:
            o.opt_type = d['opt_type']
        if 'shift_id' in d:
            o.shift_id = d['shift_id']
        if 'trip_chain' in d:
            o.trip_chain = d['trip_chain']
        if 'valid_miles' in d:
            o.valid_miles = d['valid_miles']
        if 'valid_trip_cnt' in d:
            o.valid_trip_cnt = d['valid_trip_cnt']
        if 'wait_time' in d:
            o.wait_time = d['wait_time']
        if 'work_endtime' in d:
            o.work_endtime = d['work_endtime']
        if 'work_id' in d:
            o.work_id = d['work_id']
        if 'work_starttime' in d:
            o.work_starttime = d['work_starttime']
        if 'work_time' in d:
            o.work_time = d['work_time']
        return o


