#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Role(object):

    def __init__(self):
        self._ccs_instance_id = None
        self._create_time = None
        self._creator_id = None
        self._description = None
        self._function_ids = None
        self._id = None
        self._name = None
        self._update_time = None
        self._updater_id = None

    @property
    def ccs_instance_id(self):
        return self._ccs_instance_id

    @ccs_instance_id.setter
    def ccs_instance_id(self, value):
        self._ccs_instance_id = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def creator_id(self):
        return self._creator_id

    @creator_id.setter
    def creator_id(self, value):
        self._creator_id = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def function_ids(self):
        return self._function_ids

    @function_ids.setter
    def function_ids(self, value):
        if isinstance(value, list):
            self._function_ids = list()
            for i in value:
                self._function_ids.append(i)
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value
    @property
    def updater_id(self):
        return self._updater_id

    @updater_id.setter
    def updater_id(self, value):
        self._updater_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ccs_instance_id:
            if hasattr(self.ccs_instance_id, 'to_alipay_dict'):
                params['ccs_instance_id'] = self.ccs_instance_id.to_alipay_dict()
            else:
                params['ccs_instance_id'] = self.ccs_instance_id
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.creator_id:
            if hasattr(self.creator_id, 'to_alipay_dict'):
                params['creator_id'] = self.creator_id.to_alipay_dict()
            else:
                params['creator_id'] = self.creator_id
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.function_ids:
            if isinstance(self.function_ids, list):
                for i in range(0, len(self.function_ids)):
                    element = self.function_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.function_ids[i] = element.to_alipay_dict()
            if hasattr(self.function_ids, 'to_alipay_dict'):
                params['function_ids'] = self.function_ids.to_alipay_dict()
            else:
                params['function_ids'] = self.function_ids
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.update_time:
            if hasattr(self.update_time, 'to_alipay_dict'):
                params['update_time'] = self.update_time.to_alipay_dict()
            else:
                params['update_time'] = self.update_time
        if self.updater_id:
            if hasattr(self.updater_id, 'to_alipay_dict'):
                params['updater_id'] = self.updater_id.to_alipay_dict()
            else:
                params['updater_id'] = self.updater_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Role()
        if 'ccs_instance_id' in d:
            o.ccs_instance_id = d['ccs_instance_id']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'creator_id' in d:
            o.creator_id = d['creator_id']
        if 'description' in d:
            o.description = d['description']
        if 'function_ids' in d:
            o.function_ids = d['function_ids']
        if 'id' in d:
            o.id = d['id']
        if 'name' in d:
            o.name = d['name']
        if 'update_time' in d:
            o.update_time = d['update_time']
        if 'updater_id' in d:
            o.updater_id = d['updater_id']
        return o


