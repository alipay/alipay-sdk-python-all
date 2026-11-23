#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TrustedAddrInfo(object):

    def __init__(self):
        self._addr_city = None
        self._addr_district = None
        self._addr_province = None
        self._credit_code = None
        self._ent_name = None
        self._ent_status = None
        self._ent_type = None
        self._ep_addr_confidence = None
        self._ep_address = None
        self._es_date = None
        self._fr_name = None
        self._latitude = None
        self._longitude = None
        self._oprt_scope = None
        self._reg_cap = None
        self._reg_no = None
        self._reg_org = None

    @property
    def addr_city(self):
        return self._addr_city

    @addr_city.setter
    def addr_city(self, value):
        self._addr_city = value
    @property
    def addr_district(self):
        return self._addr_district

    @addr_district.setter
    def addr_district(self, value):
        self._addr_district = value
    @property
    def addr_province(self):
        return self._addr_province

    @addr_province.setter
    def addr_province(self, value):
        self._addr_province = value
    @property
    def credit_code(self):
        return self._credit_code

    @credit_code.setter
    def credit_code(self, value):
        self._credit_code = value
    @property
    def ent_name(self):
        return self._ent_name

    @ent_name.setter
    def ent_name(self, value):
        self._ent_name = value
    @property
    def ent_status(self):
        return self._ent_status

    @ent_status.setter
    def ent_status(self, value):
        self._ent_status = value
    @property
    def ent_type(self):
        return self._ent_type

    @ent_type.setter
    def ent_type(self, value):
        self._ent_type = value
    @property
    def ep_addr_confidence(self):
        return self._ep_addr_confidence

    @ep_addr_confidence.setter
    def ep_addr_confidence(self, value):
        self._ep_addr_confidence = value
    @property
    def ep_address(self):
        return self._ep_address

    @ep_address.setter
    def ep_address(self, value):
        self._ep_address = value
    @property
    def es_date(self):
        return self._es_date

    @es_date.setter
    def es_date(self, value):
        self._es_date = value
    @property
    def fr_name(self):
        return self._fr_name

    @fr_name.setter
    def fr_name(self, value):
        self._fr_name = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def oprt_scope(self):
        return self._oprt_scope

    @oprt_scope.setter
    def oprt_scope(self, value):
        self._oprt_scope = value
    @property
    def reg_cap(self):
        return self._reg_cap

    @reg_cap.setter
    def reg_cap(self, value):
        self._reg_cap = value
    @property
    def reg_no(self):
        return self._reg_no

    @reg_no.setter
    def reg_no(self, value):
        self._reg_no = value
    @property
    def reg_org(self):
        return self._reg_org

    @reg_org.setter
    def reg_org(self, value):
        self._reg_org = value


    def to_alipay_dict(self):
        params = dict()
        if self.addr_city:
            if hasattr(self.addr_city, 'to_alipay_dict'):
                params['addr_city'] = self.addr_city.to_alipay_dict()
            else:
                params['addr_city'] = self.addr_city
        if self.addr_district:
            if hasattr(self.addr_district, 'to_alipay_dict'):
                params['addr_district'] = self.addr_district.to_alipay_dict()
            else:
                params['addr_district'] = self.addr_district
        if self.addr_province:
            if hasattr(self.addr_province, 'to_alipay_dict'):
                params['addr_province'] = self.addr_province.to_alipay_dict()
            else:
                params['addr_province'] = self.addr_province
        if self.credit_code:
            if hasattr(self.credit_code, 'to_alipay_dict'):
                params['credit_code'] = self.credit_code.to_alipay_dict()
            else:
                params['credit_code'] = self.credit_code
        if self.ent_name:
            if hasattr(self.ent_name, 'to_alipay_dict'):
                params['ent_name'] = self.ent_name.to_alipay_dict()
            else:
                params['ent_name'] = self.ent_name
        if self.ent_status:
            if hasattr(self.ent_status, 'to_alipay_dict'):
                params['ent_status'] = self.ent_status.to_alipay_dict()
            else:
                params['ent_status'] = self.ent_status
        if self.ent_type:
            if hasattr(self.ent_type, 'to_alipay_dict'):
                params['ent_type'] = self.ent_type.to_alipay_dict()
            else:
                params['ent_type'] = self.ent_type
        if self.ep_addr_confidence:
            if hasattr(self.ep_addr_confidence, 'to_alipay_dict'):
                params['ep_addr_confidence'] = self.ep_addr_confidence.to_alipay_dict()
            else:
                params['ep_addr_confidence'] = self.ep_addr_confidence
        if self.ep_address:
            if hasattr(self.ep_address, 'to_alipay_dict'):
                params['ep_address'] = self.ep_address.to_alipay_dict()
            else:
                params['ep_address'] = self.ep_address
        if self.es_date:
            if hasattr(self.es_date, 'to_alipay_dict'):
                params['es_date'] = self.es_date.to_alipay_dict()
            else:
                params['es_date'] = self.es_date
        if self.fr_name:
            if hasattr(self.fr_name, 'to_alipay_dict'):
                params['fr_name'] = self.fr_name.to_alipay_dict()
            else:
                params['fr_name'] = self.fr_name
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.oprt_scope:
            if hasattr(self.oprt_scope, 'to_alipay_dict'):
                params['oprt_scope'] = self.oprt_scope.to_alipay_dict()
            else:
                params['oprt_scope'] = self.oprt_scope
        if self.reg_cap:
            if hasattr(self.reg_cap, 'to_alipay_dict'):
                params['reg_cap'] = self.reg_cap.to_alipay_dict()
            else:
                params['reg_cap'] = self.reg_cap
        if self.reg_no:
            if hasattr(self.reg_no, 'to_alipay_dict'):
                params['reg_no'] = self.reg_no.to_alipay_dict()
            else:
                params['reg_no'] = self.reg_no
        if self.reg_org:
            if hasattr(self.reg_org, 'to_alipay_dict'):
                params['reg_org'] = self.reg_org.to_alipay_dict()
            else:
                params['reg_org'] = self.reg_org
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TrustedAddrInfo()
        if 'addr_city' in d:
            o.addr_city = d['addr_city']
        if 'addr_district' in d:
            o.addr_district = d['addr_district']
        if 'addr_province' in d:
            o.addr_province = d['addr_province']
        if 'credit_code' in d:
            o.credit_code = d['credit_code']
        if 'ent_name' in d:
            o.ent_name = d['ent_name']
        if 'ent_status' in d:
            o.ent_status = d['ent_status']
        if 'ent_type' in d:
            o.ent_type = d['ent_type']
        if 'ep_addr_confidence' in d:
            o.ep_addr_confidence = d['ep_addr_confidence']
        if 'ep_address' in d:
            o.ep_address = d['ep_address']
        if 'es_date' in d:
            o.es_date = d['es_date']
        if 'fr_name' in d:
            o.fr_name = d['fr_name']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'oprt_scope' in d:
            o.oprt_scope = d['oprt_scope']
        if 'reg_cap' in d:
            o.reg_cap = d['reg_cap']
        if 'reg_no' in d:
            o.reg_no = d['reg_no']
        if 'reg_org' in d:
            o.reg_org = d['reg_org']
        return o


