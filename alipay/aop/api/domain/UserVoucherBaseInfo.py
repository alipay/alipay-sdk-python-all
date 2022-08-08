#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserVoucherBaseInfo(object):

    def __init__(self):
        self._associate_trade_no = None
        self._create_time = None
        self._valid_begin_time = None
        self._valid_end_time = None
        self._voucher_id = None
        self._voucher_max_use_times = None
        self._voucher_name = None
        self._voucher_status = None
        self._voucher_used_times = None

    @property
    def associate_trade_no(self):
        return self._associate_trade_no

    @associate_trade_no.setter
    def associate_trade_no(self, value):
        self._associate_trade_no = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def valid_begin_time(self):
        return self._valid_begin_time

    @valid_begin_time.setter
    def valid_begin_time(self, value):
        self._valid_begin_time = value
    @property
    def valid_end_time(self):
        return self._valid_end_time

    @valid_end_time.setter
    def valid_end_time(self, value):
        self._valid_end_time = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value
    @property
    def voucher_max_use_times(self):
        return self._voucher_max_use_times

    @voucher_max_use_times.setter
    def voucher_max_use_times(self, value):
        self._voucher_max_use_times = value
    @property
    def voucher_name(self):
        return self._voucher_name

    @voucher_name.setter
    def voucher_name(self, value):
        self._voucher_name = value
    @property
    def voucher_status(self):
        return self._voucher_status

    @voucher_status.setter
    def voucher_status(self, value):
        self._voucher_status = value
    @property
    def voucher_used_times(self):
        return self._voucher_used_times

    @voucher_used_times.setter
    def voucher_used_times(self, value):
        self._voucher_used_times = value


    def to_alipay_dict(self):
        params = dict()
        if self.associate_trade_no:
            if hasattr(self.associate_trade_no, 'to_alipay_dict'):
                params['associate_trade_no'] = self.associate_trade_no.to_alipay_dict()
            else:
                params['associate_trade_no'] = self.associate_trade_no
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.valid_begin_time:
            if hasattr(self.valid_begin_time, 'to_alipay_dict'):
                params['valid_begin_time'] = self.valid_begin_time.to_alipay_dict()
            else:
                params['valid_begin_time'] = self.valid_begin_time
        if self.valid_end_time:
            if hasattr(self.valid_end_time, 'to_alipay_dict'):
                params['valid_end_time'] = self.valid_end_time.to_alipay_dict()
            else:
                params['valid_end_time'] = self.valid_end_time
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        if self.voucher_max_use_times:
            if hasattr(self.voucher_max_use_times, 'to_alipay_dict'):
                params['voucher_max_use_times'] = self.voucher_max_use_times.to_alipay_dict()
            else:
                params['voucher_max_use_times'] = self.voucher_max_use_times
        if self.voucher_name:
            if hasattr(self.voucher_name, 'to_alipay_dict'):
                params['voucher_name'] = self.voucher_name.to_alipay_dict()
            else:
                params['voucher_name'] = self.voucher_name
        if self.voucher_status:
            if hasattr(self.voucher_status, 'to_alipay_dict'):
                params['voucher_status'] = self.voucher_status.to_alipay_dict()
            else:
                params['voucher_status'] = self.voucher_status
        if self.voucher_used_times:
            if hasattr(self.voucher_used_times, 'to_alipay_dict'):
                params['voucher_used_times'] = self.voucher_used_times.to_alipay_dict()
            else:
                params['voucher_used_times'] = self.voucher_used_times
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserVoucherBaseInfo()
        if 'associate_trade_no' in d:
            o.associate_trade_no = d['associate_trade_no']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'valid_begin_time' in d:
            o.valid_begin_time = d['valid_begin_time']
        if 'valid_end_time' in d:
            o.valid_end_time = d['valid_end_time']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        if 'voucher_max_use_times' in d:
            o.voucher_max_use_times = d['voucher_max_use_times']
        if 'voucher_name' in d:
            o.voucher_name = d['voucher_name']
        if 'voucher_status' in d:
            o.voucher_status = d['voucher_status']
        if 'voucher_used_times' in d:
            o.voucher_used_times = d['voucher_used_times']
        return o


