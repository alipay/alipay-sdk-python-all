#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditSceneprodPreadmitQueryModel(object):

    def __init__(self):
        self._customer_name = None
        self._org_code = None
        self._pre_admit_rule = None
        self._product_code = None
        self._seq_no = None
        self._site = None
        self._site_open_id = None
        self._site_user_id = None

    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value):
        self._customer_name = value
    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value
    @property
    def pre_admit_rule(self):
        return self._pre_admit_rule

    @pre_admit_rule.setter
    def pre_admit_rule(self, value):
        self._pre_admit_rule = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def seq_no(self):
        return self._seq_no

    @seq_no.setter
    def seq_no(self, value):
        self._seq_no = value
    @property
    def site(self):
        return self._site

    @site.setter
    def site(self, value):
        self._site = value
    @property
    def site_open_id(self):
        return self._site_open_id

    @site_open_id.setter
    def site_open_id(self, value):
        self._site_open_id = value
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
        if self.org_code:
            if hasattr(self.org_code, 'to_alipay_dict'):
                params['org_code'] = self.org_code.to_alipay_dict()
            else:
                params['org_code'] = self.org_code
        if self.pre_admit_rule:
            if hasattr(self.pre_admit_rule, 'to_alipay_dict'):
                params['pre_admit_rule'] = self.pre_admit_rule.to_alipay_dict()
            else:
                params['pre_admit_rule'] = self.pre_admit_rule
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.seq_no:
            if hasattr(self.seq_no, 'to_alipay_dict'):
                params['seq_no'] = self.seq_no.to_alipay_dict()
            else:
                params['seq_no'] = self.seq_no
        if self.site:
            if hasattr(self.site, 'to_alipay_dict'):
                params['site'] = self.site.to_alipay_dict()
            else:
                params['site'] = self.site
        if self.site_open_id:
            if hasattr(self.site_open_id, 'to_alipay_dict'):
                params['site_open_id'] = self.site_open_id.to_alipay_dict()
            else:
                params['site_open_id'] = self.site_open_id
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
        o = MybankCreditSceneprodPreadmitQueryModel()
        if 'customer_name' in d:
            o.customer_name = d['customer_name']
        if 'org_code' in d:
            o.org_code = d['org_code']
        if 'pre_admit_rule' in d:
            o.pre_admit_rule = d['pre_admit_rule']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'seq_no' in d:
            o.seq_no = d['seq_no']
        if 'site' in d:
            o.site = d['site']
        if 'site_open_id' in d:
            o.site_open_id = d['site_open_id']
        if 'site_user_id' in d:
            o.site_user_id = d['site_user_id']
        return o


