#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHmServiceitemQueryModel(object):

    def __init__(self):
        self._package_order_id = None

    @property
    def package_order_id(self):
        return self._package_order_id

    @package_order_id.setter
    def package_order_id(self, value):
        self._package_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.package_order_id:
            if hasattr(self.package_order_id, 'to_alipay_dict'):
                params['package_order_id'] = self.package_order_id.to_alipay_dict()
            else:
                params['package_order_id'] = self.package_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHmServiceitemQueryModel()
        if 'package_order_id' in d:
            o.package_order_id = d['package_order_id']
        return o


