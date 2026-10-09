#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHdfFactorCertifyModel(object):

    def __init__(self):
        self._auth_mode = None
        self._cache_interval = None
        self._id_number = None
        self._id_type = None
        self._is_chinese_id_card = None
        self._name = None
        self._nation = None
        self._photo_data = None

    @property
    def auth_mode(self):
        return self._auth_mode

    @auth_mode.setter
    def auth_mode(self, value):
        self._auth_mode = value
    @property
    def cache_interval(self):
        return self._cache_interval

    @cache_interval.setter
    def cache_interval(self, value):
        self._cache_interval = value
    @property
    def id_number(self):
        return self._id_number

    @id_number.setter
    def id_number(self, value):
        self._id_number = value
    @property
    def id_type(self):
        return self._id_type

    @id_type.setter
    def id_type(self, value):
        self._id_type = value
    @property
    def is_chinese_id_card(self):
        return self._is_chinese_id_card

    @is_chinese_id_card.setter
    def is_chinese_id_card(self, value):
        self._is_chinese_id_card = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def nation(self):
        return self._nation

    @nation.setter
    def nation(self, value):
        self._nation = value
    @property
    def photo_data(self):
        return self._photo_data

    @photo_data.setter
    def photo_data(self, value):
        self._photo_data = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_mode:
            if hasattr(self.auth_mode, 'to_alipay_dict'):
                params['auth_mode'] = self.auth_mode.to_alipay_dict()
            else:
                params['auth_mode'] = self.auth_mode
        if self.cache_interval:
            if hasattr(self.cache_interval, 'to_alipay_dict'):
                params['cache_interval'] = self.cache_interval.to_alipay_dict()
            else:
                params['cache_interval'] = self.cache_interval
        if self.id_number:
            if hasattr(self.id_number, 'to_alipay_dict'):
                params['id_number'] = self.id_number.to_alipay_dict()
            else:
                params['id_number'] = self.id_number
        if self.id_type:
            if hasattr(self.id_type, 'to_alipay_dict'):
                params['id_type'] = self.id_type.to_alipay_dict()
            else:
                params['id_type'] = self.id_type
        if self.is_chinese_id_card:
            if hasattr(self.is_chinese_id_card, 'to_alipay_dict'):
                params['is_chinese_id_card'] = self.is_chinese_id_card.to_alipay_dict()
            else:
                params['is_chinese_id_card'] = self.is_chinese_id_card
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.nation:
            if hasattr(self.nation, 'to_alipay_dict'):
                params['nation'] = self.nation.to_alipay_dict()
            else:
                params['nation'] = self.nation
        if self.photo_data:
            if hasattr(self.photo_data, 'to_alipay_dict'):
                params['photo_data'] = self.photo_data.to_alipay_dict()
            else:
                params['photo_data'] = self.photo_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHdfFactorCertifyModel()
        if 'auth_mode' in d:
            o.auth_mode = d['auth_mode']
        if 'cache_interval' in d:
            o.cache_interval = d['cache_interval']
        if 'id_number' in d:
            o.id_number = d['id_number']
        if 'id_type' in d:
            o.id_type = d['id_type']
        if 'is_chinese_id_card' in d:
            o.is_chinese_id_card = d['is_chinese_id_card']
        if 'name' in d:
            o.name = d['name']
        if 'nation' in d:
            o.nation = d['nation']
        if 'photo_data' in d:
            o.photo_data = d['photo_data']
        return o


