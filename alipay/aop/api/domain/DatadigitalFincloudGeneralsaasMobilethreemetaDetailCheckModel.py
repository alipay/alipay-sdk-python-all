#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudGeneralsaasMobilethreemetaDetailCheckModel(object):

    def __init__(self):
        self._biz_code = None
        self._cert_name = None
        self._cert_no = None
        self._outer_biz_no = None
        self._phone = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
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
    def outer_biz_no(self):
        return self._outer_biz_no

    @outer_biz_no.setter
    def outer_biz_no(self, value):
        self._outer_biz_no = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
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
        if self.outer_biz_no:
            if hasattr(self.outer_biz_no, 'to_alipay_dict'):
                params['outer_biz_no'] = self.outer_biz_no.to_alipay_dict()
            else:
                params['outer_biz_no'] = self.outer_biz_no
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudGeneralsaasMobilethreemetaDetailCheckModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'outer_biz_no' in d:
            o.outer_biz_no = d['outer_biz_no']
        if 'phone' in d:
            o.phone = d['phone']
        return o


