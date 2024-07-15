#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppEbppInstnoticeCreateormodifyModel(object):

    def __init__(self):
        self._city_code = None
        self._city_name = None
        self._expired_time = None
        self._notice_content = None
        self._province_code = None
        self._province_name = None
        self._start_time = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def expired_time(self):
        return self._expired_time

    @expired_time.setter
    def expired_time(self, value):
        self._expired_time = value
    @property
    def notice_content(self):
        return self._notice_content

    @notice_content.setter
    def notice_content(self, value):
        if isinstance(value, list):
            self._notice_content = list()
            for i in value:
                self._notice_content.append(i)
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def province_name(self):
        return self._province_name

    @province_name.setter
    def province_name(self, value):
        self._province_name = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.expired_time:
            if hasattr(self.expired_time, 'to_alipay_dict'):
                params['expired_time'] = self.expired_time.to_alipay_dict()
            else:
                params['expired_time'] = self.expired_time
        if self.notice_content:
            if isinstance(self.notice_content, list):
                for i in range(0, len(self.notice_content)):
                    element = self.notice_content[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.notice_content[i] = element.to_alipay_dict()
            if hasattr(self.notice_content, 'to_alipay_dict'):
                params['notice_content'] = self.notice_content.to_alipay_dict()
            else:
                params['notice_content'] = self.notice_content
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.province_name:
            if hasattr(self.province_name, 'to_alipay_dict'):
                params['province_name'] = self.province_name.to_alipay_dict()
            else:
                params['province_name'] = self.province_name
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppEbppInstnoticeCreateormodifyModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'expired_time' in d:
            o.expired_time = d['expired_time']
        if 'notice_content' in d:
            o.notice_content = d['notice_content']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'province_name' in d:
            o.province_name = d['province_name']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


