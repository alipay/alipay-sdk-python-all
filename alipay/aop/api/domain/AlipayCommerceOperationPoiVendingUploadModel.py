#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusinessHoursDesc import BusinessHoursDesc


class AlipayCommerceOperationPoiVendingUploadModel(object):

    def __init__(self):
        self._address_desc = None
        self._business_hours_desc = None
        self._category_code = None
        self._contact_number = None
        self._enabled = None
        self._entity_code = None
        self._entity_name = None
        self._ext_infos = None
        self._latitude = None
        self._longitude = None
        self._upload_time = None

    @property
    def address_desc(self):
        return self._address_desc

    @address_desc.setter
    def address_desc(self, value):
        self._address_desc = value
    @property
    def business_hours_desc(self):
        return self._business_hours_desc

    @business_hours_desc.setter
    def business_hours_desc(self, value):
        if isinstance(value, list):
            self._business_hours_desc = list()
            for i in value:
                if isinstance(i, BusinessHoursDesc):
                    self._business_hours_desc.append(i)
                else:
                    self._business_hours_desc.append(BusinessHoursDesc.from_alipay_dict(i))
    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def contact_number(self):
        return self._contact_number

    @contact_number.setter
    def contact_number(self, value):
        self._contact_number = value
    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = value
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
    def ext_infos(self):
        return self._ext_infos

    @ext_infos.setter
    def ext_infos(self, value):
        self._ext_infos = value
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
        if self.business_hours_desc:
            if isinstance(self.business_hours_desc, list):
                for i in range(0, len(self.business_hours_desc)):
                    element = self.business_hours_desc[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.business_hours_desc[i] = element.to_alipay_dict()
            if hasattr(self.business_hours_desc, 'to_alipay_dict'):
                params['business_hours_desc'] = self.business_hours_desc.to_alipay_dict()
            else:
                params['business_hours_desc'] = self.business_hours_desc
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.contact_number:
            if hasattr(self.contact_number, 'to_alipay_dict'):
                params['contact_number'] = self.contact_number.to_alipay_dict()
            else:
                params['contact_number'] = self.contact_number
        if self.enabled:
            if hasattr(self.enabled, 'to_alipay_dict'):
                params['enabled'] = self.enabled.to_alipay_dict()
            else:
                params['enabled'] = self.enabled
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
        if self.ext_infos:
            if hasattr(self.ext_infos, 'to_alipay_dict'):
                params['ext_infos'] = self.ext_infos.to_alipay_dict()
            else:
                params['ext_infos'] = self.ext_infos
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
        o = AlipayCommerceOperationPoiVendingUploadModel()
        if 'address_desc' in d:
            o.address_desc = d['address_desc']
        if 'business_hours_desc' in d:
            o.business_hours_desc = d['business_hours_desc']
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'contact_number' in d:
            o.contact_number = d['contact_number']
        if 'enabled' in d:
            o.enabled = d['enabled']
        if 'entity_code' in d:
            o.entity_code = d['entity_code']
        if 'entity_name' in d:
            o.entity_name = d['entity_name']
        if 'ext_infos' in d:
            o.ext_infos = d['ext_infos']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'upload_time' in d:
            o.upload_time = d['upload_time']
        return o


