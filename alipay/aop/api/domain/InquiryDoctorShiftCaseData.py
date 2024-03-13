#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InquiryDoctorShiftCaseData(object):

    def __init__(self):
        self._ext_shift_case_id = None
        self._register_num = None
        self._register_status = None
        self._shift_date = None
        self._shift_time_slot = None
        self._shift_time_slot_type = None

    @property
    def ext_shift_case_id(self):
        return self._ext_shift_case_id

    @ext_shift_case_id.setter
    def ext_shift_case_id(self, value):
        self._ext_shift_case_id = value
    @property
    def register_num(self):
        return self._register_num

    @register_num.setter
    def register_num(self, value):
        self._register_num = value
    @property
    def register_status(self):
        return self._register_status

    @register_status.setter
    def register_status(self, value):
        self._register_status = value
    @property
    def shift_date(self):
        return self._shift_date

    @shift_date.setter
    def shift_date(self, value):
        self._shift_date = value
    @property
    def shift_time_slot(self):
        return self._shift_time_slot

    @shift_time_slot.setter
    def shift_time_slot(self, value):
        self._shift_time_slot = value
    @property
    def shift_time_slot_type(self):
        return self._shift_time_slot_type

    @shift_time_slot_type.setter
    def shift_time_slot_type(self, value):
        self._shift_time_slot_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_shift_case_id:
            if hasattr(self.ext_shift_case_id, 'to_alipay_dict'):
                params['ext_shift_case_id'] = self.ext_shift_case_id.to_alipay_dict()
            else:
                params['ext_shift_case_id'] = self.ext_shift_case_id
        if self.register_num:
            if hasattr(self.register_num, 'to_alipay_dict'):
                params['register_num'] = self.register_num.to_alipay_dict()
            else:
                params['register_num'] = self.register_num
        if self.register_status:
            if hasattr(self.register_status, 'to_alipay_dict'):
                params['register_status'] = self.register_status.to_alipay_dict()
            else:
                params['register_status'] = self.register_status
        if self.shift_date:
            if hasattr(self.shift_date, 'to_alipay_dict'):
                params['shift_date'] = self.shift_date.to_alipay_dict()
            else:
                params['shift_date'] = self.shift_date
        if self.shift_time_slot:
            if hasattr(self.shift_time_slot, 'to_alipay_dict'):
                params['shift_time_slot'] = self.shift_time_slot.to_alipay_dict()
            else:
                params['shift_time_slot'] = self.shift_time_slot
        if self.shift_time_slot_type:
            if hasattr(self.shift_time_slot_type, 'to_alipay_dict'):
                params['shift_time_slot_type'] = self.shift_time_slot_type.to_alipay_dict()
            else:
                params['shift_time_slot_type'] = self.shift_time_slot_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InquiryDoctorShiftCaseData()
        if 'ext_shift_case_id' in d:
            o.ext_shift_case_id = d['ext_shift_case_id']
        if 'register_num' in d:
            o.register_num = d['register_num']
        if 'register_status' in d:
            o.register_status = d['register_status']
        if 'shift_date' in d:
            o.shift_date = d['shift_date']
        if 'shift_time_slot' in d:
            o.shift_time_slot = d['shift_time_slot']
        if 'shift_time_slot_type' in d:
            o.shift_time_slot_type = d['shift_time_slot_type']
        return o


