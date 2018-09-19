#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditLoanCollateralCarModifyModel(object):

    def __init__(self):
        self._apply_no = None
        self._car_brand_id = None
        self._car_brand_name = None
        self._car_color = None
        self._car_engine_no = None
        self._car_mileage = None
        self._car_model_id = None
        self._car_model_name = None
        self._car_reg_date = None
        self._car_series_id = None
        self._car_series_name = None
        self._car_vin = None
        self._lic_plate_address = None
        self._lic_plate_no = None
        self._out_request_no = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def car_brand_id(self):
        return self._car_brand_id

    @car_brand_id.setter
    def car_brand_id(self, value):
        self._car_brand_id = value
    @property
    def car_brand_name(self):
        return self._car_brand_name

    @car_brand_name.setter
    def car_brand_name(self, value):
        self._car_brand_name = value
    @property
    def car_color(self):
        return self._car_color

    @car_color.setter
    def car_color(self, value):
        self._car_color = value
    @property
    def car_engine_no(self):
        return self._car_engine_no

    @car_engine_no.setter
    def car_engine_no(self, value):
        self._car_engine_no = value
    @property
    def car_mileage(self):
        return self._car_mileage

    @car_mileage.setter
    def car_mileage(self, value):
        self._car_mileage = value
    @property
    def car_model_id(self):
        return self._car_model_id

    @car_model_id.setter
    def car_model_id(self, value):
        self._car_model_id = value
    @property
    def car_model_name(self):
        return self._car_model_name

    @car_model_name.setter
    def car_model_name(self, value):
        self._car_model_name = value
    @property
    def car_reg_date(self):
        return self._car_reg_date

    @car_reg_date.setter
    def car_reg_date(self, value):
        self._car_reg_date = value
    @property
    def car_series_id(self):
        return self._car_series_id

    @car_series_id.setter
    def car_series_id(self, value):
        self._car_series_id = value
    @property
    def car_series_name(self):
        return self._car_series_name

    @car_series_name.setter
    def car_series_name(self, value):
        self._car_series_name = value
    @property
    def car_vin(self):
        return self._car_vin

    @car_vin.setter
    def car_vin(self, value):
        self._car_vin = value
    @property
    def lic_plate_address(self):
        return self._lic_plate_address

    @lic_plate_address.setter
    def lic_plate_address(self, value):
        self._lic_plate_address = value
    @property
    def lic_plate_no(self):
        return self._lic_plate_no

    @lic_plate_no.setter
    def lic_plate_no(self, value):
        self._lic_plate_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.car_brand_id:
            if hasattr(self.car_brand_id, 'to_alipay_dict'):
                params['car_brand_id'] = self.car_brand_id.to_alipay_dict()
            else:
                params['car_brand_id'] = self.car_brand_id
        if self.car_brand_name:
            if hasattr(self.car_brand_name, 'to_alipay_dict'):
                params['car_brand_name'] = self.car_brand_name.to_alipay_dict()
            else:
                params['car_brand_name'] = self.car_brand_name
        if self.car_color:
            if hasattr(self.car_color, 'to_alipay_dict'):
                params['car_color'] = self.car_color.to_alipay_dict()
            else:
                params['car_color'] = self.car_color
        if self.car_engine_no:
            if hasattr(self.car_engine_no, 'to_alipay_dict'):
                params['car_engine_no'] = self.car_engine_no.to_alipay_dict()
            else:
                params['car_engine_no'] = self.car_engine_no
        if self.car_mileage:
            if hasattr(self.car_mileage, 'to_alipay_dict'):
                params['car_mileage'] = self.car_mileage.to_alipay_dict()
            else:
                params['car_mileage'] = self.car_mileage
        if self.car_model_id:
            if hasattr(self.car_model_id, 'to_alipay_dict'):
                params['car_model_id'] = self.car_model_id.to_alipay_dict()
            else:
                params['car_model_id'] = self.car_model_id
        if self.car_model_name:
            if hasattr(self.car_model_name, 'to_alipay_dict'):
                params['car_model_name'] = self.car_model_name.to_alipay_dict()
            else:
                params['car_model_name'] = self.car_model_name
        if self.car_reg_date:
            if hasattr(self.car_reg_date, 'to_alipay_dict'):
                params['car_reg_date'] = self.car_reg_date.to_alipay_dict()
            else:
                params['car_reg_date'] = self.car_reg_date
        if self.car_series_id:
            if hasattr(self.car_series_id, 'to_alipay_dict'):
                params['car_series_id'] = self.car_series_id.to_alipay_dict()
            else:
                params['car_series_id'] = self.car_series_id
        if self.car_series_name:
            if hasattr(self.car_series_name, 'to_alipay_dict'):
                params['car_series_name'] = self.car_series_name.to_alipay_dict()
            else:
                params['car_series_name'] = self.car_series_name
        if self.car_vin:
            if hasattr(self.car_vin, 'to_alipay_dict'):
                params['car_vin'] = self.car_vin.to_alipay_dict()
            else:
                params['car_vin'] = self.car_vin
        if self.lic_plate_address:
            if hasattr(self.lic_plate_address, 'to_alipay_dict'):
                params['lic_plate_address'] = self.lic_plate_address.to_alipay_dict()
            else:
                params['lic_plate_address'] = self.lic_plate_address
        if self.lic_plate_no:
            if hasattr(self.lic_plate_no, 'to_alipay_dict'):
                params['lic_plate_no'] = self.lic_plate_no.to_alipay_dict()
            else:
                params['lic_plate_no'] = self.lic_plate_no
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditLoanCollateralCarModifyModel()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'car_brand_id' in d:
            o.car_brand_id = d['car_brand_id']
        if 'car_brand_name' in d:
            o.car_brand_name = d['car_brand_name']
        if 'car_color' in d:
            o.car_color = d['car_color']
        if 'car_engine_no' in d:
            o.car_engine_no = d['car_engine_no']
        if 'car_mileage' in d:
            o.car_mileage = d['car_mileage']
        if 'car_model_id' in d:
            o.car_model_id = d['car_model_id']
        if 'car_model_name' in d:
            o.car_model_name = d['car_model_name']
        if 'car_reg_date' in d:
            o.car_reg_date = d['car_reg_date']
        if 'car_series_id' in d:
            o.car_series_id = d['car_series_id']
        if 'car_series_name' in d:
            o.car_series_name = d['car_series_name']
        if 'car_vin' in d:
            o.car_vin = d['car_vin']
        if 'lic_plate_address' in d:
            o.lic_plate_address = d['lic_plate_address']
        if 'lic_plate_no' in d:
            o.lic_plate_no = d['lic_plate_no']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        return o


