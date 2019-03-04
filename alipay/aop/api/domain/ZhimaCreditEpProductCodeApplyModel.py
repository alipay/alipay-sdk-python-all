#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpProductCodeApplyModel(object):

    def __init__(self):
        self._apply_desc = None
        self._code_num = None
        self._org_biz_no = None
        self._product_list = None

    @property
    def apply_desc(self):
        return self._apply_desc

    @apply_desc.setter
    def apply_desc(self, value):
        self._apply_desc = value
    @property
    def code_num(self):
        return self._code_num

    @code_num.setter
    def code_num(self, value):
        self._code_num = value
    @property
    def org_biz_no(self):
        return self._org_biz_no

    @org_biz_no.setter
    def org_biz_no(self, value):
        self._org_biz_no = value
    @property
    def product_list(self):
        return self._product_list

    @product_list.setter
    def product_list(self, value):
        self._product_list = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_desc:
            if hasattr(self.apply_desc, 'to_alipay_dict'):
                params['apply_desc'] = self.apply_desc.to_alipay_dict()
            else:
                params['apply_desc'] = self.apply_desc
        if self.code_num:
            if hasattr(self.code_num, 'to_alipay_dict'):
                params['code_num'] = self.code_num.to_alipay_dict()
            else:
                params['code_num'] = self.code_num
        if self.org_biz_no:
            if hasattr(self.org_biz_no, 'to_alipay_dict'):
                params['org_biz_no'] = self.org_biz_no.to_alipay_dict()
            else:
                params['org_biz_no'] = self.org_biz_no
        if self.product_list:
            if hasattr(self.product_list, 'to_alipay_dict'):
                params['product_list'] = self.product_list.to_alipay_dict()
            else:
                params['product_list'] = self.product_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpProductCodeApplyModel()
        if 'apply_desc' in d:
            o.apply_desc = d['apply_desc']
        if 'code_num' in d:
            o.code_num = d['code_num']
        if 'org_biz_no' in d:
            o.org_biz_no = d['org_biz_no']
        if 'product_list' in d:
            o.product_list = d['product_list']
        return o


