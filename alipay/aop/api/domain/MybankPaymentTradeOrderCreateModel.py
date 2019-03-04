#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BkPosGoodsInfo import BkPosGoodsInfo


class MybankPaymentTradeOrderCreateModel(object):

    def __init__(self):
        self._currency_code = None
        self._ev_code = None
        self._goods_info = None
        self._out_trade_no = None
        self._partner_id = None
        self._pay_date = None
        self._pay_type = None
        self._pd_code = None
        self._recon_related_no = None
        self._remark = None
        self._seller_id = None
        self._total_amount = None

    @property
    def currency_code(self):
        return self._currency_code

    @currency_code.setter
    def currency_code(self, value):
        self._currency_code = value
    @property
    def ev_code(self):
        return self._ev_code

    @ev_code.setter
    def ev_code(self, value):
        self._ev_code = value
    @property
    def goods_info(self):
        return self._goods_info

    @goods_info.setter
    def goods_info(self, value):
        if isinstance(value, list):
            self._goods_info = list()
            for i in value:
                if isinstance(i, BkPosGoodsInfo):
                    self._goods_info.append(i)
                else:
                    self._goods_info.append(BkPosGoodsInfo.from_alipay_dict(i))
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def pay_date(self):
        return self._pay_date

    @pay_date.setter
    def pay_date(self, value):
        self._pay_date = value
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def pd_code(self):
        return self._pd_code

    @pd_code.setter
    def pd_code(self, value):
        self._pd_code = value
    @property
    def recon_related_no(self):
        return self._recon_related_no

    @recon_related_no.setter
    def recon_related_no(self, value):
        self._recon_related_no = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.currency_code:
            if hasattr(self.currency_code, 'to_alipay_dict'):
                params['currency_code'] = self.currency_code.to_alipay_dict()
            else:
                params['currency_code'] = self.currency_code
        if self.ev_code:
            if hasattr(self.ev_code, 'to_alipay_dict'):
                params['ev_code'] = self.ev_code.to_alipay_dict()
            else:
                params['ev_code'] = self.ev_code
        if self.goods_info:
            if isinstance(self.goods_info, list):
                for i in range(0, len(self.goods_info)):
                    element = self.goods_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_info[i] = element.to_alipay_dict()
            if hasattr(self.goods_info, 'to_alipay_dict'):
                params['goods_info'] = self.goods_info.to_alipay_dict()
            else:
                params['goods_info'] = self.goods_info
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.pay_date:
            if hasattr(self.pay_date, 'to_alipay_dict'):
                params['pay_date'] = self.pay_date.to_alipay_dict()
            else:
                params['pay_date'] = self.pay_date
        if self.pay_type:
            if hasattr(self.pay_type, 'to_alipay_dict'):
                params['pay_type'] = self.pay_type.to_alipay_dict()
            else:
                params['pay_type'] = self.pay_type
        if self.pd_code:
            if hasattr(self.pd_code, 'to_alipay_dict'):
                params['pd_code'] = self.pd_code.to_alipay_dict()
            else:
                params['pd_code'] = self.pd_code
        if self.recon_related_no:
            if hasattr(self.recon_related_no, 'to_alipay_dict'):
                params['recon_related_no'] = self.recon_related_no.to_alipay_dict()
            else:
                params['recon_related_no'] = self.recon_related_no
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankPaymentTradeOrderCreateModel()
        if 'currency_code' in d:
            o.currency_code = d['currency_code']
        if 'ev_code' in d:
            o.ev_code = d['ev_code']
        if 'goods_info' in d:
            o.goods_info = d['goods_info']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'pay_date' in d:
            o.pay_date = d['pay_date']
        if 'pay_type' in d:
            o.pay_type = d['pay_type']
        if 'pd_code' in d:
            o.pd_code = d['pd_code']
        if 'recon_related_no' in d:
            o.recon_related_no = d['recon_related_no']
        if 'remark' in d:
            o.remark = d['remark']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


