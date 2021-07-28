#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SignInfo import SignInfo


class AlipayFinancialnetPromotionApplyCreateModel(object):

    def __init__(self):
        self._apply_template_info = None
        self._apply_user_id = None
        self._asset_inst_id = None
        self._asset_resource_id = None
        self._entry_app_id = None
        self._finance_inst_iprole_id = None
        self._fund_inst_id = None
        self._org_code = None
        self._out_biz_no = None
        self._product_code = None
        self._promote_user_id = None
        self._sign_info = None

    @property
    def apply_template_info(self):
        return self._apply_template_info

    @apply_template_info.setter
    def apply_template_info(self, value):
        self._apply_template_info = value
    @property
    def apply_user_id(self):
        return self._apply_user_id

    @apply_user_id.setter
    def apply_user_id(self, value):
        self._apply_user_id = value
    @property
    def asset_inst_id(self):
        return self._asset_inst_id

    @asset_inst_id.setter
    def asset_inst_id(self, value):
        self._asset_inst_id = value
    @property
    def asset_resource_id(self):
        return self._asset_resource_id

    @asset_resource_id.setter
    def asset_resource_id(self, value):
        self._asset_resource_id = value
    @property
    def entry_app_id(self):
        return self._entry_app_id

    @entry_app_id.setter
    def entry_app_id(self, value):
        self._entry_app_id = value
    @property
    def finance_inst_iprole_id(self):
        return self._finance_inst_iprole_id

    @finance_inst_iprole_id.setter
    def finance_inst_iprole_id(self, value):
        self._finance_inst_iprole_id = value
    @property
    def fund_inst_id(self):
        return self._fund_inst_id

    @fund_inst_id.setter
    def fund_inst_id(self, value):
        self._fund_inst_id = value
    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def promote_user_id(self):
        return self._promote_user_id

    @promote_user_id.setter
    def promote_user_id(self, value):
        self._promote_user_id = value
    @property
    def sign_info(self):
        return self._sign_info

    @sign_info.setter
    def sign_info(self, value):
        if isinstance(value, SignInfo):
            self._sign_info = value
        else:
            self._sign_info = SignInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.apply_template_info:
            if hasattr(self.apply_template_info, 'to_alipay_dict'):
                params['apply_template_info'] = self.apply_template_info.to_alipay_dict()
            else:
                params['apply_template_info'] = self.apply_template_info
        if self.apply_user_id:
            if hasattr(self.apply_user_id, 'to_alipay_dict'):
                params['apply_user_id'] = self.apply_user_id.to_alipay_dict()
            else:
                params['apply_user_id'] = self.apply_user_id
        if self.asset_inst_id:
            if hasattr(self.asset_inst_id, 'to_alipay_dict'):
                params['asset_inst_id'] = self.asset_inst_id.to_alipay_dict()
            else:
                params['asset_inst_id'] = self.asset_inst_id
        if self.asset_resource_id:
            if hasattr(self.asset_resource_id, 'to_alipay_dict'):
                params['asset_resource_id'] = self.asset_resource_id.to_alipay_dict()
            else:
                params['asset_resource_id'] = self.asset_resource_id
        if self.entry_app_id:
            if hasattr(self.entry_app_id, 'to_alipay_dict'):
                params['entry_app_id'] = self.entry_app_id.to_alipay_dict()
            else:
                params['entry_app_id'] = self.entry_app_id
        if self.finance_inst_iprole_id:
            if hasattr(self.finance_inst_iprole_id, 'to_alipay_dict'):
                params['finance_inst_iprole_id'] = self.finance_inst_iprole_id.to_alipay_dict()
            else:
                params['finance_inst_iprole_id'] = self.finance_inst_iprole_id
        if self.fund_inst_id:
            if hasattr(self.fund_inst_id, 'to_alipay_dict'):
                params['fund_inst_id'] = self.fund_inst_id.to_alipay_dict()
            else:
                params['fund_inst_id'] = self.fund_inst_id
        if self.org_code:
            if hasattr(self.org_code, 'to_alipay_dict'):
                params['org_code'] = self.org_code.to_alipay_dict()
            else:
                params['org_code'] = self.org_code
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.promote_user_id:
            if hasattr(self.promote_user_id, 'to_alipay_dict'):
                params['promote_user_id'] = self.promote_user_id.to_alipay_dict()
            else:
                params['promote_user_id'] = self.promote_user_id
        if self.sign_info:
            if hasattr(self.sign_info, 'to_alipay_dict'):
                params['sign_info'] = self.sign_info.to_alipay_dict()
            else:
                params['sign_info'] = self.sign_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFinancialnetPromotionApplyCreateModel()
        if 'apply_template_info' in d:
            o.apply_template_info = d['apply_template_info']
        if 'apply_user_id' in d:
            o.apply_user_id = d['apply_user_id']
        if 'asset_inst_id' in d:
            o.asset_inst_id = d['asset_inst_id']
        if 'asset_resource_id' in d:
            o.asset_resource_id = d['asset_resource_id']
        if 'entry_app_id' in d:
            o.entry_app_id = d['entry_app_id']
        if 'finance_inst_iprole_id' in d:
            o.finance_inst_iprole_id = d['finance_inst_iprole_id']
        if 'fund_inst_id' in d:
            o.fund_inst_id = d['fund_inst_id']
        if 'org_code' in d:
            o.org_code = d['org_code']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'promote_user_id' in d:
            o.promote_user_id = d['promote_user_id']
        if 'sign_info' in d:
            o.sign_info = d['sign_info']
        return o


