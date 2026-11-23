#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FilterItem import FilterItem


class AlipayCommerceMedicalRegisterSelectablescheduleQueryModel(object):

    def __init__(self):
        self._agent_id = None
        self._alipay_user_id = None
        self._channel = None
        self._city_code = None
        self._department_id = None
        self._doctor_inner_id = None
        self._filter_item = None
        self._hospital_id = None
        self._isv_code = None
        self._latitude = None
        self._longitude = None
        self._open_id = None
        self._page_key = None
        self._platform_code = None
        self._query_agent_type = None
        self._req_prop = None
        self._scene_code = None
        self._second_page_key = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def department_id(self):
        return self._department_id

    @department_id.setter
    def department_id(self, value):
        self._department_id = value
    @property
    def doctor_inner_id(self):
        return self._doctor_inner_id

    @doctor_inner_id.setter
    def doctor_inner_id(self, value):
        self._doctor_inner_id = value
    @property
    def filter_item(self):
        return self._filter_item

    @filter_item.setter
    def filter_item(self, value):
        if isinstance(value, FilterItem):
            self._filter_item = value
        else:
            self._filter_item = FilterItem.from_alipay_dict(value)
    @property
    def hospital_id(self):
        return self._hospital_id

    @hospital_id.setter
    def hospital_id(self, value):
        self._hospital_id = value
    @property
    def isv_code(self):
        return self._isv_code

    @isv_code.setter
    def isv_code(self, value):
        self._isv_code = value
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
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def page_key(self):
        return self._page_key

    @page_key.setter
    def page_key(self, value):
        self._page_key = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def query_agent_type(self):
        return self._query_agent_type

    @query_agent_type.setter
    def query_agent_type(self, value):
        self._query_agent_type = value
    @property
    def req_prop(self):
        return self._req_prop

    @req_prop.setter
    def req_prop(self, value):
        self._req_prop = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def second_page_key(self):
        return self._second_page_key

    @second_page_key.setter
    def second_page_key(self, value):
        self._second_page_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.department_id:
            if hasattr(self.department_id, 'to_alipay_dict'):
                params['department_id'] = self.department_id.to_alipay_dict()
            else:
                params['department_id'] = self.department_id
        if self.doctor_inner_id:
            if hasattr(self.doctor_inner_id, 'to_alipay_dict'):
                params['doctor_inner_id'] = self.doctor_inner_id.to_alipay_dict()
            else:
                params['doctor_inner_id'] = self.doctor_inner_id
        if self.filter_item:
            if hasattr(self.filter_item, 'to_alipay_dict'):
                params['filter_item'] = self.filter_item.to_alipay_dict()
            else:
                params['filter_item'] = self.filter_item
        if self.hospital_id:
            if hasattr(self.hospital_id, 'to_alipay_dict'):
                params['hospital_id'] = self.hospital_id.to_alipay_dict()
            else:
                params['hospital_id'] = self.hospital_id
        if self.isv_code:
            if hasattr(self.isv_code, 'to_alipay_dict'):
                params['isv_code'] = self.isv_code.to_alipay_dict()
            else:
                params['isv_code'] = self.isv_code
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
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.page_key:
            if hasattr(self.page_key, 'to_alipay_dict'):
                params['page_key'] = self.page_key.to_alipay_dict()
            else:
                params['page_key'] = self.page_key
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.query_agent_type:
            if hasattr(self.query_agent_type, 'to_alipay_dict'):
                params['query_agent_type'] = self.query_agent_type.to_alipay_dict()
            else:
                params['query_agent_type'] = self.query_agent_type
        if self.req_prop:
            if hasattr(self.req_prop, 'to_alipay_dict'):
                params['req_prop'] = self.req_prop.to_alipay_dict()
            else:
                params['req_prop'] = self.req_prop
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.second_page_key:
            if hasattr(self.second_page_key, 'to_alipay_dict'):
                params['second_page_key'] = self.second_page_key.to_alipay_dict()
            else:
                params['second_page_key'] = self.second_page_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalRegisterSelectablescheduleQueryModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'channel' in d:
            o.channel = d['channel']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'department_id' in d:
            o.department_id = d['department_id']
        if 'doctor_inner_id' in d:
            o.doctor_inner_id = d['doctor_inner_id']
        if 'filter_item' in d:
            o.filter_item = d['filter_item']
        if 'hospital_id' in d:
            o.hospital_id = d['hospital_id']
        if 'isv_code' in d:
            o.isv_code = d['isv_code']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'page_key' in d:
            o.page_key = d['page_key']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'query_agent_type' in d:
            o.query_agent_type = d['query_agent_type']
        if 'req_prop' in d:
            o.req_prop = d['req_prop']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'second_page_key' in d:
            o.second_page_key = d['second_page_key']
        return o


