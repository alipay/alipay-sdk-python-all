#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportTaxiTripinvoiceApplyModel(object):

    def __init__(self):
        self._buyer_address = None
        self._buyer_bank_name = None
        self._buyer_name = None
        self._buyer_tax_no = None
        self._city_code = None
        self._driver_id_card = None
        self._driver_name = None
        self._order_no = None
        self._passenger_phone = None
        self._tax_no = None
        self._title_type = None
        self._trip_amount = None
        self._trip_end_location = None
        self._trip_end_time = None
        self._trip_id = None
        self._trip_start_location = None
        self._trip_start_time = None

    @property
    def buyer_address(self):
        return self._buyer_address

    @buyer_address.setter
    def buyer_address(self, value):
        self._buyer_address = value
    @property
    def buyer_bank_name(self):
        return self._buyer_bank_name

    @buyer_bank_name.setter
    def buyer_bank_name(self, value):
        self._buyer_bank_name = value
    @property
    def buyer_name(self):
        return self._buyer_name

    @buyer_name.setter
    def buyer_name(self, value):
        self._buyer_name = value
    @property
    def buyer_tax_no(self):
        return self._buyer_tax_no

    @buyer_tax_no.setter
    def buyer_tax_no(self, value):
        self._buyer_tax_no = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def driver_id_card(self):
        return self._driver_id_card

    @driver_id_card.setter
    def driver_id_card(self, value):
        self._driver_id_card = value
    @property
    def driver_name(self):
        return self._driver_name

    @driver_name.setter
    def driver_name(self, value):
        self._driver_name = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def passenger_phone(self):
        return self._passenger_phone

    @passenger_phone.setter
    def passenger_phone(self, value):
        self._passenger_phone = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value
    @property
    def title_type(self):
        return self._title_type

    @title_type.setter
    def title_type(self, value):
        self._title_type = value
    @property
    def trip_amount(self):
        return self._trip_amount

    @trip_amount.setter
    def trip_amount(self, value):
        self._trip_amount = value
    @property
    def trip_end_location(self):
        return self._trip_end_location

    @trip_end_location.setter
    def trip_end_location(self, value):
        self._trip_end_location = value
    @property
    def trip_end_time(self):
        return self._trip_end_time

    @trip_end_time.setter
    def trip_end_time(self, value):
        self._trip_end_time = value
    @property
    def trip_id(self):
        return self._trip_id

    @trip_id.setter
    def trip_id(self, value):
        self._trip_id = value
    @property
    def trip_start_location(self):
        return self._trip_start_location

    @trip_start_location.setter
    def trip_start_location(self, value):
        self._trip_start_location = value
    @property
    def trip_start_time(self):
        return self._trip_start_time

    @trip_start_time.setter
    def trip_start_time(self, value):
        self._trip_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_address:
            if hasattr(self.buyer_address, 'to_alipay_dict'):
                params['buyer_address'] = self.buyer_address.to_alipay_dict()
            else:
                params['buyer_address'] = self.buyer_address
        if self.buyer_bank_name:
            if hasattr(self.buyer_bank_name, 'to_alipay_dict'):
                params['buyer_bank_name'] = self.buyer_bank_name.to_alipay_dict()
            else:
                params['buyer_bank_name'] = self.buyer_bank_name
        if self.buyer_name:
            if hasattr(self.buyer_name, 'to_alipay_dict'):
                params['buyer_name'] = self.buyer_name.to_alipay_dict()
            else:
                params['buyer_name'] = self.buyer_name
        if self.buyer_tax_no:
            if hasattr(self.buyer_tax_no, 'to_alipay_dict'):
                params['buyer_tax_no'] = self.buyer_tax_no.to_alipay_dict()
            else:
                params['buyer_tax_no'] = self.buyer_tax_no
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.driver_id_card:
            if hasattr(self.driver_id_card, 'to_alipay_dict'):
                params['driver_id_card'] = self.driver_id_card.to_alipay_dict()
            else:
                params['driver_id_card'] = self.driver_id_card
        if self.driver_name:
            if hasattr(self.driver_name, 'to_alipay_dict'):
                params['driver_name'] = self.driver_name.to_alipay_dict()
            else:
                params['driver_name'] = self.driver_name
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.passenger_phone:
            if hasattr(self.passenger_phone, 'to_alipay_dict'):
                params['passenger_phone'] = self.passenger_phone.to_alipay_dict()
            else:
                params['passenger_phone'] = self.passenger_phone
        if self.tax_no:
            if hasattr(self.tax_no, 'to_alipay_dict'):
                params['tax_no'] = self.tax_no.to_alipay_dict()
            else:
                params['tax_no'] = self.tax_no
        if self.title_type:
            if hasattr(self.title_type, 'to_alipay_dict'):
                params['title_type'] = self.title_type.to_alipay_dict()
            else:
                params['title_type'] = self.title_type
        if self.trip_amount:
            if hasattr(self.trip_amount, 'to_alipay_dict'):
                params['trip_amount'] = self.trip_amount.to_alipay_dict()
            else:
                params['trip_amount'] = self.trip_amount
        if self.trip_end_location:
            if hasattr(self.trip_end_location, 'to_alipay_dict'):
                params['trip_end_location'] = self.trip_end_location.to_alipay_dict()
            else:
                params['trip_end_location'] = self.trip_end_location
        if self.trip_end_time:
            if hasattr(self.trip_end_time, 'to_alipay_dict'):
                params['trip_end_time'] = self.trip_end_time.to_alipay_dict()
            else:
                params['trip_end_time'] = self.trip_end_time
        if self.trip_id:
            if hasattr(self.trip_id, 'to_alipay_dict'):
                params['trip_id'] = self.trip_id.to_alipay_dict()
            else:
                params['trip_id'] = self.trip_id
        if self.trip_start_location:
            if hasattr(self.trip_start_location, 'to_alipay_dict'):
                params['trip_start_location'] = self.trip_start_location.to_alipay_dict()
            else:
                params['trip_start_location'] = self.trip_start_location
        if self.trip_start_time:
            if hasattr(self.trip_start_time, 'to_alipay_dict'):
                params['trip_start_time'] = self.trip_start_time.to_alipay_dict()
            else:
                params['trip_start_time'] = self.trip_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportTaxiTripinvoiceApplyModel()
        if 'buyer_address' in d:
            o.buyer_address = d['buyer_address']
        if 'buyer_bank_name' in d:
            o.buyer_bank_name = d['buyer_bank_name']
        if 'buyer_name' in d:
            o.buyer_name = d['buyer_name']
        if 'buyer_tax_no' in d:
            o.buyer_tax_no = d['buyer_tax_no']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'driver_id_card' in d:
            o.driver_id_card = d['driver_id_card']
        if 'driver_name' in d:
            o.driver_name = d['driver_name']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'passenger_phone' in d:
            o.passenger_phone = d['passenger_phone']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        if 'title_type' in d:
            o.title_type = d['title_type']
        if 'trip_amount' in d:
            o.trip_amount = d['trip_amount']
        if 'trip_end_location' in d:
            o.trip_end_location = d['trip_end_location']
        if 'trip_end_time' in d:
            o.trip_end_time = d['trip_end_time']
        if 'trip_id' in d:
            o.trip_id = d['trip_id']
        if 'trip_start_location' in d:
            o.trip_start_location = d['trip_start_location']
        if 'trip_start_time' in d:
            o.trip_start_time = d['trip_start_time']
        return o


