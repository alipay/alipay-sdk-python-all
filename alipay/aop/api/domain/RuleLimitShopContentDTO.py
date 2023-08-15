#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RuleLimitShopContentDTO(object):

    def __init__(self):
        self._real_shop_id = None
        self._real_shop_name = None
        self._real_shop_no = None

    @property
    def real_shop_id(self):
        return self._real_shop_id

    @real_shop_id.setter
    def real_shop_id(self, value):
        self._real_shop_id = value
    @property
    def real_shop_name(self):
        return self._real_shop_name

    @real_shop_name.setter
    def real_shop_name(self, value):
        self._real_shop_name = value
    @property
    def real_shop_no(self):
        return self._real_shop_no

    @real_shop_no.setter
    def real_shop_no(self, value):
        self._real_shop_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.real_shop_id:
            if hasattr(self.real_shop_id, 'to_alipay_dict'):
                params['real_shop_id'] = self.real_shop_id.to_alipay_dict()
            else:
                params['real_shop_id'] = self.real_shop_id
        if self.real_shop_name:
            if hasattr(self.real_shop_name, 'to_alipay_dict'):
                params['real_shop_name'] = self.real_shop_name.to_alipay_dict()
            else:
                params['real_shop_name'] = self.real_shop_name
        if self.real_shop_no:
            if hasattr(self.real_shop_no, 'to_alipay_dict'):
                params['real_shop_no'] = self.real_shop_no.to_alipay_dict()
            else:
                params['real_shop_no'] = self.real_shop_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RuleLimitShopContentDTO()
        if 'real_shop_id' in d:
            o.real_shop_id = d['real_shop_id']
        if 'real_shop_name' in d:
            o.real_shop_name = d['real_shop_name']
        if 'real_shop_no' in d:
            o.real_shop_no = d['real_shop_no']
        return o


