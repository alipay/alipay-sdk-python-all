#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EtcVehicleOwnerInfo(object):

    def __init__(self):
        self._vi_owner_address = None
        self._vi_owner_cert_end_date = None
        self._vi_owner_cert_no = None
        self._vi_owner_cert_start_date = None
        self._vi_owner_cert_type = None
        self._vi_owner_city = None
        self._vi_owner_contact = None
        self._vi_owner_district = None
        self._vi_owner_name = None
        self._vi_owner_province = None
        self._vi_owner_type = None

    @property
    def vi_owner_address(self):
        return self._vi_owner_address

    @vi_owner_address.setter
    def vi_owner_address(self, value):
        self._vi_owner_address = value
    @property
    def vi_owner_cert_end_date(self):
        return self._vi_owner_cert_end_date

    @vi_owner_cert_end_date.setter
    def vi_owner_cert_end_date(self, value):
        self._vi_owner_cert_end_date = value
    @property
    def vi_owner_cert_no(self):
        return self._vi_owner_cert_no

    @vi_owner_cert_no.setter
    def vi_owner_cert_no(self, value):
        self._vi_owner_cert_no = value
    @property
    def vi_owner_cert_start_date(self):
        return self._vi_owner_cert_start_date

    @vi_owner_cert_start_date.setter
    def vi_owner_cert_start_date(self, value):
        self._vi_owner_cert_start_date = value
    @property
    def vi_owner_cert_type(self):
        return self._vi_owner_cert_type

    @vi_owner_cert_type.setter
    def vi_owner_cert_type(self, value):
        self._vi_owner_cert_type = value
    @property
    def vi_owner_city(self):
        return self._vi_owner_city

    @vi_owner_city.setter
    def vi_owner_city(self, value):
        self._vi_owner_city = value
    @property
    def vi_owner_contact(self):
        return self._vi_owner_contact

    @vi_owner_contact.setter
    def vi_owner_contact(self, value):
        self._vi_owner_contact = value
    @property
    def vi_owner_district(self):
        return self._vi_owner_district

    @vi_owner_district.setter
    def vi_owner_district(self, value):
        self._vi_owner_district = value
    @property
    def vi_owner_name(self):
        return self._vi_owner_name

    @vi_owner_name.setter
    def vi_owner_name(self, value):
        self._vi_owner_name = value
    @property
    def vi_owner_province(self):
        return self._vi_owner_province

    @vi_owner_province.setter
    def vi_owner_province(self, value):
        self._vi_owner_province = value
    @property
    def vi_owner_type(self):
        return self._vi_owner_type

    @vi_owner_type.setter
    def vi_owner_type(self, value):
        self._vi_owner_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.vi_owner_address:
            if hasattr(self.vi_owner_address, 'to_alipay_dict'):
                params['vi_owner_address'] = self.vi_owner_address.to_alipay_dict()
            else:
                params['vi_owner_address'] = self.vi_owner_address
        if self.vi_owner_cert_end_date:
            if hasattr(self.vi_owner_cert_end_date, 'to_alipay_dict'):
                params['vi_owner_cert_end_date'] = self.vi_owner_cert_end_date.to_alipay_dict()
            else:
                params['vi_owner_cert_end_date'] = self.vi_owner_cert_end_date
        if self.vi_owner_cert_no:
            if hasattr(self.vi_owner_cert_no, 'to_alipay_dict'):
                params['vi_owner_cert_no'] = self.vi_owner_cert_no.to_alipay_dict()
            else:
                params['vi_owner_cert_no'] = self.vi_owner_cert_no
        if self.vi_owner_cert_start_date:
            if hasattr(self.vi_owner_cert_start_date, 'to_alipay_dict'):
                params['vi_owner_cert_start_date'] = self.vi_owner_cert_start_date.to_alipay_dict()
            else:
                params['vi_owner_cert_start_date'] = self.vi_owner_cert_start_date
        if self.vi_owner_cert_type:
            if hasattr(self.vi_owner_cert_type, 'to_alipay_dict'):
                params['vi_owner_cert_type'] = self.vi_owner_cert_type.to_alipay_dict()
            else:
                params['vi_owner_cert_type'] = self.vi_owner_cert_type
        if self.vi_owner_city:
            if hasattr(self.vi_owner_city, 'to_alipay_dict'):
                params['vi_owner_city'] = self.vi_owner_city.to_alipay_dict()
            else:
                params['vi_owner_city'] = self.vi_owner_city
        if self.vi_owner_contact:
            if hasattr(self.vi_owner_contact, 'to_alipay_dict'):
                params['vi_owner_contact'] = self.vi_owner_contact.to_alipay_dict()
            else:
                params['vi_owner_contact'] = self.vi_owner_contact
        if self.vi_owner_district:
            if hasattr(self.vi_owner_district, 'to_alipay_dict'):
                params['vi_owner_district'] = self.vi_owner_district.to_alipay_dict()
            else:
                params['vi_owner_district'] = self.vi_owner_district
        if self.vi_owner_name:
            if hasattr(self.vi_owner_name, 'to_alipay_dict'):
                params['vi_owner_name'] = self.vi_owner_name.to_alipay_dict()
            else:
                params['vi_owner_name'] = self.vi_owner_name
        if self.vi_owner_province:
            if hasattr(self.vi_owner_province, 'to_alipay_dict'):
                params['vi_owner_province'] = self.vi_owner_province.to_alipay_dict()
            else:
                params['vi_owner_province'] = self.vi_owner_province
        if self.vi_owner_type:
            if hasattr(self.vi_owner_type, 'to_alipay_dict'):
                params['vi_owner_type'] = self.vi_owner_type.to_alipay_dict()
            else:
                params['vi_owner_type'] = self.vi_owner_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EtcVehicleOwnerInfo()
        if 'vi_owner_address' in d:
            o.vi_owner_address = d['vi_owner_address']
        if 'vi_owner_cert_end_date' in d:
            o.vi_owner_cert_end_date = d['vi_owner_cert_end_date']
        if 'vi_owner_cert_no' in d:
            o.vi_owner_cert_no = d['vi_owner_cert_no']
        if 'vi_owner_cert_start_date' in d:
            o.vi_owner_cert_start_date = d['vi_owner_cert_start_date']
        if 'vi_owner_cert_type' in d:
            o.vi_owner_cert_type = d['vi_owner_cert_type']
        if 'vi_owner_city' in d:
            o.vi_owner_city = d['vi_owner_city']
        if 'vi_owner_contact' in d:
            o.vi_owner_contact = d['vi_owner_contact']
        if 'vi_owner_district' in d:
            o.vi_owner_district = d['vi_owner_district']
        if 'vi_owner_name' in d:
            o.vi_owner_name = d['vi_owner_name']
        if 'vi_owner_province' in d:
            o.vi_owner_province = d['vi_owner_province']
        if 'vi_owner_type' in d:
            o.vi_owner_type = d['vi_owner_type']
        return o


