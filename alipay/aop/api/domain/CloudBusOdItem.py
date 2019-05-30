#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CloudBusOdItem(object):

    def __init__(self):
        self._bus_od = None
        self._dest_geohash = None
        self._od = None

    @property
    def bus_od(self):
        return self._bus_od

    @bus_od.setter
    def bus_od(self, value):
        self._bus_od = value
    @property
    def dest_geohash(self):
        return self._dest_geohash

    @dest_geohash.setter
    def dest_geohash(self, value):
        self._dest_geohash = value
    @property
    def od(self):
        return self._od

    @od.setter
    def od(self, value):
        self._od = value


    def to_alipay_dict(self):
        params = dict()
        if self.bus_od:
            if hasattr(self.bus_od, 'to_alipay_dict'):
                params['bus_od'] = self.bus_od.to_alipay_dict()
            else:
                params['bus_od'] = self.bus_od
        if self.dest_geohash:
            if hasattr(self.dest_geohash, 'to_alipay_dict'):
                params['dest_geohash'] = self.dest_geohash.to_alipay_dict()
            else:
                params['dest_geohash'] = self.dest_geohash
        if self.od:
            if hasattr(self.od, 'to_alipay_dict'):
                params['od'] = self.od.to_alipay_dict()
            else:
                params['od'] = self.od
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CloudBusOdItem()
        if 'bus_od' in d:
            o.bus_od = d['bus_od']
        if 'dest_geohash' in d:
            o.dest_geohash = d['dest_geohash']
        if 'od' in d:
            o.od = d['od']
        return o


