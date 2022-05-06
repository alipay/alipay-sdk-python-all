#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceYuntaskHunterReceiveModel(object):

    def __init__(self):
        self._hunter_id = None
        self._merchant_pid = None
        self._out_biz_no = None
        self._shop_id = None
        self._source = None
        self._task_template_id = None

    @property
    def hunter_id(self):
        return self._hunter_id

    @hunter_id.setter
    def hunter_id(self, value):
        self._hunter_id = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def task_template_id(self):
        return self._task_template_id

    @task_template_id.setter
    def task_template_id(self, value):
        self._task_template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.hunter_id:
            if hasattr(self.hunter_id, 'to_alipay_dict'):
                params['hunter_id'] = self.hunter_id.to_alipay_dict()
            else:
                params['hunter_id'] = self.hunter_id
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.task_template_id:
            if hasattr(self.task_template_id, 'to_alipay_dict'):
                params['task_template_id'] = self.task_template_id.to_alipay_dict()
            else:
                params['task_template_id'] = self.task_template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceYuntaskHunterReceiveModel()
        if 'hunter_id' in d:
            o.hunter_id = d['hunter_id']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'source' in d:
            o.source = d['source']
        if 'task_template_id' in d:
            o.task_template_id = d['task_template_id']
        return o


