#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExtractItemScoreInfo import ExtractItemScoreInfo
from alipay.aop.api.domain.FilterItem import FilterItem
from alipay.aop.api.domain.RegisterDate import RegisterDate


class AlipayCommerceMedicalLargermodelDepartmentscheduleQueryModel(object):

    def __init__(self):
        self._channel = None
        self._chat_id = None
        self._city_code_list = None
        self._district_code_list = None
        self._downgrade_flag = None
        self._extract_item_score_info = None
        self._filter_item = None
        self._hos_grade_list = None
        self._hos_name_list = None
        self._latitude = None
        self._longitude = None
        self._open_id = None
        self._page_key = None
        self._page_no = None
        self._page_size = None
        self._province_code_list = None
        self._query = None
        self._register_date = None
        self._scene_code = None
        self._second_page_key = None
        self._univ_department_name_list = None
        self._user_city_code = None
        self._user_id = None
        self._user_province_code = None

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
    def city_code_list(self):
        return self._city_code_list

    @city_code_list.setter
    def city_code_list(self, value):
        if isinstance(value, list):
            self._city_code_list = list()
            for i in value:
                self._city_code_list.append(i)
    @property
    def district_code_list(self):
        return self._district_code_list

    @district_code_list.setter
    def district_code_list(self, value):
        if isinstance(value, list):
            self._district_code_list = list()
            for i in value:
                self._district_code_list.append(i)
    @property
    def downgrade_flag(self):
        return self._downgrade_flag

    @downgrade_flag.setter
    def downgrade_flag(self, value):
        self._downgrade_flag = value
    @property
    def extract_item_score_info(self):
        return self._extract_item_score_info

    @extract_item_score_info.setter
    def extract_item_score_info(self, value):
        if isinstance(value, ExtractItemScoreInfo):
            self._extract_item_score_info = value
        else:
            self._extract_item_score_info = ExtractItemScoreInfo.from_alipay_dict(value)
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
    def hos_grade_list(self):
        return self._hos_grade_list

    @hos_grade_list.setter
    def hos_grade_list(self, value):
        if isinstance(value, list):
            self._hos_grade_list = list()
            for i in value:
                self._hos_grade_list.append(i)
    @property
    def hos_name_list(self):
        return self._hos_name_list

    @hos_name_list.setter
    def hos_name_list(self, value):
        if isinstance(value, list):
            self._hos_name_list = list()
            for i in value:
                self._hos_name_list.append(i)
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
    def province_code_list(self):
        return self._province_code_list

    @province_code_list.setter
    def province_code_list(self, value):
        if isinstance(value, list):
            self._province_code_list = list()
            for i in value:
                self._province_code_list.append(i)
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def register_date(self):
        return self._register_date

    @register_date.setter
    def register_date(self, value):
        if isinstance(value, RegisterDate):
            self._register_date = value
        else:
            self._register_date = RegisterDate.from_alipay_dict(value)
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
    def univ_department_name_list(self):
        return self._univ_department_name_list

    @univ_department_name_list.setter
    def univ_department_name_list(self, value):
        if isinstance(value, list):
            self._univ_department_name_list = list()
            for i in value:
                self._univ_department_name_list.append(i)
    @property
    def user_city_code(self):
        return self._user_city_code

    @user_city_code.setter
    def user_city_code(self, value):
        self._user_city_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_province_code(self):
        return self._user_province_code

    @user_province_code.setter
    def user_province_code(self, value):
        self._user_province_code = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.city_code_list:
            if isinstance(self.city_code_list, list):
                for i in range(0, len(self.city_code_list)):
                    element = self.city_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.city_code_list[i] = element.to_alipay_dict()
            if hasattr(self.city_code_list, 'to_alipay_dict'):
                params['city_code_list'] = self.city_code_list.to_alipay_dict()
            else:
                params['city_code_list'] = self.city_code_list
        if self.district_code_list:
            if isinstance(self.district_code_list, list):
                for i in range(0, len(self.district_code_list)):
                    element = self.district_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.district_code_list[i] = element.to_alipay_dict()
            if hasattr(self.district_code_list, 'to_alipay_dict'):
                params['district_code_list'] = self.district_code_list.to_alipay_dict()
            else:
                params['district_code_list'] = self.district_code_list
        if self.downgrade_flag:
            if hasattr(self.downgrade_flag, 'to_alipay_dict'):
                params['downgrade_flag'] = self.downgrade_flag.to_alipay_dict()
            else:
                params['downgrade_flag'] = self.downgrade_flag
        if self.extract_item_score_info:
            if hasattr(self.extract_item_score_info, 'to_alipay_dict'):
                params['extract_item_score_info'] = self.extract_item_score_info.to_alipay_dict()
            else:
                params['extract_item_score_info'] = self.extract_item_score_info
        if self.filter_item:
            if hasattr(self.filter_item, 'to_alipay_dict'):
                params['filter_item'] = self.filter_item.to_alipay_dict()
            else:
                params['filter_item'] = self.filter_item
        if self.hos_grade_list:
            if isinstance(self.hos_grade_list, list):
                for i in range(0, len(self.hos_grade_list)):
                    element = self.hos_grade_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.hos_grade_list[i] = element.to_alipay_dict()
            if hasattr(self.hos_grade_list, 'to_alipay_dict'):
                params['hos_grade_list'] = self.hos_grade_list.to_alipay_dict()
            else:
                params['hos_grade_list'] = self.hos_grade_list
        if self.hos_name_list:
            if isinstance(self.hos_name_list, list):
                for i in range(0, len(self.hos_name_list)):
                    element = self.hos_name_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.hos_name_list[i] = element.to_alipay_dict()
            if hasattr(self.hos_name_list, 'to_alipay_dict'):
                params['hos_name_list'] = self.hos_name_list.to_alipay_dict()
            else:
                params['hos_name_list'] = self.hos_name_list
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
        if self.province_code_list:
            if isinstance(self.province_code_list, list):
                for i in range(0, len(self.province_code_list)):
                    element = self.province_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.province_code_list[i] = element.to_alipay_dict()
            if hasattr(self.province_code_list, 'to_alipay_dict'):
                params['province_code_list'] = self.province_code_list.to_alipay_dict()
            else:
                params['province_code_list'] = self.province_code_list
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.register_date:
            if hasattr(self.register_date, 'to_alipay_dict'):
                params['register_date'] = self.register_date.to_alipay_dict()
            else:
                params['register_date'] = self.register_date
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
        if self.univ_department_name_list:
            if isinstance(self.univ_department_name_list, list):
                for i in range(0, len(self.univ_department_name_list)):
                    element = self.univ_department_name_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.univ_department_name_list[i] = element.to_alipay_dict()
            if hasattr(self.univ_department_name_list, 'to_alipay_dict'):
                params['univ_department_name_list'] = self.univ_department_name_list.to_alipay_dict()
            else:
                params['univ_department_name_list'] = self.univ_department_name_list
        if self.user_city_code:
            if hasattr(self.user_city_code, 'to_alipay_dict'):
                params['user_city_code'] = self.user_city_code.to_alipay_dict()
            else:
                params['user_city_code'] = self.user_city_code
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_province_code:
            if hasattr(self.user_province_code, 'to_alipay_dict'):
                params['user_province_code'] = self.user_province_code.to_alipay_dict()
            else:
                params['user_province_code'] = self.user_province_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalLargermodelDepartmentscheduleQueryModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'chat_id' in d:
            o.chat_id = d['chat_id']
        if 'city_code_list' in d:
            o.city_code_list = d['city_code_list']
        if 'district_code_list' in d:
            o.district_code_list = d['district_code_list']
        if 'downgrade_flag' in d:
            o.downgrade_flag = d['downgrade_flag']
        if 'extract_item_score_info' in d:
            o.extract_item_score_info = d['extract_item_score_info']
        if 'filter_item' in d:
            o.filter_item = d['filter_item']
        if 'hos_grade_list' in d:
            o.hos_grade_list = d['hos_grade_list']
        if 'hos_name_list' in d:
            o.hos_name_list = d['hos_name_list']
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
        if 'province_code_list' in d:
            o.province_code_list = d['province_code_list']
        if 'query' in d:
            o.query = d['query']
        if 'register_date' in d:
            o.register_date = d['register_date']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'second_page_key' in d:
            o.second_page_key = d['second_page_key']
        if 'univ_department_name_list' in d:
            o.univ_department_name_list = d['univ_department_name_list']
        if 'user_city_code' in d:
            o.user_city_code = d['user_city_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_province_code' in d:
            o.user_province_code = d['user_province_code']
        return o


