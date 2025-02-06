#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoyagerSegmentOfPassengersChangedInfo(object):

    def __init__(self):
        self._arrive_airport_changed = None
        self._arrive_time_changed = None
        self._depart_airport_changed = None
        self._depart_time_changed = None
        self._flight_no_changed = None
        self._need_confirm_seat = None
        self._new_arrive_airport_code = None
        self._new_depart_airport_code = None
        self._new_depart_time = None
        self._new_flight_no = None
        self._old_arrive_airport_code = None
        self._old_depart_airport_code = None
        self._old_depart_time = None
        self._old_flight_no = None
        self._passenger_name = None

    @property
    def arrive_airport_changed(self):
        return self._arrive_airport_changed

    @arrive_airport_changed.setter
    def arrive_airport_changed(self, value):
        self._arrive_airport_changed = value
    @property
    def arrive_time_changed(self):
        return self._arrive_time_changed

    @arrive_time_changed.setter
    def arrive_time_changed(self, value):
        self._arrive_time_changed = value
    @property
    def depart_airport_changed(self):
        return self._depart_airport_changed

    @depart_airport_changed.setter
    def depart_airport_changed(self, value):
        self._depart_airport_changed = value
    @property
    def depart_time_changed(self):
        return self._depart_time_changed

    @depart_time_changed.setter
    def depart_time_changed(self, value):
        self._depart_time_changed = value
    @property
    def flight_no_changed(self):
        return self._flight_no_changed

    @flight_no_changed.setter
    def flight_no_changed(self, value):
        self._flight_no_changed = value
    @property
    def need_confirm_seat(self):
        return self._need_confirm_seat

    @need_confirm_seat.setter
    def need_confirm_seat(self, value):
        self._need_confirm_seat = value
    @property
    def new_arrive_airport_code(self):
        return self._new_arrive_airport_code

    @new_arrive_airport_code.setter
    def new_arrive_airport_code(self, value):
        self._new_arrive_airport_code = value
    @property
    def new_depart_airport_code(self):
        return self._new_depart_airport_code

    @new_depart_airport_code.setter
    def new_depart_airport_code(self, value):
        self._new_depart_airport_code = value
    @property
    def new_depart_time(self):
        return self._new_depart_time

    @new_depart_time.setter
    def new_depart_time(self, value):
        self._new_depart_time = value
    @property
    def new_flight_no(self):
        return self._new_flight_no

    @new_flight_no.setter
    def new_flight_no(self, value):
        self._new_flight_no = value
    @property
    def old_arrive_airport_code(self):
        return self._old_arrive_airport_code

    @old_arrive_airport_code.setter
    def old_arrive_airport_code(self, value):
        self._old_arrive_airport_code = value
    @property
    def old_depart_airport_code(self):
        return self._old_depart_airport_code

    @old_depart_airport_code.setter
    def old_depart_airport_code(self, value):
        self._old_depart_airport_code = value
    @property
    def old_depart_time(self):
        return self._old_depart_time

    @old_depart_time.setter
    def old_depart_time(self, value):
        self._old_depart_time = value
    @property
    def old_flight_no(self):
        return self._old_flight_no

    @old_flight_no.setter
    def old_flight_no(self, value):
        self._old_flight_no = value
    @property
    def passenger_name(self):
        return self._passenger_name

    @passenger_name.setter
    def passenger_name(self, value):
        self._passenger_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.arrive_airport_changed:
            if hasattr(self.arrive_airport_changed, 'to_alipay_dict'):
                params['arrive_airport_changed'] = self.arrive_airport_changed.to_alipay_dict()
            else:
                params['arrive_airport_changed'] = self.arrive_airport_changed
        if self.arrive_time_changed:
            if hasattr(self.arrive_time_changed, 'to_alipay_dict'):
                params['arrive_time_changed'] = self.arrive_time_changed.to_alipay_dict()
            else:
                params['arrive_time_changed'] = self.arrive_time_changed
        if self.depart_airport_changed:
            if hasattr(self.depart_airport_changed, 'to_alipay_dict'):
                params['depart_airport_changed'] = self.depart_airport_changed.to_alipay_dict()
            else:
                params['depart_airport_changed'] = self.depart_airport_changed
        if self.depart_time_changed:
            if hasattr(self.depart_time_changed, 'to_alipay_dict'):
                params['depart_time_changed'] = self.depart_time_changed.to_alipay_dict()
            else:
                params['depart_time_changed'] = self.depart_time_changed
        if self.flight_no_changed:
            if hasattr(self.flight_no_changed, 'to_alipay_dict'):
                params['flight_no_changed'] = self.flight_no_changed.to_alipay_dict()
            else:
                params['flight_no_changed'] = self.flight_no_changed
        if self.need_confirm_seat:
            if hasattr(self.need_confirm_seat, 'to_alipay_dict'):
                params['need_confirm_seat'] = self.need_confirm_seat.to_alipay_dict()
            else:
                params['need_confirm_seat'] = self.need_confirm_seat
        if self.new_arrive_airport_code:
            if hasattr(self.new_arrive_airport_code, 'to_alipay_dict'):
                params['new_arrive_airport_code'] = self.new_arrive_airport_code.to_alipay_dict()
            else:
                params['new_arrive_airport_code'] = self.new_arrive_airport_code
        if self.new_depart_airport_code:
            if hasattr(self.new_depart_airport_code, 'to_alipay_dict'):
                params['new_depart_airport_code'] = self.new_depart_airport_code.to_alipay_dict()
            else:
                params['new_depart_airport_code'] = self.new_depart_airport_code
        if self.new_depart_time:
            if hasattr(self.new_depart_time, 'to_alipay_dict'):
                params['new_depart_time'] = self.new_depart_time.to_alipay_dict()
            else:
                params['new_depart_time'] = self.new_depart_time
        if self.new_flight_no:
            if hasattr(self.new_flight_no, 'to_alipay_dict'):
                params['new_flight_no'] = self.new_flight_no.to_alipay_dict()
            else:
                params['new_flight_no'] = self.new_flight_no
        if self.old_arrive_airport_code:
            if hasattr(self.old_arrive_airport_code, 'to_alipay_dict'):
                params['old_arrive_airport_code'] = self.old_arrive_airport_code.to_alipay_dict()
            else:
                params['old_arrive_airport_code'] = self.old_arrive_airport_code
        if self.old_depart_airport_code:
            if hasattr(self.old_depart_airport_code, 'to_alipay_dict'):
                params['old_depart_airport_code'] = self.old_depart_airport_code.to_alipay_dict()
            else:
                params['old_depart_airport_code'] = self.old_depart_airport_code
        if self.old_depart_time:
            if hasattr(self.old_depart_time, 'to_alipay_dict'):
                params['old_depart_time'] = self.old_depart_time.to_alipay_dict()
            else:
                params['old_depart_time'] = self.old_depart_time
        if self.old_flight_no:
            if hasattr(self.old_flight_no, 'to_alipay_dict'):
                params['old_flight_no'] = self.old_flight_no.to_alipay_dict()
            else:
                params['old_flight_no'] = self.old_flight_no
        if self.passenger_name:
            if hasattr(self.passenger_name, 'to_alipay_dict'):
                params['passenger_name'] = self.passenger_name.to_alipay_dict()
            else:
                params['passenger_name'] = self.passenger_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoyagerSegmentOfPassengersChangedInfo()
        if 'arrive_airport_changed' in d:
            o.arrive_airport_changed = d['arrive_airport_changed']
        if 'arrive_time_changed' in d:
            o.arrive_time_changed = d['arrive_time_changed']
        if 'depart_airport_changed' in d:
            o.depart_airport_changed = d['depart_airport_changed']
        if 'depart_time_changed' in d:
            o.depart_time_changed = d['depart_time_changed']
        if 'flight_no_changed' in d:
            o.flight_no_changed = d['flight_no_changed']
        if 'need_confirm_seat' in d:
            o.need_confirm_seat = d['need_confirm_seat']
        if 'new_arrive_airport_code' in d:
            o.new_arrive_airport_code = d['new_arrive_airport_code']
        if 'new_depart_airport_code' in d:
            o.new_depart_airport_code = d['new_depart_airport_code']
        if 'new_depart_time' in d:
            o.new_depart_time = d['new_depart_time']
        if 'new_flight_no' in d:
            o.new_flight_no = d['new_flight_no']
        if 'old_arrive_airport_code' in d:
            o.old_arrive_airport_code = d['old_arrive_airport_code']
        if 'old_depart_airport_code' in d:
            o.old_depart_airport_code = d['old_depart_airport_code']
        if 'old_depart_time' in d:
            o.old_depart_time = d['old_depart_time']
        if 'old_flight_no' in d:
            o.old_flight_no = d['old_flight_no']
        if 'passenger_name' in d:
            o.passenger_name = d['passenger_name']
        return o


