#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SceneProdPaymentAccountInfo import SceneProdPaymentAccountInfo


class MybankCreditSceneprodDrawdownApplyModel(object):

    def __init__(self):
        self._customer_name = None
        self._mybk_order_no = None
        self._operate_type = None
        self._out_order_no = None
        self._out_param = None
        self._out_seq_no = None
        self._payment_detail_list = None
        self._site = None
        self._site_user_id = None

    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value):
        self._customer_name = value
    @property
    def mybk_order_no(self):
        return self._mybk_order_no

    @mybk_order_no.setter
    def mybk_order_no(self, value):
        self._mybk_order_no = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def out_param(self):
        return self._out_param

    @out_param.setter
    def out_param(self, value):
        self._out_param = value
    @property
    def out_seq_no(self):
        return self._out_seq_no

    @out_seq_no.setter
    def out_seq_no(self, value):
        self._out_seq_no = value
    @property
    def payment_detail_list(self):
        return self._payment_detail_list

    @payment_detail_list.setter
    def payment_detail_list(self, value):
        if isinstance(value, list):
            self._payment_detail_list = list()
            for i in value:
                if isinstance(i, SceneProdPaymentAccountInfo):
                    self._payment_detail_list.append(i)
                else:
                    self._payment_detail_list.append(SceneProdPaymentAccountInfo.from_alipay_dict(i))
    @property
    def site(self):
        return self._site

    @site.setter
    def site(self, value):
        self._site = value
    @property
    def site_user_id(self):
        return self._site_user_id

    @site_user_id.setter
    def site_user_id(self, value):
        self._site_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.customer_name:
            if hasattr(self.customer_name, 'to_alipay_dict'):
                params['customer_name'] = self.customer_name.to_alipay_dict()
            else:
                params['customer_name'] = self.customer_name
        if self.mybk_order_no:
            if hasattr(self.mybk_order_no, 'to_alipay_dict'):
                params['mybk_order_no'] = self.mybk_order_no.to_alipay_dict()
            else:
                params['mybk_order_no'] = self.mybk_order_no
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.out_param:
            if hasattr(self.out_param, 'to_alipay_dict'):
                params['out_param'] = self.out_param.to_alipay_dict()
            else:
                params['out_param'] = self.out_param
        if self.out_seq_no:
            if hasattr(self.out_seq_no, 'to_alipay_dict'):
                params['out_seq_no'] = self.out_seq_no.to_alipay_dict()
            else:
                params['out_seq_no'] = self.out_seq_no
        if self.payment_detail_list:
            if isinstance(self.payment_detail_list, list):
                for i in range(0, len(self.payment_detail_list)):
                    element = self.payment_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.payment_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.payment_detail_list, 'to_alipay_dict'):
                params['payment_detail_list'] = self.payment_detail_list.to_alipay_dict()
            else:
                params['payment_detail_list'] = self.payment_detail_list
        if self.site:
            if hasattr(self.site, 'to_alipay_dict'):
                params['site'] = self.site.to_alipay_dict()
            else:
                params['site'] = self.site
        if self.site_user_id:
            if hasattr(self.site_user_id, 'to_alipay_dict'):
                params['site_user_id'] = self.site_user_id.to_alipay_dict()
            else:
                params['site_user_id'] = self.site_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSceneprodDrawdownApplyModel()
        if 'customer_name' in d:
            o.customer_name = d['customer_name']
        if 'mybk_order_no' in d:
            o.mybk_order_no = d['mybk_order_no']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'out_param' in d:
            o.out_param = d['out_param']
        if 'out_seq_no' in d:
            o.out_seq_no = d['out_seq_no']
        if 'payment_detail_list' in d:
            o.payment_detail_list = d['payment_detail_list']
        if 'site' in d:
            o.site = d['site']
        if 'site_user_id' in d:
            o.site_user_id = d['site_user_id']
        return o


