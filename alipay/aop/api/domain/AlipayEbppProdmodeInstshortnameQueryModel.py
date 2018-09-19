#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppProdmodeInstshortnameQueryModel(object):

    def __init__(self):
        self._chargeinst_cn_name = None

    @property
    def chargeinst_cn_name(self):
        return self._chargeinst_cn_name

    @chargeinst_cn_name.setter
    def chargeinst_cn_name(self, value):
        self._chargeinst_cn_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.chargeinst_cn_name:
            if hasattr(self.chargeinst_cn_name, 'to_alipay_dict'):
                params['chargeinst_cn_name'] = self.chargeinst_cn_name.to_alipay_dict()
            else:
                params['chargeinst_cn_name'] = self.chargeinst_cn_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppProdmodeInstshortnameQueryModel()
        if 'chargeinst_cn_name' in d:
            o.chargeinst_cn_name = d['chargeinst_cn_name']
        return o


