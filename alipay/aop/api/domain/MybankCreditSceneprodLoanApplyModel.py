#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SceneExtParam import SceneExtParam


class MybankCreditSceneprodLoanApplyModel(object):

    def __init__(self):
        self._alipay_version = None
        self._back_url = None
        self._channel = None
        self._ext_param = None
        self._ext_param_info = None
        self._finance_inst_iprole_id = None
        self._loan_amt = None
        self._loan_period = None
        self._order_type = None
        self._org_code = None
        self._out_order_no = None
        self._product_code = None
        self._sales_product_code = None
        self._scene = None
        self._site = None
        self._site_user_id = None
        self._verify_id = None

    @property
    def alipay_version(self):
        return self._alipay_version

    @alipay_version.setter
    def alipay_version(self, value):
        self._alipay_version = value
    @property
    def back_url(self):
        return self._back_url

    @back_url.setter
    def back_url(self, value):
        self._back_url = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
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
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
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
    def sales_product_code(self):
        return self._sales_product_code

    @sales_product_code.setter
    def sales_product_code(self, value):
        self._sales_product_code = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
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
    def verify_id(self):
        return self._verify_id

    @verify_id.setter
    def verify_id(self, value):
        self._verify_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_version:
            if hasattr(self.alipay_version, 'to_alipay_dict'):
                params['alipay_version'] = self.alipay_version.to_alipay_dict()
            else:
                params['alipay_version'] = self.alipay_version
        if self.back_url:
            if hasattr(self.back_url, 'to_alipay_dict'):
                params['back_url'] = self.back_url.to_alipay_dict()
            else:
                params['back_url'] = self.back_url
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
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
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
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
        if self.sales_product_code:
            if hasattr(self.sales_product_code, 'to_alipay_dict'):
                params['sales_product_code'] = self.sales_product_code.to_alipay_dict()
            else:
                params['sales_product_code'] = self.sales_product_code
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
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
        if self.verify_id:
            if hasattr(self.verify_id, 'to_alipay_dict'):
                params['verify_id'] = self.verify_id.to_alipay_dict()
            else:
                params['verify_id'] = self.verify_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSceneprodLoanApplyModel()
        if 'alipay_version' in d:
            o.alipay_version = d['alipay_version']
        if 'back_url' in d:
            o.back_url = d['back_url']
        if 'channel' in d:
            o.channel = d['channel']
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
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'org_code' in d:
            o.org_code = d['org_code']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'sales_product_code' in d:
            o.sales_product_code = d['sales_product_code']
        if 'scene' in d:
            o.scene = d['scene']
        if 'site' in d:
            o.site = d['site']
        if 'site_user_id' in d:
            o.site_user_id = d['site_user_id']
        if 'verify_id' in d:
            o.verify_id = d['verify_id']
        return o


