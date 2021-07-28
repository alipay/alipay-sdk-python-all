#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PlateNoCertDto(object):

    def __init__(self):
        self._cert_result = None
        self._plate_no = None

    @property
    def cert_result(self):
        return self._cert_result

    @cert_result.setter
    def cert_result(self, value):
        self._cert_result = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_result:
            if hasattr(self.cert_result, 'to_alipay_dict'):
                params['cert_result'] = self.cert_result.to_alipay_dict()
            else:
                params['cert_result'] = self.cert_result
        if self.plate_no:
            if hasattr(self.plate_no, 'to_alipay_dict'):
                params['plate_no'] = self.plate_no.to_alipay_dict()
            else:
                params['plate_no'] = self.plate_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PlateNoCertDto()
        if 'cert_result' in d:
            o.cert_result = d['cert_result']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        return o


