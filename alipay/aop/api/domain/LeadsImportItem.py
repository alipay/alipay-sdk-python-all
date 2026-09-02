#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LeadsImportItem(object):

    def __init__(self):
        self._city = None
        self._company_name = None
        self._driver_cert_no = None
        self._driver_name = None
        self._driver_plate = None
        self._driver_tax_no = None
        self._phone_one = None
        self._phone_three = None
        self._phone_two = None
        self._remark = None
        self._source = None

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
    def driver_cert_no(self):
        return self._driver_cert_no

    @driver_cert_no.setter
    def driver_cert_no(self, value):
        self._driver_cert_no = value
    @property
    def driver_name(self):
        return self._driver_name

    @driver_name.setter
    def driver_name(self, value):
        self._driver_name = value
    @property
    def driver_plate(self):
        return self._driver_plate

    @driver_plate.setter
    def driver_plate(self, value):
        self._driver_plate = value
    @property
    def driver_tax_no(self):
        return self._driver_tax_no

    @driver_tax_no.setter
    def driver_tax_no(self, value):
        self._driver_tax_no = value
    @property
    def phone_one(self):
        return self._phone_one

    @phone_one.setter
    def phone_one(self, value):
        self._phone_one = value
    @property
    def phone_three(self):
        return self._phone_three

    @phone_three.setter
    def phone_three(self, value):
        self._phone_three = value
    @property
    def phone_two(self):
        return self._phone_two

    @phone_two.setter
    def phone_two(self, value):
        self._phone_two = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


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
        if self.driver_cert_no:
            if hasattr(self.driver_cert_no, 'to_alipay_dict'):
                params['driver_cert_no'] = self.driver_cert_no.to_alipay_dict()
            else:
                params['driver_cert_no'] = self.driver_cert_no
        if self.driver_name:
            if hasattr(self.driver_name, 'to_alipay_dict'):
                params['driver_name'] = self.driver_name.to_alipay_dict()
            else:
                params['driver_name'] = self.driver_name
        if self.driver_plate:
            if hasattr(self.driver_plate, 'to_alipay_dict'):
                params['driver_plate'] = self.driver_plate.to_alipay_dict()
            else:
                params['driver_plate'] = self.driver_plate
        if self.driver_tax_no:
            if hasattr(self.driver_tax_no, 'to_alipay_dict'):
                params['driver_tax_no'] = self.driver_tax_no.to_alipay_dict()
            else:
                params['driver_tax_no'] = self.driver_tax_no
        if self.phone_one:
            if hasattr(self.phone_one, 'to_alipay_dict'):
                params['phone_one'] = self.phone_one.to_alipay_dict()
            else:
                params['phone_one'] = self.phone_one
        if self.phone_three:
            if hasattr(self.phone_three, 'to_alipay_dict'):
                params['phone_three'] = self.phone_three.to_alipay_dict()
            else:
                params['phone_three'] = self.phone_three
        if self.phone_two:
            if hasattr(self.phone_two, 'to_alipay_dict'):
                params['phone_two'] = self.phone_two.to_alipay_dict()
            else:
                params['phone_two'] = self.phone_two
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LeadsImportItem()
        if 'city' in d:
            o.city = d['city']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'driver_cert_no' in d:
            o.driver_cert_no = d['driver_cert_no']
        if 'driver_name' in d:
            o.driver_name = d['driver_name']
        if 'driver_plate' in d:
            o.driver_plate = d['driver_plate']
        if 'driver_tax_no' in d:
            o.driver_tax_no = d['driver_tax_no']
        if 'phone_one' in d:
            o.phone_one = d['phone_one']
        if 'phone_three' in d:
            o.phone_three = d['phone_three']
        if 'phone_two' in d:
            o.phone_two = d['phone_two']
        if 'remark' in d:
            o.remark = d['remark']
        if 'source' in d:
            o.source = d['source']
        return o


