#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CertAvailableNumVO(object):

    def __init__(self):
        self._available_num = None
        self._cert_template_id = None

    @property
    def available_num(self):
        return self._available_num

    @available_num.setter
    def available_num(self, value):
        self._available_num = value
    @property
    def cert_template_id(self):
        return self._cert_template_id

    @cert_template_id.setter
    def cert_template_id(self, value):
        self._cert_template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_num:
            if hasattr(self.available_num, 'to_alipay_dict'):
                params['available_num'] = self.available_num.to_alipay_dict()
            else:
                params['available_num'] = self.available_num
        if self.cert_template_id:
            if hasattr(self.cert_template_id, 'to_alipay_dict'):
                params['cert_template_id'] = self.cert_template_id.to_alipay_dict()
            else:
                params['cert_template_id'] = self.cert_template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CertAvailableNumVO()
        if 'available_num' in d:
            o.available_num = d['available_num']
        if 'cert_template_id' in d:
            o.cert_template_id = d['cert_template_id']
        return o


