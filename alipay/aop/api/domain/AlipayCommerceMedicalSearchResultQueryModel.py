#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KeyInfo import KeyInfo


class AlipayCommerceMedicalSearchResultQueryModel(object):

    def __init__(self):
        self._account = None
        self._account_type = None
        self._channel_code = None
        self._city_code = None
        self._consultation_hours = None
        self._department_id = None
        self._doctor_tag = None
        self._hos_category = None
        self._hos_character = None
        self._hos_grade = None
        self._hos_tag = None
        self._hospital_grade = None
        self._key_list = None
        self._page_no = None
        self._page_size = None
        self._price = None
        self._query = None
        self._reception_speed = None
        self._scene_code = None
        self._search_type = None
        self._service = None
        self._sort_condition = None
        self._title = None
        self._user_city_code = None
        self._user_latitude = None
        self._user_longitude = None
        self._user_province_code = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def channel_code(self):
        return self._channel_code

    @channel_code.setter
    def channel_code(self, value):
        self._channel_code = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def consultation_hours(self):
        return self._consultation_hours

    @consultation_hours.setter
    def consultation_hours(self, value):
        self._consultation_hours = value
    @property
    def department_id(self):
        return self._department_id

    @department_id.setter
    def department_id(self, value):
        self._department_id = value
    @property
    def doctor_tag(self):
        return self._doctor_tag

    @doctor_tag.setter
    def doctor_tag(self, value):
        self._doctor_tag = value
    @property
    def hos_category(self):
        return self._hos_category

    @hos_category.setter
    def hos_category(self, value):
        if isinstance(value, list):
            self._hos_category = list()
            for i in value:
                self._hos_category.append(i)
    @property
    def hos_character(self):
        return self._hos_character

    @hos_character.setter
    def hos_character(self, value):
        self._hos_character = value
    @property
    def hos_grade(self):
        return self._hos_grade

    @hos_grade.setter
    def hos_grade(self, value):
        if isinstance(value, list):
            self._hos_grade = list()
            for i in value:
                self._hos_grade.append(i)
    @property
    def hos_tag(self):
        return self._hos_tag

    @hos_tag.setter
    def hos_tag(self, value):
        if isinstance(value, list):
            self._hos_tag = list()
            for i in value:
                self._hos_tag.append(i)
    @property
    def hospital_grade(self):
        return self._hospital_grade

    @hospital_grade.setter
    def hospital_grade(self, value):
        self._hospital_grade = value
    @property
    def key_list(self):
        return self._key_list

    @key_list.setter
    def key_list(self, value):
        if isinstance(value, list):
            self._key_list = list()
            for i in value:
                if isinstance(i, KeyInfo):
                    self._key_list.append(i)
                else:
                    self._key_list.append(KeyInfo.from_alipay_dict(i))
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
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def reception_speed(self):
        return self._reception_speed

    @reception_speed.setter
    def reception_speed(self, value):
        self._reception_speed = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def search_type(self):
        return self._search_type

    @search_type.setter
    def search_type(self, value):
        self._search_type = value
    @property
    def service(self):
        return self._service

    @service.setter
    def service(self, value):
        self._service = value
    @property
    def sort_condition(self):
        return self._sort_condition

    @sort_condition.setter
    def sort_condition(self, value):
        self._sort_condition = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def user_city_code(self):
        return self._user_city_code

    @user_city_code.setter
    def user_city_code(self, value):
        self._user_city_code = value
    @property
    def user_latitude(self):
        return self._user_latitude

    @user_latitude.setter
    def user_latitude(self, value):
        self._user_latitude = value
    @property
    def user_longitude(self):
        return self._user_longitude

    @user_longitude.setter
    def user_longitude(self, value):
        self._user_longitude = value
    @property
    def user_province_code(self):
        return self._user_province_code

    @user_province_code.setter
    def user_province_code(self, value):
        self._user_province_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.account:
            if hasattr(self.account, 'to_alipay_dict'):
                params['account'] = self.account.to_alipay_dict()
            else:
                params['account'] = self.account
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.channel_code:
            if hasattr(self.channel_code, 'to_alipay_dict'):
                params['channel_code'] = self.channel_code.to_alipay_dict()
            else:
                params['channel_code'] = self.channel_code
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.consultation_hours:
            if hasattr(self.consultation_hours, 'to_alipay_dict'):
                params['consultation_hours'] = self.consultation_hours.to_alipay_dict()
            else:
                params['consultation_hours'] = self.consultation_hours
        if self.department_id:
            if hasattr(self.department_id, 'to_alipay_dict'):
                params['department_id'] = self.department_id.to_alipay_dict()
            else:
                params['department_id'] = self.department_id
        if self.doctor_tag:
            if hasattr(self.doctor_tag, 'to_alipay_dict'):
                params['doctor_tag'] = self.doctor_tag.to_alipay_dict()
            else:
                params['doctor_tag'] = self.doctor_tag
        if self.hos_category:
            if isinstance(self.hos_category, list):
                for i in range(0, len(self.hos_category)):
                    element = self.hos_category[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.hos_category[i] = element.to_alipay_dict()
            if hasattr(self.hos_category, 'to_alipay_dict'):
                params['hos_category'] = self.hos_category.to_alipay_dict()
            else:
                params['hos_category'] = self.hos_category
        if self.hos_character:
            if hasattr(self.hos_character, 'to_alipay_dict'):
                params['hos_character'] = self.hos_character.to_alipay_dict()
            else:
                params['hos_character'] = self.hos_character
        if self.hos_grade:
            if isinstance(self.hos_grade, list):
                for i in range(0, len(self.hos_grade)):
                    element = self.hos_grade[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.hos_grade[i] = element.to_alipay_dict()
            if hasattr(self.hos_grade, 'to_alipay_dict'):
                params['hos_grade'] = self.hos_grade.to_alipay_dict()
            else:
                params['hos_grade'] = self.hos_grade
        if self.hos_tag:
            if isinstance(self.hos_tag, list):
                for i in range(0, len(self.hos_tag)):
                    element = self.hos_tag[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.hos_tag[i] = element.to_alipay_dict()
            if hasattr(self.hos_tag, 'to_alipay_dict'):
                params['hos_tag'] = self.hos_tag.to_alipay_dict()
            else:
                params['hos_tag'] = self.hos_tag
        if self.hospital_grade:
            if hasattr(self.hospital_grade, 'to_alipay_dict'):
                params['hospital_grade'] = self.hospital_grade.to_alipay_dict()
            else:
                params['hospital_grade'] = self.hospital_grade
        if self.key_list:
            if isinstance(self.key_list, list):
                for i in range(0, len(self.key_list)):
                    element = self.key_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.key_list[i] = element.to_alipay_dict()
            if hasattr(self.key_list, 'to_alipay_dict'):
                params['key_list'] = self.key_list.to_alipay_dict()
            else:
                params['key_list'] = self.key_list
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
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.reception_speed:
            if hasattr(self.reception_speed, 'to_alipay_dict'):
                params['reception_speed'] = self.reception_speed.to_alipay_dict()
            else:
                params['reception_speed'] = self.reception_speed
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.search_type:
            if hasattr(self.search_type, 'to_alipay_dict'):
                params['search_type'] = self.search_type.to_alipay_dict()
            else:
                params['search_type'] = self.search_type
        if self.service:
            if hasattr(self.service, 'to_alipay_dict'):
                params['service'] = self.service.to_alipay_dict()
            else:
                params['service'] = self.service
        if self.sort_condition:
            if hasattr(self.sort_condition, 'to_alipay_dict'):
                params['sort_condition'] = self.sort_condition.to_alipay_dict()
            else:
                params['sort_condition'] = self.sort_condition
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.user_city_code:
            if hasattr(self.user_city_code, 'to_alipay_dict'):
                params['user_city_code'] = self.user_city_code.to_alipay_dict()
            else:
                params['user_city_code'] = self.user_city_code
        if self.user_latitude:
            if hasattr(self.user_latitude, 'to_alipay_dict'):
                params['user_latitude'] = self.user_latitude.to_alipay_dict()
            else:
                params['user_latitude'] = self.user_latitude
        if self.user_longitude:
            if hasattr(self.user_longitude, 'to_alipay_dict'):
                params['user_longitude'] = self.user_longitude.to_alipay_dict()
            else:
                params['user_longitude'] = self.user_longitude
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
        o = AlipayCommerceMedicalSearchResultQueryModel()
        if 'account' in d:
            o.account = d['account']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'channel_code' in d:
            o.channel_code = d['channel_code']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'consultation_hours' in d:
            o.consultation_hours = d['consultation_hours']
        if 'department_id' in d:
            o.department_id = d['department_id']
        if 'doctor_tag' in d:
            o.doctor_tag = d['doctor_tag']
        if 'hos_category' in d:
            o.hos_category = d['hos_category']
        if 'hos_character' in d:
            o.hos_character = d['hos_character']
        if 'hos_grade' in d:
            o.hos_grade = d['hos_grade']
        if 'hos_tag' in d:
            o.hos_tag = d['hos_tag']
        if 'hospital_grade' in d:
            o.hospital_grade = d['hospital_grade']
        if 'key_list' in d:
            o.key_list = d['key_list']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'price' in d:
            o.price = d['price']
        if 'query' in d:
            o.query = d['query']
        if 'reception_speed' in d:
            o.reception_speed = d['reception_speed']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'search_type' in d:
            o.search_type = d['search_type']
        if 'service' in d:
            o.service = d['service']
        if 'sort_condition' in d:
            o.sort_condition = d['sort_condition']
        if 'title' in d:
            o.title = d['title']
        if 'user_city_code' in d:
            o.user_city_code = d['user_city_code']
        if 'user_latitude' in d:
            o.user_latitude = d['user_latitude']
        if 'user_longitude' in d:
            o.user_longitude = d['user_longitude']
        if 'user_province_code' in d:
            o.user_province_code = d['user_province_code']
        return o


