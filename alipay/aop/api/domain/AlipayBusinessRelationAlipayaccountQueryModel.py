#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBusinessRelationAlipayaccountQueryModel(object):

    def __init__(self):
        self._mall_pid = None
        self._shopmember_pid = None

    @property
    def mall_pid(self):
        return self._mall_pid

    @mall_pid.setter
    def mall_pid(self, value):
        self._mall_pid = value
    @property
    def shopmember_pid(self):
        return self._shopmember_pid

    @shopmember_pid.setter
    def shopmember_pid(self, value):
        self._shopmember_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.mall_pid:
            if hasattr(self.mall_pid, 'to_alipay_dict'):
                params['mall_pid'] = self.mall_pid.to_alipay_dict()
            else:
                params['mall_pid'] = self.mall_pid
        if self.shopmember_pid:
            if hasattr(self.shopmember_pid, 'to_alipay_dict'):
                params['shopmember_pid'] = self.shopmember_pid.to_alipay_dict()
            else:
                params['shopmember_pid'] = self.shopmember_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBusinessRelationAlipayaccountQueryModel()
        if 'mall_pid' in d:
            o.mall_pid = d['mall_pid']
        if 'shopmember_pid' in d:
            o.shopmember_pid = d['shopmember_pid']
        return o


