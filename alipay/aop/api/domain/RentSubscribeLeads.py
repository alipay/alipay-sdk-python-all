#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentSubscribeLeads(object):

    def __init__(self):
        self._appointment_date = None
        self._appointment_time = None
        self._remarks = None
        self._renter_mobile_num = None
        self._renter_name = None
        self._room_code = None

    @property
    def appointment_date(self):
        return self._appointment_date

    @appointment_date.setter
    def appointment_date(self, value):
        self._appointment_date = value
    @property
    def appointment_time(self):
        return self._appointment_time

    @appointment_time.setter
    def appointment_time(self, value):
        self._appointment_time = value
    @property
    def remarks(self):
        return self._remarks

    @remarks.setter
    def remarks(self, value):
        self._remarks = value
    @property
    def renter_mobile_num(self):
        return self._renter_mobile_num

    @renter_mobile_num.setter
    def renter_mobile_num(self, value):
        self._renter_mobile_num = value
    @property
    def renter_name(self):
        return self._renter_name

    @renter_name.setter
    def renter_name(self, value):
        self._renter_name = value
    @property
    def room_code(self):
        return self._room_code

    @room_code.setter
    def room_code(self, value):
        self._room_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.appointment_date:
            if hasattr(self.appointment_date, 'to_alipay_dict'):
                params['appointment_date'] = self.appointment_date.to_alipay_dict()
            else:
                params['appointment_date'] = self.appointment_date
        if self.appointment_time:
            if hasattr(self.appointment_time, 'to_alipay_dict'):
                params['appointment_time'] = self.appointment_time.to_alipay_dict()
            else:
                params['appointment_time'] = self.appointment_time
        if self.remarks:
            if hasattr(self.remarks, 'to_alipay_dict'):
                params['remarks'] = self.remarks.to_alipay_dict()
            else:
                params['remarks'] = self.remarks
        if self.renter_mobile_num:
            if hasattr(self.renter_mobile_num, 'to_alipay_dict'):
                params['renter_mobile_num'] = self.renter_mobile_num.to_alipay_dict()
            else:
                params['renter_mobile_num'] = self.renter_mobile_num
        if self.renter_name:
            if hasattr(self.renter_name, 'to_alipay_dict'):
                params['renter_name'] = self.renter_name.to_alipay_dict()
            else:
                params['renter_name'] = self.renter_name
        if self.room_code:
            if hasattr(self.room_code, 'to_alipay_dict'):
                params['room_code'] = self.room_code.to_alipay_dict()
            else:
                params['room_code'] = self.room_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentSubscribeLeads()
        if 'appointment_date' in d:
            o.appointment_date = d['appointment_date']
        if 'appointment_time' in d:
            o.appointment_time = d['appointment_time']
        if 'remarks' in d:
            o.remarks = d['remarks']
        if 'renter_mobile_num' in d:
            o.renter_mobile_num = d['renter_mobile_num']
        if 'renter_name' in d:
            o.renter_name = d['renter_name']
        if 'room_code' in d:
            o.room_code = d['room_code']
        return o


