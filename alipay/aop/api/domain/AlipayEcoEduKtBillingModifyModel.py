#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoEduKtBillingModifyModel(object):

    def __init__(self):
        self._buyer_logon_id = None
        self._buyer_user_id = None
        self._fund_change = None
        self._gmt_refund = None
        self._out_request_no = None
        self._out_trade_no = None
        self._refund_amount = None
        self._refund_detail_item_list = None
        self._refund_reason = None
        self._status = None
        self._trade_no = None

    @property
    def buyer_logon_id(self):
        return self._buyer_logon_id

    @buyer_logon_id.setter
    def buyer_logon_id(self, value):
        self._buyer_logon_id = value
    @property
    def buyer_user_id(self):
        return self._buyer_user_id

    @buyer_user_id.setter
    def buyer_user_id(self, value):
        self._buyer_user_id = value
    @property
    def fund_change(self):
        return self._fund_change

    @fund_change.setter
    def fund_change(self, value):
        self._fund_change = value
    @property
    def gmt_refund(self):
        return self._gmt_refund

    @gmt_refund.setter
    def gmt_refund(self, value):
        self._gmt_refund = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_detail_item_list(self):
        return self._refund_detail_item_list

    @refund_detail_item_list.setter
    def refund_detail_item_list(self, value):
        self._refund_detail_item_list = value
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_logon_id:
            if hasattr(self.buyer_logon_id, 'to_alipay_dict'):
                params['buyer_logon_id'] = self.buyer_logon_id.to_alipay_dict()
            else:
                params['buyer_logon_id'] = self.buyer_logon_id
        if self.buyer_user_id:
            if hasattr(self.buyer_user_id, 'to_alipay_dict'):
                params['buyer_user_id'] = self.buyer_user_id.to_alipay_dict()
            else:
                params['buyer_user_id'] = self.buyer_user_id
        if self.fund_change:
            if hasattr(self.fund_change, 'to_alipay_dict'):
                params['fund_change'] = self.fund_change.to_alipay_dict()
            else:
                params['fund_change'] = self.fund_change
        if self.gmt_refund:
            if hasattr(self.gmt_refund, 'to_alipay_dict'):
                params['gmt_refund'] = self.gmt_refund.to_alipay_dict()
            else:
                params['gmt_refund'] = self.gmt_refund
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_detail_item_list:
            if hasattr(self.refund_detail_item_list, 'to_alipay_dict'):
                params['refund_detail_item_list'] = self.refund_detail_item_list.to_alipay_dict()
            else:
                params['refund_detail_item_list'] = self.refund_detail_item_list
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        o = AlipayEcoEduKtBillingModifyModel()
        if 'buyer_logon_id' in d:
            o.buyer_logon_id = d['buyer_logon_id']
        if 'buyer_user_id' in d:
            o.buyer_user_id = d['buyer_user_id']
        if 'fund_change' in d:
            o.fund_change = d['fund_change']
        if 'gmt_refund' in d:
            o.gmt_refund = d['gmt_refund']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_detail_item_list' in d:
            o.refund_detail_item_list = d['refund_detail_item_list']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        if 'status' in d:
            o.status = d['status']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


