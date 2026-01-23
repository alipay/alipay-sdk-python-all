#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AxfBookingInfo(object):

    def __init__(self):
        self._booking_create_time = None
        self._booking_date = None
        self._booking_id = None
        self._card_id = None
        self._end_time = None
        self._nick = None
        self._out_booking_id = None
        self._phone = None
        self._remark = None
        self._service_id = None
        self._shop_id = None
        self._start_time = None
        self._status = None
        self._technician_id = None

    @property
    def booking_create_time(self):
        return self._booking_create_time

    @booking_create_time.setter
    def booking_create_time(self, value):
        self._booking_create_time = value
    @property
    def booking_date(self):
        return self._booking_date

    @booking_date.setter
    def booking_date(self, value):
        self._booking_date = value
    @property
    def booking_id(self):
        return self._booking_id

    @booking_id.setter
    def booking_id(self, value):
        self._booking_id = value
    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def nick(self):
        return self._nick

    @nick.setter
    def nick(self, value):
        self._nick = value
    @property
    def out_booking_id(self):
        return self._out_booking_id

    @out_booking_id.setter
    def out_booking_id(self, value):
        self._out_booking_id = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def technician_id(self):
        return self._technician_id

    @technician_id.setter
    def technician_id(self, value):
        self._technician_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.booking_create_time:
            if hasattr(self.booking_create_time, 'to_alipay_dict'):
                params['booking_create_time'] = self.booking_create_time.to_alipay_dict()
            else:
                params['booking_create_time'] = self.booking_create_time
        if self.booking_date:
            if hasattr(self.booking_date, 'to_alipay_dict'):
                params['booking_date'] = self.booking_date.to_alipay_dict()
            else:
                params['booking_date'] = self.booking_date
        if self.booking_id:
            if hasattr(self.booking_id, 'to_alipay_dict'):
                params['booking_id'] = self.booking_id.to_alipay_dict()
            else:
                params['booking_id'] = self.booking_id
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.nick:
            if hasattr(self.nick, 'to_alipay_dict'):
                params['nick'] = self.nick.to_alipay_dict()
            else:
                params['nick'] = self.nick
        if self.out_booking_id:
            if hasattr(self.out_booking_id, 'to_alipay_dict'):
                params['out_booking_id'] = self.out_booking_id.to_alipay_dict()
            else:
                params['out_booking_id'] = self.out_booking_id
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.technician_id:
            if hasattr(self.technician_id, 'to_alipay_dict'):
                params['technician_id'] = self.technician_id.to_alipay_dict()
            else:
                params['technician_id'] = self.technician_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AxfBookingInfo()
        if 'booking_create_time' in d:
            o.booking_create_time = d['booking_create_time']
        if 'booking_date' in d:
            o.booking_date = d['booking_date']
        if 'booking_id' in d:
            o.booking_id = d['booking_id']
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'nick' in d:
            o.nick = d['nick']
        if 'out_booking_id' in d:
            o.out_booking_id = d['out_booking_id']
        if 'phone' in d:
            o.phone = d['phone']
        if 'remark' in d:
            o.remark = d['remark']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        if 'technician_id' in d:
            o.technician_id = d['technician_id']
        return o


