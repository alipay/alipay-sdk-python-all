#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataAiserviceCloudbusOridestodGetModel(object):

    def __init__(self):
        self._app_version = None
        self._city_code = None
        self._dest_geo = None
        self._end_date = None
        self._ori_geo = None
        self._partner_id = None
        self._start_date = None

    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def dest_geo(self):
        return self._dest_geo

    @dest_geo.setter
    def dest_geo(self, value):
        if isinstance(value, list):
            self._dest_geo = list()
            for i in value:
                self._dest_geo.append(i)
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def ori_geo(self):
        return self._ori_geo

    @ori_geo.setter
    def ori_geo(self, value):
        if isinstance(value, list):
            self._ori_geo = list()
            for i in value:
                self._ori_geo.append(i)
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.dest_geo:
            if isinstance(self.dest_geo, list):
                for i in range(0, len(self.dest_geo)):
                    element = self.dest_geo[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dest_geo[i] = element.to_alipay_dict()
            if hasattr(self.dest_geo, 'to_alipay_dict'):
                params['dest_geo'] = self.dest_geo.to_alipay_dict()
            else:
                params['dest_geo'] = self.dest_geo
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.ori_geo:
            if isinstance(self.ori_geo, list):
                for i in range(0, len(self.ori_geo)):
                    element = self.ori_geo[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ori_geo[i] = element.to_alipay_dict()
            if hasattr(self.ori_geo, 'to_alipay_dict'):
                params['ori_geo'] = self.ori_geo.to_alipay_dict()
            else:
                params['ori_geo'] = self.ori_geo
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
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
        o = AlipayDataAiserviceCloudbusOridestodGetModel()
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'dest_geo' in d:
            o.dest_geo = d['dest_geo']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'ori_geo' in d:
            o.ori_geo = d['ori_geo']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


