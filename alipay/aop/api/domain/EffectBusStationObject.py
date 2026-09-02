#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EffectBusStationObject(object):

    def __init__(self):
        self._impact_type = None
        self._passenger_volume = None
        self._rank = None
        self._station_name = None

    @property
    def impact_type(self):
        return self._impact_type

    @impact_type.setter
    def impact_type(self, value):
        self._impact_type = value
    @property
    def passenger_volume(self):
        return self._passenger_volume

    @passenger_volume.setter
    def passenger_volume(self, value):
        self._passenger_volume = value
    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value
    @property
    def station_name(self):
        return self._station_name

    @station_name.setter
    def station_name(self, value):
        self._station_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.impact_type:
            if hasattr(self.impact_type, 'to_alipay_dict'):
                params['impact_type'] = self.impact_type.to_alipay_dict()
            else:
                params['impact_type'] = self.impact_type
        if self.passenger_volume:
            if hasattr(self.passenger_volume, 'to_alipay_dict'):
                params['passenger_volume'] = self.passenger_volume.to_alipay_dict()
            else:
                params['passenger_volume'] = self.passenger_volume
        if self.rank:
            if hasattr(self.rank, 'to_alipay_dict'):
                params['rank'] = self.rank.to_alipay_dict()
            else:
                params['rank'] = self.rank
        if self.station_name:
            if hasattr(self.station_name, 'to_alipay_dict'):
                params['station_name'] = self.station_name.to_alipay_dict()
            else:
                params['station_name'] = self.station_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EffectBusStationObject()
        if 'impact_type' in d:
            o.impact_type = d['impact_type']
        if 'passenger_volume' in d:
            o.passenger_volume = d['passenger_volume']
        if 'rank' in d:
            o.rank = d['rank']
        if 'station_name' in d:
            o.station_name = d['station_name']
        return o


