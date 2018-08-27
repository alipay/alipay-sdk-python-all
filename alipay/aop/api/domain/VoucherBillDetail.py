#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherBillDetail(object):

    def __init__(self):
        self._amount = None
        self._biz_type = None
        self._gmt_create = None
        self._partner_id = None
        self._partner_name = None
        self._status = None
        self._trade_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def partner_name(self):
        return self._partner_name

    @partner_name.setter
    def partner_name(self, value):
        self._partner_name = value
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
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.partner_name:
            if hasattr(self.partner_name, 'to_alipay_dict'):
                params['partner_name'] = self.partner_name.to_alipay_dict()
            else:
                params['partner_name'] = self.partner_name
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
        o = VoucherBillDetail()
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'partner_name' in d:
            o.partner_name = d['partner_name']
        if 'status' in d:
            o.status = d['status']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


