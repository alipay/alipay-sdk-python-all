#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ObjectTaskStatus(object):

    def __init__(self):
        self._basket_no = None
        self._biz_object_no = None
        self._number = None
        self._status = None

    @property
    def basket_no(self):
        return self._basket_no

    @basket_no.setter
    def basket_no(self, value):
        self._basket_no = value
    @property
    def biz_object_no(self):
        return self._biz_object_no

    @biz_object_no.setter
    def biz_object_no(self, value):
        self._biz_object_no = value
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.basket_no:
            if hasattr(self.basket_no, 'to_alipay_dict'):
                params['basket_no'] = self.basket_no.to_alipay_dict()
            else:
                params['basket_no'] = self.basket_no
        if self.biz_object_no:
            if hasattr(self.biz_object_no, 'to_alipay_dict'):
                params['biz_object_no'] = self.biz_object_no.to_alipay_dict()
            else:
                params['biz_object_no'] = self.biz_object_no
        if self.number:
            if hasattr(self.number, 'to_alipay_dict'):
                params['number'] = self.number.to_alipay_dict()
            else:
                params['number'] = self.number
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
        o = ObjectTaskStatus()
        if 'basket_no' in d:
            o.basket_no = d['basket_no']
        if 'biz_object_no' in d:
            o.biz_object_no = d['biz_object_no']
        if 'number' in d:
            o.number = d['number']
        if 'status' in d:
            o.status = d['status']
        return o


