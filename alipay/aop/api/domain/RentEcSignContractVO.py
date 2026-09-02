#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentEcSignContractVO(object):

    def __init__(self):
        self._ec_template_code = None
        self._file_url = None
        self._status = None

    @property
    def ec_template_code(self):
        return self._ec_template_code

    @ec_template_code.setter
    def ec_template_code(self, value):
        self._ec_template_code = value
    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.ec_template_code:
            if hasattr(self.ec_template_code, 'to_alipay_dict'):
                params['ec_template_code'] = self.ec_template_code.to_alipay_dict()
            else:
                params['ec_template_code'] = self.ec_template_code
        if self.file_url:
            if hasattr(self.file_url, 'to_alipay_dict'):
                params['file_url'] = self.file_url.to_alipay_dict()
            else:
                params['file_url'] = self.file_url
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentEcSignContractVO()
        if 'ec_template_code' in d:
            o.ec_template_code = d['ec_template_code']
        if 'file_url' in d:
            o.file_url = d['file_url']
        if 'status' in d:
            o.status = d['status']
        return o


