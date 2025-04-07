#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalIndustrydataUserdoctorrelationSyncModel(object):

    def __init__(self):
        self._biz_type = None
        self._data_type = None
        self._doctor_id_list = None
        self._user_id_list = None
        self._user_id_list_open_ids = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def doctor_id_list(self):
        return self._doctor_id_list

    @doctor_id_list.setter
    def doctor_id_list(self, value):
        if isinstance(value, list):
            self._doctor_id_list = list()
            for i in value:
                self._doctor_id_list.append(i)
    @property
    def user_id_list(self):
        return self._user_id_list

    @user_id_list.setter
    def user_id_list(self, value):
        if isinstance(value, list):
            self._user_id_list = list()
            for i in value:
                self._user_id_list.append(i)
    @property
    def user_id_list_open_ids(self):
        return self._user_id_list_open_ids

    @user_id_list_open_ids.setter
    def user_id_list_open_ids(self, value):
        if isinstance(value, list):
            self._user_id_list_open_ids = list()
            for i in value:
                self._user_id_list_open_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.doctor_id_list:
            if isinstance(self.doctor_id_list, list):
                for i in range(0, len(self.doctor_id_list)):
                    element = self.doctor_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.doctor_id_list[i] = element.to_alipay_dict()
            if hasattr(self.doctor_id_list, 'to_alipay_dict'):
                params['doctor_id_list'] = self.doctor_id_list.to_alipay_dict()
            else:
                params['doctor_id_list'] = self.doctor_id_list
        if self.user_id_list:
            if isinstance(self.user_id_list, list):
                for i in range(0, len(self.user_id_list)):
                    element = self.user_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_id_list[i] = element.to_alipay_dict()
            if hasattr(self.user_id_list, 'to_alipay_dict'):
                params['user_id_list'] = self.user_id_list.to_alipay_dict()
            else:
                params['user_id_list'] = self.user_id_list
        if self.user_id_list_open_ids:
            if isinstance(self.user_id_list_open_ids, list):
                for i in range(0, len(self.user_id_list_open_ids)):
                    element = self.user_id_list_open_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_id_list_open_ids[i] = element.to_alipay_dict()
            if hasattr(self.user_id_list_open_ids, 'to_alipay_dict'):
                params['user_id_list_open_ids'] = self.user_id_list_open_ids.to_alipay_dict()
            else:
                params['user_id_list_open_ids'] = self.user_id_list_open_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalIndustrydataUserdoctorrelationSyncModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'doctor_id_list' in d:
            o.doctor_id_list = d['doctor_id_list']
        if 'user_id_list' in d:
            o.user_id_list = d['user_id_list']
        if 'user_id_list_open_ids' in d:
            o.user_id_list_open_ids = d['user_id_list_open_ids']
        return o


