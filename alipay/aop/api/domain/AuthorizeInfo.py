#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AuthorizeInfo(object):

    def __init__(self):
        self._auth_ids = None
        self._auth_materials = None
        self._auth_name = None
        self._end_date = None
        self._start_date = None

    @property
    def auth_ids(self):
        return self._auth_ids

    @auth_ids.setter
    def auth_ids(self, value):
        if isinstance(value, list):
            self._auth_ids = list()
            for i in value:
                self._auth_ids.append(i)
    @property
    def auth_materials(self):
        return self._auth_materials

    @auth_materials.setter
    def auth_materials(self, value):
        if isinstance(value, list):
            self._auth_materials = list()
            for i in value:
                self._auth_materials.append(i)
    @property
    def auth_name(self):
        return self._auth_name

    @auth_name.setter
    def auth_name(self, value):
        self._auth_name = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_ids:
            if isinstance(self.auth_ids, list):
                for i in range(0, len(self.auth_ids)):
                    element = self.auth_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.auth_ids[i] = element.to_alipay_dict()
            if hasattr(self.auth_ids, 'to_alipay_dict'):
                params['auth_ids'] = self.auth_ids.to_alipay_dict()
            else:
                params['auth_ids'] = self.auth_ids
        if self.auth_materials:
            if isinstance(self.auth_materials, list):
                for i in range(0, len(self.auth_materials)):
                    element = self.auth_materials[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.auth_materials[i] = element.to_alipay_dict()
            if hasattr(self.auth_materials, 'to_alipay_dict'):
                params['auth_materials'] = self.auth_materials.to_alipay_dict()
            else:
                params['auth_materials'] = self.auth_materials
        if self.auth_name:
            if hasattr(self.auth_name, 'to_alipay_dict'):
                params['auth_name'] = self.auth_name.to_alipay_dict()
            else:
                params['auth_name'] = self.auth_name
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AuthorizeInfo()
        if 'auth_ids' in d:
            o.auth_ids = d['auth_ids']
        if 'auth_materials' in d:
            o.auth_materials = d['auth_materials']
        if 'auth_name' in d:
            o.auth_name = d['auth_name']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


