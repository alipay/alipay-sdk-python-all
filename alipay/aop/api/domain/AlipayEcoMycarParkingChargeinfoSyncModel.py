#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarParkingChargeinfoSyncModel(object):

    def __init__(self):
        self._business_hours = None
        self._car_daylight_advanced_price = None
        self._car_daylight_base_price = None
        self._car_night_advanced_price = None
        self._car_night_base_price = None
        self._car_onetime_price = None
        self._daily_price_upperbound = None
        self._daylight_business_hours = None
        self._free_period = None
        self._has_charging_pile = None
        self._is_charge = None
        self._night_business_hours = None
        self._parking_id = None
        self._parking_space_count = None
        self._remark = None
        self._truck_daylight_advanced_price = None
        self._truck_daylight_base_price = None
        self._truck_night_advanced_price = None
        self._truck_night_base_price = None
        self._truck_onetime_price = None

    @property
    def business_hours(self):
        return self._business_hours

    @business_hours.setter
    def business_hours(self, value):
        self._business_hours = value
    @property
    def car_daylight_advanced_price(self):
        return self._car_daylight_advanced_price

    @car_daylight_advanced_price.setter
    def car_daylight_advanced_price(self, value):
        self._car_daylight_advanced_price = value
    @property
    def car_daylight_base_price(self):
        return self._car_daylight_base_price

    @car_daylight_base_price.setter
    def car_daylight_base_price(self, value):
        self._car_daylight_base_price = value
    @property
    def car_night_advanced_price(self):
        return self._car_night_advanced_price

    @car_night_advanced_price.setter
    def car_night_advanced_price(self, value):
        self._car_night_advanced_price = value
    @property
    def car_night_base_price(self):
        return self._car_night_base_price

    @car_night_base_price.setter
    def car_night_base_price(self, value):
        self._car_night_base_price = value
    @property
    def car_onetime_price(self):
        return self._car_onetime_price

    @car_onetime_price.setter
    def car_onetime_price(self, value):
        self._car_onetime_price = value
    @property
    def daily_price_upperbound(self):
        return self._daily_price_upperbound

    @daily_price_upperbound.setter
    def daily_price_upperbound(self, value):
        self._daily_price_upperbound = value
    @property
    def daylight_business_hours(self):
        return self._daylight_business_hours

    @daylight_business_hours.setter
    def daylight_business_hours(self, value):
        self._daylight_business_hours = value
    @property
    def free_period(self):
        return self._free_period

    @free_period.setter
    def free_period(self, value):
        self._free_period = value
    @property
    def has_charging_pile(self):
        return self._has_charging_pile

    @has_charging_pile.setter
    def has_charging_pile(self, value):
        self._has_charging_pile = value
    @property
    def is_charge(self):
        return self._is_charge

    @is_charge.setter
    def is_charge(self, value):
        self._is_charge = value
    @property
    def night_business_hours(self):
        return self._night_business_hours

    @night_business_hours.setter
    def night_business_hours(self, value):
        self._night_business_hours = value
    @property
    def parking_id(self):
        return self._parking_id

    @parking_id.setter
    def parking_id(self, value):
        self._parking_id = value
    @property
    def parking_space_count(self):
        return self._parking_space_count

    @parking_space_count.setter
    def parking_space_count(self, value):
        self._parking_space_count = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def truck_daylight_advanced_price(self):
        return self._truck_daylight_advanced_price

    @truck_daylight_advanced_price.setter
    def truck_daylight_advanced_price(self, value):
        self._truck_daylight_advanced_price = value
    @property
    def truck_daylight_base_price(self):
        return self._truck_daylight_base_price

    @truck_daylight_base_price.setter
    def truck_daylight_base_price(self, value):
        self._truck_daylight_base_price = value
    @property
    def truck_night_advanced_price(self):
        return self._truck_night_advanced_price

    @truck_night_advanced_price.setter
    def truck_night_advanced_price(self, value):
        self._truck_night_advanced_price = value
    @property
    def truck_night_base_price(self):
        return self._truck_night_base_price

    @truck_night_base_price.setter
    def truck_night_base_price(self, value):
        self._truck_night_base_price = value
    @property
    def truck_onetime_price(self):
        return self._truck_onetime_price

    @truck_onetime_price.setter
    def truck_onetime_price(self, value):
        self._truck_onetime_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_hours:
            if hasattr(self.business_hours, 'to_alipay_dict'):
                params['business_hours'] = self.business_hours.to_alipay_dict()
            else:
                params['business_hours'] = self.business_hours
        if self.car_daylight_advanced_price:
            if hasattr(self.car_daylight_advanced_price, 'to_alipay_dict'):
                params['car_daylight_advanced_price'] = self.car_daylight_advanced_price.to_alipay_dict()
            else:
                params['car_daylight_advanced_price'] = self.car_daylight_advanced_price
        if self.car_daylight_base_price:
            if hasattr(self.car_daylight_base_price, 'to_alipay_dict'):
                params['car_daylight_base_price'] = self.car_daylight_base_price.to_alipay_dict()
            else:
                params['car_daylight_base_price'] = self.car_daylight_base_price
        if self.car_night_advanced_price:
            if hasattr(self.car_night_advanced_price, 'to_alipay_dict'):
                params['car_night_advanced_price'] = self.car_night_advanced_price.to_alipay_dict()
            else:
                params['car_night_advanced_price'] = self.car_night_advanced_price
        if self.car_night_base_price:
            if hasattr(self.car_night_base_price, 'to_alipay_dict'):
                params['car_night_base_price'] = self.car_night_base_price.to_alipay_dict()
            else:
                params['car_night_base_price'] = self.car_night_base_price
        if self.car_onetime_price:
            if hasattr(self.car_onetime_price, 'to_alipay_dict'):
                params['car_onetime_price'] = self.car_onetime_price.to_alipay_dict()
            else:
                params['car_onetime_price'] = self.car_onetime_price
        if self.daily_price_upperbound:
            if hasattr(self.daily_price_upperbound, 'to_alipay_dict'):
                params['daily_price_upperbound'] = self.daily_price_upperbound.to_alipay_dict()
            else:
                params['daily_price_upperbound'] = self.daily_price_upperbound
        if self.daylight_business_hours:
            if hasattr(self.daylight_business_hours, 'to_alipay_dict'):
                params['daylight_business_hours'] = self.daylight_business_hours.to_alipay_dict()
            else:
                params['daylight_business_hours'] = self.daylight_business_hours
        if self.free_period:
            if hasattr(self.free_period, 'to_alipay_dict'):
                params['free_period'] = self.free_period.to_alipay_dict()
            else:
                params['free_period'] = self.free_period
        if self.has_charging_pile:
            if hasattr(self.has_charging_pile, 'to_alipay_dict'):
                params['has_charging_pile'] = self.has_charging_pile.to_alipay_dict()
            else:
                params['has_charging_pile'] = self.has_charging_pile
        if self.is_charge:
            if hasattr(self.is_charge, 'to_alipay_dict'):
                params['is_charge'] = self.is_charge.to_alipay_dict()
            else:
                params['is_charge'] = self.is_charge
        if self.night_business_hours:
            if hasattr(self.night_business_hours, 'to_alipay_dict'):
                params['night_business_hours'] = self.night_business_hours.to_alipay_dict()
            else:
                params['night_business_hours'] = self.night_business_hours
        if self.parking_id:
            if hasattr(self.parking_id, 'to_alipay_dict'):
                params['parking_id'] = self.parking_id.to_alipay_dict()
            else:
                params['parking_id'] = self.parking_id
        if self.parking_space_count:
            if hasattr(self.parking_space_count, 'to_alipay_dict'):
                params['parking_space_count'] = self.parking_space_count.to_alipay_dict()
            else:
                params['parking_space_count'] = self.parking_space_count
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.truck_daylight_advanced_price:
            if hasattr(self.truck_daylight_advanced_price, 'to_alipay_dict'):
                params['truck_daylight_advanced_price'] = self.truck_daylight_advanced_price.to_alipay_dict()
            else:
                params['truck_daylight_advanced_price'] = self.truck_daylight_advanced_price
        if self.truck_daylight_base_price:
            if hasattr(self.truck_daylight_base_price, 'to_alipay_dict'):
                params['truck_daylight_base_price'] = self.truck_daylight_base_price.to_alipay_dict()
            else:
                params['truck_daylight_base_price'] = self.truck_daylight_base_price
        if self.truck_night_advanced_price:
            if hasattr(self.truck_night_advanced_price, 'to_alipay_dict'):
                params['truck_night_advanced_price'] = self.truck_night_advanced_price.to_alipay_dict()
            else:
                params['truck_night_advanced_price'] = self.truck_night_advanced_price
        if self.truck_night_base_price:
            if hasattr(self.truck_night_base_price, 'to_alipay_dict'):
                params['truck_night_base_price'] = self.truck_night_base_price.to_alipay_dict()
            else:
                params['truck_night_base_price'] = self.truck_night_base_price
        if self.truck_onetime_price:
            if hasattr(self.truck_onetime_price, 'to_alipay_dict'):
                params['truck_onetime_price'] = self.truck_onetime_price.to_alipay_dict()
            else:
                params['truck_onetime_price'] = self.truck_onetime_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarParkingChargeinfoSyncModel()
        if 'business_hours' in d:
            o.business_hours = d['business_hours']
        if 'car_daylight_advanced_price' in d:
            o.car_daylight_advanced_price = d['car_daylight_advanced_price']
        if 'car_daylight_base_price' in d:
            o.car_daylight_base_price = d['car_daylight_base_price']
        if 'car_night_advanced_price' in d:
            o.car_night_advanced_price = d['car_night_advanced_price']
        if 'car_night_base_price' in d:
            o.car_night_base_price = d['car_night_base_price']
        if 'car_onetime_price' in d:
            o.car_onetime_price = d['car_onetime_price']
        if 'daily_price_upperbound' in d:
            o.daily_price_upperbound = d['daily_price_upperbound']
        if 'daylight_business_hours' in d:
            o.daylight_business_hours = d['daylight_business_hours']
        if 'free_period' in d:
            o.free_period = d['free_period']
        if 'has_charging_pile' in d:
            o.has_charging_pile = d['has_charging_pile']
        if 'is_charge' in d:
            o.is_charge = d['is_charge']
        if 'night_business_hours' in d:
            o.night_business_hours = d['night_business_hours']
        if 'parking_id' in d:
            o.parking_id = d['parking_id']
        if 'parking_space_count' in d:
            o.parking_space_count = d['parking_space_count']
        if 'remark' in d:
            o.remark = d['remark']
        if 'truck_daylight_advanced_price' in d:
            o.truck_daylight_advanced_price = d['truck_daylight_advanced_price']
        if 'truck_daylight_base_price' in d:
            o.truck_daylight_base_price = d['truck_daylight_base_price']
        if 'truck_night_advanced_price' in d:
            o.truck_night_advanced_price = d['truck_night_advanced_price']
        if 'truck_night_base_price' in d:
            o.truck_night_base_price = d['truck_night_base_price']
        if 'truck_onetime_price' in d:
            o.truck_onetime_price = d['truck_onetime_price']
        return o


