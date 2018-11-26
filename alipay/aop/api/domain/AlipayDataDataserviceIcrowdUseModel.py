#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IcrowdUseParam import IcrowdUseParam


class AlipayDataDataserviceIcrowdUseModel(object):

    def __init__(self):
        self._icrowd_use_param = None

    @property
    def icrowd_use_param(self):
        return self._icrowd_use_param

    @icrowd_use_param.setter
    def icrowd_use_param(self, value):
        if isinstance(value, IcrowdUseParam):
            self._icrowd_use_param = value
        else:
            self._icrowd_use_param = IcrowdUseParam.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.icrowd_use_param:
            if hasattr(self.icrowd_use_param, 'to_alipay_dict'):
                params['icrowd_use_param'] = self.icrowd_use_param.to_alipay_dict()
            else:
                params['icrowd_use_param'] = self.icrowd_use_param
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceIcrowdUseModel()
        if 'icrowd_use_param' in d:
            o.icrowd_use_param = d['icrowd_use_param']
        return o


