#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CarfinRegistrationTransferInfo(object):

    def __init__(self):
        self._acquisition_method = None
        self._social_code = None
        self._transfer_name = None
        self._transfer_registration_date = None
        self._vehicle_registration_number = None

    @property
    def acquisition_method(self):
        return self._acquisition_method

    @acquisition_method.setter
    def acquisition_method(self, value):
        self._acquisition_method = value
    @property
    def social_code(self):
        return self._social_code

    @social_code.setter
    def social_code(self, value):
        self._social_code = value
    @property
    def transfer_name(self):
        return self._transfer_name

    @transfer_name.setter
    def transfer_name(self, value):
        self._transfer_name = value
    @property
    def transfer_registration_date(self):
        return self._transfer_registration_date

    @transfer_registration_date.setter
    def transfer_registration_date(self, value):
        self._transfer_registration_date = value
    @property
    def vehicle_registration_number(self):
        return self._vehicle_registration_number

    @vehicle_registration_number.setter
    def vehicle_registration_number(self, value):
        self._vehicle_registration_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.acquisition_method:
            if hasattr(self.acquisition_method, 'to_alipay_dict'):
                params['acquisition_method'] = self.acquisition_method.to_alipay_dict()
            else:
                params['acquisition_method'] = self.acquisition_method
        if self.social_code:
            if hasattr(self.social_code, 'to_alipay_dict'):
                params['social_code'] = self.social_code.to_alipay_dict()
            else:
                params['social_code'] = self.social_code
        if self.transfer_name:
            if hasattr(self.transfer_name, 'to_alipay_dict'):
                params['transfer_name'] = self.transfer_name.to_alipay_dict()
            else:
                params['transfer_name'] = self.transfer_name
        if self.transfer_registration_date:
            if hasattr(self.transfer_registration_date, 'to_alipay_dict'):
                params['transfer_registration_date'] = self.transfer_registration_date.to_alipay_dict()
            else:
                params['transfer_registration_date'] = self.transfer_registration_date
        if self.vehicle_registration_number:
            if hasattr(self.vehicle_registration_number, 'to_alipay_dict'):
                params['vehicle_registration_number'] = self.vehicle_registration_number.to_alipay_dict()
            else:
                params['vehicle_registration_number'] = self.vehicle_registration_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarfinRegistrationTransferInfo()
        if 'acquisition_method' in d:
            o.acquisition_method = d['acquisition_method']
        if 'social_code' in d:
            o.social_code = d['social_code']
        if 'transfer_name' in d:
            o.transfer_name = d['transfer_name']
        if 'transfer_registration_date' in d:
            o.transfer_registration_date = d['transfer_registration_date']
        if 'vehicle_registration_number' in d:
            o.vehicle_registration_number = d['vehicle_registration_number']
        return o


