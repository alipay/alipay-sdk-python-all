#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BookingInfoDTO(object):

    def __init__(self):
        self._booking_time = None
        self._check_in_date = None
        self._check_in_time = None
        self._check_out_date = None
        self._check_out_time = None
        self._confirm_booking_time = None
        self._customer_service_mobile = None
        self._deadline = None
        self._have_stay_time = None
        self._refund_rule = None
        self._room_num = None

    @property
    def booking_time(self):
        return self._booking_time

    @booking_time.setter
    def booking_time(self, value):
        self._booking_time = value
    @property
    def check_in_date(self):
        return self._check_in_date

    @check_in_date.setter
    def check_in_date(self, value):
        self._check_in_date = value
    @property
    def check_in_time(self):
        return self._check_in_time

    @check_in_time.setter
    def check_in_time(self, value):
        self._check_in_time = value
    @property
    def check_out_date(self):
        return self._check_out_date

    @check_out_date.setter
    def check_out_date(self, value):
        self._check_out_date = value
    @property
    def check_out_time(self):
        return self._check_out_time

    @check_out_time.setter
    def check_out_time(self, value):
        self._check_out_time = value
    @property
    def confirm_booking_time(self):
        return self._confirm_booking_time

    @confirm_booking_time.setter
    def confirm_booking_time(self, value):
        self._confirm_booking_time = value
    @property
    def customer_service_mobile(self):
        return self._customer_service_mobile

    @customer_service_mobile.setter
    def customer_service_mobile(self, value):
        self._customer_service_mobile = value
    @property
    def deadline(self):
        return self._deadline

    @deadline.setter
    def deadline(self, value):
        self._deadline = value
    @property
    def have_stay_time(self):
        return self._have_stay_time

    @have_stay_time.setter
    def have_stay_time(self, value):
        self._have_stay_time = value
    @property
    def refund_rule(self):
        return self._refund_rule

    @refund_rule.setter
    def refund_rule(self, value):
        self._refund_rule = value
    @property
    def room_num(self):
        return self._room_num

    @room_num.setter
    def room_num(self, value):
        self._room_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.booking_time:
            if hasattr(self.booking_time, 'to_alipay_dict'):
                params['booking_time'] = self.booking_time.to_alipay_dict()
            else:
                params['booking_time'] = self.booking_time
        if self.check_in_date:
            if hasattr(self.check_in_date, 'to_alipay_dict'):
                params['check_in_date'] = self.check_in_date.to_alipay_dict()
            else:
                params['check_in_date'] = self.check_in_date
        if self.check_in_time:
            if hasattr(self.check_in_time, 'to_alipay_dict'):
                params['check_in_time'] = self.check_in_time.to_alipay_dict()
            else:
                params['check_in_time'] = self.check_in_time
        if self.check_out_date:
            if hasattr(self.check_out_date, 'to_alipay_dict'):
                params['check_out_date'] = self.check_out_date.to_alipay_dict()
            else:
                params['check_out_date'] = self.check_out_date
        if self.check_out_time:
            if hasattr(self.check_out_time, 'to_alipay_dict'):
                params['check_out_time'] = self.check_out_time.to_alipay_dict()
            else:
                params['check_out_time'] = self.check_out_time
        if self.confirm_booking_time:
            if hasattr(self.confirm_booking_time, 'to_alipay_dict'):
                params['confirm_booking_time'] = self.confirm_booking_time.to_alipay_dict()
            else:
                params['confirm_booking_time'] = self.confirm_booking_time
        if self.customer_service_mobile:
            if hasattr(self.customer_service_mobile, 'to_alipay_dict'):
                params['customer_service_mobile'] = self.customer_service_mobile.to_alipay_dict()
            else:
                params['customer_service_mobile'] = self.customer_service_mobile
        if self.deadline:
            if hasattr(self.deadline, 'to_alipay_dict'):
                params['deadline'] = self.deadline.to_alipay_dict()
            else:
                params['deadline'] = self.deadline
        if self.have_stay_time:
            if hasattr(self.have_stay_time, 'to_alipay_dict'):
                params['have_stay_time'] = self.have_stay_time.to_alipay_dict()
            else:
                params['have_stay_time'] = self.have_stay_time
        if self.refund_rule:
            if hasattr(self.refund_rule, 'to_alipay_dict'):
                params['refund_rule'] = self.refund_rule.to_alipay_dict()
            else:
                params['refund_rule'] = self.refund_rule
        if self.room_num:
            if hasattr(self.room_num, 'to_alipay_dict'):
                params['room_num'] = self.room_num.to_alipay_dict()
            else:
                params['room_num'] = self.room_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BookingInfoDTO()
        if 'booking_time' in d:
            o.booking_time = d['booking_time']
        if 'check_in_date' in d:
            o.check_in_date = d['check_in_date']
        if 'check_in_time' in d:
            o.check_in_time = d['check_in_time']
        if 'check_out_date' in d:
            o.check_out_date = d['check_out_date']
        if 'check_out_time' in d:
            o.check_out_time = d['check_out_time']
        if 'confirm_booking_time' in d:
            o.confirm_booking_time = d['confirm_booking_time']
        if 'customer_service_mobile' in d:
            o.customer_service_mobile = d['customer_service_mobile']
        if 'deadline' in d:
            o.deadline = d['deadline']
        if 'have_stay_time' in d:
            o.have_stay_time = d['have_stay_time']
        if 'refund_rule' in d:
            o.refund_rule = d['refund_rule']
        if 'room_num' in d:
            o.room_num = d['room_num']
        return o


