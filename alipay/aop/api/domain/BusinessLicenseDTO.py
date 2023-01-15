#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusinessLicenseDTO(object):

    def __init__(self):
        self._cert_mobile = None
        self._cert_name = None
        self._cert_no = None
        self._cert_pic = None
        self._cert_type = None
        self._date_limitation = None

    @property
    def cert_mobile(self):
        return self._cert_mobile

    @cert_mobile.setter
    def cert_mobile(self, value):
        self._cert_mobile = value
    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_pic(self):
        return self._cert_pic

    @cert_pic.setter
    def cert_pic(self, value):
        self._cert_pic = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def date_limitation(self):
        return self._date_limitation

    @date_limitation.setter
    def date_limitation(self, value):
        self._date_limitation = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_mobile:
            if hasattr(self.cert_mobile, 'to_alipay_dict'):
                params['cert_mobile'] = self.cert_mobile.to_alipay_dict()
            else:
                params['cert_mobile'] = self.cert_mobile
        if self.cert_name:
            if hasattr(self.cert_name, 'to_alipay_dict'):
                params['cert_name'] = self.cert_name.to_alipay_dict()
            else:
                params['cert_name'] = self.cert_name
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_pic:
            if hasattr(self.cert_pic, 'to_alipay_dict'):
                params['cert_pic'] = self.cert_pic.to_alipay_dict()
            else:
                params['cert_pic'] = self.cert_pic
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.date_limitation:
            if hasattr(self.date_limitation, 'to_alipay_dict'):
                params['date_limitation'] = self.date_limitation.to_alipay_dict()
            else:
                params['date_limitation'] = self.date_limitation
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessLicenseDTO()
        if 'cert_mobile' in d:
            o.cert_mobile = d['cert_mobile']
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_pic' in d:
            o.cert_pic = d['cert_pic']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'date_limitation' in d:
            o.date_limitation = d['date_limitation']
        return o


