#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RefundPaymentAssetInfo(object):

    def __init__(self):
        self._bank_inst_id = None
        self._origin_order_id = None
        self._receiver_asset_code = None
        self._receiver_asset_no = None
        self._receiver_logon_id = None
        self._refund_amount = None

    @property
    def bank_inst_id(self):
        return self._bank_inst_id

    @bank_inst_id.setter
    def bank_inst_id(self, value):
        self._bank_inst_id = value
    @property
    def origin_order_id(self):
        return self._origin_order_id

    @origin_order_id.setter
    def origin_order_id(self, value):
        self._origin_order_id = value
    @property
    def receiver_asset_code(self):
        return self._receiver_asset_code

    @receiver_asset_code.setter
    def receiver_asset_code(self, value):
        self._receiver_asset_code = value
    @property
    def receiver_asset_no(self):
        return self._receiver_asset_no

    @receiver_asset_no.setter
    def receiver_asset_no(self, value):
        self._receiver_asset_no = value
    @property
    def receiver_logon_id(self):
        return self._receiver_logon_id

    @receiver_logon_id.setter
    def receiver_logon_id(self, value):
        self._receiver_logon_id = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_inst_id:
            if hasattr(self.bank_inst_id, 'to_alipay_dict'):
                params['bank_inst_id'] = self.bank_inst_id.to_alipay_dict()
            else:
                params['bank_inst_id'] = self.bank_inst_id
        if self.origin_order_id:
            if hasattr(self.origin_order_id, 'to_alipay_dict'):
                params['origin_order_id'] = self.origin_order_id.to_alipay_dict()
            else:
                params['origin_order_id'] = self.origin_order_id
        if self.receiver_asset_code:
            if hasattr(self.receiver_asset_code, 'to_alipay_dict'):
                params['receiver_asset_code'] = self.receiver_asset_code.to_alipay_dict()
            else:
                params['receiver_asset_code'] = self.receiver_asset_code
        if self.receiver_asset_no:
            if hasattr(self.receiver_asset_no, 'to_alipay_dict'):
                params['receiver_asset_no'] = self.receiver_asset_no.to_alipay_dict()
            else:
                params['receiver_asset_no'] = self.receiver_asset_no
        if self.receiver_logon_id:
            if hasattr(self.receiver_logon_id, 'to_alipay_dict'):
                params['receiver_logon_id'] = self.receiver_logon_id.to_alipay_dict()
            else:
                params['receiver_logon_id'] = self.receiver_logon_id
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RefundPaymentAssetInfo()
        if 'bank_inst_id' in d:
            o.bank_inst_id = d['bank_inst_id']
        if 'origin_order_id' in d:
            o.origin_order_id = d['origin_order_id']
        if 'receiver_asset_code' in d:
            o.receiver_asset_code = d['receiver_asset_code']
        if 'receiver_asset_no' in d:
            o.receiver_asset_no = d['receiver_asset_no']
        if 'receiver_logon_id' in d:
            o.receiver_logon_id = d['receiver_logon_id']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        return o


