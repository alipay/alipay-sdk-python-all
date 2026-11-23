#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalServiceuserUserQueryModel(object):

    def __init__(self):
        self._hdf_user_list = None

    @property
    def hdf_user_list(self):
        return self._hdf_user_list

    @hdf_user_list.setter
    def hdf_user_list(self, value):
        if isinstance(value, list):
            self._hdf_user_list = list()
            for i in value:
                self._hdf_user_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.hdf_user_list:
            if isinstance(self.hdf_user_list, list):
                for i in range(0, len(self.hdf_user_list)):
                    element = self.hdf_user_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.hdf_user_list[i] = element.to_alipay_dict()
            if hasattr(self.hdf_user_list, 'to_alipay_dict'):
                params['hdf_user_list'] = self.hdf_user_list.to_alipay_dict()
            else:
                params['hdf_user_list'] = self.hdf_user_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalServiceuserUserQueryModel()
        if 'hdf_user_list' in d:
            o.hdf_user_list = d['hdf_user_list']
        return o


