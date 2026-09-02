#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LocationParam import LocationParam


class EbikeChargeStation(object):

    def __init__(self):
        self._address = None
        self._available_plug_count = None
        self._brand_code = None
        self._brand_name = None
        self._city_code = None
        self._city_name = None
        self._device_lbs = None
        self._device_name = None
        self._device_no = None
        self._device_status = None
        self._device_type = None
        self._fee_desc = None
        self._maximum_power = None
        self._station_name = None
        self._station_no = None
        self._total_plug_count = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def available_plug_count(self):
        return self._available_plug_count

    @available_plug_count.setter
    def available_plug_count(self, value):
        self._available_plug_count = value
    @property
    def brand_code(self):
        return self._brand_code

    @brand_code.setter
    def brand_code(self, value):
        self._brand_code = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def device_lbs(self):
        return self._device_lbs

    @device_lbs.setter
    def device_lbs(self, value):
        if isinstance(value, LocationParam):
            self._device_lbs = value
        else:
            self._device_lbs = LocationParam.from_alipay_dict(value)
    @property
    def device_name(self):
        return self._device_name

    @device_name.setter
    def device_name(self, value):
        self._device_name = value
    @property
    def device_no(self):
        return self._device_no

    @device_no.setter
    def device_no(self, value):
        self._device_no = value
    @property
    def device_status(self):
        return self._device_status

    @device_status.setter
    def device_status(self, value):
        self._device_status = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def fee_desc(self):
        return self._fee_desc

    @fee_desc.setter
    def fee_desc(self, value):
        self._fee_desc = value
    @property
    def maximum_power(self):
        return self._maximum_power

    @maximum_power.setter
    def maximum_power(self, value):
        self._maximum_power = value
    @property
    def station_name(self):
        return self._station_name

    @station_name.setter
    def station_name(self, value):
        self._station_name = value
    @property
    def station_no(self):
        return self._station_no

    @station_no.setter
    def station_no(self, value):
        self._station_no = value
    @property
    def total_plug_count(self):
        return self._total_plug_count

    @total_plug_count.setter
    def total_plug_count(self, value):
        self._total_plug_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.available_plug_count:
            if hasattr(self.available_plug_count, 'to_alipay_dict'):
                params['available_plug_count'] = self.available_plug_count.to_alipay_dict()
            else:
                params['available_plug_count'] = self.available_plug_count
        if self.brand_code:
            if hasattr(self.brand_code, 'to_alipay_dict'):
                params['brand_code'] = self.brand_code.to_alipay_dict()
            else:
                params['brand_code'] = self.brand_code
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.device_lbs:
            if hasattr(self.device_lbs, 'to_alipay_dict'):
                params['device_lbs'] = self.device_lbs.to_alipay_dict()
            else:
                params['device_lbs'] = self.device_lbs
        if self.device_name:
            if hasattr(self.device_name, 'to_alipay_dict'):
                params['device_name'] = self.device_name.to_alipay_dict()
            else:
                params['device_name'] = self.device_name
        if self.device_no:
            if hasattr(self.device_no, 'to_alipay_dict'):
                params['device_no'] = self.device_no.to_alipay_dict()
            else:
                params['device_no'] = self.device_no
        if self.device_status:
            if hasattr(self.device_status, 'to_alipay_dict'):
                params['device_status'] = self.device_status.to_alipay_dict()
            else:
                params['device_status'] = self.device_status
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.fee_desc:
            if hasattr(self.fee_desc, 'to_alipay_dict'):
                params['fee_desc'] = self.fee_desc.to_alipay_dict()
            else:
                params['fee_desc'] = self.fee_desc
        if self.maximum_power:
            if hasattr(self.maximum_power, 'to_alipay_dict'):
                params['maximum_power'] = self.maximum_power.to_alipay_dict()
            else:
                params['maximum_power'] = self.maximum_power
        if self.station_name:
            if hasattr(self.station_name, 'to_alipay_dict'):
                params['station_name'] = self.station_name.to_alipay_dict()
            else:
                params['station_name'] = self.station_name
        if self.station_no:
            if hasattr(self.station_no, 'to_alipay_dict'):
                params['station_no'] = self.station_no.to_alipay_dict()
            else:
                params['station_no'] = self.station_no
        if self.total_plug_count:
            if hasattr(self.total_plug_count, 'to_alipay_dict'):
                params['total_plug_count'] = self.total_plug_count.to_alipay_dict()
            else:
                params['total_plug_count'] = self.total_plug_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EbikeChargeStation()
        if 'address' in d:
            o.address = d['address']
        if 'available_plug_count' in d:
            o.available_plug_count = d['available_plug_count']
        if 'brand_code' in d:
            o.brand_code = d['brand_code']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'device_lbs' in d:
            o.device_lbs = d['device_lbs']
        if 'device_name' in d:
            o.device_name = d['device_name']
        if 'device_no' in d:
            o.device_no = d['device_no']
        if 'device_status' in d:
            o.device_status = d['device_status']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'fee_desc' in d:
            o.fee_desc = d['fee_desc']
        if 'maximum_power' in d:
            o.maximum_power = d['maximum_power']
        if 'station_name' in d:
            o.station_name = d['station_name']
        if 'station_no' in d:
            o.station_no = d['station_no']
        if 'total_plug_count' in d:
            o.total_plug_count = d['total_plug_count']
        return o


