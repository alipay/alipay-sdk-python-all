#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CarfinRegistrationInfo(object):

    def __init__(self):
        self._acquisition_method = None
        self._barcode = None
        self._engine_no = None
        self._fuel_type = None
        self._issue_date = None
        self._last_renewal_date = None
        self._last_replacement_date = None
        self._last_transfer_date = None
        self._manufacture_date = None
        self._mortgage_release_date = None
        self._mortgage_status = None
        self._owner = None
        self._owner_identification_number = None
        self._registration_authority = None
        self._registration_date = None
        self._transfer_count = None
        self._use_type = None
        self._vehicle_brand = None
        self._vehicle_license = None
        self._vehicle_model = None
        self._vehicle_series = None
        self._vehicle_type = None
        self._vehicle_vin = None

    @property
    def acquisition_method(self):
        return self._acquisition_method

    @acquisition_method.setter
    def acquisition_method(self, value):
        self._acquisition_method = value
    @property
    def barcode(self):
        return self._barcode

    @barcode.setter
    def barcode(self, value):
        self._barcode = value
    @property
    def engine_no(self):
        return self._engine_no

    @engine_no.setter
    def engine_no(self, value):
        self._engine_no = value
    @property
    def fuel_type(self):
        return self._fuel_type

    @fuel_type.setter
    def fuel_type(self, value):
        self._fuel_type = value
    @property
    def issue_date(self):
        return self._issue_date

    @issue_date.setter
    def issue_date(self, value):
        self._issue_date = value
    @property
    def last_renewal_date(self):
        return self._last_renewal_date

    @last_renewal_date.setter
    def last_renewal_date(self, value):
        self._last_renewal_date = value
    @property
    def last_replacement_date(self):
        return self._last_replacement_date

    @last_replacement_date.setter
    def last_replacement_date(self, value):
        self._last_replacement_date = value
    @property
    def last_transfer_date(self):
        return self._last_transfer_date

    @last_transfer_date.setter
    def last_transfer_date(self, value):
        self._last_transfer_date = value
    @property
    def manufacture_date(self):
        return self._manufacture_date

    @manufacture_date.setter
    def manufacture_date(self, value):
        self._manufacture_date = value
    @property
    def mortgage_release_date(self):
        return self._mortgage_release_date

    @mortgage_release_date.setter
    def mortgage_release_date(self, value):
        self._mortgage_release_date = value
    @property
    def mortgage_status(self):
        return self._mortgage_status

    @mortgage_status.setter
    def mortgage_status(self, value):
        self._mortgage_status = value
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value
    @property
    def owner_identification_number(self):
        return self._owner_identification_number

    @owner_identification_number.setter
    def owner_identification_number(self, value):
        self._owner_identification_number = value
    @property
    def registration_authority(self):
        return self._registration_authority

    @registration_authority.setter
    def registration_authority(self, value):
        self._registration_authority = value
    @property
    def registration_date(self):
        return self._registration_date

    @registration_date.setter
    def registration_date(self, value):
        self._registration_date = value
    @property
    def transfer_count(self):
        return self._transfer_count

    @transfer_count.setter
    def transfer_count(self, value):
        self._transfer_count = value
    @property
    def use_type(self):
        return self._use_type

    @use_type.setter
    def use_type(self, value):
        self._use_type = value
    @property
    def vehicle_brand(self):
        return self._vehicle_brand

    @vehicle_brand.setter
    def vehicle_brand(self, value):
        self._vehicle_brand = value
    @property
    def vehicle_license(self):
        return self._vehicle_license

    @vehicle_license.setter
    def vehicle_license(self, value):
        self._vehicle_license = value
    @property
    def vehicle_model(self):
        return self._vehicle_model

    @vehicle_model.setter
    def vehicle_model(self, value):
        self._vehicle_model = value
    @property
    def vehicle_series(self):
        return self._vehicle_series

    @vehicle_series.setter
    def vehicle_series(self, value):
        self._vehicle_series = value
    @property
    def vehicle_type(self):
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, value):
        self._vehicle_type = value
    @property
    def vehicle_vin(self):
        return self._vehicle_vin

    @vehicle_vin.setter
    def vehicle_vin(self, value):
        self._vehicle_vin = value


    def to_alipay_dict(self):
        params = dict()
        if self.acquisition_method:
            if hasattr(self.acquisition_method, 'to_alipay_dict'):
                params['acquisition_method'] = self.acquisition_method.to_alipay_dict()
            else:
                params['acquisition_method'] = self.acquisition_method
        if self.barcode:
            if hasattr(self.barcode, 'to_alipay_dict'):
                params['barcode'] = self.barcode.to_alipay_dict()
            else:
                params['barcode'] = self.barcode
        if self.engine_no:
            if hasattr(self.engine_no, 'to_alipay_dict'):
                params['engine_no'] = self.engine_no.to_alipay_dict()
            else:
                params['engine_no'] = self.engine_no
        if self.fuel_type:
            if hasattr(self.fuel_type, 'to_alipay_dict'):
                params['fuel_type'] = self.fuel_type.to_alipay_dict()
            else:
                params['fuel_type'] = self.fuel_type
        if self.issue_date:
            if hasattr(self.issue_date, 'to_alipay_dict'):
                params['issue_date'] = self.issue_date.to_alipay_dict()
            else:
                params['issue_date'] = self.issue_date
        if self.last_renewal_date:
            if hasattr(self.last_renewal_date, 'to_alipay_dict'):
                params['last_renewal_date'] = self.last_renewal_date.to_alipay_dict()
            else:
                params['last_renewal_date'] = self.last_renewal_date
        if self.last_replacement_date:
            if hasattr(self.last_replacement_date, 'to_alipay_dict'):
                params['last_replacement_date'] = self.last_replacement_date.to_alipay_dict()
            else:
                params['last_replacement_date'] = self.last_replacement_date
        if self.last_transfer_date:
            if hasattr(self.last_transfer_date, 'to_alipay_dict'):
                params['last_transfer_date'] = self.last_transfer_date.to_alipay_dict()
            else:
                params['last_transfer_date'] = self.last_transfer_date
        if self.manufacture_date:
            if hasattr(self.manufacture_date, 'to_alipay_dict'):
                params['manufacture_date'] = self.manufacture_date.to_alipay_dict()
            else:
                params['manufacture_date'] = self.manufacture_date
        if self.mortgage_release_date:
            if hasattr(self.mortgage_release_date, 'to_alipay_dict'):
                params['mortgage_release_date'] = self.mortgage_release_date.to_alipay_dict()
            else:
                params['mortgage_release_date'] = self.mortgage_release_date
        if self.mortgage_status:
            if hasattr(self.mortgage_status, 'to_alipay_dict'):
                params['mortgage_status'] = self.mortgage_status.to_alipay_dict()
            else:
                params['mortgage_status'] = self.mortgage_status
        if self.owner:
            if hasattr(self.owner, 'to_alipay_dict'):
                params['owner'] = self.owner.to_alipay_dict()
            else:
                params['owner'] = self.owner
        if self.owner_identification_number:
            if hasattr(self.owner_identification_number, 'to_alipay_dict'):
                params['owner_identification_number'] = self.owner_identification_number.to_alipay_dict()
            else:
                params['owner_identification_number'] = self.owner_identification_number
        if self.registration_authority:
            if hasattr(self.registration_authority, 'to_alipay_dict'):
                params['registration_authority'] = self.registration_authority.to_alipay_dict()
            else:
                params['registration_authority'] = self.registration_authority
        if self.registration_date:
            if hasattr(self.registration_date, 'to_alipay_dict'):
                params['registration_date'] = self.registration_date.to_alipay_dict()
            else:
                params['registration_date'] = self.registration_date
        if self.transfer_count:
            if hasattr(self.transfer_count, 'to_alipay_dict'):
                params['transfer_count'] = self.transfer_count.to_alipay_dict()
            else:
                params['transfer_count'] = self.transfer_count
        if self.use_type:
            if hasattr(self.use_type, 'to_alipay_dict'):
                params['use_type'] = self.use_type.to_alipay_dict()
            else:
                params['use_type'] = self.use_type
        if self.vehicle_brand:
            if hasattr(self.vehicle_brand, 'to_alipay_dict'):
                params['vehicle_brand'] = self.vehicle_brand.to_alipay_dict()
            else:
                params['vehicle_brand'] = self.vehicle_brand
        if self.vehicle_license:
            if hasattr(self.vehicle_license, 'to_alipay_dict'):
                params['vehicle_license'] = self.vehicle_license.to_alipay_dict()
            else:
                params['vehicle_license'] = self.vehicle_license
        if self.vehicle_model:
            if hasattr(self.vehicle_model, 'to_alipay_dict'):
                params['vehicle_model'] = self.vehicle_model.to_alipay_dict()
            else:
                params['vehicle_model'] = self.vehicle_model
        if self.vehicle_series:
            if hasattr(self.vehicle_series, 'to_alipay_dict'):
                params['vehicle_series'] = self.vehicle_series.to_alipay_dict()
            else:
                params['vehicle_series'] = self.vehicle_series
        if self.vehicle_type:
            if hasattr(self.vehicle_type, 'to_alipay_dict'):
                params['vehicle_type'] = self.vehicle_type.to_alipay_dict()
            else:
                params['vehicle_type'] = self.vehicle_type
        if self.vehicle_vin:
            if hasattr(self.vehicle_vin, 'to_alipay_dict'):
                params['vehicle_vin'] = self.vehicle_vin.to_alipay_dict()
            else:
                params['vehicle_vin'] = self.vehicle_vin
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarfinRegistrationInfo()
        if 'acquisition_method' in d:
            o.acquisition_method = d['acquisition_method']
        if 'barcode' in d:
            o.barcode = d['barcode']
        if 'engine_no' in d:
            o.engine_no = d['engine_no']
        if 'fuel_type' in d:
            o.fuel_type = d['fuel_type']
        if 'issue_date' in d:
            o.issue_date = d['issue_date']
        if 'last_renewal_date' in d:
            o.last_renewal_date = d['last_renewal_date']
        if 'last_replacement_date' in d:
            o.last_replacement_date = d['last_replacement_date']
        if 'last_transfer_date' in d:
            o.last_transfer_date = d['last_transfer_date']
        if 'manufacture_date' in d:
            o.manufacture_date = d['manufacture_date']
        if 'mortgage_release_date' in d:
            o.mortgage_release_date = d['mortgage_release_date']
        if 'mortgage_status' in d:
            o.mortgage_status = d['mortgage_status']
        if 'owner' in d:
            o.owner = d['owner']
        if 'owner_identification_number' in d:
            o.owner_identification_number = d['owner_identification_number']
        if 'registration_authority' in d:
            o.registration_authority = d['registration_authority']
        if 'registration_date' in d:
            o.registration_date = d['registration_date']
        if 'transfer_count' in d:
            o.transfer_count = d['transfer_count']
        if 'use_type' in d:
            o.use_type = d['use_type']
        if 'vehicle_brand' in d:
            o.vehicle_brand = d['vehicle_brand']
        if 'vehicle_license' in d:
            o.vehicle_license = d['vehicle_license']
        if 'vehicle_model' in d:
            o.vehicle_model = d['vehicle_model']
        if 'vehicle_series' in d:
            o.vehicle_series = d['vehicle_series']
        if 'vehicle_type' in d:
            o.vehicle_type = d['vehicle_type']
        if 'vehicle_vin' in d:
            o.vehicle_vin = d['vehicle_vin']
        return o


