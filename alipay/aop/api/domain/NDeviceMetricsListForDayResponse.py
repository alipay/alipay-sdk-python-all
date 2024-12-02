#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NDeviceMetricsListForDayResponse(object):

    def __init__(self):
        self._alipay_amount = None
        self._alipay_transaction_count = None
        self._be_lighted_up = None
        self._be_register = None
        self._be_turnon_device = None
        self._binding_location = None
        self._city_code = None
        self._city_name = None
        self._district_code = None
        self._district_name = None
        self._do_check_in = None
        self._has_nfc_trade = None
        self._leads_worker_id = None
        self._leads_worker_name = None
        self._light_up_time = None
        self._location_address = None
        self._metrics_date = None
        self._nfc_amount = None
        self._nfc_transaction_count = None
        self._open_id = None
        self._province_code = None
        self._province_name = None
        self._register_time = None
        self._shipping_time = None
        self._sn = None
        self._store_id = None

    @property
    def alipay_amount(self):
        return self._alipay_amount

    @alipay_amount.setter
    def alipay_amount(self, value):
        self._alipay_amount = value
    @property
    def alipay_transaction_count(self):
        return self._alipay_transaction_count

    @alipay_transaction_count.setter
    def alipay_transaction_count(self, value):
        self._alipay_transaction_count = value
    @property
    def be_lighted_up(self):
        return self._be_lighted_up

    @be_lighted_up.setter
    def be_lighted_up(self, value):
        self._be_lighted_up = value
    @property
    def be_register(self):
        return self._be_register

    @be_register.setter
    def be_register(self, value):
        self._be_register = value
    @property
    def be_turnon_device(self):
        return self._be_turnon_device

    @be_turnon_device.setter
    def be_turnon_device(self, value):
        self._be_turnon_device = value
    @property
    def binding_location(self):
        return self._binding_location

    @binding_location.setter
    def binding_location(self, value):
        self._binding_location = value
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
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def district_name(self):
        return self._district_name

    @district_name.setter
    def district_name(self, value):
        self._district_name = value
    @property
    def do_check_in(self):
        return self._do_check_in

    @do_check_in.setter
    def do_check_in(self, value):
        self._do_check_in = value
    @property
    def has_nfc_trade(self):
        return self._has_nfc_trade

    @has_nfc_trade.setter
    def has_nfc_trade(self, value):
        self._has_nfc_trade = value
    @property
    def leads_worker_id(self):
        return self._leads_worker_id

    @leads_worker_id.setter
    def leads_worker_id(self, value):
        self._leads_worker_id = value
    @property
    def leads_worker_name(self):
        return self._leads_worker_name

    @leads_worker_name.setter
    def leads_worker_name(self, value):
        self._leads_worker_name = value
    @property
    def light_up_time(self):
        return self._light_up_time

    @light_up_time.setter
    def light_up_time(self, value):
        self._light_up_time = value
    @property
    def location_address(self):
        return self._location_address

    @location_address.setter
    def location_address(self, value):
        self._location_address = value
    @property
    def metrics_date(self):
        return self._metrics_date

    @metrics_date.setter
    def metrics_date(self, value):
        self._metrics_date = value
    @property
    def nfc_amount(self):
        return self._nfc_amount

    @nfc_amount.setter
    def nfc_amount(self, value):
        self._nfc_amount = value
    @property
    def nfc_transaction_count(self):
        return self._nfc_transaction_count

    @nfc_transaction_count.setter
    def nfc_transaction_count(self, value):
        self._nfc_transaction_count = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def province_name(self):
        return self._province_name

    @province_name.setter
    def province_name(self, value):
        self._province_name = value
    @property
    def register_time(self):
        return self._register_time

    @register_time.setter
    def register_time(self, value):
        self._register_time = value
    @property
    def shipping_time(self):
        return self._shipping_time

    @shipping_time.setter
    def shipping_time(self, value):
        self._shipping_time = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_amount:
            if hasattr(self.alipay_amount, 'to_alipay_dict'):
                params['alipay_amount'] = self.alipay_amount.to_alipay_dict()
            else:
                params['alipay_amount'] = self.alipay_amount
        if self.alipay_transaction_count:
            if hasattr(self.alipay_transaction_count, 'to_alipay_dict'):
                params['alipay_transaction_count'] = self.alipay_transaction_count.to_alipay_dict()
            else:
                params['alipay_transaction_count'] = self.alipay_transaction_count
        if self.be_lighted_up:
            if hasattr(self.be_lighted_up, 'to_alipay_dict'):
                params['be_lighted_up'] = self.be_lighted_up.to_alipay_dict()
            else:
                params['be_lighted_up'] = self.be_lighted_up
        if self.be_register:
            if hasattr(self.be_register, 'to_alipay_dict'):
                params['be_register'] = self.be_register.to_alipay_dict()
            else:
                params['be_register'] = self.be_register
        if self.be_turnon_device:
            if hasattr(self.be_turnon_device, 'to_alipay_dict'):
                params['be_turnon_device'] = self.be_turnon_device.to_alipay_dict()
            else:
                params['be_turnon_device'] = self.be_turnon_device
        if self.binding_location:
            if hasattr(self.binding_location, 'to_alipay_dict'):
                params['binding_location'] = self.binding_location.to_alipay_dict()
            else:
                params['binding_location'] = self.binding_location
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
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.district_name:
            if hasattr(self.district_name, 'to_alipay_dict'):
                params['district_name'] = self.district_name.to_alipay_dict()
            else:
                params['district_name'] = self.district_name
        if self.do_check_in:
            if hasattr(self.do_check_in, 'to_alipay_dict'):
                params['do_check_in'] = self.do_check_in.to_alipay_dict()
            else:
                params['do_check_in'] = self.do_check_in
        if self.has_nfc_trade:
            if hasattr(self.has_nfc_trade, 'to_alipay_dict'):
                params['has_nfc_trade'] = self.has_nfc_trade.to_alipay_dict()
            else:
                params['has_nfc_trade'] = self.has_nfc_trade
        if self.leads_worker_id:
            if hasattr(self.leads_worker_id, 'to_alipay_dict'):
                params['leads_worker_id'] = self.leads_worker_id.to_alipay_dict()
            else:
                params['leads_worker_id'] = self.leads_worker_id
        if self.leads_worker_name:
            if hasattr(self.leads_worker_name, 'to_alipay_dict'):
                params['leads_worker_name'] = self.leads_worker_name.to_alipay_dict()
            else:
                params['leads_worker_name'] = self.leads_worker_name
        if self.light_up_time:
            if hasattr(self.light_up_time, 'to_alipay_dict'):
                params['light_up_time'] = self.light_up_time.to_alipay_dict()
            else:
                params['light_up_time'] = self.light_up_time
        if self.location_address:
            if hasattr(self.location_address, 'to_alipay_dict'):
                params['location_address'] = self.location_address.to_alipay_dict()
            else:
                params['location_address'] = self.location_address
        if self.metrics_date:
            if hasattr(self.metrics_date, 'to_alipay_dict'):
                params['metrics_date'] = self.metrics_date.to_alipay_dict()
            else:
                params['metrics_date'] = self.metrics_date
        if self.nfc_amount:
            if hasattr(self.nfc_amount, 'to_alipay_dict'):
                params['nfc_amount'] = self.nfc_amount.to_alipay_dict()
            else:
                params['nfc_amount'] = self.nfc_amount
        if self.nfc_transaction_count:
            if hasattr(self.nfc_transaction_count, 'to_alipay_dict'):
                params['nfc_transaction_count'] = self.nfc_transaction_count.to_alipay_dict()
            else:
                params['nfc_transaction_count'] = self.nfc_transaction_count
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.province_name:
            if hasattr(self.province_name, 'to_alipay_dict'):
                params['province_name'] = self.province_name.to_alipay_dict()
            else:
                params['province_name'] = self.province_name
        if self.register_time:
            if hasattr(self.register_time, 'to_alipay_dict'):
                params['register_time'] = self.register_time.to_alipay_dict()
            else:
                params['register_time'] = self.register_time
        if self.shipping_time:
            if hasattr(self.shipping_time, 'to_alipay_dict'):
                params['shipping_time'] = self.shipping_time.to_alipay_dict()
            else:
                params['shipping_time'] = self.shipping_time
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NDeviceMetricsListForDayResponse()
        if 'alipay_amount' in d:
            o.alipay_amount = d['alipay_amount']
        if 'alipay_transaction_count' in d:
            o.alipay_transaction_count = d['alipay_transaction_count']
        if 'be_lighted_up' in d:
            o.be_lighted_up = d['be_lighted_up']
        if 'be_register' in d:
            o.be_register = d['be_register']
        if 'be_turnon_device' in d:
            o.be_turnon_device = d['be_turnon_device']
        if 'binding_location' in d:
            o.binding_location = d['binding_location']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'district_name' in d:
            o.district_name = d['district_name']
        if 'do_check_in' in d:
            o.do_check_in = d['do_check_in']
        if 'has_nfc_trade' in d:
            o.has_nfc_trade = d['has_nfc_trade']
        if 'leads_worker_id' in d:
            o.leads_worker_id = d['leads_worker_id']
        if 'leads_worker_name' in d:
            o.leads_worker_name = d['leads_worker_name']
        if 'light_up_time' in d:
            o.light_up_time = d['light_up_time']
        if 'location_address' in d:
            o.location_address = d['location_address']
        if 'metrics_date' in d:
            o.metrics_date = d['metrics_date']
        if 'nfc_amount' in d:
            o.nfc_amount = d['nfc_amount']
        if 'nfc_transaction_count' in d:
            o.nfc_transaction_count = d['nfc_transaction_count']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'province_name' in d:
            o.province_name = d['province_name']
        if 'register_time' in d:
            o.register_time = d['register_time']
        if 'shipping_time' in d:
            o.shipping_time = d['shipping_time']
        if 'sn' in d:
            o.sn = d['sn']
        if 'store_id' in d:
            o.store_id = d['store_id']
        return o


