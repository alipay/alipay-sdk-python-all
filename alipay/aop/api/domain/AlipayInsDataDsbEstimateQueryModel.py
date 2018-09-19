#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsDataDsbEstimateQueryModel(object):

    def __init__(self):
        self._estimate_no = None
        self._frame_no = None
        self._garage_type = None
        self._license_no = None

    @property
    def estimate_no(self):
        return self._estimate_no

    @estimate_no.setter
    def estimate_no(self, value):
        self._estimate_no = value
    @property
    def frame_no(self):
        return self._frame_no

    @frame_no.setter
    def frame_no(self, value):
        self._frame_no = value
    @property
    def garage_type(self):
        return self._garage_type

    @garage_type.setter
    def garage_type(self, value):
        self._garage_type = value
    @property
    def license_no(self):
        return self._license_no

    @license_no.setter
    def license_no(self, value):
        self._license_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.estimate_no:
            if hasattr(self.estimate_no, 'to_alipay_dict'):
                params['estimate_no'] = self.estimate_no.to_alipay_dict()
            else:
                params['estimate_no'] = self.estimate_no
        if self.frame_no:
            if hasattr(self.frame_no, 'to_alipay_dict'):
                params['frame_no'] = self.frame_no.to_alipay_dict()
            else:
                params['frame_no'] = self.frame_no
        if self.garage_type:
            if hasattr(self.garage_type, 'to_alipay_dict'):
                params['garage_type'] = self.garage_type.to_alipay_dict()
            else:
                params['garage_type'] = self.garage_type
        if self.license_no:
            if hasattr(self.license_no, 'to_alipay_dict'):
                params['license_no'] = self.license_no.to_alipay_dict()
            else:
                params['license_no'] = self.license_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsDataDsbEstimateQueryModel()
        if 'estimate_no' in d:
            o.estimate_no = d['estimate_no']
        if 'frame_no' in d:
            o.frame_no = d['frame_no']
        if 'garage_type' in d:
            o.garage_type = d['garage_type']
        if 'license_no' in d:
            o.license_no = d['license_no']
        return o


