#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentRefundTransVO import RentRefundTransVO


class RentRefundInfoVO(object):

    def __init__(self):
        self._out_trade_no = None
        self._pay_amount = None
        self._rent_refund_trans_infos = None
        self._trade_no = None

    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def rent_refund_trans_infos(self):
        return self._rent_refund_trans_infos

    @rent_refund_trans_infos.setter
    def rent_refund_trans_infos(self, value):
        if isinstance(value, list):
            self._rent_refund_trans_infos = list()
            for i in value:
                if isinstance(i, RentRefundTransVO):
                    self._rent_refund_trans_infos.append(i)
                else:
                    self._rent_refund_trans_infos.append(RentRefundTransVO.from_alipay_dict(i))
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.rent_refund_trans_infos:
            if isinstance(self.rent_refund_trans_infos, list):
                for i in range(0, len(self.rent_refund_trans_infos)):
                    element = self.rent_refund_trans_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rent_refund_trans_infos[i] = element.to_alipay_dict()
            if hasattr(self.rent_refund_trans_infos, 'to_alipay_dict'):
                params['rent_refund_trans_infos'] = self.rent_refund_trans_infos.to_alipay_dict()
            else:
                params['rent_refund_trans_infos'] = self.rent_refund_trans_infos
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentRefundInfoVO()
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'rent_refund_trans_infos' in d:
            o.rent_refund_trans_infos = d['rent_refund_trans_infos']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


