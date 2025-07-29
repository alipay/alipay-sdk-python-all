#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityDataQingliangceshiCeshioneQueryModel(object):

    def __init__(self):
        self._blance_id = None

    @property
    def blance_id(self):
        return self._blance_id

    @blance_id.setter
    def blance_id(self, value):
        self._blance_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.blance_id:
            if hasattr(self.blance_id, 'to_alipay_dict'):
                params['blance_id'] = self.blance_id.to_alipay_dict()
            else:
                params['blance_id'] = self.blance_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityDataQingliangceshiCeshioneQueryModel()
        if 'blance_id' in d:
            o.blance_id = d['blance_id']
        return o


