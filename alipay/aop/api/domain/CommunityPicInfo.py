#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommunityPicInfo(object):

    def __init__(self):
        self._activity_pic_list = None
        self._gate_pic_list = None
        self._inner_env_pic_list = None
        self._parking_pic_list = None

    @property
    def activity_pic_list(self):
        return self._activity_pic_list

    @activity_pic_list.setter
    def activity_pic_list(self, value):
        if isinstance(value, list):
            self._activity_pic_list = list()
            for i in value:
                self._activity_pic_list.append(i)
    @property
    def gate_pic_list(self):
        return self._gate_pic_list

    @gate_pic_list.setter
    def gate_pic_list(self, value):
        if isinstance(value, list):
            self._gate_pic_list = list()
            for i in value:
                self._gate_pic_list.append(i)
    @property
    def inner_env_pic_list(self):
        return self._inner_env_pic_list

    @inner_env_pic_list.setter
    def inner_env_pic_list(self, value):
        if isinstance(value, list):
            self._inner_env_pic_list = list()
            for i in value:
                self._inner_env_pic_list.append(i)
    @property
    def parking_pic_list(self):
        return self._parking_pic_list

    @parking_pic_list.setter
    def parking_pic_list(self, value):
        if isinstance(value, list):
            self._parking_pic_list = list()
            for i in value:
                self._parking_pic_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.activity_pic_list:
            if isinstance(self.activity_pic_list, list):
                for i in range(0, len(self.activity_pic_list)):
                    element = self.activity_pic_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activity_pic_list[i] = element.to_alipay_dict()
            if hasattr(self.activity_pic_list, 'to_alipay_dict'):
                params['activity_pic_list'] = self.activity_pic_list.to_alipay_dict()
            else:
                params['activity_pic_list'] = self.activity_pic_list
        if self.gate_pic_list:
            if isinstance(self.gate_pic_list, list):
                for i in range(0, len(self.gate_pic_list)):
                    element = self.gate_pic_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.gate_pic_list[i] = element.to_alipay_dict()
            if hasattr(self.gate_pic_list, 'to_alipay_dict'):
                params['gate_pic_list'] = self.gate_pic_list.to_alipay_dict()
            else:
                params['gate_pic_list'] = self.gate_pic_list
        if self.inner_env_pic_list:
            if isinstance(self.inner_env_pic_list, list):
                for i in range(0, len(self.inner_env_pic_list)):
                    element = self.inner_env_pic_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.inner_env_pic_list[i] = element.to_alipay_dict()
            if hasattr(self.inner_env_pic_list, 'to_alipay_dict'):
                params['inner_env_pic_list'] = self.inner_env_pic_list.to_alipay_dict()
            else:
                params['inner_env_pic_list'] = self.inner_env_pic_list
        if self.parking_pic_list:
            if isinstance(self.parking_pic_list, list):
                for i in range(0, len(self.parking_pic_list)):
                    element = self.parking_pic_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.parking_pic_list[i] = element.to_alipay_dict()
            if hasattr(self.parking_pic_list, 'to_alipay_dict'):
                params['parking_pic_list'] = self.parking_pic_list.to_alipay_dict()
            else:
                params['parking_pic_list'] = self.parking_pic_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommunityPicInfo()
        if 'activity_pic_list' in d:
            o.activity_pic_list = d['activity_pic_list']
        if 'gate_pic_list' in d:
            o.gate_pic_list = d['gate_pic_list']
        if 'inner_env_pic_list' in d:
            o.inner_env_pic_list = d['inner_env_pic_list']
        if 'parking_pic_list' in d:
            o.parking_pic_list = d['parking_pic_list']
        return o


