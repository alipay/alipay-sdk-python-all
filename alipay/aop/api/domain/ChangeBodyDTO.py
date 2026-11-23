#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsOpenUserDTO import InsOpenUserDTO
from alipay.aop.api.domain.InsOpenUserDTO import InsOpenUserDTO
from alipay.aop.api.domain.EcomOrderDTO import EcomOrderDTO


class ChangeBodyDTO(object):

    def __init__(self):
        self._consult_order_id = None
        self._event_type = None
        self._main_order_id = None
        self._new_car_no = None
        self._new_car_renter = None
        self._new_car_type = None
        self._new_end_time = None
        self._new_engine_number = None
        self._new_insured = None
        self._new_order = None
        self._new_seat_num = None
        self._new_start_time = None
        self._new_vehicle_brand = None
        self._new_vin = None

    @property
    def consult_order_id(self):
        return self._consult_order_id

    @consult_order_id.setter
    def consult_order_id(self, value):
        self._consult_order_id = value
    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
    @property
    def main_order_id(self):
        return self._main_order_id

    @main_order_id.setter
    def main_order_id(self, value):
        self._main_order_id = value
    @property
    def new_car_no(self):
        return self._new_car_no

    @new_car_no.setter
    def new_car_no(self, value):
        self._new_car_no = value
    @property
    def new_car_renter(self):
        return self._new_car_renter

    @new_car_renter.setter
    def new_car_renter(self, value):
        if isinstance(value, InsOpenUserDTO):
            self._new_car_renter = value
        else:
            self._new_car_renter = InsOpenUserDTO.from_alipay_dict(value)
    @property
    def new_car_type(self):
        return self._new_car_type

    @new_car_type.setter
    def new_car_type(self, value):
        self._new_car_type = value
    @property
    def new_end_time(self):
        return self._new_end_time

    @new_end_time.setter
    def new_end_time(self, value):
        self._new_end_time = value
    @property
    def new_engine_number(self):
        return self._new_engine_number

    @new_engine_number.setter
    def new_engine_number(self, value):
        self._new_engine_number = value
    @property
    def new_insured(self):
        return self._new_insured

    @new_insured.setter
    def new_insured(self, value):
        if isinstance(value, InsOpenUserDTO):
            self._new_insured = value
        else:
            self._new_insured = InsOpenUserDTO.from_alipay_dict(value)
    @property
    def new_order(self):
        return self._new_order

    @new_order.setter
    def new_order(self, value):
        if isinstance(value, EcomOrderDTO):
            self._new_order = value
        else:
            self._new_order = EcomOrderDTO.from_alipay_dict(value)
    @property
    def new_seat_num(self):
        return self._new_seat_num

    @new_seat_num.setter
    def new_seat_num(self, value):
        self._new_seat_num = value
    @property
    def new_start_time(self):
        return self._new_start_time

    @new_start_time.setter
    def new_start_time(self, value):
        self._new_start_time = value
    @property
    def new_vehicle_brand(self):
        return self._new_vehicle_brand

    @new_vehicle_brand.setter
    def new_vehicle_brand(self, value):
        self._new_vehicle_brand = value
    @property
    def new_vin(self):
        return self._new_vin

    @new_vin.setter
    def new_vin(self, value):
        self._new_vin = value


    def to_alipay_dict(self):
        params = dict()
        if self.consult_order_id:
            if hasattr(self.consult_order_id, 'to_alipay_dict'):
                params['consult_order_id'] = self.consult_order_id.to_alipay_dict()
            else:
                params['consult_order_id'] = self.consult_order_id
        if self.event_type:
            if hasattr(self.event_type, 'to_alipay_dict'):
                params['event_type'] = self.event_type.to_alipay_dict()
            else:
                params['event_type'] = self.event_type
        if self.main_order_id:
            if hasattr(self.main_order_id, 'to_alipay_dict'):
                params['main_order_id'] = self.main_order_id.to_alipay_dict()
            else:
                params['main_order_id'] = self.main_order_id
        if self.new_car_no:
            if hasattr(self.new_car_no, 'to_alipay_dict'):
                params['new_car_no'] = self.new_car_no.to_alipay_dict()
            else:
                params['new_car_no'] = self.new_car_no
        if self.new_car_renter:
            if hasattr(self.new_car_renter, 'to_alipay_dict'):
                params['new_car_renter'] = self.new_car_renter.to_alipay_dict()
            else:
                params['new_car_renter'] = self.new_car_renter
        if self.new_car_type:
            if hasattr(self.new_car_type, 'to_alipay_dict'):
                params['new_car_type'] = self.new_car_type.to_alipay_dict()
            else:
                params['new_car_type'] = self.new_car_type
        if self.new_end_time:
            if hasattr(self.new_end_time, 'to_alipay_dict'):
                params['new_end_time'] = self.new_end_time.to_alipay_dict()
            else:
                params['new_end_time'] = self.new_end_time
        if self.new_engine_number:
            if hasattr(self.new_engine_number, 'to_alipay_dict'):
                params['new_engine_number'] = self.new_engine_number.to_alipay_dict()
            else:
                params['new_engine_number'] = self.new_engine_number
        if self.new_insured:
            if hasattr(self.new_insured, 'to_alipay_dict'):
                params['new_insured'] = self.new_insured.to_alipay_dict()
            else:
                params['new_insured'] = self.new_insured
        if self.new_order:
            if hasattr(self.new_order, 'to_alipay_dict'):
                params['new_order'] = self.new_order.to_alipay_dict()
            else:
                params['new_order'] = self.new_order
        if self.new_seat_num:
            if hasattr(self.new_seat_num, 'to_alipay_dict'):
                params['new_seat_num'] = self.new_seat_num.to_alipay_dict()
            else:
                params['new_seat_num'] = self.new_seat_num
        if self.new_start_time:
            if hasattr(self.new_start_time, 'to_alipay_dict'):
                params['new_start_time'] = self.new_start_time.to_alipay_dict()
            else:
                params['new_start_time'] = self.new_start_time
        if self.new_vehicle_brand:
            if hasattr(self.new_vehicle_brand, 'to_alipay_dict'):
                params['new_vehicle_brand'] = self.new_vehicle_brand.to_alipay_dict()
            else:
                params['new_vehicle_brand'] = self.new_vehicle_brand
        if self.new_vin:
            if hasattr(self.new_vin, 'to_alipay_dict'):
                params['new_vin'] = self.new_vin.to_alipay_dict()
            else:
                params['new_vin'] = self.new_vin
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChangeBodyDTO()
        if 'consult_order_id' in d:
            o.consult_order_id = d['consult_order_id']
        if 'event_type' in d:
            o.event_type = d['event_type']
        if 'main_order_id' in d:
            o.main_order_id = d['main_order_id']
        if 'new_car_no' in d:
            o.new_car_no = d['new_car_no']
        if 'new_car_renter' in d:
            o.new_car_renter = d['new_car_renter']
        if 'new_car_type' in d:
            o.new_car_type = d['new_car_type']
        if 'new_end_time' in d:
            o.new_end_time = d['new_end_time']
        if 'new_engine_number' in d:
            o.new_engine_number = d['new_engine_number']
        if 'new_insured' in d:
            o.new_insured = d['new_insured']
        if 'new_order' in d:
            o.new_order = d['new_order']
        if 'new_seat_num' in d:
            o.new_seat_num = d['new_seat_num']
        if 'new_start_time' in d:
            o.new_start_time = d['new_start_time']
        if 'new_vehicle_brand' in d:
            o.new_vehicle_brand = d['new_vehicle_brand']
        if 'new_vin' in d:
            o.new_vin = d['new_vin']
        return o


