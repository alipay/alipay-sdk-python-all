#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsPreOrdeNotifyDTO(object):

    def __init__(self):
        self._out_employee_biz_no = None
        self._pre_order_id = None

    @property
    def out_employee_biz_no(self):
        return self._out_employee_biz_no

    @out_employee_biz_no.setter
    def out_employee_biz_no(self, value):
        self._out_employee_biz_no = value
    @property
    def pre_order_id(self):
        return self._pre_order_id

    @pre_order_id.setter
    def pre_order_id(self, value):
        self._pre_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_employee_biz_no:
            if hasattr(self.out_employee_biz_no, 'to_alipay_dict'):
                params['out_employee_biz_no'] = self.out_employee_biz_no.to_alipay_dict()
            else:
                params['out_employee_biz_no'] = self.out_employee_biz_no
        if self.pre_order_id:
            if hasattr(self.pre_order_id, 'to_alipay_dict'):
                params['pre_order_id'] = self.pre_order_id.to_alipay_dict()
            else:
                params['pre_order_id'] = self.pre_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsPreOrdeNotifyDTO()
        if 'out_employee_biz_no' in d:
            o.out_employee_biz_no = d['out_employee_biz_no']
        if 'pre_order_id' in d:
            o.pre_order_id = d['pre_order_id']
        return o


