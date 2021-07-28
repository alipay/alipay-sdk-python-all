#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlipassInstanceOpInfo import AlipassInstanceOpInfo


class AlipayUserPassInstancebatchAddModel(object):

    def __init__(self):
        self._instance_op_list = None
        self._recognition_info = None
        self._recognition_type = None

    @property
    def instance_op_list(self):
        return self._instance_op_list

    @instance_op_list.setter
    def instance_op_list(self, value):
        if isinstance(value, list):
            self._instance_op_list = list()
            for i in value:
                if isinstance(i, AlipassInstanceOpInfo):
                    self._instance_op_list.append(i)
                else:
                    self._instance_op_list.append(AlipassInstanceOpInfo.from_alipay_dict(i))
    @property
    def recognition_info(self):
        return self._recognition_info

    @recognition_info.setter
    def recognition_info(self, value):
        self._recognition_info = value
    @property
    def recognition_type(self):
        return self._recognition_type

    @recognition_type.setter
    def recognition_type(self, value):
        self._recognition_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.instance_op_list:
            if isinstance(self.instance_op_list, list):
                for i in range(0, len(self.instance_op_list)):
                    element = self.instance_op_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.instance_op_list[i] = element.to_alipay_dict()
            if hasattr(self.instance_op_list, 'to_alipay_dict'):
                params['instance_op_list'] = self.instance_op_list.to_alipay_dict()
            else:
                params['instance_op_list'] = self.instance_op_list
        if self.recognition_info:
            if hasattr(self.recognition_info, 'to_alipay_dict'):
                params['recognition_info'] = self.recognition_info.to_alipay_dict()
            else:
                params['recognition_info'] = self.recognition_info
        if self.recognition_type:
            if hasattr(self.recognition_type, 'to_alipay_dict'):
                params['recognition_type'] = self.recognition_type.to_alipay_dict()
            else:
                params['recognition_type'] = self.recognition_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserPassInstancebatchAddModel()
        if 'instance_op_list' in d:
            o.instance_op_list = d['instance_op_list']
        if 'recognition_info' in d:
            o.recognition_info = d['recognition_info']
        if 'recognition_type' in d:
            o.recognition_type = d['recognition_type']
        return o


