#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Attach(object):

    def __init__(self):
        self._file_location = None
        self._file_name = None

    @property
    def file_location(self):
        return self._file_location

    @file_location.setter
    def file_location(self, value):
        self._file_location = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_location:
            if hasattr(self.file_location, 'to_alipay_dict'):
                params['file_location'] = self.file_location.to_alipay_dict()
            else:
                params['file_location'] = self.file_location
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Attach()
        if 'file_location' in d:
            o.file_location = d['file_location']
        if 'file_name' in d:
            o.file_name = d['file_name']
        return o


