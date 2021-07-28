#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AmlAssetRecord(object):

    def __init__(self):
        self._active_date = None
        self._lid = None
        self._uid = None
        self._value = None

    @property
    def active_date(self):
        return self._active_date

    @active_date.setter
    def active_date(self, value):
        self._active_date = value
    @property
    def lid(self):
        return self._lid

    @lid.setter
    def lid(self, value):
        self._lid = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.active_date:
            if hasattr(self.active_date, 'to_alipay_dict'):
                params['active_date'] = self.active_date.to_alipay_dict()
            else:
                params['active_date'] = self.active_date
        if self.lid:
            if hasattr(self.lid, 'to_alipay_dict'):
                params['lid'] = self.lid.to_alipay_dict()
            else:
                params['lid'] = self.lid
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AmlAssetRecord()
        if 'active_date' in d:
            o.active_date = d['active_date']
        if 'lid' in d:
            o.lid = d['lid']
        if 'uid' in d:
            o.uid = d['uid']
        if 'value' in d:
            o.value = d['value']
        return o


