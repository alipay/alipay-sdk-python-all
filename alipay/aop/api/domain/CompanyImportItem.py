#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CompanyImportItem(object):

    def __init__(self):
        self._city = None
        self._company_name = None
        self._company_tax_no = None
        self._contact_address = None
        self._contact_email = None
        self._contact_name = None
        self._contact_phone = None
        self._source = None
        self._surveyed_driver_count = None
        self._surveyed_vehicle_count = None

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def company_tax_no(self):
        return self._company_tax_no

    @company_tax_no.setter
    def company_tax_no(self, value):
        self._company_tax_no = value
    @property
    def contact_address(self):
        return self._contact_address

    @contact_address.setter
    def contact_address(self, value):
        self._contact_address = value
    @property
    def contact_email(self):
        return self._contact_email

    @contact_email.setter
    def contact_email(self, value):
        self._contact_email = value
    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def contact_phone(self):
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, value):
        self._contact_phone = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def surveyed_driver_count(self):
        return self._surveyed_driver_count

    @surveyed_driver_count.setter
    def surveyed_driver_count(self, value):
        self._surveyed_driver_count = value
    @property
    def surveyed_vehicle_count(self):
        return self._surveyed_vehicle_count

    @surveyed_vehicle_count.setter
    def surveyed_vehicle_count(self, value):
        self._surveyed_vehicle_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.company_tax_no:
            if hasattr(self.company_tax_no, 'to_alipay_dict'):
                params['company_tax_no'] = self.company_tax_no.to_alipay_dict()
            else:
                params['company_tax_no'] = self.company_tax_no
        if self.contact_address:
            if hasattr(self.contact_address, 'to_alipay_dict'):
                params['contact_address'] = self.contact_address.to_alipay_dict()
            else:
                params['contact_address'] = self.contact_address
        if self.contact_email:
            if hasattr(self.contact_email, 'to_alipay_dict'):
                params['contact_email'] = self.contact_email.to_alipay_dict()
            else:
                params['contact_email'] = self.contact_email
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = self.contact_name.to_alipay_dict()
            else:
                params['contact_name'] = self.contact_name
        if self.contact_phone:
            if hasattr(self.contact_phone, 'to_alipay_dict'):
                params['contact_phone'] = self.contact_phone.to_alipay_dict()
            else:
                params['contact_phone'] = self.contact_phone
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.surveyed_driver_count:
            if hasattr(self.surveyed_driver_count, 'to_alipay_dict'):
                params['surveyed_driver_count'] = self.surveyed_driver_count.to_alipay_dict()
            else:
                params['surveyed_driver_count'] = self.surveyed_driver_count
        if self.surveyed_vehicle_count:
            if hasattr(self.surveyed_vehicle_count, 'to_alipay_dict'):
                params['surveyed_vehicle_count'] = self.surveyed_vehicle_count.to_alipay_dict()
            else:
                params['surveyed_vehicle_count'] = self.surveyed_vehicle_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CompanyImportItem()
        if 'city' in d:
            o.city = d['city']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'company_tax_no' in d:
            o.company_tax_no = d['company_tax_no']
        if 'contact_address' in d:
            o.contact_address = d['contact_address']
        if 'contact_email' in d:
            o.contact_email = d['contact_email']
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'contact_phone' in d:
            o.contact_phone = d['contact_phone']
        if 'source' in d:
            o.source = d['source']
        if 'surveyed_driver_count' in d:
            o.surveyed_driver_count = d['surveyed_driver_count']
        if 'surveyed_vehicle_count' in d:
            o.surveyed_vehicle_count = d['surveyed_vehicle_count']
        return o


