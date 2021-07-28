#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ServiceAddressSimpleVO import ServiceAddressSimpleVO
from alipay.aop.api.domain.ServiceAttributeSimpleVO import ServiceAttributeSimpleVO
from alipay.aop.api.domain.ServiceRegionSimpleVO import ServiceRegionSimpleVO
from alipay.aop.api.domain.ServiceContactSimpleVO import ServiceContactSimpleVO


class AlipayOpenAppServiceSyncModel(object):

    def __init__(self):
        self._address = None
        self._attributes = None
        self._biz_id = None
        self._category_id = None
        self._date_timestamp = None
        self._granularity_type = None
        self._logo = None
        self._region = None
        self._service_app_id = None
        self._service_contact = None
        self._service_name = None
        self._simple_desc = None
        self._spec_code = None
        self._url = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if isinstance(value, list):
            self._address = list()
            for i in value:
                if isinstance(i, ServiceAddressSimpleVO):
                    self._address.append(i)
                else:
                    self._address.append(ServiceAddressSimpleVO.from_alipay_dict(i))
    @property
    def attributes(self):
        return self._attributes

    @attributes.setter
    def attributes(self, value):
        if isinstance(value, ServiceAttributeSimpleVO):
            self._attributes = value
        else:
            self._attributes = ServiceAttributeSimpleVO.from_alipay_dict(value)
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def date_timestamp(self):
        return self._date_timestamp

    @date_timestamp.setter
    def date_timestamp(self, value):
        self._date_timestamp = value
    @property
    def granularity_type(self):
        return self._granularity_type

    @granularity_type.setter
    def granularity_type(self, value):
        self._granularity_type = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        if isinstance(value, list):
            self._region = list()
            for i in value:
                if isinstance(i, ServiceRegionSimpleVO):
                    self._region.append(i)
                else:
                    self._region.append(ServiceRegionSimpleVO.from_alipay_dict(i))
    @property
    def service_app_id(self):
        return self._service_app_id

    @service_app_id.setter
    def service_app_id(self, value):
        self._service_app_id = value
    @property
    def service_contact(self):
        return self._service_contact

    @service_contact.setter
    def service_contact(self, value):
        if isinstance(value, list):
            self._service_contact = list()
            for i in value:
                if isinstance(i, ServiceContactSimpleVO):
                    self._service_contact.append(i)
                else:
                    self._service_contact.append(ServiceContactSimpleVO.from_alipay_dict(i))
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def simple_desc(self):
        return self._simple_desc

    @simple_desc.setter
    def simple_desc(self, value):
        self._simple_desc = value
    @property
    def spec_code(self):
        return self._spec_code

    @spec_code.setter
    def spec_code(self, value):
        self._spec_code = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if isinstance(self.address, list):
                for i in range(0, len(self.address)):
                    element = self.address[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.address[i] = element.to_alipay_dict()
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.attributes:
            if hasattr(self.attributes, 'to_alipay_dict'):
                params['attributes'] = self.attributes.to_alipay_dict()
            else:
                params['attributes'] = self.attributes
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.date_timestamp:
            if hasattr(self.date_timestamp, 'to_alipay_dict'):
                params['date_timestamp'] = self.date_timestamp.to_alipay_dict()
            else:
                params['date_timestamp'] = self.date_timestamp
        if self.granularity_type:
            if hasattr(self.granularity_type, 'to_alipay_dict'):
                params['granularity_type'] = self.granularity_type.to_alipay_dict()
            else:
                params['granularity_type'] = self.granularity_type
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.region:
            if isinstance(self.region, list):
                for i in range(0, len(self.region)):
                    element = self.region[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.region[i] = element.to_alipay_dict()
            if hasattr(self.region, 'to_alipay_dict'):
                params['region'] = self.region.to_alipay_dict()
            else:
                params['region'] = self.region
        if self.service_app_id:
            if hasattr(self.service_app_id, 'to_alipay_dict'):
                params['service_app_id'] = self.service_app_id.to_alipay_dict()
            else:
                params['service_app_id'] = self.service_app_id
        if self.service_contact:
            if isinstance(self.service_contact, list):
                for i in range(0, len(self.service_contact)):
                    element = self.service_contact[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_contact[i] = element.to_alipay_dict()
            if hasattr(self.service_contact, 'to_alipay_dict'):
                params['service_contact'] = self.service_contact.to_alipay_dict()
            else:
                params['service_contact'] = self.service_contact
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.simple_desc:
            if hasattr(self.simple_desc, 'to_alipay_dict'):
                params['simple_desc'] = self.simple_desc.to_alipay_dict()
            else:
                params['simple_desc'] = self.simple_desc
        if self.spec_code:
            if hasattr(self.spec_code, 'to_alipay_dict'):
                params['spec_code'] = self.spec_code.to_alipay_dict()
            else:
                params['spec_code'] = self.spec_code
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppServiceSyncModel()
        if 'address' in d:
            o.address = d['address']
        if 'attributes' in d:
            o.attributes = d['attributes']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'date_timestamp' in d:
            o.date_timestamp = d['date_timestamp']
        if 'granularity_type' in d:
            o.granularity_type = d['granularity_type']
        if 'logo' in d:
            o.logo = d['logo']
        if 'region' in d:
            o.region = d['region']
        if 'service_app_id' in d:
            o.service_app_id = d['service_app_id']
        if 'service_contact' in d:
            o.service_contact = d['service_contact']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'simple_desc' in d:
            o.simple_desc = d['simple_desc']
        if 'spec_code' in d:
            o.spec_code = d['spec_code']
        if 'url' in d:
            o.url = d['url']
        return o


