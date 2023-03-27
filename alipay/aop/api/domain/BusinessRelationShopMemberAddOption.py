#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusinessRelationShopMemberAddOption(object):

    def __init__(self):
        self._biz_value = None
        self._option_type = None

    @property
    def biz_value(self):
        return self._biz_value

    @biz_value.setter
    def biz_value(self, value):
        self._biz_value = value
    @property
    def option_type(self):
        return self._option_type

    @option_type.setter
    def option_type(self, value):
        self._option_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_value:
            if hasattr(self.biz_value, 'to_alipay_dict'):
                params['biz_value'] = self.biz_value.to_alipay_dict()
            else:
                params['biz_value'] = self.biz_value
        if self.option_type:
            if hasattr(self.option_type, 'to_alipay_dict'):
                params['option_type'] = self.option_type.to_alipay_dict()
            else:
                params['option_type'] = self.option_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessRelationShopMemberAddOption()
        if 'biz_value' in d:
            o.biz_value = d['biz_value']
        if 'option_type' in d:
            o.option_type = d['option_type']
        return o


