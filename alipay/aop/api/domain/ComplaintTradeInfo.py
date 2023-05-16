#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ComplaintTradeInfo(object):

    def __init__(self):
        self._amount = None
        self._complaint_record_id = None
        self._gmt_refund = None
        self._gmt_trade = None
        self._id = None
        self._out_no = None
        self._status = None
        self._status_description = None
        self._trade_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def complaint_record_id(self):
        return self._complaint_record_id

    @complaint_record_id.setter
    def complaint_record_id(self, value):
        self._complaint_record_id = value
    @property
    def gmt_refund(self):
        return self._gmt_refund

    @gmt_refund.setter
    def gmt_refund(self, value):
        self._gmt_refund = value
    @property
    def gmt_trade(self):
        return self._gmt_trade

    @gmt_trade.setter
    def gmt_trade(self, value):
        self._gmt_trade = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def out_no(self):
        return self._out_no

    @out_no.setter
    def out_no(self, value):
        self._out_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_description(self):
        return self._status_description

    @status_description.setter
    def status_description(self, value):
        self._status_description = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.complaint_record_id:
            if hasattr(self.complaint_record_id, 'to_alipay_dict'):
                params['complaint_record_id'] = self.complaint_record_id.to_alipay_dict()
            else:
                params['complaint_record_id'] = self.complaint_record_id
        if self.gmt_refund:
            if hasattr(self.gmt_refund, 'to_alipay_dict'):
                params['gmt_refund'] = self.gmt_refund.to_alipay_dict()
            else:
                params['gmt_refund'] = self.gmt_refund
        if self.gmt_trade:
            if hasattr(self.gmt_trade, 'to_alipay_dict'):
                params['gmt_trade'] = self.gmt_trade.to_alipay_dict()
            else:
                params['gmt_trade'] = self.gmt_trade
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.out_no:
            if hasattr(self.out_no, 'to_alipay_dict'):
                params['out_no'] = self.out_no.to_alipay_dict()
            else:
                params['out_no'] = self.out_no
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_description:
            if hasattr(self.status_description, 'to_alipay_dict'):
                params['status_description'] = self.status_description.to_alipay_dict()
            else:
                params['status_description'] = self.status_description
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
        o = ComplaintTradeInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'complaint_record_id' in d:
            o.complaint_record_id = d['complaint_record_id']
        if 'gmt_refund' in d:
            o.gmt_refund = d['gmt_refund']
        if 'gmt_trade' in d:
            o.gmt_trade = d['gmt_trade']
        if 'id' in d:
            o.id = d['id']
        if 'out_no' in d:
            o.out_no = d['out_no']
        if 'status' in d:
            o.status = d['status']
        if 'status_description' in d:
            o.status_description = d['status_description']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


