#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpInteopAppauthCreateModel(object):

    def __init__(self):
        self._inteop_order_no = None
        self._isv_app_id = None

    @property
    def inteop_order_no(self):
        return self._inteop_order_no

    @inteop_order_no.setter
    def inteop_order_no(self, value):
        self._inteop_order_no = value
    @property
    def isv_app_id(self):
        return self._isv_app_id

    @isv_app_id.setter
    def isv_app_id(self, value):
        self._isv_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.inteop_order_no:
            if hasattr(self.inteop_order_no, 'to_alipay_dict'):
                params['inteop_order_no'] = self.inteop_order_no.to_alipay_dict()
            else:
                params['inteop_order_no'] = self.inteop_order_no
        if self.isv_app_id:
            if hasattr(self.isv_app_id, 'to_alipay_dict'):
                params['isv_app_id'] = self.isv_app_id.to_alipay_dict()
            else:
                params['isv_app_id'] = self.isv_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpInteopAppauthCreateModel()
        if 'inteop_order_no' in d:
            o.inteop_order_no = d['inteop_order_no']
        if 'isv_app_id' in d:
            o.isv_app_id = d['isv_app_id']
        return o


