#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DefaultInCartInfo import DefaultInCartInfo


class KbdishRuleInfo(object):

    def __init__(self):
        self._biz_type = None
        self._default_in_cart_info = None
        self._dish_id = None
        self._ext_info = None
        self._rule_type = None
        self._rule_value = None
        self._sku_id = None
        self._status = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def default_in_cart_info(self):
        return self._default_in_cart_info

    @default_in_cart_info.setter
    def default_in_cart_info(self, value):
        if isinstance(value, DefaultInCartInfo):
            self._default_in_cart_info = value
        else:
            self._default_in_cart_info = DefaultInCartInfo.from_alipay_dict(value)
    @property
    def dish_id(self):
        return self._dish_id

    @dish_id.setter
    def dish_id(self, value):
        self._dish_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def rule_type(self):
        return self._rule_type

    @rule_type.setter
    def rule_type(self, value):
        self._rule_type = value
    @property
    def rule_value(self):
        return self._rule_value

    @rule_value.setter
    def rule_value(self, value):
        if isinstance(value, list):
            self._rule_value = list()
            for i in value:
                self._rule_value.append(i)
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.default_in_cart_info:
            if hasattr(self.default_in_cart_info, 'to_alipay_dict'):
                params['default_in_cart_info'] = self.default_in_cart_info.to_alipay_dict()
            else:
                params['default_in_cart_info'] = self.default_in_cart_info
        if self.dish_id:
            if hasattr(self.dish_id, 'to_alipay_dict'):
                params['dish_id'] = self.dish_id.to_alipay_dict()
            else:
                params['dish_id'] = self.dish_id
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.rule_type:
            if hasattr(self.rule_type, 'to_alipay_dict'):
                params['rule_type'] = self.rule_type.to_alipay_dict()
            else:
                params['rule_type'] = self.rule_type
        if self.rule_value:
            if isinstance(self.rule_value, list):
                for i in range(0, len(self.rule_value)):
                    element = self.rule_value[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rule_value[i] = element.to_alipay_dict()
            if hasattr(self.rule_value, 'to_alipay_dict'):
                params['rule_value'] = self.rule_value.to_alipay_dict()
            else:
                params['rule_value'] = self.rule_value
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishRuleInfo()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'default_in_cart_info' in d:
            o.default_in_cart_info = d['default_in_cart_info']
        if 'dish_id' in d:
            o.dish_id = d['dish_id']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'rule_type' in d:
            o.rule_type = d['rule_type']
        if 'rule_value' in d:
            o.rule_value = d['rule_value']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'status' in d:
            o.status = d['status']
        return o


