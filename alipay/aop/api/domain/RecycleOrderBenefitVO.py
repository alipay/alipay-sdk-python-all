#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleOrderBenefitVO(object):

    def __init__(self):
        self._benefit_name = None
        self._benefit_node = None
        self._benefit_num = None
        self._benefit_status = None
        self._benefit_sub_type = None
        self._benefit_type = None
        self._unit_type = None

    @property
    def benefit_name(self):
        return self._benefit_name

    @benefit_name.setter
    def benefit_name(self, value):
        self._benefit_name = value
    @property
    def benefit_node(self):
        return self._benefit_node

    @benefit_node.setter
    def benefit_node(self, value):
        self._benefit_node = value
    @property
    def benefit_num(self):
        return self._benefit_num

    @benefit_num.setter
    def benefit_num(self, value):
        self._benefit_num = value
    @property
    def benefit_status(self):
        return self._benefit_status

    @benefit_status.setter
    def benefit_status(self, value):
        self._benefit_status = value
    @property
    def benefit_sub_type(self):
        return self._benefit_sub_type

    @benefit_sub_type.setter
    def benefit_sub_type(self, value):
        self._benefit_sub_type = value
    @property
    def benefit_type(self):
        return self._benefit_type

    @benefit_type.setter
    def benefit_type(self, value):
        self._benefit_type = value
    @property
    def unit_type(self):
        return self._unit_type

    @unit_type.setter
    def unit_type(self, value):
        self._unit_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_name:
            if hasattr(self.benefit_name, 'to_alipay_dict'):
                params['benefit_name'] = self.benefit_name.to_alipay_dict()
            else:
                params['benefit_name'] = self.benefit_name
        if self.benefit_node:
            if hasattr(self.benefit_node, 'to_alipay_dict'):
                params['benefit_node'] = self.benefit_node.to_alipay_dict()
            else:
                params['benefit_node'] = self.benefit_node
        if self.benefit_num:
            if hasattr(self.benefit_num, 'to_alipay_dict'):
                params['benefit_num'] = self.benefit_num.to_alipay_dict()
            else:
                params['benefit_num'] = self.benefit_num
        if self.benefit_status:
            if hasattr(self.benefit_status, 'to_alipay_dict'):
                params['benefit_status'] = self.benefit_status.to_alipay_dict()
            else:
                params['benefit_status'] = self.benefit_status
        if self.benefit_sub_type:
            if hasattr(self.benefit_sub_type, 'to_alipay_dict'):
                params['benefit_sub_type'] = self.benefit_sub_type.to_alipay_dict()
            else:
                params['benefit_sub_type'] = self.benefit_sub_type
        if self.benefit_type:
            if hasattr(self.benefit_type, 'to_alipay_dict'):
                params['benefit_type'] = self.benefit_type.to_alipay_dict()
            else:
                params['benefit_type'] = self.benefit_type
        if self.unit_type:
            if hasattr(self.unit_type, 'to_alipay_dict'):
                params['unit_type'] = self.unit_type.to_alipay_dict()
            else:
                params['unit_type'] = self.unit_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleOrderBenefitVO()
        if 'benefit_name' in d:
            o.benefit_name = d['benefit_name']
        if 'benefit_node' in d:
            o.benefit_node = d['benefit_node']
        if 'benefit_num' in d:
            o.benefit_num = d['benefit_num']
        if 'benefit_status' in d:
            o.benefit_status = d['benefit_status']
        if 'benefit_sub_type' in d:
            o.benefit_sub_type = d['benefit_sub_type']
        if 'benefit_type' in d:
            o.benefit_type = d['benefit_type']
        if 'unit_type' in d:
            o.unit_type = d['unit_type']
        return o


