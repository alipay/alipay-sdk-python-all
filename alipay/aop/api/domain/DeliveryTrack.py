#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HealthServiceTimeslot import HealthServiceTimeslot


class DeliveryTrack(object):

    def __init__(self):
        self._arrive_timeslot = None
        self._courier_latitude = None
        self._courier_longitude = None
        self._courier_name = None
        self._courier_phone = None
        self._receiver_latitude = None
        self._receiver_longitude = None
        self._remaining_delivery_minutes = None
        self._remaining_distance_km = None

    @property
    def arrive_timeslot(self):
        return self._arrive_timeslot

    @arrive_timeslot.setter
    def arrive_timeslot(self, value):
        if isinstance(value, HealthServiceTimeslot):
            self._arrive_timeslot = value
        else:
            self._arrive_timeslot = HealthServiceTimeslot.from_alipay_dict(value)
    @property
    def courier_latitude(self):
        return self._courier_latitude

    @courier_latitude.setter
    def courier_latitude(self, value):
        self._courier_latitude = value
    @property
    def courier_longitude(self):
        return self._courier_longitude

    @courier_longitude.setter
    def courier_longitude(self, value):
        self._courier_longitude = value
    @property
    def courier_name(self):
        return self._courier_name

    @courier_name.setter
    def courier_name(self, value):
        self._courier_name = value
    @property
    def courier_phone(self):
        return self._courier_phone

    @courier_phone.setter
    def courier_phone(self, value):
        self._courier_phone = value
    @property
    def receiver_latitude(self):
        return self._receiver_latitude

    @receiver_latitude.setter
    def receiver_latitude(self, value):
        self._receiver_latitude = value
    @property
    def receiver_longitude(self):
        return self._receiver_longitude

    @receiver_longitude.setter
    def receiver_longitude(self, value):
        self._receiver_longitude = value
    @property
    def remaining_delivery_minutes(self):
        return self._remaining_delivery_minutes

    @remaining_delivery_minutes.setter
    def remaining_delivery_minutes(self, value):
        self._remaining_delivery_minutes = value
    @property
    def remaining_distance_km(self):
        return self._remaining_distance_km

    @remaining_distance_km.setter
    def remaining_distance_km(self, value):
        self._remaining_distance_km = value


    def to_alipay_dict(self):
        params = dict()
        if self.arrive_timeslot:
            if hasattr(self.arrive_timeslot, 'to_alipay_dict'):
                params['arrive_timeslot'] = self.arrive_timeslot.to_alipay_dict()
            else:
                params['arrive_timeslot'] = self.arrive_timeslot
        if self.courier_latitude:
            if hasattr(self.courier_latitude, 'to_alipay_dict'):
                params['courier_latitude'] = self.courier_latitude.to_alipay_dict()
            else:
                params['courier_latitude'] = self.courier_latitude
        if self.courier_longitude:
            if hasattr(self.courier_longitude, 'to_alipay_dict'):
                params['courier_longitude'] = self.courier_longitude.to_alipay_dict()
            else:
                params['courier_longitude'] = self.courier_longitude
        if self.courier_name:
            if hasattr(self.courier_name, 'to_alipay_dict'):
                params['courier_name'] = self.courier_name.to_alipay_dict()
            else:
                params['courier_name'] = self.courier_name
        if self.courier_phone:
            if hasattr(self.courier_phone, 'to_alipay_dict'):
                params['courier_phone'] = self.courier_phone.to_alipay_dict()
            else:
                params['courier_phone'] = self.courier_phone
        if self.receiver_latitude:
            if hasattr(self.receiver_latitude, 'to_alipay_dict'):
                params['receiver_latitude'] = self.receiver_latitude.to_alipay_dict()
            else:
                params['receiver_latitude'] = self.receiver_latitude
        if self.receiver_longitude:
            if hasattr(self.receiver_longitude, 'to_alipay_dict'):
                params['receiver_longitude'] = self.receiver_longitude.to_alipay_dict()
            else:
                params['receiver_longitude'] = self.receiver_longitude
        if self.remaining_delivery_minutes:
            if hasattr(self.remaining_delivery_minutes, 'to_alipay_dict'):
                params['remaining_delivery_minutes'] = self.remaining_delivery_minutes.to_alipay_dict()
            else:
                params['remaining_delivery_minutes'] = self.remaining_delivery_minutes
        if self.remaining_distance_km:
            if hasattr(self.remaining_distance_km, 'to_alipay_dict'):
                params['remaining_distance_km'] = self.remaining_distance_km.to_alipay_dict()
            else:
                params['remaining_distance_km'] = self.remaining_distance_km
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryTrack()
        if 'arrive_timeslot' in d:
            o.arrive_timeslot = d['arrive_timeslot']
        if 'courier_latitude' in d:
            o.courier_latitude = d['courier_latitude']
        if 'courier_longitude' in d:
            o.courier_longitude = d['courier_longitude']
        if 'courier_name' in d:
            o.courier_name = d['courier_name']
        if 'courier_phone' in d:
            o.courier_phone = d['courier_phone']
        if 'receiver_latitude' in d:
            o.receiver_latitude = d['receiver_latitude']
        if 'receiver_longitude' in d:
            o.receiver_longitude = d['receiver_longitude']
        if 'remaining_delivery_minutes' in d:
            o.remaining_delivery_minutes = d['remaining_delivery_minutes']
        if 'remaining_distance_km' in d:
            o.remaining_distance_km = d['remaining_distance_km']
        return o


