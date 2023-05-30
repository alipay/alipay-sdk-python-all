#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCustomerLiferecordBatchqueryModel(object):

    def __init__(self):
        self._merchant_id = None
        self._open_id = None
        self._out_biz_nos = None
        self._status_list = None
        self._template_ids = None
        self._user_id = None

    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_nos(self):
        return self._out_biz_nos

    @out_biz_nos.setter
    def out_biz_nos(self, value):
        if isinstance(value, list):
            self._out_biz_nos = list()
            for i in value:
                self._out_biz_nos.append(i)
    @property
    def status_list(self):
        return self._status_list

    @status_list.setter
    def status_list(self, value):
        if isinstance(value, list):
            self._status_list = list()
            for i in value:
                self._status_list.append(i)
    @property
    def template_ids(self):
        return self._template_ids

    @template_ids.setter
    def template_ids(self, value):
        if isinstance(value, list):
            self._template_ids = list()
            for i in value:
                self._template_ids.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_nos:
            if isinstance(self.out_biz_nos, list):
                for i in range(0, len(self.out_biz_nos)):
                    element = self.out_biz_nos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_biz_nos[i] = element.to_alipay_dict()
            if hasattr(self.out_biz_nos, 'to_alipay_dict'):
                params['out_biz_nos'] = self.out_biz_nos.to_alipay_dict()
            else:
                params['out_biz_nos'] = self.out_biz_nos
        if self.status_list:
            if isinstance(self.status_list, list):
                for i in range(0, len(self.status_list)):
                    element = self.status_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.status_list[i] = element.to_alipay_dict()
            if hasattr(self.status_list, 'to_alipay_dict'):
                params['status_list'] = self.status_list.to_alipay_dict()
            else:
                params['status_list'] = self.status_list
        if self.template_ids:
            if isinstance(self.template_ids, list):
                for i in range(0, len(self.template_ids)):
                    element = self.template_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.template_ids[i] = element.to_alipay_dict()
            if hasattr(self.template_ids, 'to_alipay_dict'):
                params['template_ids'] = self.template_ids.to_alipay_dict()
            else:
                params['template_ids'] = self.template_ids
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCustomerLiferecordBatchqueryModel()
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_nos' in d:
            o.out_biz_nos = d['out_biz_nos']
        if 'status_list' in d:
            o.status_list = d['status_list']
        if 'template_ids' in d:
            o.template_ids = d['template_ids']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


