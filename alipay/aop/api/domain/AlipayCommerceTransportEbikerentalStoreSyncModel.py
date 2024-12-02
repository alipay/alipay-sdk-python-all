#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportEbikerentalStoreSyncModel(object):

    def __init__(self):
        self._business_time = None
        self._city_code = None
        self._city_name = None
        self._other_return_store_ids = None
        self._province_code = None
        self._province_name = None
        self._service_provider = None
        self._status = None
        self._store_address = None
        self._store_contact = None
        self._store_ebike_config_tags = None
        self._store_id = None
        self._store_image_url = None
        self._store_location_coordinates = None
        self._store_name = None
        self._store_service_tags = None
        self._support_multiple_stores_return_flag = None
        self._sync_type = None

    @property
    def business_time(self):
        return self._business_time

    @business_time.setter
    def business_time(self, value):
        self._business_time = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def other_return_store_ids(self):
        return self._other_return_store_ids

    @other_return_store_ids.setter
    def other_return_store_ids(self, value):
        if isinstance(value, list):
            self._other_return_store_ids = list()
            for i in value:
                self._other_return_store_ids.append(i)
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def province_name(self):
        return self._province_name

    @province_name.setter
    def province_name(self, value):
        self._province_name = value
    @property
    def service_provider(self):
        return self._service_provider

    @service_provider.setter
    def service_provider(self, value):
        self._service_provider = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def store_address(self):
        return self._store_address

    @store_address.setter
    def store_address(self, value):
        self._store_address = value
    @property
    def store_contact(self):
        return self._store_contact

    @store_contact.setter
    def store_contact(self, value):
        self._store_contact = value
    @property
    def store_ebike_config_tags(self):
        return self._store_ebike_config_tags

    @store_ebike_config_tags.setter
    def store_ebike_config_tags(self, value):
        self._store_ebike_config_tags = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def store_image_url(self):
        return self._store_image_url

    @store_image_url.setter
    def store_image_url(self, value):
        self._store_image_url = value
    @property
    def store_location_coordinates(self):
        return self._store_location_coordinates

    @store_location_coordinates.setter
    def store_location_coordinates(self, value):
        self._store_location_coordinates = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value
    @property
    def store_service_tags(self):
        return self._store_service_tags

    @store_service_tags.setter
    def store_service_tags(self, value):
        self._store_service_tags = value
    @property
    def support_multiple_stores_return_flag(self):
        return self._support_multiple_stores_return_flag

    @support_multiple_stores_return_flag.setter
    def support_multiple_stores_return_flag(self, value):
        self._support_multiple_stores_return_flag = value
    @property
    def sync_type(self):
        return self._sync_type

    @sync_type.setter
    def sync_type(self, value):
        self._sync_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_time:
            if hasattr(self.business_time, 'to_alipay_dict'):
                params['business_time'] = self.business_time.to_alipay_dict()
            else:
                params['business_time'] = self.business_time
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.other_return_store_ids:
            if isinstance(self.other_return_store_ids, list):
                for i in range(0, len(self.other_return_store_ids)):
                    element = self.other_return_store_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.other_return_store_ids[i] = element.to_alipay_dict()
            if hasattr(self.other_return_store_ids, 'to_alipay_dict'):
                params['other_return_store_ids'] = self.other_return_store_ids.to_alipay_dict()
            else:
                params['other_return_store_ids'] = self.other_return_store_ids
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.province_name:
            if hasattr(self.province_name, 'to_alipay_dict'):
                params['province_name'] = self.province_name.to_alipay_dict()
            else:
                params['province_name'] = self.province_name
        if self.service_provider:
            if hasattr(self.service_provider, 'to_alipay_dict'):
                params['service_provider'] = self.service_provider.to_alipay_dict()
            else:
                params['service_provider'] = self.service_provider
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.store_address:
            if hasattr(self.store_address, 'to_alipay_dict'):
                params['store_address'] = self.store_address.to_alipay_dict()
            else:
                params['store_address'] = self.store_address
        if self.store_contact:
            if hasattr(self.store_contact, 'to_alipay_dict'):
                params['store_contact'] = self.store_contact.to_alipay_dict()
            else:
                params['store_contact'] = self.store_contact
        if self.store_ebike_config_tags:
            if hasattr(self.store_ebike_config_tags, 'to_alipay_dict'):
                params['store_ebike_config_tags'] = self.store_ebike_config_tags.to_alipay_dict()
            else:
                params['store_ebike_config_tags'] = self.store_ebike_config_tags
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.store_image_url:
            if hasattr(self.store_image_url, 'to_alipay_dict'):
                params['store_image_url'] = self.store_image_url.to_alipay_dict()
            else:
                params['store_image_url'] = self.store_image_url
        if self.store_location_coordinates:
            if hasattr(self.store_location_coordinates, 'to_alipay_dict'):
                params['store_location_coordinates'] = self.store_location_coordinates.to_alipay_dict()
            else:
                params['store_location_coordinates'] = self.store_location_coordinates
        if self.store_name:
            if hasattr(self.store_name, 'to_alipay_dict'):
                params['store_name'] = self.store_name.to_alipay_dict()
            else:
                params['store_name'] = self.store_name
        if self.store_service_tags:
            if hasattr(self.store_service_tags, 'to_alipay_dict'):
                params['store_service_tags'] = self.store_service_tags.to_alipay_dict()
            else:
                params['store_service_tags'] = self.store_service_tags
        if self.support_multiple_stores_return_flag:
            if hasattr(self.support_multiple_stores_return_flag, 'to_alipay_dict'):
                params['support_multiple_stores_return_flag'] = self.support_multiple_stores_return_flag.to_alipay_dict()
            else:
                params['support_multiple_stores_return_flag'] = self.support_multiple_stores_return_flag
        if self.sync_type:
            if hasattr(self.sync_type, 'to_alipay_dict'):
                params['sync_type'] = self.sync_type.to_alipay_dict()
            else:
                params['sync_type'] = self.sync_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEbikerentalStoreSyncModel()
        if 'business_time' in d:
            o.business_time = d['business_time']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'other_return_store_ids' in d:
            o.other_return_store_ids = d['other_return_store_ids']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'province_name' in d:
            o.province_name = d['province_name']
        if 'service_provider' in d:
            o.service_provider = d['service_provider']
        if 'status' in d:
            o.status = d['status']
        if 'store_address' in d:
            o.store_address = d['store_address']
        if 'store_contact' in d:
            o.store_contact = d['store_contact']
        if 'store_ebike_config_tags' in d:
            o.store_ebike_config_tags = d['store_ebike_config_tags']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'store_image_url' in d:
            o.store_image_url = d['store_image_url']
        if 'store_location_coordinates' in d:
            o.store_location_coordinates = d['store_location_coordinates']
        if 'store_name' in d:
            o.store_name = d['store_name']
        if 'store_service_tags' in d:
            o.store_service_tags = d['store_service_tags']
        if 'support_multiple_stores_return_flag' in d:
            o.support_multiple_stores_return_flag = d['support_multiple_stores_return_flag']
        if 'sync_type' in d:
            o.sync_type = d['sync_type']
        return o


