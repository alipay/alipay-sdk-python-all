#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentCarSpuExpoInfo(object):

    def __init__(self):
        self._car_type = None
        self._city_name = None
        self._expo_rank = None
        self._order_rank = None
        self._spu_id = None
        self._spu_name = None
        self._veh_name = None

    @property
    def car_type(self):
        return self._car_type

    @car_type.setter
    def car_type(self, value):
        self._car_type = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def expo_rank(self):
        return self._expo_rank

    @expo_rank.setter
    def expo_rank(self, value):
        self._expo_rank = value
    @property
    def order_rank(self):
        return self._order_rank

    @order_rank.setter
    def order_rank(self, value):
        self._order_rank = value
    @property
    def spu_id(self):
        return self._spu_id

    @spu_id.setter
    def spu_id(self, value):
        self._spu_id = value
    @property
    def spu_name(self):
        return self._spu_name

    @spu_name.setter
    def spu_name(self, value):
        self._spu_name = value
    @property
    def veh_name(self):
        return self._veh_name

    @veh_name.setter
    def veh_name(self, value):
        self._veh_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.car_type:
            if hasattr(self.car_type, 'to_alipay_dict'):
                params['car_type'] = self.car_type.to_alipay_dict()
            else:
                params['car_type'] = self.car_type
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.expo_rank:
            if hasattr(self.expo_rank, 'to_alipay_dict'):
                params['expo_rank'] = self.expo_rank.to_alipay_dict()
            else:
                params['expo_rank'] = self.expo_rank
        if self.order_rank:
            if hasattr(self.order_rank, 'to_alipay_dict'):
                params['order_rank'] = self.order_rank.to_alipay_dict()
            else:
                params['order_rank'] = self.order_rank
        if self.spu_id:
            if hasattr(self.spu_id, 'to_alipay_dict'):
                params['spu_id'] = self.spu_id.to_alipay_dict()
            else:
                params['spu_id'] = self.spu_id
        if self.spu_name:
            if hasattr(self.spu_name, 'to_alipay_dict'):
                params['spu_name'] = self.spu_name.to_alipay_dict()
            else:
                params['spu_name'] = self.spu_name
        if self.veh_name:
            if hasattr(self.veh_name, 'to_alipay_dict'):
                params['veh_name'] = self.veh_name.to_alipay_dict()
            else:
                params['veh_name'] = self.veh_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentCarSpuExpoInfo()
        if 'car_type' in d:
            o.car_type = d['car_type']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'expo_rank' in d:
            o.expo_rank = d['expo_rank']
        if 'order_rank' in d:
            o.order_rank = d['order_rank']
        if 'spu_id' in d:
            o.spu_id = d['spu_id']
        if 'spu_name' in d:
            o.spu_name = d['spu_name']
        if 'veh_name' in d:
            o.veh_name = d['veh_name']
        return o


