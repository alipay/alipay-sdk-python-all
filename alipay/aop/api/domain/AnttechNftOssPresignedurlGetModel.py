#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechNftOssPresignedurlGetModel(object):

    def __init__(self):
        self._business_date = None
        self._file_size = None
        self._scenario_type = None

    @property
    def business_date(self):
        return self._business_date

    @business_date.setter
    def business_date(self, value):
        self._business_date = value
    @property
    def file_size(self):
        return self._file_size

    @file_size.setter
    def file_size(self, value):
        self._file_size = value
    @property
    def scenario_type(self):
        return self._scenario_type

    @scenario_type.setter
    def scenario_type(self, value):
        self._scenario_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_date:
            if hasattr(self.business_date, 'to_alipay_dict'):
                params['business_date'] = self.business_date.to_alipay_dict()
            else:
                params['business_date'] = self.business_date
        if self.file_size:
            if hasattr(self.file_size, 'to_alipay_dict'):
                params['file_size'] = self.file_size.to_alipay_dict()
            else:
                params['file_size'] = self.file_size
        if self.scenario_type:
            if hasattr(self.scenario_type, 'to_alipay_dict'):
                params['scenario_type'] = self.scenario_type.to_alipay_dict()
            else:
                params['scenario_type'] = self.scenario_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechNftOssPresignedurlGetModel()
        if 'business_date' in d:
            o.business_date = d['business_date']
        if 'file_size' in d:
            o.file_size = d['file_size']
        if 'scenario_type' in d:
            o.scenario_type = d['scenario_type']
        return o


