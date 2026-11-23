#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RegisterFilterItem import RegisterFilterItem


class AlipayCommerceMedicalRegisterHospitallistQueryModel(object):

    def __init__(self):
        self._agent_id = None
        self._alipay_user_id = None
        self._channel = None
        self._chat_id = None
        self._city_code = None
        self._district_code = None
        self._filter_item = None
        self._hos_institution_code = None
        self._hos_uniq_code = None
        self._hospital_name = None
        self._isv_code = None
        self._latitude = None
        self._longitude = None
        self._open_id = None
        self._page_key = None
        self._page_no = None
        self._page_size = None
        self._platform_code = None
        self._province_code = None
        self._query = None
        self._query_agent_type = None
        self._req_prop = None
        self._scene_code = None
        self._second_page_key = None
        self._sort_type = None
        self._univ_department_name = None

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
    def chat_id(self):
        return self._chat_id

    @chat_id.setter
    def chat_id(self, value):
        self._chat_id = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def filter_item(self):
        return self._filter_item

    @filter_item.setter
    def filter_item(self, value):
        if isinstance(value, RegisterFilterItem):
            self._filter_item = value
        else:
            self._filter_item = RegisterFilterItem.from_alipay_dict(value)
    @property
    def hos_institution_code(self):
        return self._hos_institution_code

    @hos_institution_code.setter
    def hos_institution_code(self, value):
        self._hos_institution_code = value
    @property
    def hos_uniq_code(self):
        return self._hos_uniq_code

    @hos_uniq_code.setter
    def hos_uniq_code(self, value):
        self._hos_uniq_code = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
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
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
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
    @property
    def sort_type(self):
        return self._sort_type

    @sort_type.setter
    def sort_type(self, value):
        self._sort_type = value
    @property
    def univ_department_name(self):
        return self._univ_department_name

    @univ_department_name.setter
    def univ_department_name(self, value):
        self._univ_department_name = value


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
        if self.chat_id:
            if hasattr(self.chat_id, 'to_alipay_dict'):
                params['chat_id'] = self.chat_id.to_alipay_dict()
            else:
                params['chat_id'] = self.chat_id
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.filter_item:
            if hasattr(self.filter_item, 'to_alipay_dict'):
                params['filter_item'] = self.filter_item.to_alipay_dict()
            else:
                params['filter_item'] = self.filter_item
        if self.hos_institution_code:
            if hasattr(self.hos_institution_code, 'to_alipay_dict'):
                params['hos_institution_code'] = self.hos_institution_code.to_alipay_dict()
            else:
                params['hos_institution_code'] = self.hos_institution_code
        if self.hos_uniq_code:
            if hasattr(self.hos_uniq_code, 'to_alipay_dict'):
                params['hos_uniq_code'] = self.hos_uniq_code.to_alipay_dict()
            else:
                params['hos_uniq_code'] = self.hos_uniq_code
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
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
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
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
        if self.sort_type:
            if hasattr(self.sort_type, 'to_alipay_dict'):
                params['sort_type'] = self.sort_type.to_alipay_dict()
            else:
                params['sort_type'] = self.sort_type
        if self.univ_department_name:
            if hasattr(self.univ_department_name, 'to_alipay_dict'):
                params['univ_department_name'] = self.univ_department_name.to_alipay_dict()
            else:
                params['univ_department_name'] = self.univ_department_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalRegisterHospitallistQueryModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'channel' in d:
            o.channel = d['channel']
        if 'chat_id' in d:
            o.chat_id = d['chat_id']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'filter_item' in d:
            o.filter_item = d['filter_item']
        if 'hos_institution_code' in d:
            o.hos_institution_code = d['hos_institution_code']
        if 'hos_uniq_code' in d:
            o.hos_uniq_code = d['hos_uniq_code']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
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
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'query' in d:
            o.query = d['query']
        if 'query_agent_type' in d:
            o.query_agent_type = d['query_agent_type']
        if 'req_prop' in d:
            o.req_prop = d['req_prop']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'second_page_key' in d:
            o.second_page_key = d['second_page_key']
        if 'sort_type' in d:
            o.sort_type = d['sort_type']
        if 'univ_department_name' in d:
            o.univ_department_name = d['univ_department_name']
        return o


