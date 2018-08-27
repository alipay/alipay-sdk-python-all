#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditSceneprodLoanAssetTransferModel(object):

    def __init__(self):
        self._account_no = None
        self._ext_param = None
        self._finance_inst_iprole_id = None
        self._org_code = None
        self._out_order_no = None
        self._product_code = None
        self._service_inst_iprole_id = None
        self._site = None
        self._site_user_id = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def finance_inst_iprole_id(self):
        return self._finance_inst_iprole_id

    @finance_inst_iprole_id.setter
    def finance_inst_iprole_id(self, value):
        self._finance_inst_iprole_id = value
    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def service_inst_iprole_id(self):
        return self._service_inst_iprole_id

    @service_inst_iprole_id.setter
    def service_inst_iprole_id(self, value):
        self._service_inst_iprole_id = value
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
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.finance_inst_iprole_id:
            if hasattr(self.finance_inst_iprole_id, 'to_alipay_dict'):
                params['finance_inst_iprole_id'] = self.finance_inst_iprole_id.to_alipay_dict()
            else:
                params['finance_inst_iprole_id'] = self.finance_inst_iprole_id
        if self.org_code:
            if hasattr(self.org_code, 'to_alipay_dict'):
                params['org_code'] = self.org_code.to_alipay_dict()
            else:
                params['org_code'] = self.org_code
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.service_inst_iprole_id:
            if hasattr(self.service_inst_iprole_id, 'to_alipay_dict'):
                params['service_inst_iprole_id'] = self.service_inst_iprole_id.to_alipay_dict()
            else:
                params['service_inst_iprole_id'] = self.service_inst_iprole_id
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
        o = MybankCreditSceneprodLoanAssetTransferModel()
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'finance_inst_iprole_id' in d:
            o.finance_inst_iprole_id = d['finance_inst_iprole_id']
        if 'org_code' in d:
            o.org_code = d['org_code']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'service_inst_iprole_id' in d:
            o.service_inst_iprole_id = d['service_inst_iprole_id']
        if 'site' in d:
            o.site = d['site']
        if 'site_user_id' in d:
            o.site_user_id = d['site_user_id']
        return o


