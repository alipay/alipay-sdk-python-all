#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalHospitalOrderUploadResult(object):

    def __init__(self):
        self._order_id_list = None
        self._out_biz_no = None
        self._trace_id = None

    @property
    def order_id_list(self):
        return self._order_id_list

    @order_id_list.setter
    def order_id_list(self, value):
        if isinstance(value, list):
            self._order_id_list = list()
            for i in value:
                self._order_id_list.append(i)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_id_list:
            if isinstance(self.order_id_list, list):
                for i in range(0, len(self.order_id_list)):
                    element = self.order_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_id_list[i] = element.to_alipay_dict()
            if hasattr(self.order_id_list, 'to_alipay_dict'):
                params['order_id_list'] = self.order_id_list.to_alipay_dict()
            else:
                params['order_id_list'] = self.order_id_list
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.trace_id:
            if hasattr(self.trace_id, 'to_alipay_dict'):
                params['trace_id'] = self.trace_id.to_alipay_dict()
            else:
                params['trace_id'] = self.trace_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalHospitalOrderUploadResult()
        if 'order_id_list' in d:
            o.order_id_list = d['order_id_list']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        return o


