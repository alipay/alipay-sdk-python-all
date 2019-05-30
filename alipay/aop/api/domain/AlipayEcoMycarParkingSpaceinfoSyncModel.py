#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarParkingSpaceinfoSyncModel(object):

    def __init__(self):
        self._free_charging_pile = None
        self._free_parking_space = None
        self._parking_id = None
        self._parking_space_status = None

    @property
    def free_charging_pile(self):
        return self._free_charging_pile

    @free_charging_pile.setter
    def free_charging_pile(self, value):
        self._free_charging_pile = value
    @property
    def free_parking_space(self):
        return self._free_parking_space

    @free_parking_space.setter
    def free_parking_space(self, value):
        self._free_parking_space = value
    @property
    def parking_id(self):
        return self._parking_id

    @parking_id.setter
    def parking_id(self, value):
        self._parking_id = value
    @property
    def parking_space_status(self):
        return self._parking_space_status

    @parking_space_status.setter
    def parking_space_status(self, value):
        self._parking_space_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.free_charging_pile:
            if hasattr(self.free_charging_pile, 'to_alipay_dict'):
                params['free_charging_pile'] = self.free_charging_pile.to_alipay_dict()
            else:
                params['free_charging_pile'] = self.free_charging_pile
        if self.free_parking_space:
            if hasattr(self.free_parking_space, 'to_alipay_dict'):
                params['free_parking_space'] = self.free_parking_space.to_alipay_dict()
            else:
                params['free_parking_space'] = self.free_parking_space
        if self.parking_id:
            if hasattr(self.parking_id, 'to_alipay_dict'):
                params['parking_id'] = self.parking_id.to_alipay_dict()
            else:
                params['parking_id'] = self.parking_id
        if self.parking_space_status:
            if hasattr(self.parking_space_status, 'to_alipay_dict'):
                params['parking_space_status'] = self.parking_space_status.to_alipay_dict()
            else:
                params['parking_space_status'] = self.parking_space_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarParkingSpaceinfoSyncModel()
        if 'free_charging_pile' in d:
            o.free_charging_pile = d['free_charging_pile']
        if 'free_parking_space' in d:
            o.free_parking_space = d['free_parking_space']
        if 'parking_id' in d:
            o.parking_id = d['parking_id']
        if 'parking_space_status' in d:
            o.parking_space_status = d['parking_space_status']
        return o


