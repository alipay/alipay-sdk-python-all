#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommercePoiPowerbankUploadModel(object):

    def __init__(self):
        self._address_desc = None
        self._can_borrow = None
        self._can_borrow_cnt = None
        self._contact_number = None
        self._entity_code = None
        self._entity_name = None
        self._ext_properties = None
        self._latitude = None
        self._longitude = None
        self._office_hours_desc = None
        self._upload_time = None

    @property
    def address_desc(self):
        return self._address_desc

    @address_desc.setter
    def address_desc(self, value):
        self._address_desc = value
    @property
    def can_borrow(self):
        return self._can_borrow

    @can_borrow.setter
    def can_borrow(self, value):
        self._can_borrow = value
    @property
    def can_borrow_cnt(self):
        return self._can_borrow_cnt

    @can_borrow_cnt.setter
    def can_borrow_cnt(self, value):
        self._can_borrow_cnt = value
    @property
    def contact_number(self):
        return self._contact_number

    @contact_number.setter
    def contact_number(self, value):
        self._contact_number = value
    @property
    def entity_code(self):
        return self._entity_code

    @entity_code.setter
    def entity_code(self, value):
        self._entity_code = value
    @property
    def entity_name(self):
        return self._entity_name

    @entity_name.setter
    def entity_name(self, value):
        self._entity_name = value
    @property
    def ext_properties(self):
        return self._ext_properties

    @ext_properties.setter
    def ext_properties(self, value):
        self._ext_properties = value
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
    def office_hours_desc(self):
        return self._office_hours_desc

    @office_hours_desc.setter
    def office_hours_desc(self, value):
        self._office_hours_desc = value
    @property
    def upload_time(self):
        return self._upload_time

    @upload_time.setter
    def upload_time(self, value):
        self._upload_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.address_desc:
            if hasattr(self.address_desc, 'to_alipay_dict'):
                params['address_desc'] = self.address_desc.to_alipay_dict()
            else:
                params['address_desc'] = self.address_desc
        if self.can_borrow:
            if hasattr(self.can_borrow, 'to_alipay_dict'):
                params['can_borrow'] = self.can_borrow.to_alipay_dict()
            else:
                params['can_borrow'] = self.can_borrow
        if self.can_borrow_cnt:
            if hasattr(self.can_borrow_cnt, 'to_alipay_dict'):
                params['can_borrow_cnt'] = self.can_borrow_cnt.to_alipay_dict()
            else:
                params['can_borrow_cnt'] = self.can_borrow_cnt
        if self.contact_number:
            if hasattr(self.contact_number, 'to_alipay_dict'):
                params['contact_number'] = self.contact_number.to_alipay_dict()
            else:
                params['contact_number'] = self.contact_number
        if self.entity_code:
            if hasattr(self.entity_code, 'to_alipay_dict'):
                params['entity_code'] = self.entity_code.to_alipay_dict()
            else:
                params['entity_code'] = self.entity_code
        if self.entity_name:
            if hasattr(self.entity_name, 'to_alipay_dict'):
                params['entity_name'] = self.entity_name.to_alipay_dict()
            else:
                params['entity_name'] = self.entity_name
        if self.ext_properties:
            if hasattr(self.ext_properties, 'to_alipay_dict'):
                params['ext_properties'] = self.ext_properties.to_alipay_dict()
            else:
                params['ext_properties'] = self.ext_properties
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
        if self.office_hours_desc:
            if hasattr(self.office_hours_desc, 'to_alipay_dict'):
                params['office_hours_desc'] = self.office_hours_desc.to_alipay_dict()
            else:
                params['office_hours_desc'] = self.office_hours_desc
        if self.upload_time:
            if hasattr(self.upload_time, 'to_alipay_dict'):
                params['upload_time'] = self.upload_time.to_alipay_dict()
            else:
                params['upload_time'] = self.upload_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommercePoiPowerbankUploadModel()
        if 'address_desc' in d:
            o.address_desc = d['address_desc']
        if 'can_borrow' in d:
            o.can_borrow = d['can_borrow']
        if 'can_borrow_cnt' in d:
            o.can_borrow_cnt = d['can_borrow_cnt']
        if 'contact_number' in d:
            o.contact_number = d['contact_number']
        if 'entity_code' in d:
            o.entity_code = d['entity_code']
        if 'entity_name' in d:
            o.entity_name = d['entity_name']
        if 'ext_properties' in d:
            o.ext_properties = d['ext_properties']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'office_hours_desc' in d:
            o.office_hours_desc = d['office_hours_desc']
        if 'upload_time' in d:
            o.upload_time = d['upload_time']
        return o


