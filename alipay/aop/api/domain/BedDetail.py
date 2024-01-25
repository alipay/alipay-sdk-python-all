#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BedDetail(object):

    def __init__(self):
        self._bed_length = None
        self._bed_number = None
        self._bed_type = None
        self._bed_width = None

    @property
    def bed_length(self):
        return self._bed_length

    @bed_length.setter
    def bed_length(self, value):
        self._bed_length = value
    @property
    def bed_number(self):
        return self._bed_number

    @bed_number.setter
    def bed_number(self, value):
        self._bed_number = value
    @property
    def bed_type(self):
        return self._bed_type

    @bed_type.setter
    def bed_type(self, value):
        self._bed_type = value
    @property
    def bed_width(self):
        return self._bed_width

    @bed_width.setter
    def bed_width(self, value):
        self._bed_width = value


    def to_alipay_dict(self):
        params = dict()
        if self.bed_length:
            if hasattr(self.bed_length, 'to_alipay_dict'):
                params['bed_length'] = self.bed_length.to_alipay_dict()
            else:
                params['bed_length'] = self.bed_length
        if self.bed_number:
            if hasattr(self.bed_number, 'to_alipay_dict'):
                params['bed_number'] = self.bed_number.to_alipay_dict()
            else:
                params['bed_number'] = self.bed_number
        if self.bed_type:
            if hasattr(self.bed_type, 'to_alipay_dict'):
                params['bed_type'] = self.bed_type.to_alipay_dict()
            else:
                params['bed_type'] = self.bed_type
        if self.bed_width:
            if hasattr(self.bed_width, 'to_alipay_dict'):
                params['bed_width'] = self.bed_width.to_alipay_dict()
            else:
                params['bed_width'] = self.bed_width
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BedDetail()
        if 'bed_length' in d:
            o.bed_length = d['bed_length']
        if 'bed_number' in d:
            o.bed_number = d['bed_number']
        if 'bed_type' in d:
            o.bed_type = d['bed_type']
        if 'bed_width' in d:
            o.bed_width = d['bed_width']
        return o


