#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoyagerEnvInfo import VoyagerEnvInfo
from alipay.aop.api.domain.VoyagerFeedbackRecord import VoyagerFeedbackRecord


class AlipayVoyagerMarketingFeedbackModel(object):

    def __init__(self):
        self._city_code = None
        self._env_info = None
        self._last_spm = None
        self._open_id = None
        self._record_list = None
        self._src_spm = None
        self._user_id = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def env_info(self):
        return self._env_info

    @env_info.setter
    def env_info(self, value):
        if isinstance(value, VoyagerEnvInfo):
            self._env_info = value
        else:
            self._env_info = VoyagerEnvInfo.from_alipay_dict(value)
    @property
    def last_spm(self):
        return self._last_spm

    @last_spm.setter
    def last_spm(self, value):
        self._last_spm = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def record_list(self):
        return self._record_list

    @record_list.setter
    def record_list(self, value):
        if isinstance(value, list):
            self._record_list = list()
            for i in value:
                if isinstance(i, VoyagerFeedbackRecord):
                    self._record_list.append(i)
                else:
                    self._record_list.append(VoyagerFeedbackRecord.from_alipay_dict(i))
    @property
    def src_spm(self):
        return self._src_spm

    @src_spm.setter
    def src_spm(self, value):
        self._src_spm = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.env_info:
            if hasattr(self.env_info, 'to_alipay_dict'):
                params['env_info'] = self.env_info.to_alipay_dict()
            else:
                params['env_info'] = self.env_info
        if self.last_spm:
            if hasattr(self.last_spm, 'to_alipay_dict'):
                params['last_spm'] = self.last_spm.to_alipay_dict()
            else:
                params['last_spm'] = self.last_spm
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.record_list:
            if isinstance(self.record_list, list):
                for i in range(0, len(self.record_list)):
                    element = self.record_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.record_list[i] = element.to_alipay_dict()
            if hasattr(self.record_list, 'to_alipay_dict'):
                params['record_list'] = self.record_list.to_alipay_dict()
            else:
                params['record_list'] = self.record_list
        if self.src_spm:
            if hasattr(self.src_spm, 'to_alipay_dict'):
                params['src_spm'] = self.src_spm.to_alipay_dict()
            else:
                params['src_spm'] = self.src_spm
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
        o = AlipayVoyagerMarketingFeedbackModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'env_info' in d:
            o.env_info = d['env_info']
        if 'last_spm' in d:
            o.last_spm = d['last_spm']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'record_list' in d:
            o.record_list = d['record_list']
        if 'src_spm' in d:
            o.src_spm = d['src_spm']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


