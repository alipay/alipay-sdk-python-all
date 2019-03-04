#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMemberDataOutuserinfoModifyModel(object):

    def __init__(self):
        self._avatar_url = None
        self._city = None
        self._country = None
        self._gender = None
        self._nick_name = None
        self._out_user_id = None
        self._phone_number = None
        self._province = None

    @property
    def avatar_url(self):
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, value):
        self._avatar_url = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value


    def to_alipay_dict(self):
        params = dict()
        if self.avatar_url:
            if hasattr(self.avatar_url, 'to_alipay_dict'):
                params['avatar_url'] = self.avatar_url.to_alipay_dict()
            else:
                params['avatar_url'] = self.avatar_url
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.country:
            if hasattr(self.country, 'to_alipay_dict'):
                params['country'] = self.country.to_alipay_dict()
            else:
                params['country'] = self.country
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.nick_name:
            if hasattr(self.nick_name, 'to_alipay_dict'):
                params['nick_name'] = self.nick_name.to_alipay_dict()
            else:
                params['nick_name'] = self.nick_name
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        if self.phone_number:
            if hasattr(self.phone_number, 'to_alipay_dict'):
                params['phone_number'] = self.phone_number.to_alipay_dict()
            else:
                params['phone_number'] = self.phone_number
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMemberDataOutuserinfoModifyModel()
        if 'avatar_url' in d:
            o.avatar_url = d['avatar_url']
        if 'city' in d:
            o.city = d['city']
        if 'country' in d:
            o.country = d['country']
        if 'gender' in d:
            o.gender = d['gender']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        if 'province' in d:
            o.province = d['province']
        return o


