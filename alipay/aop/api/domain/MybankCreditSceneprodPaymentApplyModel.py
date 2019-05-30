#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SceneProdPaymentAccountInfo import SceneProdPaymentAccountInfo
from alipay.aop.api.domain.SceneProdPaymentAccountInfo import SceneProdPaymentAccountInfo


class MybankCreditSceneprodPaymentApplyModel(object):

    def __init__(self):
        self._amount = None
        self._biz_product_code = None
        self._biz_type = None
        self._cust_name = None
        self._drawdown_no = None
        self._id_card = None
        self._login_account = None
        self._mybk_order_no = None
        self._out_order_no = None
        self._out_param = None
        self._out_seq_no = None
        self._payee_account_list = None
        self._payer_account_list = None
        self._payment_product_code = None
        self._user_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_product_code(self):
        return self._biz_product_code

    @biz_product_code.setter
    def biz_product_code(self, value):
        self._biz_product_code = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def cust_name(self):
        return self._cust_name

    @cust_name.setter
    def cust_name(self, value):
        self._cust_name = value
    @property
    def drawdown_no(self):
        return self._drawdown_no

    @drawdown_no.setter
    def drawdown_no(self, value):
        self._drawdown_no = value
    @property
    def id_card(self):
        return self._id_card

    @id_card.setter
    def id_card(self, value):
        self._id_card = value
    @property
    def login_account(self):
        return self._login_account

    @login_account.setter
    def login_account(self, value):
        self._login_account = value
    @property
    def mybk_order_no(self):
        return self._mybk_order_no

    @mybk_order_no.setter
    def mybk_order_no(self, value):
        self._mybk_order_no = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def out_param(self):
        return self._out_param

    @out_param.setter
    def out_param(self, value):
        self._out_param = value
    @property
    def out_seq_no(self):
        return self._out_seq_no

    @out_seq_no.setter
    def out_seq_no(self, value):
        self._out_seq_no = value
    @property
    def payee_account_list(self):
        return self._payee_account_list

    @payee_account_list.setter
    def payee_account_list(self, value):
        if isinstance(value, list):
            self._payee_account_list = list()
            for i in value:
                if isinstance(i, SceneProdPaymentAccountInfo):
                    self._payee_account_list.append(i)
                else:
                    self._payee_account_list.append(SceneProdPaymentAccountInfo.from_alipay_dict(i))
    @property
    def payer_account_list(self):
        return self._payer_account_list

    @payer_account_list.setter
    def payer_account_list(self, value):
        if isinstance(value, list):
            self._payer_account_list = list()
            for i in value:
                if isinstance(i, SceneProdPaymentAccountInfo):
                    self._payer_account_list.append(i)
                else:
                    self._payer_account_list.append(SceneProdPaymentAccountInfo.from_alipay_dict(i))
    @property
    def payment_product_code(self):
        return self._payment_product_code

    @payment_product_code.setter
    def payment_product_code(self, value):
        self._payment_product_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.biz_product_code:
            if hasattr(self.biz_product_code, 'to_alipay_dict'):
                params['biz_product_code'] = self.biz_product_code.to_alipay_dict()
            else:
                params['biz_product_code'] = self.biz_product_code
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.cust_name:
            if hasattr(self.cust_name, 'to_alipay_dict'):
                params['cust_name'] = self.cust_name.to_alipay_dict()
            else:
                params['cust_name'] = self.cust_name
        if self.drawdown_no:
            if hasattr(self.drawdown_no, 'to_alipay_dict'):
                params['drawdown_no'] = self.drawdown_no.to_alipay_dict()
            else:
                params['drawdown_no'] = self.drawdown_no
        if self.id_card:
            if hasattr(self.id_card, 'to_alipay_dict'):
                params['id_card'] = self.id_card.to_alipay_dict()
            else:
                params['id_card'] = self.id_card
        if self.login_account:
            if hasattr(self.login_account, 'to_alipay_dict'):
                params['login_account'] = self.login_account.to_alipay_dict()
            else:
                params['login_account'] = self.login_account
        if self.mybk_order_no:
            if hasattr(self.mybk_order_no, 'to_alipay_dict'):
                params['mybk_order_no'] = self.mybk_order_no.to_alipay_dict()
            else:
                params['mybk_order_no'] = self.mybk_order_no
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.out_param:
            if hasattr(self.out_param, 'to_alipay_dict'):
                params['out_param'] = self.out_param.to_alipay_dict()
            else:
                params['out_param'] = self.out_param
        if self.out_seq_no:
            if hasattr(self.out_seq_no, 'to_alipay_dict'):
                params['out_seq_no'] = self.out_seq_no.to_alipay_dict()
            else:
                params['out_seq_no'] = self.out_seq_no
        if self.payee_account_list:
            if isinstance(self.payee_account_list, list):
                for i in range(0, len(self.payee_account_list)):
                    element = self.payee_account_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.payee_account_list[i] = element.to_alipay_dict()
            if hasattr(self.payee_account_list, 'to_alipay_dict'):
                params['payee_account_list'] = self.payee_account_list.to_alipay_dict()
            else:
                params['payee_account_list'] = self.payee_account_list
        if self.payer_account_list:
            if isinstance(self.payer_account_list, list):
                for i in range(0, len(self.payer_account_list)):
                    element = self.payer_account_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.payer_account_list[i] = element.to_alipay_dict()
            if hasattr(self.payer_account_list, 'to_alipay_dict'):
                params['payer_account_list'] = self.payer_account_list.to_alipay_dict()
            else:
                params['payer_account_list'] = self.payer_account_list
        if self.payment_product_code:
            if hasattr(self.payment_product_code, 'to_alipay_dict'):
                params['payment_product_code'] = self.payment_product_code.to_alipay_dict()
            else:
                params['payment_product_code'] = self.payment_product_code
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
        o = MybankCreditSceneprodPaymentApplyModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_product_code' in d:
            o.biz_product_code = d['biz_product_code']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'cust_name' in d:
            o.cust_name = d['cust_name']
        if 'drawdown_no' in d:
            o.drawdown_no = d['drawdown_no']
        if 'id_card' in d:
            o.id_card = d['id_card']
        if 'login_account' in d:
            o.login_account = d['login_account']
        if 'mybk_order_no' in d:
            o.mybk_order_no = d['mybk_order_no']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'out_param' in d:
            o.out_param = d['out_param']
        if 'out_seq_no' in d:
            o.out_seq_no = d['out_seq_no']
        if 'payee_account_list' in d:
            o.payee_account_list = d['payee_account_list']
        if 'payer_account_list' in d:
            o.payer_account_list = d['payer_account_list']
        if 'payment_product_code' in d:
            o.payment_product_code = d['payment_product_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


