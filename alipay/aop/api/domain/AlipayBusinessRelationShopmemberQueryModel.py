#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBusinessRelationShopmemberQueryModel(object):

    def __init__(self):
        self._mall_pid = None
        self._real_shop_no = None

    @property
    def mall_pid(self):
        return self._mall_pid

    @mall_pid.setter
    def mall_pid(self, value):
        self._mall_pid = value
    @property
    def real_shop_no(self):
        return self._real_shop_no

    @real_shop_no.setter
    def real_shop_no(self, value):
        self._real_shop_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.mall_pid:
            if hasattr(self.mall_pid, 'to_alipay_dict'):
                params['mall_pid'] = self.mall_pid.to_alipay_dict()
            else:
                params['mall_pid'] = self.mall_pid
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
        o = AlipayBusinessRelationShopmemberQueryModel()
        if 'mall_pid' in d:
            o.mall_pid = d['mall_pid']
        if 'real_shop_no' in d:
            o.real_shop_no = d['real_shop_no']
        return o


