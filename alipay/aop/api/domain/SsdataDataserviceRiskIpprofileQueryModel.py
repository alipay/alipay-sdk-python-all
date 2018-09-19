#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SsdataDataserviceRiskIpprofileQueryModel(object):

    def __init__(self):
        self._cert_no = None
        self._city = None
        self._district = None
        self._ip_address = None
        self._partner_id = None
        self._phone = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def district(self):
        return self._district

    @district.setter
    def district(self, value):
        self._district = value
    @property
    def ip_address(self):
        return self._ip_address

    @ip_address.setter
    def ip_address(self, value):
        self._ip_address = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.district:
            if hasattr(self.district, 'to_alipay_dict'):
                params['district'] = self.district.to_alipay_dict()
            else:
                params['district'] = self.district
        if self.ip_address:
            if hasattr(self.ip_address, 'to_alipay_dict'):
                params['ip_address'] = self.ip_address.to_alipay_dict()
            else:
                params['ip_address'] = self.ip_address
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SsdataDataserviceRiskIpprofileQueryModel()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'city' in d:
            o.city = d['city']
        if 'district' in d:
            o.district = d['district']
        if 'ip_address' in d:
            o.ip_address = d['ip_address']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'phone' in d:
            o.phone = d['phone']
        return o


