#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HotelInfo import HotelInfo


class AlipayCommerceDataHotelServiceSyncModel(object):

    def __init__(self):
        self._hotel_app_id = None
        self._hotel_info = None
        self._operate_type = None
        self._outer_hotel_id = None
        self._service_description = None
        self._service_id = None
        self._service_name = None
        self._service_submit_type = None
        self._service_url = None
        self._source_system = None

    @property
    def hotel_app_id(self):
        return self._hotel_app_id

    @hotel_app_id.setter
    def hotel_app_id(self, value):
        self._hotel_app_id = value
    @property
    def hotel_info(self):
        return self._hotel_info

    @hotel_info.setter
    def hotel_info(self, value):
        if isinstance(value, HotelInfo):
            self._hotel_info = value
        else:
            self._hotel_info = HotelInfo.from_alipay_dict(value)
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def outer_hotel_id(self):
        return self._outer_hotel_id

    @outer_hotel_id.setter
    def outer_hotel_id(self, value):
        self._outer_hotel_id = value
    @property
    def service_description(self):
        return self._service_description

    @service_description.setter
    def service_description(self, value):
        self._service_description = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def service_submit_type(self):
        return self._service_submit_type

    @service_submit_type.setter
    def service_submit_type(self, value):
        self._service_submit_type = value
    @property
    def service_url(self):
        return self._service_url

    @service_url.setter
    def service_url(self, value):
        self._service_url = value
    @property
    def source_system(self):
        return self._source_system

    @source_system.setter
    def source_system(self, value):
        self._source_system = value


    def to_alipay_dict(self):
        params = dict()
        if self.hotel_app_id:
            if hasattr(self.hotel_app_id, 'to_alipay_dict'):
                params['hotel_app_id'] = self.hotel_app_id.to_alipay_dict()
            else:
                params['hotel_app_id'] = self.hotel_app_id
        if self.hotel_info:
            if hasattr(self.hotel_info, 'to_alipay_dict'):
                params['hotel_info'] = self.hotel_info.to_alipay_dict()
            else:
                params['hotel_info'] = self.hotel_info
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.outer_hotel_id:
            if hasattr(self.outer_hotel_id, 'to_alipay_dict'):
                params['outer_hotel_id'] = self.outer_hotel_id.to_alipay_dict()
            else:
                params['outer_hotel_id'] = self.outer_hotel_id
        if self.service_description:
            if hasattr(self.service_description, 'to_alipay_dict'):
                params['service_description'] = self.service_description.to_alipay_dict()
            else:
                params['service_description'] = self.service_description
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.service_submit_type:
            if hasattr(self.service_submit_type, 'to_alipay_dict'):
                params['service_submit_type'] = self.service_submit_type.to_alipay_dict()
            else:
                params['service_submit_type'] = self.service_submit_type
        if self.service_url:
            if hasattr(self.service_url, 'to_alipay_dict'):
                params['service_url'] = self.service_url.to_alipay_dict()
            else:
                params['service_url'] = self.service_url
        if self.source_system:
            if hasattr(self.source_system, 'to_alipay_dict'):
                params['source_system'] = self.source_system.to_alipay_dict()
            else:
                params['source_system'] = self.source_system
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceDataHotelServiceSyncModel()
        if 'hotel_app_id' in d:
            o.hotel_app_id = d['hotel_app_id']
        if 'hotel_info' in d:
            o.hotel_info = d['hotel_info']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'outer_hotel_id' in d:
            o.outer_hotel_id = d['outer_hotel_id']
        if 'service_description' in d:
            o.service_description = d['service_description']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'service_submit_type' in d:
            o.service_submit_type = d['service_submit_type']
        if 'service_url' in d:
            o.service_url = d['service_url']
        if 'source_system' in d:
            o.source_system = d['source_system']
        return o


