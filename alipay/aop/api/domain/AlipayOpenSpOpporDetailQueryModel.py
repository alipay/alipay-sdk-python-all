#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpOpporDetailQueryModel(object):

    def __init__(self):
        self._isv_pid = None
        self._oppor_id = None

    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def oppor_id(self):
        return self._oppor_id

    @oppor_id.setter
    def oppor_id(self, value):
        self._oppor_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.oppor_id:
            if hasattr(self.oppor_id, 'to_alipay_dict'):
                params['oppor_id'] = self.oppor_id.to_alipay_dict()
            else:
                params['oppor_id'] = self.oppor_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpOpporDetailQueryModel()
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'oppor_id' in d:
            o.oppor_id = d['oppor_id']
        return o


