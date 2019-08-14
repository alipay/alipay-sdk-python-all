#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiServindustryExerciseMemberCreateModel(object):

    def __init__(self):
        self._external_member_id = None
        self._fitness_id = None
        self._gmt_end = None
        self._gmt_start = None
        self._level = None
        self._name = None
        self._parent_id = None
        self._request_id = None
        self._subject_id_list = None
        self._subject_type = None
        self._user_id = None

    @property
    def external_member_id(self):
        return self._external_member_id

    @external_member_id.setter
    def external_member_id(self, value):
        self._external_member_id = value
    @property
    def fitness_id(self):
        return self._fitness_id

    @fitness_id.setter
    def fitness_id(self, value):
        self._fitness_id = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def gmt_start(self):
        return self._gmt_start

    @gmt_start.setter
    def gmt_start(self, value):
        self._gmt_start = value
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def parent_id(self):
        return self._parent_id

    @parent_id.setter
    def parent_id(self, value):
        self._parent_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def subject_id_list(self):
        return self._subject_id_list

    @subject_id_list.setter
    def subject_id_list(self, value):
        if isinstance(value, list):
            self._subject_id_list = list()
            for i in value:
                self._subject_id_list.append(i)
    @property
    def subject_type(self):
        return self._subject_type

    @subject_type.setter
    def subject_type(self, value):
        self._subject_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.external_member_id:
            if hasattr(self.external_member_id, 'to_alipay_dict'):
                params['external_member_id'] = self.external_member_id.to_alipay_dict()
            else:
                params['external_member_id'] = self.external_member_id
        if self.fitness_id:
            if hasattr(self.fitness_id, 'to_alipay_dict'):
                params['fitness_id'] = self.fitness_id.to_alipay_dict()
            else:
                params['fitness_id'] = self.fitness_id
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.gmt_start:
            if hasattr(self.gmt_start, 'to_alipay_dict'):
                params['gmt_start'] = self.gmt_start.to_alipay_dict()
            else:
                params['gmt_start'] = self.gmt_start
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.parent_id:
            if hasattr(self.parent_id, 'to_alipay_dict'):
                params['parent_id'] = self.parent_id.to_alipay_dict()
            else:
                params['parent_id'] = self.parent_id
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.subject_id_list:
            if isinstance(self.subject_id_list, list):
                for i in range(0, len(self.subject_id_list)):
                    element = self.subject_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.subject_id_list[i] = element.to_alipay_dict()
            if hasattr(self.subject_id_list, 'to_alipay_dict'):
                params['subject_id_list'] = self.subject_id_list.to_alipay_dict()
            else:
                params['subject_id_list'] = self.subject_id_list
        if self.subject_type:
            if hasattr(self.subject_type, 'to_alipay_dict'):
                params['subject_type'] = self.subject_type.to_alipay_dict()
            else:
                params['subject_type'] = self.subject_type
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
        o = KoubeiServindustryExerciseMemberCreateModel()
        if 'external_member_id' in d:
            o.external_member_id = d['external_member_id']
        if 'fitness_id' in d:
            o.fitness_id = d['fitness_id']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'gmt_start' in d:
            o.gmt_start = d['gmt_start']
        if 'level' in d:
            o.level = d['level']
        if 'name' in d:
            o.name = d['name']
        if 'parent_id' in d:
            o.parent_id = d['parent_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'subject_id_list' in d:
            o.subject_id_list = d['subject_id_list']
        if 'subject_type' in d:
            o.subject_type = d['subject_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


