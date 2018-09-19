#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsAutoCarSaveModel(object):

    def __init__(self):
        self._car_no = None
        self._user_id = None

    @property
    def car_no(self):
        return self._car_no

    @car_no.setter
    def car_no(self, value):
        self._car_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.car_no:
            if hasattr(self.car_no, 'to_alipay_dict'):
                params['car_no'] = self.car_no.to_alipay_dict()
            else:
                params['car_no'] = self.car_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsAutoCarSaveModel()
        if 'car_no' in d:
            o.car_no = d['car_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


