#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VenueOrderTradeInfo(object):

    def __init__(self):
        self._amount = None
        self._desc = None
        self._id = None
        self._operation_time = None
        self._partner_id = None
        self._refund_request_no = None
        self._trade_no = None
        self._trade_type = None
        self._user_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def operation_time(self):
        return self._operation_time

    @operation_time.setter
    def operation_time(self, value):
        self._operation_time = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def refund_request_no(self):
        return self._refund_request_no

    @refund_request_no.setter
    def refund_request_no(self, value):
        self._refund_request_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_type(self):
        return self._trade_type

    @trade_type.setter
    def trade_type(self, value):
        self._trade_type = value
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
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.operation_time:
            if hasattr(self.operation_time, 'to_alipay_dict'):
                params['operation_time'] = self.operation_time.to_alipay_dict()
            else:
                params['operation_time'] = self.operation_time
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.refund_request_no:
            if hasattr(self.refund_request_no, 'to_alipay_dict'):
                params['refund_request_no'] = self.refund_request_no.to_alipay_dict()
            else:
                params['refund_request_no'] = self.refund_request_no
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.trade_type:
            if hasattr(self.trade_type, 'to_alipay_dict'):
                params['trade_type'] = self.trade_type.to_alipay_dict()
            else:
                params['trade_type'] = self.trade_type
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
        o = VenueOrderTradeInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'desc' in d:
            o.desc = d['desc']
        if 'id' in d:
            o.id = d['id']
        if 'operation_time' in d:
            o.operation_time = d['operation_time']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'refund_request_no' in d:
            o.refund_request_no = d['refund_request_no']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_type' in d:
            o.trade_type = d['trade_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


