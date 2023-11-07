#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneInsserviceprodServiceApplyModel(object):

    def __init__(self):
        self._ant_contract_no = None
        self._apply_order_type = None
        self._biz_data = None
        self._create_time = None
        self._out_biz_no = None

    @property
    def ant_contract_no(self):
        return self._ant_contract_no

    @ant_contract_no.setter
    def ant_contract_no(self, value):
        self._ant_contract_no = value
    @property
    def apply_order_type(self):
        return self._apply_order_type

    @apply_order_type.setter
    def apply_order_type(self, value):
        self._apply_order_type = value
    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.ant_contract_no:
            if hasattr(self.ant_contract_no, 'to_alipay_dict'):
                params['ant_contract_no'] = self.ant_contract_no.to_alipay_dict()
            else:
                params['ant_contract_no'] = self.ant_contract_no
        if self.apply_order_type:
            if hasattr(self.apply_order_type, 'to_alipay_dict'):
                params['apply_order_type'] = self.apply_order_type.to_alipay_dict()
            else:
                params['apply_order_type'] = self.apply_order_type
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneInsserviceprodServiceApplyModel()
        if 'ant_contract_no' in d:
            o.ant_contract_no = d['ant_contract_no']
        if 'apply_order_type' in d:
            o.apply_order_type = d['apply_order_type']
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


