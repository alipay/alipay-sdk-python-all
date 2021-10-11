#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFinancialnetAuthFundQueryModel(object):

    def __init__(self):
        self._account_no = None
        self._bank_card_no = None
        self._biz_ext_id = None
        self._biz_ext_info = None
        self._biz_ext_type = None
        self._biz_type = None
        self._contract_id = None
        self._inst_id = None
        self._mobile_num = None
        self._product_id = None
        self._scene_id = None
        self._submit_no = None
        self._user_id = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def bank_card_no(self):
        return self._bank_card_no

    @bank_card_no.setter
    def bank_card_no(self, value):
        self._bank_card_no = value
    @property
    def biz_ext_id(self):
        return self._biz_ext_id

    @biz_ext_id.setter
    def biz_ext_id(self, value):
        self._biz_ext_id = value
    @property
    def biz_ext_info(self):
        return self._biz_ext_info

    @biz_ext_info.setter
    def biz_ext_info(self, value):
        self._biz_ext_info = value
    @property
    def biz_ext_type(self):
        return self._biz_ext_type

    @biz_ext_type.setter
    def biz_ext_type(self, value):
        self._biz_ext_type = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def contract_id(self):
        return self._contract_id

    @contract_id.setter
    def contract_id(self, value):
        self._contract_id = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def mobile_num(self):
        return self._mobile_num

    @mobile_num.setter
    def mobile_num(self, value):
        self._mobile_num = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def scene_id(self):
        return self._scene_id

    @scene_id.setter
    def scene_id(self, value):
        self._scene_id = value
    @property
    def submit_no(self):
        return self._submit_no

    @submit_no.setter
    def submit_no(self, value):
        self._submit_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.bank_card_no:
            if hasattr(self.bank_card_no, 'to_alipay_dict'):
                params['bank_card_no'] = self.bank_card_no.to_alipay_dict()
            else:
                params['bank_card_no'] = self.bank_card_no
        if self.biz_ext_id:
            if hasattr(self.biz_ext_id, 'to_alipay_dict'):
                params['biz_ext_id'] = self.biz_ext_id.to_alipay_dict()
            else:
                params['biz_ext_id'] = self.biz_ext_id
        if self.biz_ext_info:
            if hasattr(self.biz_ext_info, 'to_alipay_dict'):
                params['biz_ext_info'] = self.biz_ext_info.to_alipay_dict()
            else:
                params['biz_ext_info'] = self.biz_ext_info
        if self.biz_ext_type:
            if hasattr(self.biz_ext_type, 'to_alipay_dict'):
                params['biz_ext_type'] = self.biz_ext_type.to_alipay_dict()
            else:
                params['biz_ext_type'] = self.biz_ext_type
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.contract_id:
            if hasattr(self.contract_id, 'to_alipay_dict'):
                params['contract_id'] = self.contract_id.to_alipay_dict()
            else:
                params['contract_id'] = self.contract_id
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.mobile_num:
            if hasattr(self.mobile_num, 'to_alipay_dict'):
                params['mobile_num'] = self.mobile_num.to_alipay_dict()
            else:
                params['mobile_num'] = self.mobile_num
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.scene_id:
            if hasattr(self.scene_id, 'to_alipay_dict'):
                params['scene_id'] = self.scene_id.to_alipay_dict()
            else:
                params['scene_id'] = self.scene_id
        if self.submit_no:
            if hasattr(self.submit_no, 'to_alipay_dict'):
                params['submit_no'] = self.submit_no.to_alipay_dict()
            else:
                params['submit_no'] = self.submit_no
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
        o = AlipayFinancialnetAuthFundQueryModel()
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'bank_card_no' in d:
            o.bank_card_no = d['bank_card_no']
        if 'biz_ext_id' in d:
            o.biz_ext_id = d['biz_ext_id']
        if 'biz_ext_info' in d:
            o.biz_ext_info = d['biz_ext_info']
        if 'biz_ext_type' in d:
            o.biz_ext_type = d['biz_ext_type']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'contract_id' in d:
            o.contract_id = d['contract_id']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'mobile_num' in d:
            o.mobile_num = d['mobile_num']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'scene_id' in d:
            o.scene_id = d['scene_id']
        if 'submit_no' in d:
            o.submit_no = d['submit_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


