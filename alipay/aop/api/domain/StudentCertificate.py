#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StudentCertificate(object):

    def __init__(self):
        self._cert_category = None
        self._cert_code = None
        self._cert_name = None
        self._cert_num = None
        self._cert_type = None
        self._desc = None
        self._end_time = None
        self._start_time = None
        self._url = None
        self._url_type = None

    @property
    def cert_category(self):
        return self._cert_category

    @cert_category.setter
    def cert_category(self, value):
        self._cert_category = value
    @property
    def cert_code(self):
        return self._cert_code

    @cert_code.setter
    def cert_code(self, value):
        self._cert_code = value
    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def cert_num(self):
        return self._cert_num

    @cert_num.setter
    def cert_num(self, value):
        self._cert_num = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
    @property
    def url_type(self):
        return self._url_type

    @url_type.setter
    def url_type(self, value):
        self._url_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_category:
            if hasattr(self.cert_category, 'to_alipay_dict'):
                params['cert_category'] = self.cert_category.to_alipay_dict()
            else:
                params['cert_category'] = self.cert_category
        if self.cert_code:
            if hasattr(self.cert_code, 'to_alipay_dict'):
                params['cert_code'] = self.cert_code.to_alipay_dict()
            else:
                params['cert_code'] = self.cert_code
        if self.cert_name:
            if hasattr(self.cert_name, 'to_alipay_dict'):
                params['cert_name'] = self.cert_name.to_alipay_dict()
            else:
                params['cert_name'] = self.cert_name
        if self.cert_num:
            if hasattr(self.cert_num, 'to_alipay_dict'):
                params['cert_num'] = self.cert_num.to_alipay_dict()
            else:
                params['cert_num'] = self.cert_num
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        if self.url_type:
            if hasattr(self.url_type, 'to_alipay_dict'):
                params['url_type'] = self.url_type.to_alipay_dict()
            else:
                params['url_type'] = self.url_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StudentCertificate()
        if 'cert_category' in d:
            o.cert_category = d['cert_category']
        if 'cert_code' in d:
            o.cert_code = d['cert_code']
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_num' in d:
            o.cert_num = d['cert_num']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'desc' in d:
            o.desc = d['desc']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'url' in d:
            o.url = d['url']
        if 'url_type' in d:
            o.url_type = d['url_type']
        return o


