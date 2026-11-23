#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DtdeployShift(object):

    def __init__(self):
        self._nebula_user_id = None
        self._pb_code = None
        self._pb_end_time = None
        self._pb_start_time = None
        self._shift_type = None
        self._tnt_inst_id = None

    @property
    def nebula_user_id(self):
        return self._nebula_user_id

    @nebula_user_id.setter
    def nebula_user_id(self, value):
        self._nebula_user_id = value
    @property
    def pb_code(self):
        return self._pb_code

    @pb_code.setter
    def pb_code(self, value):
        self._pb_code = value
    @property
    def pb_end_time(self):
        return self._pb_end_time

    @pb_end_time.setter
    def pb_end_time(self, value):
        self._pb_end_time = value
    @property
    def pb_start_time(self):
        return self._pb_start_time

    @pb_start_time.setter
    def pb_start_time(self, value):
        self._pb_start_time = value
    @property
    def shift_type(self):
        return self._shift_type

    @shift_type.setter
    def shift_type(self, value):
        self._shift_type = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.nebula_user_id:
            if hasattr(self.nebula_user_id, 'to_alipay_dict'):
                params['nebula_user_id'] = self.nebula_user_id.to_alipay_dict()
            else:
                params['nebula_user_id'] = self.nebula_user_id
        if self.pb_code:
            if hasattr(self.pb_code, 'to_alipay_dict'):
                params['pb_code'] = self.pb_code.to_alipay_dict()
            else:
                params['pb_code'] = self.pb_code
        if self.pb_end_time:
            if hasattr(self.pb_end_time, 'to_alipay_dict'):
                params['pb_end_time'] = self.pb_end_time.to_alipay_dict()
            else:
                params['pb_end_time'] = self.pb_end_time
        if self.pb_start_time:
            if hasattr(self.pb_start_time, 'to_alipay_dict'):
                params['pb_start_time'] = self.pb_start_time.to_alipay_dict()
            else:
                params['pb_start_time'] = self.pb_start_time
        if self.shift_type:
            if hasattr(self.shift_type, 'to_alipay_dict'):
                params['shift_type'] = self.shift_type.to_alipay_dict()
            else:
                params['shift_type'] = self.shift_type
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DtdeployShift()
        if 'nebula_user_id' in d:
            o.nebula_user_id = d['nebula_user_id']
        if 'pb_code' in d:
            o.pb_code = d['pb_code']
        if 'pb_end_time' in d:
            o.pb_end_time = d['pb_end_time']
        if 'pb_start_time' in d:
            o.pb_start_time = d['pb_start_time']
        if 'shift_type' in d:
            o.shift_type = d['shift_type']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


