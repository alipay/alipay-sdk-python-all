#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantQipanCrowdpoolCreateModel(object):

    def __init__(self):
        self._apply_channel_list = None
        self._crowd_code_list = None
        self._crowd_name = None
        self._operation_type = None

    @property
    def apply_channel_list(self):
        return self._apply_channel_list

    @apply_channel_list.setter
    def apply_channel_list(self, value):
        if isinstance(value, list):
            self._apply_channel_list = list()
            for i in value:
                self._apply_channel_list.append(i)
    @property
    def crowd_code_list(self):
        return self._crowd_code_list

    @crowd_code_list.setter
    def crowd_code_list(self, value):
        if isinstance(value, list):
            self._crowd_code_list = list()
            for i in value:
                self._crowd_code_list.append(i)
    @property
    def crowd_name(self):
        return self._crowd_name

    @crowd_name.setter
    def crowd_name(self, value):
        self._crowd_name = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_channel_list:
            if isinstance(self.apply_channel_list, list):
                for i in range(0, len(self.apply_channel_list)):
                    element = self.apply_channel_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.apply_channel_list[i] = element.to_alipay_dict()
            if hasattr(self.apply_channel_list, 'to_alipay_dict'):
                params['apply_channel_list'] = self.apply_channel_list.to_alipay_dict()
            else:
                params['apply_channel_list'] = self.apply_channel_list
        if self.crowd_code_list:
            if isinstance(self.crowd_code_list, list):
                for i in range(0, len(self.crowd_code_list)):
                    element = self.crowd_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.crowd_code_list[i] = element.to_alipay_dict()
            if hasattr(self.crowd_code_list, 'to_alipay_dict'):
                params['crowd_code_list'] = self.crowd_code_list.to_alipay_dict()
            else:
                params['crowd_code_list'] = self.crowd_code_list
        if self.crowd_name:
            if hasattr(self.crowd_name, 'to_alipay_dict'):
                params['crowd_name'] = self.crowd_name.to_alipay_dict()
            else:
                params['crowd_name'] = self.crowd_name
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantQipanCrowdpoolCreateModel()
        if 'apply_channel_list' in d:
            o.apply_channel_list = d['apply_channel_list']
        if 'crowd_code_list' in d:
            o.crowd_code_list = d['crowd_code_list']
        if 'crowd_name' in d:
            o.crowd_name = d['crowd_name']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        return o


