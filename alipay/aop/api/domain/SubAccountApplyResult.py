#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubAccountApplyResult(object):

    def __init__(self):
        self._alipay_virtual_id = None

    @property
    def alipay_virtual_id(self):
        return self._alipay_virtual_id

    @alipay_virtual_id.setter
    def alipay_virtual_id(self, value):
        self._alipay_virtual_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_virtual_id:
            if hasattr(self.alipay_virtual_id, 'to_alipay_dict'):
                params['alipay_virtual_id'] = self.alipay_virtual_id.to_alipay_dict()
            else:
                params['alipay_virtual_id'] = self.alipay_virtual_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubAccountApplyResult()
        if 'alipay_virtual_id' in d:
            o.alipay_virtual_id = d['alipay_virtual_id']
        return o


