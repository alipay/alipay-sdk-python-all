#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SceneExtParam import SceneExtParam


class MybankCreditSceneprodLoanModifyModel(object):

    def __init__(self):
        self._ext_param = None
        self._ext_param_info = None
        self._finance_inst_iprole_id = None
        self._loan_amt = None
        self._loan_period = None
        self._org_code = None
        self._out_order_no = None
        self._product_code = None
        self._site = None
        self._site_user_id = None
        self._status = None

    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def ext_param_info(self):
        return self._ext_param_info

    @ext_param_info.setter
    def ext_param_info(self, value):
        if isinstance(value, SceneExtParam):
            self._ext_param_info = value
        else:
            self._ext_param_info = SceneExtParam.from_alipay_dict(value)
    @property
    def finance_inst_iprole_id(self):
        return self._finance_inst_iprole_id

    @finance_inst_iprole_id.setter
    def finance_inst_iprole_id(self, value):
        self._finance_inst_iprole_id = value
    @property
    def loan_amt(self):
        return self._loan_amt

    @loan_amt.setter
    def loan_amt(self, value):
        self._loan_amt = value
    @property
    def loan_period(self):
        return self._loan_period

    @loan_period.setter
    def loan_period(self, value):
        self._loan_period = value
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
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.ext_param_info:
            if hasattr(self.ext_param_info, 'to_alipay_dict'):
                params['ext_param_info'] = self.ext_param_info.to_alipay_dict()
            else:
                params['ext_param_info'] = self.ext_param_info
        if self.finance_inst_iprole_id:
            if hasattr(self.finance_inst_iprole_id, 'to_alipay_dict'):
                params['finance_inst_iprole_id'] = self.finance_inst_iprole_id.to_alipay_dict()
            else:
                params['finance_inst_iprole_id'] = self.finance_inst_iprole_id
        if self.loan_amt:
            if hasattr(self.loan_amt, 'to_alipay_dict'):
                params['loan_amt'] = self.loan_amt.to_alipay_dict()
            else:
                params['loan_amt'] = self.loan_amt
        if self.loan_period:
            if hasattr(self.loan_period, 'to_alipay_dict'):
                params['loan_period'] = self.loan_period.to_alipay_dict()
            else:
                params['loan_period'] = self.loan_period
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
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSceneprodLoanModifyModel()
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'ext_param_info' in d:
            o.ext_param_info = d['ext_param_info']
        if 'finance_inst_iprole_id' in d:
            o.finance_inst_iprole_id = d['finance_inst_iprole_id']
        if 'loan_amt' in d:
            o.loan_amt = d['loan_amt']
        if 'loan_period' in d:
            o.loan_period = d['loan_period']
        if 'org_code' in d:
            o.org_code = d['org_code']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'site' in d:
            o.site = d['site']
        if 'site_user_id' in d:
            o.site_user_id = d['site_user_id']
        if 'status' in d:
            o.status = d['status']
        return o


