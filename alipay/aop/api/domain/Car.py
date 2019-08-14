#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VehicleInfo import VehicleInfo
from alipay.aop.api.domain.VehicleInfo import VehicleInfo


class Car(object):

    def __init__(self):
        self._car_engine_no = None
        self._car_frame_no = None
        self._car_model_code = None
        self._car_no = None
        self._data_source = None
        self._first_register_date = None
        self._is_new = None
        self._license_address = None
        self._loan_flag = None
        self._seat_number = None
        self._transfer_car = None
        self._transfer_date = None
        self._vehicle_info = None
        self._vehicle_info_list = None
        self._vehicle_type = None

    @property
    def car_engine_no(self):
        return self._car_engine_no

    @car_engine_no.setter
    def car_engine_no(self, value):
        self._car_engine_no = value
    @property
    def car_frame_no(self):
        return self._car_frame_no

    @car_frame_no.setter
    def car_frame_no(self, value):
        self._car_frame_no = value
    @property
    def car_model_code(self):
        return self._car_model_code

    @car_model_code.setter
    def car_model_code(self, value):
        self._car_model_code = value
    @property
    def car_no(self):
        return self._car_no

    @car_no.setter
    def car_no(self, value):
        self._car_no = value
    @property
    def data_source(self):
        return self._data_source

    @data_source.setter
    def data_source(self, value):
        self._data_source = value
    @property
    def first_register_date(self):
        return self._first_register_date

    @first_register_date.setter
    def first_register_date(self, value):
        self._first_register_date = value
    @property
    def is_new(self):
        return self._is_new

    @is_new.setter
    def is_new(self, value):
        self._is_new = value
    @property
    def license_address(self):
        return self._license_address

    @license_address.setter
    def license_address(self, value):
        self._license_address = value
    @property
    def loan_flag(self):
        return self._loan_flag

    @loan_flag.setter
    def loan_flag(self, value):
        self._loan_flag = value
    @property
    def seat_number(self):
        return self._seat_number

    @seat_number.setter
    def seat_number(self, value):
        self._seat_number = value
    @property
    def transfer_car(self):
        return self._transfer_car

    @transfer_car.setter
    def transfer_car(self, value):
        self._transfer_car = value
    @property
    def transfer_date(self):
        return self._transfer_date

    @transfer_date.setter
    def transfer_date(self, value):
        self._transfer_date = value
    @property
    def vehicle_info(self):
        return self._vehicle_info

    @vehicle_info.setter
    def vehicle_info(self, value):
        if isinstance(value, VehicleInfo):
            self._vehicle_info = value
        else:
            self._vehicle_info = VehicleInfo.from_alipay_dict(value)
    @property
    def vehicle_info_list(self):
        return self._vehicle_info_list

    @vehicle_info_list.setter
    def vehicle_info_list(self, value):
        if isinstance(value, list):
            self._vehicle_info_list = list()
            for i in value:
                if isinstance(i, VehicleInfo):
                    self._vehicle_info_list.append(i)
                else:
                    self._vehicle_info_list.append(VehicleInfo.from_alipay_dict(i))
    @property
    def vehicle_type(self):
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, value):
        self._vehicle_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.car_engine_no:
            if hasattr(self.car_engine_no, 'to_alipay_dict'):
                params['car_engine_no'] = self.car_engine_no.to_alipay_dict()
            else:
                params['car_engine_no'] = self.car_engine_no
        if self.car_frame_no:
            if hasattr(self.car_frame_no, 'to_alipay_dict'):
                params['car_frame_no'] = self.car_frame_no.to_alipay_dict()
            else:
                params['car_frame_no'] = self.car_frame_no
        if self.car_model_code:
            if hasattr(self.car_model_code, 'to_alipay_dict'):
                params['car_model_code'] = self.car_model_code.to_alipay_dict()
            else:
                params['car_model_code'] = self.car_model_code
        if self.car_no:
            if hasattr(self.car_no, 'to_alipay_dict'):
                params['car_no'] = self.car_no.to_alipay_dict()
            else:
                params['car_no'] = self.car_no
        if self.data_source:
            if hasattr(self.data_source, 'to_alipay_dict'):
                params['data_source'] = self.data_source.to_alipay_dict()
            else:
                params['data_source'] = self.data_source
        if self.first_register_date:
            if hasattr(self.first_register_date, 'to_alipay_dict'):
                params['first_register_date'] = self.first_register_date.to_alipay_dict()
            else:
                params['first_register_date'] = self.first_register_date
        if self.is_new:
            if hasattr(self.is_new, 'to_alipay_dict'):
                params['is_new'] = self.is_new.to_alipay_dict()
            else:
                params['is_new'] = self.is_new
        if self.license_address:
            if hasattr(self.license_address, 'to_alipay_dict'):
                params['license_address'] = self.license_address.to_alipay_dict()
            else:
                params['license_address'] = self.license_address
        if self.loan_flag:
            if hasattr(self.loan_flag, 'to_alipay_dict'):
                params['loan_flag'] = self.loan_flag.to_alipay_dict()
            else:
                params['loan_flag'] = self.loan_flag
        if self.seat_number:
            if hasattr(self.seat_number, 'to_alipay_dict'):
                params['seat_number'] = self.seat_number.to_alipay_dict()
            else:
                params['seat_number'] = self.seat_number
        if self.transfer_car:
            if hasattr(self.transfer_car, 'to_alipay_dict'):
                params['transfer_car'] = self.transfer_car.to_alipay_dict()
            else:
                params['transfer_car'] = self.transfer_car
        if self.transfer_date:
            if hasattr(self.transfer_date, 'to_alipay_dict'):
                params['transfer_date'] = self.transfer_date.to_alipay_dict()
            else:
                params['transfer_date'] = self.transfer_date
        if self.vehicle_info:
            if hasattr(self.vehicle_info, 'to_alipay_dict'):
                params['vehicle_info'] = self.vehicle_info.to_alipay_dict()
            else:
                params['vehicle_info'] = self.vehicle_info
        if self.vehicle_info_list:
            if isinstance(self.vehicle_info_list, list):
                for i in range(0, len(self.vehicle_info_list)):
                    element = self.vehicle_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.vehicle_info_list[i] = element.to_alipay_dict()
            if hasattr(self.vehicle_info_list, 'to_alipay_dict'):
                params['vehicle_info_list'] = self.vehicle_info_list.to_alipay_dict()
            else:
                params['vehicle_info_list'] = self.vehicle_info_list
        if self.vehicle_type:
            if hasattr(self.vehicle_type, 'to_alipay_dict'):
                params['vehicle_type'] = self.vehicle_type.to_alipay_dict()
            else:
                params['vehicle_type'] = self.vehicle_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Car()
        if 'car_engine_no' in d:
            o.car_engine_no = d['car_engine_no']
        if 'car_frame_no' in d:
            o.car_frame_no = d['car_frame_no']
        if 'car_model_code' in d:
            o.car_model_code = d['car_model_code']
        if 'car_no' in d:
            o.car_no = d['car_no']
        if 'data_source' in d:
            o.data_source = d['data_source']
        if 'first_register_date' in d:
            o.first_register_date = d['first_register_date']
        if 'is_new' in d:
            o.is_new = d['is_new']
        if 'license_address' in d:
            o.license_address = d['license_address']
        if 'loan_flag' in d:
            o.loan_flag = d['loan_flag']
        if 'seat_number' in d:
            o.seat_number = d['seat_number']
        if 'transfer_car' in d:
            o.transfer_car = d['transfer_car']
        if 'transfer_date' in d:
            o.transfer_date = d['transfer_date']
        if 'vehicle_info' in d:
            o.vehicle_info = d['vehicle_info']
        if 'vehicle_info_list' in d:
            o.vehicle_info_list = d['vehicle_info_list']
        if 'vehicle_type' in d:
            o.vehicle_type = d['vehicle_type']
        return o


