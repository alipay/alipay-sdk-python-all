#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LocationDTO(object):

    def __init__(self):
        self._city = None
        self._imei = None
        self._imsi = None
        self._ip = None
        self._latitude = None
        self._longitude = None
        self._mac_addr = None

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def imei(self):
        return self._imei

    @imei.setter
    def imei(self, value):
        self._imei = value
    @property
    def imsi(self):
        return self._imsi

    @imsi.setter
    def imsi(self, value):
        self._imsi = value
    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value):
        self._ip = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def mac_addr(self):
        return self._mac_addr

    @mac_addr.setter
    def mac_addr(self, value):
        self._mac_addr = value


    def to_alipay_dict(self):
        params = dict()
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.imei:
            if hasattr(self.imei, 'to_alipay_dict'):
                params['imei'] = self.imei.to_alipay_dict()
            else:
                params['imei'] = self.imei
        if self.imsi:
            if hasattr(self.imsi, 'to_alipay_dict'):
                params['imsi'] = self.imsi.to_alipay_dict()
            else:
                params['imsi'] = self.imsi
        if self.ip:
            if hasattr(self.ip, 'to_alipay_dict'):
                params['ip'] = self.ip.to_alipay_dict()
            else:
                params['ip'] = self.ip
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.mac_addr:
            if hasattr(self.mac_addr, 'to_alipay_dict'):
                params['mac_addr'] = self.mac_addr.to_alipay_dict()
            else:
                params['mac_addr'] = self.mac_addr
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LocationDTO()
        if 'city' in d:
            o.city = d['city']
        if 'imei' in d:
            o.imei = d['imei']
        if 'imsi' in d:
            o.imsi = d['imsi']
        if 'ip' in d:
            o.ip = d['ip']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'mac_addr' in d:
            o.mac_addr = d['mac_addr']
        return o


