#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsOpenUserDTO import InsOpenUserDTO


class InsTransportItineraryDTO(object):

    def __init__(self):
        self._end_address = None
        self._end_city = None
        self._end_station = None
        self._end_time = None
        self._itinerary_order_no = None
        self._passenger = None
        self._seq = None
        self._start_address = None
        self._start_city = None
        self._start_station = None
        self._start_time = None
        self._transport_mode = None
        self._transport_no = None

    @property
    def end_address(self):
        return self._end_address

    @end_address.setter
    def end_address(self, value):
        self._end_address = value
    @property
    def end_city(self):
        return self._end_city

    @end_city.setter
    def end_city(self, value):
        self._end_city = value
    @property
    def end_station(self):
        return self._end_station

    @end_station.setter
    def end_station(self, value):
        self._end_station = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def itinerary_order_no(self):
        return self._itinerary_order_no

    @itinerary_order_no.setter
    def itinerary_order_no(self, value):
        self._itinerary_order_no = value
    @property
    def passenger(self):
        return self._passenger

    @passenger.setter
    def passenger(self, value):
        if isinstance(value, InsOpenUserDTO):
            self._passenger = value
        else:
            self._passenger = InsOpenUserDTO.from_alipay_dict(value)
    @property
    def seq(self):
        return self._seq

    @seq.setter
    def seq(self, value):
        self._seq = value
    @property
    def start_address(self):
        return self._start_address

    @start_address.setter
    def start_address(self, value):
        self._start_address = value
    @property
    def start_city(self):
        return self._start_city

    @start_city.setter
    def start_city(self, value):
        self._start_city = value
    @property
    def start_station(self):
        return self._start_station

    @start_station.setter
    def start_station(self, value):
        self._start_station = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def transport_mode(self):
        return self._transport_mode

    @transport_mode.setter
    def transport_mode(self, value):
        self._transport_mode = value
    @property
    def transport_no(self):
        return self._transport_no

    @transport_no.setter
    def transport_no(self, value):
        self._transport_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_address:
            if hasattr(self.end_address, 'to_alipay_dict'):
                params['end_address'] = self.end_address.to_alipay_dict()
            else:
                params['end_address'] = self.end_address
        if self.end_city:
            if hasattr(self.end_city, 'to_alipay_dict'):
                params['end_city'] = self.end_city.to_alipay_dict()
            else:
                params['end_city'] = self.end_city
        if self.end_station:
            if hasattr(self.end_station, 'to_alipay_dict'):
                params['end_station'] = self.end_station.to_alipay_dict()
            else:
                params['end_station'] = self.end_station
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.itinerary_order_no:
            if hasattr(self.itinerary_order_no, 'to_alipay_dict'):
                params['itinerary_order_no'] = self.itinerary_order_no.to_alipay_dict()
            else:
                params['itinerary_order_no'] = self.itinerary_order_no
        if self.passenger:
            if hasattr(self.passenger, 'to_alipay_dict'):
                params['passenger'] = self.passenger.to_alipay_dict()
            else:
                params['passenger'] = self.passenger
        if self.seq:
            if hasattr(self.seq, 'to_alipay_dict'):
                params['seq'] = self.seq.to_alipay_dict()
            else:
                params['seq'] = self.seq
        if self.start_address:
            if hasattr(self.start_address, 'to_alipay_dict'):
                params['start_address'] = self.start_address.to_alipay_dict()
            else:
                params['start_address'] = self.start_address
        if self.start_city:
            if hasattr(self.start_city, 'to_alipay_dict'):
                params['start_city'] = self.start_city.to_alipay_dict()
            else:
                params['start_city'] = self.start_city
        if self.start_station:
            if hasattr(self.start_station, 'to_alipay_dict'):
                params['start_station'] = self.start_station.to_alipay_dict()
            else:
                params['start_station'] = self.start_station
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.transport_mode:
            if hasattr(self.transport_mode, 'to_alipay_dict'):
                params['transport_mode'] = self.transport_mode.to_alipay_dict()
            else:
                params['transport_mode'] = self.transport_mode
        if self.transport_no:
            if hasattr(self.transport_no, 'to_alipay_dict'):
                params['transport_no'] = self.transport_no.to_alipay_dict()
            else:
                params['transport_no'] = self.transport_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsTransportItineraryDTO()
        if 'end_address' in d:
            o.end_address = d['end_address']
        if 'end_city' in d:
            o.end_city = d['end_city']
        if 'end_station' in d:
            o.end_station = d['end_station']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'itinerary_order_no' in d:
            o.itinerary_order_no = d['itinerary_order_no']
        if 'passenger' in d:
            o.passenger = d['passenger']
        if 'seq' in d:
            o.seq = d['seq']
        if 'start_address' in d:
            o.start_address = d['start_address']
        if 'start_city' in d:
            o.start_city = d['start_city']
        if 'start_station' in d:
            o.start_station = d['start_station']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'transport_mode' in d:
            o.transport_mode = d['transport_mode']
        if 'transport_no' in d:
            o.transport_no = d['transport_no']
        return o


