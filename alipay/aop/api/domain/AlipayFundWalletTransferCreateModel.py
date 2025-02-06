#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.WalletTransferInfo import WalletTransferInfo
from alipay.aop.api.domain.WalletTransferInfo import WalletTransferInfo


class AlipayFundWalletTransferCreateModel(object):

    def __init__(self):
        self._amount = None
        self._biz_scene = None
        self._open_id = None
        self._operate_type = None
        self._operate_user_id = None
        self._out_biz_no = None
        self._payee_fund_detail = None
        self._payer_fund_detail = None
        self._product_code = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def operate_user_id(self):
        return self._operate_user_id

    @operate_user_id.setter
    def operate_user_id(self, value):
        self._operate_user_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def payee_fund_detail(self):
        return self._payee_fund_detail

    @payee_fund_detail.setter
    def payee_fund_detail(self, value):
        if isinstance(value, WalletTransferInfo):
            self._payee_fund_detail = value
        else:
            self._payee_fund_detail = WalletTransferInfo.from_alipay_dict(value)
    @property
    def payer_fund_detail(self):
        return self._payer_fund_detail

    @payer_fund_detail.setter
    def payer_fund_detail(self, value):
        if isinstance(value, WalletTransferInfo):
            self._payer_fund_detail = value
        else:
            self._payer_fund_detail = WalletTransferInfo.from_alipay_dict(value)
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.operate_user_id:
            if hasattr(self.operate_user_id, 'to_alipay_dict'):
                params['operate_user_id'] = self.operate_user_id.to_alipay_dict()
            else:
                params['operate_user_id'] = self.operate_user_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.payee_fund_detail:
            if hasattr(self.payee_fund_detail, 'to_alipay_dict'):
                params['payee_fund_detail'] = self.payee_fund_detail.to_alipay_dict()
            else:
                params['payee_fund_detail'] = self.payee_fund_detail
        if self.payer_fund_detail:
            if hasattr(self.payer_fund_detail, 'to_alipay_dict'):
                params['payer_fund_detail'] = self.payer_fund_detail.to_alipay_dict()
            else:
                params['payer_fund_detail'] = self.payer_fund_detail
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundWalletTransferCreateModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'operate_user_id' in d:
            o.operate_user_id = d['operate_user_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'payee_fund_detail' in d:
            o.payee_fund_detail = d['payee_fund_detail']
        if 'payer_fund_detail' in d:
            o.payer_fund_detail = d['payer_fund_detail']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


