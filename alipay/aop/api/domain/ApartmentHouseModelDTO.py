#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApartmentHouseModelDTO(object):

    def __init__(self):
        self._apartment_house_id = None
        self._apartment_id = None
        self._check_in_time = None
        self._deposit = None
        self._doorplate_number = None
        self._external_id = None
        self._has_private_bathroom = None
        self._internal_area = None
        self._name = None
        self._orientation = None
        self._payment_method = None
        self._rent = None
        self._rent_unit = None
        self._status = None
        self._verification_code = None

    @property
    def apartment_house_id(self):
        return self._apartment_house_id

    @apartment_house_id.setter
    def apartment_house_id(self, value):
        self._apartment_house_id = value
    @property
    def apartment_id(self):
        return self._apartment_id

    @apartment_id.setter
    def apartment_id(self, value):
        self._apartment_id = value
    @property
    def check_in_time(self):
        return self._check_in_time

    @check_in_time.setter
    def check_in_time(self, value):
        self._check_in_time = value
    @property
    def deposit(self):
        return self._deposit

    @deposit.setter
    def deposit(self, value):
        self._deposit = value
    @property
    def doorplate_number(self):
        return self._doorplate_number

    @doorplate_number.setter
    def doorplate_number(self, value):
        self._doorplate_number = value
    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value
    @property
    def has_private_bathroom(self):
        return self._has_private_bathroom

    @has_private_bathroom.setter
    def has_private_bathroom(self, value):
        self._has_private_bathroom = value
    @property
    def internal_area(self):
        return self._internal_area

    @internal_area.setter
    def internal_area(self, value):
        self._internal_area = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def orientation(self):
        return self._orientation

    @orientation.setter
    def orientation(self, value):
        self._orientation = value
    @property
    def payment_method(self):
        return self._payment_method

    @payment_method.setter
    def payment_method(self, value):
        self._payment_method = value
    @property
    def rent(self):
        return self._rent

    @rent.setter
    def rent(self, value):
        self._rent = value
    @property
    def rent_unit(self):
        return self._rent_unit

    @rent_unit.setter
    def rent_unit(self, value):
        self._rent_unit = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def verification_code(self):
        return self._verification_code

    @verification_code.setter
    def verification_code(self, value):
        self._verification_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.apartment_house_id:
            if hasattr(self.apartment_house_id, 'to_alipay_dict'):
                params['apartment_house_id'] = self.apartment_house_id.to_alipay_dict()
            else:
                params['apartment_house_id'] = self.apartment_house_id
        if self.apartment_id:
            if hasattr(self.apartment_id, 'to_alipay_dict'):
                params['apartment_id'] = self.apartment_id.to_alipay_dict()
            else:
                params['apartment_id'] = self.apartment_id
        if self.check_in_time:
            if hasattr(self.check_in_time, 'to_alipay_dict'):
                params['check_in_time'] = self.check_in_time.to_alipay_dict()
            else:
                params['check_in_time'] = self.check_in_time
        if self.deposit:
            if hasattr(self.deposit, 'to_alipay_dict'):
                params['deposit'] = self.deposit.to_alipay_dict()
            else:
                params['deposit'] = self.deposit
        if self.doorplate_number:
            if hasattr(self.doorplate_number, 'to_alipay_dict'):
                params['doorplate_number'] = self.doorplate_number.to_alipay_dict()
            else:
                params['doorplate_number'] = self.doorplate_number
        if self.external_id:
            if hasattr(self.external_id, 'to_alipay_dict'):
                params['external_id'] = self.external_id.to_alipay_dict()
            else:
                params['external_id'] = self.external_id
        if self.has_private_bathroom:
            if hasattr(self.has_private_bathroom, 'to_alipay_dict'):
                params['has_private_bathroom'] = self.has_private_bathroom.to_alipay_dict()
            else:
                params['has_private_bathroom'] = self.has_private_bathroom
        if self.internal_area:
            if hasattr(self.internal_area, 'to_alipay_dict'):
                params['internal_area'] = self.internal_area.to_alipay_dict()
            else:
                params['internal_area'] = self.internal_area
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.orientation:
            if hasattr(self.orientation, 'to_alipay_dict'):
                params['orientation'] = self.orientation.to_alipay_dict()
            else:
                params['orientation'] = self.orientation
        if self.payment_method:
            if hasattr(self.payment_method, 'to_alipay_dict'):
                params['payment_method'] = self.payment_method.to_alipay_dict()
            else:
                params['payment_method'] = self.payment_method
        if self.rent:
            if hasattr(self.rent, 'to_alipay_dict'):
                params['rent'] = self.rent.to_alipay_dict()
            else:
                params['rent'] = self.rent
        if self.rent_unit:
            if hasattr(self.rent_unit, 'to_alipay_dict'):
                params['rent_unit'] = self.rent_unit.to_alipay_dict()
            else:
                params['rent_unit'] = self.rent_unit
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.verification_code:
            if hasattr(self.verification_code, 'to_alipay_dict'):
                params['verification_code'] = self.verification_code.to_alipay_dict()
            else:
                params['verification_code'] = self.verification_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApartmentHouseModelDTO()
        if 'apartment_house_id' in d:
            o.apartment_house_id = d['apartment_house_id']
        if 'apartment_id' in d:
            o.apartment_id = d['apartment_id']
        if 'check_in_time' in d:
            o.check_in_time = d['check_in_time']
        if 'deposit' in d:
            o.deposit = d['deposit']
        if 'doorplate_number' in d:
            o.doorplate_number = d['doorplate_number']
        if 'external_id' in d:
            o.external_id = d['external_id']
        if 'has_private_bathroom' in d:
            o.has_private_bathroom = d['has_private_bathroom']
        if 'internal_area' in d:
            o.internal_area = d['internal_area']
        if 'name' in d:
            o.name = d['name']
        if 'orientation' in d:
            o.orientation = d['orientation']
        if 'payment_method' in d:
            o.payment_method = d['payment_method']
        if 'rent' in d:
            o.rent = d['rent']
        if 'rent_unit' in d:
            o.rent_unit = d['rent_unit']
        if 'status' in d:
            o.status = d['status']
        if 'verification_code' in d:
            o.verification_code = d['verification_code']
        return o


