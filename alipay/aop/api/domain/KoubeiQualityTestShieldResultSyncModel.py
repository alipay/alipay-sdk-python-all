#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CheckResultList import CheckResultList


class KoubeiQualityTestShieldResultSyncModel(object):

    def __init__(self):
        self._batch_no = None
        self._check_result_list = None
        self._order_id = None
        self._out_biz_no = None
        self._partner_id = None
        self._pay_style = None
        self._shop_id = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def check_result_list(self):
        return self._check_result_list

    @check_result_list.setter
    def check_result_list(self, value):
        if isinstance(value, list):
            self._check_result_list = list()
            for i in value:
                if isinstance(i, CheckResultList):
                    self._check_result_list.append(i)
                else:
                    self._check_result_list.append(CheckResultList.from_alipay_dict(i))
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def pay_style(self):
        return self._pay_style

    @pay_style.setter
    def pay_style(self, value):
        self._pay_style = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.check_result_list:
            if isinstance(self.check_result_list, list):
                for i in range(0, len(self.check_result_list)):
                    element = self.check_result_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.check_result_list[i] = element.to_alipay_dict()
            if hasattr(self.check_result_list, 'to_alipay_dict'):
                params['check_result_list'] = self.check_result_list.to_alipay_dict()
            else:
                params['check_result_list'] = self.check_result_list
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.pay_style:
            if hasattr(self.pay_style, 'to_alipay_dict'):
                params['pay_style'] = self.pay_style.to_alipay_dict()
            else:
                params['pay_style'] = self.pay_style
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiQualityTestShieldResultSyncModel()
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'check_result_list' in d:
            o.check_result_list = d['check_result_list']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'pay_style' in d:
            o.pay_style = d['pay_style']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


