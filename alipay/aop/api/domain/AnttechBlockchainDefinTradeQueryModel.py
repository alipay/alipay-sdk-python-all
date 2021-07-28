#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SystemParam import SystemParam


class AnttechBlockchainDefinTradeQueryModel(object):

    def __init__(self):
        self._encoded_biz_param = None
        self._sys_param = None

    @property
    def encoded_biz_param(self):
        return self._encoded_biz_param

    @encoded_biz_param.setter
    def encoded_biz_param(self, value):
        self._encoded_biz_param = value
    @property
    def sys_param(self):
        return self._sys_param

    @sys_param.setter
    def sys_param(self, value):
        if isinstance(value, SystemParam):
            self._sys_param = value
        else:
            self._sys_param = SystemParam.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.encoded_biz_param:
            if hasattr(self.encoded_biz_param, 'to_alipay_dict'):
                params['encoded_biz_param'] = self.encoded_biz_param.to_alipay_dict()
            else:
                params['encoded_biz_param'] = self.encoded_biz_param
        if self.sys_param:
            if hasattr(self.sys_param, 'to_alipay_dict'):
                params['sys_param'] = self.sys_param.to_alipay_dict()
            else:
                params['sys_param'] = self.sys_param
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainDefinTradeQueryModel()
        if 'encoded_biz_param' in d:
            o.encoded_biz_param = d['encoded_biz_param']
        if 'sys_param' in d:
            o.sys_param = d['sys_param']
        return o


