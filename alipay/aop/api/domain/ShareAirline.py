#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShareAirline(object):

    def __init__(self):
        self._ac_code = None
        self._ac_name = None
        self._flight_no = None
        self._plane_model = None
        self._plane_model_size = None

    @property
    def ac_code(self):
        return self._ac_code

    @ac_code.setter
    def ac_code(self, value):
        self._ac_code = value
    @property
    def ac_name(self):
        return self._ac_name

    @ac_name.setter
    def ac_name(self, value):
        self._ac_name = value
    @property
    def flight_no(self):
        return self._flight_no

    @flight_no.setter
    def flight_no(self, value):
        self._flight_no = value
    @property
    def plane_model(self):
        return self._plane_model

    @plane_model.setter
    def plane_model(self, value):
        self._plane_model = value
    @property
    def plane_model_size(self):
        return self._plane_model_size

    @plane_model_size.setter
    def plane_model_size(self, value):
        self._plane_model_size = value


    def to_alipay_dict(self):
        params = dict()
        if self.ac_code:
            if hasattr(self.ac_code, 'to_alipay_dict'):
                params['ac_code'] = self.ac_code.to_alipay_dict()
            else:
                params['ac_code'] = self.ac_code
        if self.ac_name:
            if hasattr(self.ac_name, 'to_alipay_dict'):
                params['ac_name'] = self.ac_name.to_alipay_dict()
            else:
                params['ac_name'] = self.ac_name
        if self.flight_no:
            if hasattr(self.flight_no, 'to_alipay_dict'):
                params['flight_no'] = self.flight_no.to_alipay_dict()
            else:
                params['flight_no'] = self.flight_no
        if self.plane_model:
            if hasattr(self.plane_model, 'to_alipay_dict'):
                params['plane_model'] = self.plane_model.to_alipay_dict()
            else:
                params['plane_model'] = self.plane_model
        if self.plane_model_size:
            if hasattr(self.plane_model_size, 'to_alipay_dict'):
                params['plane_model_size'] = self.plane_model_size.to_alipay_dict()
            else:
                params['plane_model_size'] = self.plane_model_size
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShareAirline()
        if 'ac_code' in d:
            o.ac_code = d['ac_code']
        if 'ac_name' in d:
            o.ac_name = d['ac_name']
        if 'flight_no' in d:
            o.flight_no = d['flight_no']
        if 'plane_model' in d:
            o.plane_model = d['plane_model']
        if 'plane_model_size' in d:
            o.plane_model_size = d['plane_model_size']
        return o


