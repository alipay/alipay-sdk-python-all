#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SceneProdPaymentAccountInfo(object):

    def __init__(self):
        self._account_ext_no = None
        self._account_fip_code = None
        self._account_fip_name = None
        self._account_no = None
        self._account_type = None
        self._amt = None
        self._bank_card_category = None
        self._card_holder_name = None
        self._ext_card_type = None
        self._ext_info = None
        self._inst_out_code = None
        self._ip_id = None
        self._ip_role_id = None
        self._payment_mark = None

    @property
    def account_ext_no(self):
        return self._account_ext_no

    @account_ext_no.setter
    def account_ext_no(self, value):
        self._account_ext_no = value
    @property
    def account_fip_code(self):
        return self._account_fip_code

    @account_fip_code.setter
    def account_fip_code(self, value):
        self._account_fip_code = value
    @property
    def account_fip_name(self):
        return self._account_fip_name

    @account_fip_name.setter
    def account_fip_name(self, value):
        self._account_fip_name = value
    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def amt(self):
        return self._amt

    @amt.setter
    def amt(self, value):
        self._amt = value
    @property
    def bank_card_category(self):
        return self._bank_card_category

    @bank_card_category.setter
    def bank_card_category(self, value):
        self._bank_card_category = value
    @property
    def card_holder_name(self):
        return self._card_holder_name

    @card_holder_name.setter
    def card_holder_name(self, value):
        self._card_holder_name = value
    @property
    def ext_card_type(self):
        return self._ext_card_type

    @ext_card_type.setter
    def ext_card_type(self, value):
        self._ext_card_type = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def inst_out_code(self):
        return self._inst_out_code

    @inst_out_code.setter
    def inst_out_code(self, value):
        self._inst_out_code = value
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def payment_mark(self):
        return self._payment_mark

    @payment_mark.setter
    def payment_mark(self, value):
        self._payment_mark = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_ext_no:
            if hasattr(self.account_ext_no, 'to_alipay_dict'):
                params['account_ext_no'] = self.account_ext_no.to_alipay_dict()
            else:
                params['account_ext_no'] = self.account_ext_no
        if self.account_fip_code:
            if hasattr(self.account_fip_code, 'to_alipay_dict'):
                params['account_fip_code'] = self.account_fip_code.to_alipay_dict()
            else:
                params['account_fip_code'] = self.account_fip_code
        if self.account_fip_name:
            if hasattr(self.account_fip_name, 'to_alipay_dict'):
                params['account_fip_name'] = self.account_fip_name.to_alipay_dict()
            else:
                params['account_fip_name'] = self.account_fip_name
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.amt:
            if hasattr(self.amt, 'to_alipay_dict'):
                params['amt'] = self.amt.to_alipay_dict()
            else:
                params['amt'] = self.amt
        if self.bank_card_category:
            if hasattr(self.bank_card_category, 'to_alipay_dict'):
                params['bank_card_category'] = self.bank_card_category.to_alipay_dict()
            else:
                params['bank_card_category'] = self.bank_card_category
        if self.card_holder_name:
            if hasattr(self.card_holder_name, 'to_alipay_dict'):
                params['card_holder_name'] = self.card_holder_name.to_alipay_dict()
            else:
                params['card_holder_name'] = self.card_holder_name
        if self.ext_card_type:
            if hasattr(self.ext_card_type, 'to_alipay_dict'):
                params['ext_card_type'] = self.ext_card_type.to_alipay_dict()
            else:
                params['ext_card_type'] = self.ext_card_type
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.inst_out_code:
            if hasattr(self.inst_out_code, 'to_alipay_dict'):
                params['inst_out_code'] = self.inst_out_code.to_alipay_dict()
            else:
                params['inst_out_code'] = self.inst_out_code
        if self.ip_id:
            if hasattr(self.ip_id, 'to_alipay_dict'):
                params['ip_id'] = self.ip_id.to_alipay_dict()
            else:
                params['ip_id'] = self.ip_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.payment_mark:
            if hasattr(self.payment_mark, 'to_alipay_dict'):
                params['payment_mark'] = self.payment_mark.to_alipay_dict()
            else:
                params['payment_mark'] = self.payment_mark
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SceneProdPaymentAccountInfo()
        if 'account_ext_no' in d:
            o.account_ext_no = d['account_ext_no']
        if 'account_fip_code' in d:
            o.account_fip_code = d['account_fip_code']
        if 'account_fip_name' in d:
            o.account_fip_name = d['account_fip_name']
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'amt' in d:
            o.amt = d['amt']
        if 'bank_card_category' in d:
            o.bank_card_category = d['bank_card_category']
        if 'card_holder_name' in d:
            o.card_holder_name = d['card_holder_name']
        if 'ext_card_type' in d:
            o.ext_card_type = d['ext_card_type']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'inst_out_code' in d:
            o.inst_out_code = d['inst_out_code']
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'payment_mark' in d:
            o.payment_mark = d['payment_mark']
        return o


