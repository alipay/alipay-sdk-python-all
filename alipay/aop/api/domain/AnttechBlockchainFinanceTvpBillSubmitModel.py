#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TrustAccountInfo import TrustAccountInfo
from alipay.aop.api.domain.TrustEntityInfo import TrustEntityInfo
from alipay.aop.api.domain.TrustEntityInfo import TrustEntityInfo


class AnttechBlockchainFinanceTvpBillSubmitModel(object):

    def __init__(self):
        self._actual_total_amount = None
        self._adjusted_amount = None
        self._bill_biz_info = None
        self._bill_name = None
        self._billing_date = None
        self._end_date = None
        self._expire_time = None
        self._original_total_amount = None
        self._out_bill_no = None
        self._payee_account = None
        self._payee_entity = None
        self._payer_entity = None
        self._product_code = None
        self._remark = None
        self._start_date = None
        self._type = None

    @property
    def actual_total_amount(self):
        return self._actual_total_amount

    @actual_total_amount.setter
    def actual_total_amount(self, value):
        self._actual_total_amount = value
    @property
    def adjusted_amount(self):
        return self._adjusted_amount

    @adjusted_amount.setter
    def adjusted_amount(self, value):
        self._adjusted_amount = value
    @property
    def bill_biz_info(self):
        return self._bill_biz_info

    @bill_biz_info.setter
    def bill_biz_info(self, value):
        self._bill_biz_info = value
    @property
    def bill_name(self):
        return self._bill_name

    @bill_name.setter
    def bill_name(self, value):
        self._bill_name = value
    @property
    def billing_date(self):
        return self._billing_date

    @billing_date.setter
    def billing_date(self, value):
        self._billing_date = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def original_total_amount(self):
        return self._original_total_amount

    @original_total_amount.setter
    def original_total_amount(self, value):
        self._original_total_amount = value
    @property
    def out_bill_no(self):
        return self._out_bill_no

    @out_bill_no.setter
    def out_bill_no(self, value):
        self._out_bill_no = value
    @property
    def payee_account(self):
        return self._payee_account

    @payee_account.setter
    def payee_account(self, value):
        if isinstance(value, TrustAccountInfo):
            self._payee_account = value
        else:
            self._payee_account = TrustAccountInfo.from_alipay_dict(value)
    @property
    def payee_entity(self):
        return self._payee_entity

    @payee_entity.setter
    def payee_entity(self, value):
        if isinstance(value, TrustEntityInfo):
            self._payee_entity = value
        else:
            self._payee_entity = TrustEntityInfo.from_alipay_dict(value)
    @property
    def payer_entity(self):
        return self._payer_entity

    @payer_entity.setter
    def payer_entity(self, value):
        if isinstance(value, TrustEntityInfo):
            self._payer_entity = value
        else:
            self._payer_entity = TrustEntityInfo.from_alipay_dict(value)
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_total_amount:
            if hasattr(self.actual_total_amount, 'to_alipay_dict'):
                params['actual_total_amount'] = self.actual_total_amount.to_alipay_dict()
            else:
                params['actual_total_amount'] = self.actual_total_amount
        if self.adjusted_amount:
            if hasattr(self.adjusted_amount, 'to_alipay_dict'):
                params['adjusted_amount'] = self.adjusted_amount.to_alipay_dict()
            else:
                params['adjusted_amount'] = self.adjusted_amount
        if self.bill_biz_info:
            if hasattr(self.bill_biz_info, 'to_alipay_dict'):
                params['bill_biz_info'] = self.bill_biz_info.to_alipay_dict()
            else:
                params['bill_biz_info'] = self.bill_biz_info
        if self.bill_name:
            if hasattr(self.bill_name, 'to_alipay_dict'):
                params['bill_name'] = self.bill_name.to_alipay_dict()
            else:
                params['bill_name'] = self.bill_name
        if self.billing_date:
            if hasattr(self.billing_date, 'to_alipay_dict'):
                params['billing_date'] = self.billing_date.to_alipay_dict()
            else:
                params['billing_date'] = self.billing_date
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.original_total_amount:
            if hasattr(self.original_total_amount, 'to_alipay_dict'):
                params['original_total_amount'] = self.original_total_amount.to_alipay_dict()
            else:
                params['original_total_amount'] = self.original_total_amount
        if self.out_bill_no:
            if hasattr(self.out_bill_no, 'to_alipay_dict'):
                params['out_bill_no'] = self.out_bill_no.to_alipay_dict()
            else:
                params['out_bill_no'] = self.out_bill_no
        if self.payee_account:
            if hasattr(self.payee_account, 'to_alipay_dict'):
                params['payee_account'] = self.payee_account.to_alipay_dict()
            else:
                params['payee_account'] = self.payee_account
        if self.payee_entity:
            if hasattr(self.payee_entity, 'to_alipay_dict'):
                params['payee_entity'] = self.payee_entity.to_alipay_dict()
            else:
                params['payee_entity'] = self.payee_entity
        if self.payer_entity:
            if hasattr(self.payer_entity, 'to_alipay_dict'):
                params['payer_entity'] = self.payer_entity.to_alipay_dict()
            else:
                params['payer_entity'] = self.payer_entity
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceTvpBillSubmitModel()
        if 'actual_total_amount' in d:
            o.actual_total_amount = d['actual_total_amount']
        if 'adjusted_amount' in d:
            o.adjusted_amount = d['adjusted_amount']
        if 'bill_biz_info' in d:
            o.bill_biz_info = d['bill_biz_info']
        if 'bill_name' in d:
            o.bill_name = d['bill_name']
        if 'billing_date' in d:
            o.billing_date = d['billing_date']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'original_total_amount' in d:
            o.original_total_amount = d['original_total_amount']
        if 'out_bill_no' in d:
            o.out_bill_no = d['out_bill_no']
        if 'payee_account' in d:
            o.payee_account = d['payee_account']
        if 'payee_entity' in d:
            o.payee_entity = d['payee_entity']
        if 'payer_entity' in d:
            o.payer_entity = d['payer_entity']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'remark' in d:
            o.remark = d['remark']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'type' in d:
            o.type = d['type']
        return o


