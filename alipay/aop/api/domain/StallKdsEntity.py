#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StallKdsEntity(object):

    def __init__(self):
        self._dinner_type = None
        self._kds_id = None
        self._kds_name = None
        self._kds_type = None
        self._print_flag = None
        self._printer_id = None

    @property
    def dinner_type(self):
        return self._dinner_type

    @dinner_type.setter
    def dinner_type(self, value):
        self._dinner_type = value
    @property
    def kds_id(self):
        return self._kds_id

    @kds_id.setter
    def kds_id(self, value):
        self._kds_id = value
    @property
    def kds_name(self):
        return self._kds_name

    @kds_name.setter
    def kds_name(self, value):
        self._kds_name = value
    @property
    def kds_type(self):
        return self._kds_type

    @kds_type.setter
    def kds_type(self, value):
        self._kds_type = value
    @property
    def print_flag(self):
        return self._print_flag

    @print_flag.setter
    def print_flag(self, value):
        self._print_flag = value
    @property
    def printer_id(self):
        return self._printer_id

    @printer_id.setter
    def printer_id(self, value):
        self._printer_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.dinner_type:
            if hasattr(self.dinner_type, 'to_alipay_dict'):
                params['dinner_type'] = self.dinner_type.to_alipay_dict()
            else:
                params['dinner_type'] = self.dinner_type
        if self.kds_id:
            if hasattr(self.kds_id, 'to_alipay_dict'):
                params['kds_id'] = self.kds_id.to_alipay_dict()
            else:
                params['kds_id'] = self.kds_id
        if self.kds_name:
            if hasattr(self.kds_name, 'to_alipay_dict'):
                params['kds_name'] = self.kds_name.to_alipay_dict()
            else:
                params['kds_name'] = self.kds_name
        if self.kds_type:
            if hasattr(self.kds_type, 'to_alipay_dict'):
                params['kds_type'] = self.kds_type.to_alipay_dict()
            else:
                params['kds_type'] = self.kds_type
        if self.print_flag:
            if hasattr(self.print_flag, 'to_alipay_dict'):
                params['print_flag'] = self.print_flag.to_alipay_dict()
            else:
                params['print_flag'] = self.print_flag
        if self.printer_id:
            if hasattr(self.printer_id, 'to_alipay_dict'):
                params['printer_id'] = self.printer_id.to_alipay_dict()
            else:
                params['printer_id'] = self.printer_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StallKdsEntity()
        if 'dinner_type' in d:
            o.dinner_type = d['dinner_type']
        if 'kds_id' in d:
            o.kds_id = d['kds_id']
        if 'kds_name' in d:
            o.kds_name = d['kds_name']
        if 'kds_type' in d:
            o.kds_type = d['kds_type']
        if 'print_flag' in d:
            o.print_flag = d['print_flag']
        if 'printer_id' in d:
            o.printer_id = d['printer_id']
        return o


