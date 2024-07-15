#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MedicalShopDeliveryPoint import MedicalShopDeliveryPoint
from alipay.aop.api.domain.MedicalShopTimePeriod import MedicalShopTimePeriod
from alipay.aop.api.domain.MedicalShopDeliverySpecialTimePrice import MedicalShopDeliverySpecialTimePrice
from alipay.aop.api.domain.MedicalShopDeliverySpecialTimePrice import MedicalShopDeliverySpecialTimePrice


class MedicalShopDeliveryInfo(object):

    def __init__(self):
        self._delivery_area = None
        self._delivery_area_type = None
        self._delivery_fee = None
        self._delivery_radius = None
        self._effective_period = None
        self._start_price = None
        self._time_ext_fee = None
        self._time_ext_price = None

    @property
    def delivery_area(self):
        return self._delivery_area

    @delivery_area.setter
    def delivery_area(self, value):
        if isinstance(value, list):
            self._delivery_area = list()
            for i in value:
                if isinstance(i, MedicalShopDeliveryPoint):
                    self._delivery_area.append(i)
                else:
                    self._delivery_area.append(MedicalShopDeliveryPoint.from_alipay_dict(i))
    @property
    def delivery_area_type(self):
        return self._delivery_area_type

    @delivery_area_type.setter
    def delivery_area_type(self, value):
        self._delivery_area_type = value
    @property
    def delivery_fee(self):
        return self._delivery_fee

    @delivery_fee.setter
    def delivery_fee(self, value):
        self._delivery_fee = value
    @property
    def delivery_radius(self):
        return self._delivery_radius

    @delivery_radius.setter
    def delivery_radius(self, value):
        self._delivery_radius = value
    @property
    def effective_period(self):
        return self._effective_period

    @effective_period.setter
    def effective_period(self, value):
        if isinstance(value, list):
            self._effective_period = list()
            for i in value:
                if isinstance(i, MedicalShopTimePeriod):
                    self._effective_period.append(i)
                else:
                    self._effective_period.append(MedicalShopTimePeriod.from_alipay_dict(i))
    @property
    def start_price(self):
        return self._start_price

    @start_price.setter
    def start_price(self, value):
        self._start_price = value
    @property
    def time_ext_fee(self):
        return self._time_ext_fee

    @time_ext_fee.setter
    def time_ext_fee(self, value):
        if isinstance(value, list):
            self._time_ext_fee = list()
            for i in value:
                if isinstance(i, MedicalShopDeliverySpecialTimePrice):
                    self._time_ext_fee.append(i)
                else:
                    self._time_ext_fee.append(MedicalShopDeliverySpecialTimePrice.from_alipay_dict(i))
    @property
    def time_ext_price(self):
        return self._time_ext_price

    @time_ext_price.setter
    def time_ext_price(self, value):
        if isinstance(value, list):
            self._time_ext_price = list()
            for i in value:
                if isinstance(i, MedicalShopDeliverySpecialTimePrice):
                    self._time_ext_price.append(i)
                else:
                    self._time_ext_price.append(MedicalShopDeliverySpecialTimePrice.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_area:
            if isinstance(self.delivery_area, list):
                for i in range(0, len(self.delivery_area)):
                    element = self.delivery_area[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.delivery_area[i] = element.to_alipay_dict()
            if hasattr(self.delivery_area, 'to_alipay_dict'):
                params['delivery_area'] = self.delivery_area.to_alipay_dict()
            else:
                params['delivery_area'] = self.delivery_area
        if self.delivery_area_type:
            if hasattr(self.delivery_area_type, 'to_alipay_dict'):
                params['delivery_area_type'] = self.delivery_area_type.to_alipay_dict()
            else:
                params['delivery_area_type'] = self.delivery_area_type
        if self.delivery_fee:
            if hasattr(self.delivery_fee, 'to_alipay_dict'):
                params['delivery_fee'] = self.delivery_fee.to_alipay_dict()
            else:
                params['delivery_fee'] = self.delivery_fee
        if self.delivery_radius:
            if hasattr(self.delivery_radius, 'to_alipay_dict'):
                params['delivery_radius'] = self.delivery_radius.to_alipay_dict()
            else:
                params['delivery_radius'] = self.delivery_radius
        if self.effective_period:
            if isinstance(self.effective_period, list):
                for i in range(0, len(self.effective_period)):
                    element = self.effective_period[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.effective_period[i] = element.to_alipay_dict()
            if hasattr(self.effective_period, 'to_alipay_dict'):
                params['effective_period'] = self.effective_period.to_alipay_dict()
            else:
                params['effective_period'] = self.effective_period
        if self.start_price:
            if hasattr(self.start_price, 'to_alipay_dict'):
                params['start_price'] = self.start_price.to_alipay_dict()
            else:
                params['start_price'] = self.start_price
        if self.time_ext_fee:
            if isinstance(self.time_ext_fee, list):
                for i in range(0, len(self.time_ext_fee)):
                    element = self.time_ext_fee[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.time_ext_fee[i] = element.to_alipay_dict()
            if hasattr(self.time_ext_fee, 'to_alipay_dict'):
                params['time_ext_fee'] = self.time_ext_fee.to_alipay_dict()
            else:
                params['time_ext_fee'] = self.time_ext_fee
        if self.time_ext_price:
            if isinstance(self.time_ext_price, list):
                for i in range(0, len(self.time_ext_price)):
                    element = self.time_ext_price[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.time_ext_price[i] = element.to_alipay_dict()
            if hasattr(self.time_ext_price, 'to_alipay_dict'):
                params['time_ext_price'] = self.time_ext_price.to_alipay_dict()
            else:
                params['time_ext_price'] = self.time_ext_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalShopDeliveryInfo()
        if 'delivery_area' in d:
            o.delivery_area = d['delivery_area']
        if 'delivery_area_type' in d:
            o.delivery_area_type = d['delivery_area_type']
        if 'delivery_fee' in d:
            o.delivery_fee = d['delivery_fee']
        if 'delivery_radius' in d:
            o.delivery_radius = d['delivery_radius']
        if 'effective_period' in d:
            o.effective_period = d['effective_period']
        if 'start_price' in d:
            o.start_price = d['start_price']
        if 'time_ext_fee' in d:
            o.time_ext_fee = d['time_ext_fee']
        if 'time_ext_price' in d:
            o.time_ext_price = d['time_ext_price']
        return o


