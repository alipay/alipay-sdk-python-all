#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdAfsrcVulQueryModel(object):

    def __init__(self):
        self._vul_id = None

    @property
    def vul_id(self):
        return self._vul_id

    @vul_id.setter
    def vul_id(self, value):
        self._vul_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.vul_id:
            if hasattr(self.vul_id, 'to_alipay_dict'):
                params['vul_id'] = self.vul_id.to_alipay_dict()
            else:
                params['vul_id'] = self.vul_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdAfsrcVulQueryModel()
        if 'vul_id' in d:
            o.vul_id = d['vul_id']
        return o


