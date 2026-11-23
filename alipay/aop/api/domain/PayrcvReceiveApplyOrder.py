#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PayrcvReceiveApplyOrder(object):

    def __init__(self):
        self._apply_end_date = None
        self._apply_id = None
        self._apply_start_date = None
        self._inst_id = None
        self._page_num = None
        self._page_size = None
        self._receive_apply_type_list = None
        self._sales_product_code = None
        self._settle_ip_role_id = None

    @property
    def apply_end_date(self):
        return self._apply_end_date

    @apply_end_date.setter
    def apply_end_date(self, value):
        self._apply_end_date = value
    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def apply_start_date(self):
        return self._apply_start_date

    @apply_start_date.setter
    def apply_start_date(self, value):
        self._apply_start_date = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def receive_apply_type_list(self):
        return self._receive_apply_type_list

    @receive_apply_type_list.setter
    def receive_apply_type_list(self, value):
        self._receive_apply_type_list = value
    @property
    def sales_product_code(self):
        return self._sales_product_code

    @sales_product_code.setter
    def sales_product_code(self, value):
        self._sales_product_code = value
    @property
    def settle_ip_role_id(self):
        return self._settle_ip_role_id

    @settle_ip_role_id.setter
    def settle_ip_role_id(self, value):
        self._settle_ip_role_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_end_date:
            if hasattr(self.apply_end_date, 'to_alipay_dict'):
                params['apply_end_date'] = self.apply_end_date.to_alipay_dict()
            else:
                params['apply_end_date'] = self.apply_end_date
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.apply_start_date:
            if hasattr(self.apply_start_date, 'to_alipay_dict'):
                params['apply_start_date'] = self.apply_start_date.to_alipay_dict()
            else:
                params['apply_start_date'] = self.apply_start_date
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.receive_apply_type_list:
            if hasattr(self.receive_apply_type_list, 'to_alipay_dict'):
                params['receive_apply_type_list'] = self.receive_apply_type_list.to_alipay_dict()
            else:
                params['receive_apply_type_list'] = self.receive_apply_type_list
        if self.sales_product_code:
            if hasattr(self.sales_product_code, 'to_alipay_dict'):
                params['sales_product_code'] = self.sales_product_code.to_alipay_dict()
            else:
                params['sales_product_code'] = self.sales_product_code
        if self.settle_ip_role_id:
            if hasattr(self.settle_ip_role_id, 'to_alipay_dict'):
                params['settle_ip_role_id'] = self.settle_ip_role_id.to_alipay_dict()
            else:
                params['settle_ip_role_id'] = self.settle_ip_role_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PayrcvReceiveApplyOrder()
        if 'apply_end_date' in d:
            o.apply_end_date = d['apply_end_date']
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'apply_start_date' in d:
            o.apply_start_date = d['apply_start_date']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'receive_apply_type_list' in d:
            o.receive_apply_type_list = d['receive_apply_type_list']
        if 'sales_product_code' in d:
            o.sales_product_code = d['sales_product_code']
        if 'settle_ip_role_id' in d:
            o.settle_ip_role_id = d['settle_ip_role_id']
        return o


