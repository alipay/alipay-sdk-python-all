#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OperatorInfo(object):

    def __init__(self):
        self._operator_cert_indate = None
        self._operator_cert_no = None
        self._operator_cert_pic_back = None
        self._operator_cert_pic_front = None
        self._operator_cert_type = None
        self._operator_name = None

    @property
    def operator_cert_indate(self):
        return self._operator_cert_indate

    @operator_cert_indate.setter
    def operator_cert_indate(self, value):
        self._operator_cert_indate = value
    @property
    def operator_cert_no(self):
        return self._operator_cert_no

    @operator_cert_no.setter
    def operator_cert_no(self, value):
        self._operator_cert_no = value
    @property
    def operator_cert_pic_back(self):
        return self._operator_cert_pic_back

    @operator_cert_pic_back.setter
    def operator_cert_pic_back(self, value):
        self._operator_cert_pic_back = value
    @property
    def operator_cert_pic_front(self):
        return self._operator_cert_pic_front

    @operator_cert_pic_front.setter
    def operator_cert_pic_front(self, value):
        self._operator_cert_pic_front = value
    @property
    def operator_cert_type(self):
        return self._operator_cert_type

    @operator_cert_type.setter
    def operator_cert_type(self, value):
        self._operator_cert_type = value
    @property
    def operator_name(self):
        return self._operator_name

    @operator_name.setter
    def operator_name(self, value):
        self._operator_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.operator_cert_indate:
            if hasattr(self.operator_cert_indate, 'to_alipay_dict'):
                params['operator_cert_indate'] = self.operator_cert_indate.to_alipay_dict()
            else:
                params['operator_cert_indate'] = self.operator_cert_indate
        if self.operator_cert_no:
            if hasattr(self.operator_cert_no, 'to_alipay_dict'):
                params['operator_cert_no'] = self.operator_cert_no.to_alipay_dict()
            else:
                params['operator_cert_no'] = self.operator_cert_no
        if self.operator_cert_pic_back:
            if hasattr(self.operator_cert_pic_back, 'to_alipay_dict'):
                params['operator_cert_pic_back'] = self.operator_cert_pic_back.to_alipay_dict()
            else:
                params['operator_cert_pic_back'] = self.operator_cert_pic_back
        if self.operator_cert_pic_front:
            if hasattr(self.operator_cert_pic_front, 'to_alipay_dict'):
                params['operator_cert_pic_front'] = self.operator_cert_pic_front.to_alipay_dict()
            else:
                params['operator_cert_pic_front'] = self.operator_cert_pic_front
        if self.operator_cert_type:
            if hasattr(self.operator_cert_type, 'to_alipay_dict'):
                params['operator_cert_type'] = self.operator_cert_type.to_alipay_dict()
            else:
                params['operator_cert_type'] = self.operator_cert_type
        if self.operator_name:
            if hasattr(self.operator_name, 'to_alipay_dict'):
                params['operator_name'] = self.operator_name.to_alipay_dict()
            else:
                params['operator_name'] = self.operator_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OperatorInfo()
        if 'operator_cert_indate' in d:
            o.operator_cert_indate = d['operator_cert_indate']
        if 'operator_cert_no' in d:
            o.operator_cert_no = d['operator_cert_no']
        if 'operator_cert_pic_back' in d:
            o.operator_cert_pic_back = d['operator_cert_pic_back']
        if 'operator_cert_pic_front' in d:
            o.operator_cert_pic_front = d['operator_cert_pic_front']
        if 'operator_cert_type' in d:
            o.operator_cert_type = d['operator_cert_type']
        if 'operator_name' in d:
            o.operator_name = d['operator_name']
        return o


