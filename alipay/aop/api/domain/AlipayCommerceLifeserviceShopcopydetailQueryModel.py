#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLifeserviceShopcopydetailQueryModel(object):

    def __init__(self):
        self._copy_id = None
        self._open_id = None
        self._pid = None

    @property
    def copy_id(self):
        return self._copy_id

    @copy_id.setter
    def copy_id(self, value):
        self._copy_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.copy_id:
            if hasattr(self.copy_id, 'to_alipay_dict'):
                params['copy_id'] = self.copy_id.to_alipay_dict()
            else:
                params['copy_id'] = self.copy_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLifeserviceShopcopydetailQueryModel()
        if 'copy_id' in d:
            o.copy_id = d['copy_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'pid' in d:
            o.pid = d['pid']
        return o


