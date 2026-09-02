#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLifeserviceShopcopydetailQueryModel(object):

    def __init__(self):
        self._copy_id = None

    @property
    def copy_id(self):
        return self._copy_id

    @copy_id.setter
    def copy_id(self, value):
        self._copy_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.copy_id:
            if hasattr(self.copy_id, 'to_alipay_dict'):
                params['copy_id'] = self.copy_id.to_alipay_dict()
            else:
                params['copy_id'] = self.copy_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLifeserviceShopcopydetailQueryModel()
        if 'copy_id' in d:
            o.copy_id = d['copy_id']
        return o


