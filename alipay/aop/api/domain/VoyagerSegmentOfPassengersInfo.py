#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoyagerSegmentOfPassengersInfo(object):

    def __init__(self):
        self._arrive_airport_code = None
        self._arrive_city_code = None
        self._arrive_terminal = None
        self._arrive_time = None
        self._cabin_class_code = None
        self._depart_airport_code = None
        self._depart_city_code = None
        self._depart_date = None
        self._depart_terminal = None
        self._depart_time = None
        self._expire_reason = None
        self._flight_duration = None
        self._flight_no = None
        self._journey_index = None
        self._passenger_name = None
        self._passenger_type = None
        self._pnr = None
        self._segment_index = None
        self._segment_type = None
        self._ticket_no = None

    @property
    def arrive_airport_code(self):
        return self._arrive_airport_code

    @arrive_airport_code.setter
    def arrive_airport_code(self, value):
        self._arrive_airport_code = value
    @property
    def arrive_city_code(self):
        return self._arrive_city_code

    @arrive_city_code.setter
    def arrive_city_code(self, value):
        self._arrive_city_code = value
    @property
    def arrive_terminal(self):
        return self._arrive_terminal

    @arrive_terminal.setter
    def arrive_terminal(self, value):
        self._arrive_terminal = value
    @property
    def arrive_time(self):
        return self._arrive_time

    @arrive_time.setter
    def arrive_time(self, value):
        self._arrive_time = value
    @property
    def cabin_class_code(self):
        return self._cabin_class_code

    @cabin_class_code.setter
    def cabin_class_code(self, value):
        self._cabin_class_code = value
    @property
    def depart_airport_code(self):
        return self._depart_airport_code

    @depart_airport_code.setter
    def depart_airport_code(self, value):
        self._depart_airport_code = value
    @property
    def depart_city_code(self):
        return self._depart_city_code

    @depart_city_code.setter
    def depart_city_code(self, value):
        self._depart_city_code = value
    @property
    def depart_date(self):
        return self._depart_date

    @depart_date.setter
    def depart_date(self, value):
        self._depart_date = value
    @property
    def depart_terminal(self):
        return self._depart_terminal

    @depart_terminal.setter
    def depart_terminal(self, value):
        self._depart_terminal = value
    @property
    def depart_time(self):
        return self._depart_time

    @depart_time.setter
    def depart_time(self, value):
        self._depart_time = value
    @property
    def expire_reason(self):
        return self._expire_reason

    @expire_reason.setter
    def expire_reason(self, value):
        self._expire_reason = value
    @property
    def flight_duration(self):
        return self._flight_duration

    @flight_duration.setter
    def flight_duration(self, value):
        self._flight_duration = value
    @property
    def flight_no(self):
        return self._flight_no

    @flight_no.setter
    def flight_no(self, value):
        self._flight_no = value
    @property
    def journey_index(self):
        return self._journey_index

    @journey_index.setter
    def journey_index(self, value):
        self._journey_index = value
    @property
    def passenger_name(self):
        return self._passenger_name

    @passenger_name.setter
    def passenger_name(self, value):
        self._passenger_name = value
    @property
    def passenger_type(self):
        return self._passenger_type

    @passenger_type.setter
    def passenger_type(self, value):
        self._passenger_type = value
    @property
    def pnr(self):
        return self._pnr

    @pnr.setter
    def pnr(self, value):
        self._pnr = value
    @property
    def segment_index(self):
        return self._segment_index

    @segment_index.setter
    def segment_index(self, value):
        self._segment_index = value
    @property
    def segment_type(self):
        return self._segment_type

    @segment_type.setter
    def segment_type(self, value):
        self._segment_type = value
    @property
    def ticket_no(self):
        return self._ticket_no

    @ticket_no.setter
    def ticket_no(self, value):
        self._ticket_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.arrive_airport_code:
            if hasattr(self.arrive_airport_code, 'to_alipay_dict'):
                params['arrive_airport_code'] = self.arrive_airport_code.to_alipay_dict()
            else:
                params['arrive_airport_code'] = self.arrive_airport_code
        if self.arrive_city_code:
            if hasattr(self.arrive_city_code, 'to_alipay_dict'):
                params['arrive_city_code'] = self.arrive_city_code.to_alipay_dict()
            else:
                params['arrive_city_code'] = self.arrive_city_code
        if self.arrive_terminal:
            if hasattr(self.arrive_terminal, 'to_alipay_dict'):
                params['arrive_terminal'] = self.arrive_terminal.to_alipay_dict()
            else:
                params['arrive_terminal'] = self.arrive_terminal
        if self.arrive_time:
            if hasattr(self.arrive_time, 'to_alipay_dict'):
                params['arrive_time'] = self.arrive_time.to_alipay_dict()
            else:
                params['arrive_time'] = self.arrive_time
        if self.cabin_class_code:
            if hasattr(self.cabin_class_code, 'to_alipay_dict'):
                params['cabin_class_code'] = self.cabin_class_code.to_alipay_dict()
            else:
                params['cabin_class_code'] = self.cabin_class_code
        if self.depart_airport_code:
            if hasattr(self.depart_airport_code, 'to_alipay_dict'):
                params['depart_airport_code'] = self.depart_airport_code.to_alipay_dict()
            else:
                params['depart_airport_code'] = self.depart_airport_code
        if self.depart_city_code:
            if hasattr(self.depart_city_code, 'to_alipay_dict'):
                params['depart_city_code'] = self.depart_city_code.to_alipay_dict()
            else:
                params['depart_city_code'] = self.depart_city_code
        if self.depart_date:
            if hasattr(self.depart_date, 'to_alipay_dict'):
                params['depart_date'] = self.depart_date.to_alipay_dict()
            else:
                params['depart_date'] = self.depart_date
        if self.depart_terminal:
            if hasattr(self.depart_terminal, 'to_alipay_dict'):
                params['depart_terminal'] = self.depart_terminal.to_alipay_dict()
            else:
                params['depart_terminal'] = self.depart_terminal
        if self.depart_time:
            if hasattr(self.depart_time, 'to_alipay_dict'):
                params['depart_time'] = self.depart_time.to_alipay_dict()
            else:
                params['depart_time'] = self.depart_time
        if self.expire_reason:
            if hasattr(self.expire_reason, 'to_alipay_dict'):
                params['expire_reason'] = self.expire_reason.to_alipay_dict()
            else:
                params['expire_reason'] = self.expire_reason
        if self.flight_duration:
            if hasattr(self.flight_duration, 'to_alipay_dict'):
                params['flight_duration'] = self.flight_duration.to_alipay_dict()
            else:
                params['flight_duration'] = self.flight_duration
        if self.flight_no:
            if hasattr(self.flight_no, 'to_alipay_dict'):
                params['flight_no'] = self.flight_no.to_alipay_dict()
            else:
                params['flight_no'] = self.flight_no
        if self.journey_index:
            if hasattr(self.journey_index, 'to_alipay_dict'):
                params['journey_index'] = self.journey_index.to_alipay_dict()
            else:
                params['journey_index'] = self.journey_index
        if self.passenger_name:
            if hasattr(self.passenger_name, 'to_alipay_dict'):
                params['passenger_name'] = self.passenger_name.to_alipay_dict()
            else:
                params['passenger_name'] = self.passenger_name
        if self.passenger_type:
            if hasattr(self.passenger_type, 'to_alipay_dict'):
                params['passenger_type'] = self.passenger_type.to_alipay_dict()
            else:
                params['passenger_type'] = self.passenger_type
        if self.pnr:
            if hasattr(self.pnr, 'to_alipay_dict'):
                params['pnr'] = self.pnr.to_alipay_dict()
            else:
                params['pnr'] = self.pnr
        if self.segment_index:
            if hasattr(self.segment_index, 'to_alipay_dict'):
                params['segment_index'] = self.segment_index.to_alipay_dict()
            else:
                params['segment_index'] = self.segment_index
        if self.segment_type:
            if hasattr(self.segment_type, 'to_alipay_dict'):
                params['segment_type'] = self.segment_type.to_alipay_dict()
            else:
                params['segment_type'] = self.segment_type
        if self.ticket_no:
            if hasattr(self.ticket_no, 'to_alipay_dict'):
                params['ticket_no'] = self.ticket_no.to_alipay_dict()
            else:
                params['ticket_no'] = self.ticket_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoyagerSegmentOfPassengersInfo()
        if 'arrive_airport_code' in d:
            o.arrive_airport_code = d['arrive_airport_code']
        if 'arrive_city_code' in d:
            o.arrive_city_code = d['arrive_city_code']
        if 'arrive_terminal' in d:
            o.arrive_terminal = d['arrive_terminal']
        if 'arrive_time' in d:
            o.arrive_time = d['arrive_time']
        if 'cabin_class_code' in d:
            o.cabin_class_code = d['cabin_class_code']
        if 'depart_airport_code' in d:
            o.depart_airport_code = d['depart_airport_code']
        if 'depart_city_code' in d:
            o.depart_city_code = d['depart_city_code']
        if 'depart_date' in d:
            o.depart_date = d['depart_date']
        if 'depart_terminal' in d:
            o.depart_terminal = d['depart_terminal']
        if 'depart_time' in d:
            o.depart_time = d['depart_time']
        if 'expire_reason' in d:
            o.expire_reason = d['expire_reason']
        if 'flight_duration' in d:
            o.flight_duration = d['flight_duration']
        if 'flight_no' in d:
            o.flight_no = d['flight_no']
        if 'journey_index' in d:
            o.journey_index = d['journey_index']
        if 'passenger_name' in d:
            o.passenger_name = d['passenger_name']
        if 'passenger_type' in d:
            o.passenger_type = d['passenger_type']
        if 'pnr' in d:
            o.pnr = d['pnr']
        if 'segment_index' in d:
            o.segment_index = d['segment_index']
        if 'segment_type' in d:
            o.segment_type = d['segment_type']
        if 'ticket_no' in d:
            o.ticket_no = d['ticket_no']
        return o


