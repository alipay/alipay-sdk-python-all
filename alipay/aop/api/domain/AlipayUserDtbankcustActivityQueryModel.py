#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserDtbankcustActivityQueryModel(object):

    def __init__(self):
        self._activity_type_list = None
        self._bank_card_type_list = None
        self._bank_inst_id_list = None
        self._discount_use_scene_map_string = None
        self._last_activity_id = None
        self._limit = None
        self._source = None
        self._sub_source = None
        self._user_id = None

    @property
    def activity_type_list(self):
        return self._activity_type_list

    @activity_type_list.setter
    def activity_type_list(self, value):
        if isinstance(value, list):
            self._activity_type_list = list()
            for i in value:
                self._activity_type_list.append(i)
    @property
    def bank_card_type_list(self):
        return self._bank_card_type_list

    @bank_card_type_list.setter
    def bank_card_type_list(self, value):
        if isinstance(value, list):
            self._bank_card_type_list = list()
            for i in value:
                self._bank_card_type_list.append(i)
    @property
    def bank_inst_id_list(self):
        return self._bank_inst_id_list

    @bank_inst_id_list.setter
    def bank_inst_id_list(self, value):
        if isinstance(value, list):
            self._bank_inst_id_list = list()
            for i in value:
                self._bank_inst_id_list.append(i)
    @property
    def discount_use_scene_map_string(self):
        return self._discount_use_scene_map_string

    @discount_use_scene_map_string.setter
    def discount_use_scene_map_string(self, value):
        self._discount_use_scene_map_string = value
    @property
    def last_activity_id(self):
        return self._last_activity_id

    @last_activity_id.setter
    def last_activity_id(self, value):
        self._last_activity_id = value
    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, value):
        self._limit = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def sub_source(self):
        return self._sub_source

    @sub_source.setter
    def sub_source(self, value):
        self._sub_source = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_type_list:
            if isinstance(self.activity_type_list, list):
                for i in range(0, len(self.activity_type_list)):
                    element = self.activity_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activity_type_list[i] = element.to_alipay_dict()
            if hasattr(self.activity_type_list, 'to_alipay_dict'):
                params['activity_type_list'] = self.activity_type_list.to_alipay_dict()
            else:
                params['activity_type_list'] = self.activity_type_list
        if self.bank_card_type_list:
            if isinstance(self.bank_card_type_list, list):
                for i in range(0, len(self.bank_card_type_list)):
                    element = self.bank_card_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bank_card_type_list[i] = element.to_alipay_dict()
            if hasattr(self.bank_card_type_list, 'to_alipay_dict'):
                params['bank_card_type_list'] = self.bank_card_type_list.to_alipay_dict()
            else:
                params['bank_card_type_list'] = self.bank_card_type_list
        if self.bank_inst_id_list:
            if isinstance(self.bank_inst_id_list, list):
                for i in range(0, len(self.bank_inst_id_list)):
                    element = self.bank_inst_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bank_inst_id_list[i] = element.to_alipay_dict()
            if hasattr(self.bank_inst_id_list, 'to_alipay_dict'):
                params['bank_inst_id_list'] = self.bank_inst_id_list.to_alipay_dict()
            else:
                params['bank_inst_id_list'] = self.bank_inst_id_list
        if self.discount_use_scene_map_string:
            if hasattr(self.discount_use_scene_map_string, 'to_alipay_dict'):
                params['discount_use_scene_map_string'] = self.discount_use_scene_map_string.to_alipay_dict()
            else:
                params['discount_use_scene_map_string'] = self.discount_use_scene_map_string
        if self.last_activity_id:
            if hasattr(self.last_activity_id, 'to_alipay_dict'):
                params['last_activity_id'] = self.last_activity_id.to_alipay_dict()
            else:
                params['last_activity_id'] = self.last_activity_id
        if self.limit:
            if hasattr(self.limit, 'to_alipay_dict'):
                params['limit'] = self.limit.to_alipay_dict()
            else:
                params['limit'] = self.limit
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.sub_source:
            if hasattr(self.sub_source, 'to_alipay_dict'):
                params['sub_source'] = self.sub_source.to_alipay_dict()
            else:
                params['sub_source'] = self.sub_source
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserDtbankcustActivityQueryModel()
        if 'activity_type_list' in d:
            o.activity_type_list = d['activity_type_list']
        if 'bank_card_type_list' in d:
            o.bank_card_type_list = d['bank_card_type_list']
        if 'bank_inst_id_list' in d:
            o.bank_inst_id_list = d['bank_inst_id_list']
        if 'discount_use_scene_map_string' in d:
            o.discount_use_scene_map_string = d['discount_use_scene_map_string']
        if 'last_activity_id' in d:
            o.last_activity_id = d['last_activity_id']
        if 'limit' in d:
            o.limit = d['limit']
        if 'source' in d:
            o.source = d['source']
        if 'sub_source' in d:
            o.sub_source = d['sub_source']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


