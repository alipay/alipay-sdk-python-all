#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VirtualDeliverInfoVO(object):

    def __init__(self):
        self._virtual_deliver_method = None
        self._virtual_deliver_sub_method = None
        self._virtual_deliver_sub_method_description = None
        self._virtual_deliver_value = None

    @property
    def virtual_deliver_method(self):
        return self._virtual_deliver_method

    @virtual_deliver_method.setter
    def virtual_deliver_method(self, value):
        self._virtual_deliver_method = value
    @property
    def virtual_deliver_sub_method(self):
        return self._virtual_deliver_sub_method

    @virtual_deliver_sub_method.setter
    def virtual_deliver_sub_method(self, value):
        self._virtual_deliver_sub_method = value
    @property
    def virtual_deliver_sub_method_description(self):
        return self._virtual_deliver_sub_method_description

    @virtual_deliver_sub_method_description.setter
    def virtual_deliver_sub_method_description(self, value):
        self._virtual_deliver_sub_method_description = value
    @property
    def virtual_deliver_value(self):
        return self._virtual_deliver_value

    @virtual_deliver_value.setter
    def virtual_deliver_value(self, value):
        self._virtual_deliver_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.virtual_deliver_method:
            if hasattr(self.virtual_deliver_method, 'to_alipay_dict'):
                params['virtual_deliver_method'] = self.virtual_deliver_method.to_alipay_dict()
            else:
                params['virtual_deliver_method'] = self.virtual_deliver_method
        if self.virtual_deliver_sub_method:
            if hasattr(self.virtual_deliver_sub_method, 'to_alipay_dict'):
                params['virtual_deliver_sub_method'] = self.virtual_deliver_sub_method.to_alipay_dict()
            else:
                params['virtual_deliver_sub_method'] = self.virtual_deliver_sub_method
        if self.virtual_deliver_sub_method_description:
            if hasattr(self.virtual_deliver_sub_method_description, 'to_alipay_dict'):
                params['virtual_deliver_sub_method_description'] = self.virtual_deliver_sub_method_description.to_alipay_dict()
            else:
                params['virtual_deliver_sub_method_description'] = self.virtual_deliver_sub_method_description
        if self.virtual_deliver_value:
            if hasattr(self.virtual_deliver_value, 'to_alipay_dict'):
                params['virtual_deliver_value'] = self.virtual_deliver_value.to_alipay_dict()
            else:
                params['virtual_deliver_value'] = self.virtual_deliver_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VirtualDeliverInfoVO()
        if 'virtual_deliver_method' in d:
            o.virtual_deliver_method = d['virtual_deliver_method']
        if 'virtual_deliver_sub_method' in d:
            o.virtual_deliver_sub_method = d['virtual_deliver_sub_method']
        if 'virtual_deliver_sub_method_description' in d:
            o.virtual_deliver_sub_method_description = d['virtual_deliver_sub_method_description']
        if 'virtual_deliver_value' in d:
            o.virtual_deliver_value = d['virtual_deliver_value']
        return o


