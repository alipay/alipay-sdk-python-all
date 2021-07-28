#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarVehicleCertifiedQueryModel(object):

    def __init__(self):
        self._plate_no_list = None
        self._user_id = None

    @property
    def plate_no_list(self):
        return self._plate_no_list

    @plate_no_list.setter
    def plate_no_list(self, value):
        if isinstance(value, list):
            self._plate_no_list = list()
            for i in value:
                self._plate_no_list.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.plate_no_list:
            if isinstance(self.plate_no_list, list):
                for i in range(0, len(self.plate_no_list)):
                    element = self.plate_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.plate_no_list[i] = element.to_alipay_dict()
            if hasattr(self.plate_no_list, 'to_alipay_dict'):
                params['plate_no_list'] = self.plate_no_list.to_alipay_dict()
            else:
                params['plate_no_list'] = self.plate_no_list
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
        o = AlipayEcoMycarVehicleCertifiedQueryModel()
        if 'plate_no_list' in d:
            o.plate_no_list = d['plate_no_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


