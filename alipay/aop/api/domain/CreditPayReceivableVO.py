#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditPayMoneyVO import CreditPayMoneyVO
from alipay.aop.api.domain.CreditPayMoneyVO import CreditPayMoneyVO
from alipay.aop.api.domain.CreditPayMoneyVO import CreditPayMoneyVO
from alipay.aop.api.domain.CreditPayUserVO import CreditPayUserVO
from alipay.aop.api.domain.CreditPayMoneyVO import CreditPayMoneyVO
from alipay.aop.api.domain.CreditPayMoneyVO import CreditPayMoneyVO
from alipay.aop.api.domain.CreditPayMoneyVO import CreditPayMoneyVO
from alipay.aop.api.domain.CreditPayMoneyVO import CreditPayMoneyVO
from alipay.aop.api.domain.CreditPayMoneyVO import CreditPayMoneyVO
from alipay.aop.api.domain.CreditPayMoneyVO import CreditPayMoneyVO


class CreditPayReceivableVO(object):

    def __init__(self):
        self._clear_date = None
        self._create_time = None
        self._due_date = None
        self._effective_date = None
        self._fee_balance_amt = None
        self._fee_dbt_amt = None
        self._freeze_amt = None
        self._grant_account = None
        self._invalid_date = None
        self._order_no = None
        self._payer = None
        self._platform_order_no = None
        self._rct_amt = None
        self._rcv_balance_amt = None
        self._receivable_amt = None
        self._refund_amt = None
        self._status = None
        self._trade_origin_amt = None
        self._transfer_amt = None

    @property
    def clear_date(self):
        return self._clear_date

    @clear_date.setter
    def clear_date(self, value):
        self._clear_date = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        self._due_date = value
    @property
    def effective_date(self):
        return self._effective_date

    @effective_date.setter
    def effective_date(self, value):
        self._effective_date = value
    @property
    def fee_balance_amt(self):
        return self._fee_balance_amt

    @fee_balance_amt.setter
    def fee_balance_amt(self, value):
        if isinstance(value, CreditPayMoneyVO):
            self._fee_balance_amt = value
        else:
            self._fee_balance_amt = CreditPayMoneyVO.from_alipay_dict(value)
    @property
    def fee_dbt_amt(self):
        return self._fee_dbt_amt

    @fee_dbt_amt.setter
    def fee_dbt_amt(self, value):
        if isinstance(value, CreditPayMoneyVO):
            self._fee_dbt_amt = value
        else:
            self._fee_dbt_amt = CreditPayMoneyVO.from_alipay_dict(value)
    @property
    def freeze_amt(self):
        return self._freeze_amt

    @freeze_amt.setter
    def freeze_amt(self, value):
        if isinstance(value, CreditPayMoneyVO):
            self._freeze_amt = value
        else:
            self._freeze_amt = CreditPayMoneyVO.from_alipay_dict(value)
    @property
    def grant_account(self):
        return self._grant_account

    @grant_account.setter
    def grant_account(self, value):
        self._grant_account = value
    @property
    def invalid_date(self):
        return self._invalid_date

    @invalid_date.setter
    def invalid_date(self, value):
        self._invalid_date = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def payer(self):
        return self._payer

    @payer.setter
    def payer(self, value):
        if isinstance(value, CreditPayUserVO):
            self._payer = value
        else:
            self._payer = CreditPayUserVO.from_alipay_dict(value)
    @property
    def platform_order_no(self):
        return self._platform_order_no

    @platform_order_no.setter
    def platform_order_no(self, value):
        self._platform_order_no = value
    @property
    def rct_amt(self):
        return self._rct_amt

    @rct_amt.setter
    def rct_amt(self, value):
        if isinstance(value, CreditPayMoneyVO):
            self._rct_amt = value
        else:
            self._rct_amt = CreditPayMoneyVO.from_alipay_dict(value)
    @property
    def rcv_balance_amt(self):
        return self._rcv_balance_amt

    @rcv_balance_amt.setter
    def rcv_balance_amt(self, value):
        if isinstance(value, CreditPayMoneyVO):
            self._rcv_balance_amt = value
        else:
            self._rcv_balance_amt = CreditPayMoneyVO.from_alipay_dict(value)
    @property
    def receivable_amt(self):
        return self._receivable_amt

    @receivable_amt.setter
    def receivable_amt(self, value):
        if isinstance(value, CreditPayMoneyVO):
            self._receivable_amt = value
        else:
            self._receivable_amt = CreditPayMoneyVO.from_alipay_dict(value)
    @property
    def refund_amt(self):
        return self._refund_amt

    @refund_amt.setter
    def refund_amt(self, value):
        if isinstance(value, CreditPayMoneyVO):
            self._refund_amt = value
        else:
            self._refund_amt = CreditPayMoneyVO.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trade_origin_amt(self):
        return self._trade_origin_amt

    @trade_origin_amt.setter
    def trade_origin_amt(self, value):
        if isinstance(value, CreditPayMoneyVO):
            self._trade_origin_amt = value
        else:
            self._trade_origin_amt = CreditPayMoneyVO.from_alipay_dict(value)
    @property
    def transfer_amt(self):
        return self._transfer_amt

    @transfer_amt.setter
    def transfer_amt(self, value):
        if isinstance(value, CreditPayMoneyVO):
            self._transfer_amt = value
        else:
            self._transfer_amt = CreditPayMoneyVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.clear_date:
            if hasattr(self.clear_date, 'to_alipay_dict'):
                params['clear_date'] = self.clear_date.to_alipay_dict()
            else:
                params['clear_date'] = self.clear_date
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.due_date:
            if hasattr(self.due_date, 'to_alipay_dict'):
                params['due_date'] = self.due_date.to_alipay_dict()
            else:
                params['due_date'] = self.due_date
        if self.effective_date:
            if hasattr(self.effective_date, 'to_alipay_dict'):
                params['effective_date'] = self.effective_date.to_alipay_dict()
            else:
                params['effective_date'] = self.effective_date
        if self.fee_balance_amt:
            if hasattr(self.fee_balance_amt, 'to_alipay_dict'):
                params['fee_balance_amt'] = self.fee_balance_amt.to_alipay_dict()
            else:
                params['fee_balance_amt'] = self.fee_balance_amt
        if self.fee_dbt_amt:
            if hasattr(self.fee_dbt_amt, 'to_alipay_dict'):
                params['fee_dbt_amt'] = self.fee_dbt_amt.to_alipay_dict()
            else:
                params['fee_dbt_amt'] = self.fee_dbt_amt
        if self.freeze_amt:
            if hasattr(self.freeze_amt, 'to_alipay_dict'):
                params['freeze_amt'] = self.freeze_amt.to_alipay_dict()
            else:
                params['freeze_amt'] = self.freeze_amt
        if self.grant_account:
            if hasattr(self.grant_account, 'to_alipay_dict'):
                params['grant_account'] = self.grant_account.to_alipay_dict()
            else:
                params['grant_account'] = self.grant_account
        if self.invalid_date:
            if hasattr(self.invalid_date, 'to_alipay_dict'):
                params['invalid_date'] = self.invalid_date.to_alipay_dict()
            else:
                params['invalid_date'] = self.invalid_date
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.payer:
            if hasattr(self.payer, 'to_alipay_dict'):
                params['payer'] = self.payer.to_alipay_dict()
            else:
                params['payer'] = self.payer
        if self.platform_order_no:
            if hasattr(self.platform_order_no, 'to_alipay_dict'):
                params['platform_order_no'] = self.platform_order_no.to_alipay_dict()
            else:
                params['platform_order_no'] = self.platform_order_no
        if self.rct_amt:
            if hasattr(self.rct_amt, 'to_alipay_dict'):
                params['rct_amt'] = self.rct_amt.to_alipay_dict()
            else:
                params['rct_amt'] = self.rct_amt
        if self.rcv_balance_amt:
            if hasattr(self.rcv_balance_amt, 'to_alipay_dict'):
                params['rcv_balance_amt'] = self.rcv_balance_amt.to_alipay_dict()
            else:
                params['rcv_balance_amt'] = self.rcv_balance_amt
        if self.receivable_amt:
            if hasattr(self.receivable_amt, 'to_alipay_dict'):
                params['receivable_amt'] = self.receivable_amt.to_alipay_dict()
            else:
                params['receivable_amt'] = self.receivable_amt
        if self.refund_amt:
            if hasattr(self.refund_amt, 'to_alipay_dict'):
                params['refund_amt'] = self.refund_amt.to_alipay_dict()
            else:
                params['refund_amt'] = self.refund_amt
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.trade_origin_amt:
            if hasattr(self.trade_origin_amt, 'to_alipay_dict'):
                params['trade_origin_amt'] = self.trade_origin_amt.to_alipay_dict()
            else:
                params['trade_origin_amt'] = self.trade_origin_amt
        if self.transfer_amt:
            if hasattr(self.transfer_amt, 'to_alipay_dict'):
                params['transfer_amt'] = self.transfer_amt.to_alipay_dict()
            else:
                params['transfer_amt'] = self.transfer_amt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditPayReceivableVO()
        if 'clear_date' in d:
            o.clear_date = d['clear_date']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'due_date' in d:
            o.due_date = d['due_date']
        if 'effective_date' in d:
            o.effective_date = d['effective_date']
        if 'fee_balance_amt' in d:
            o.fee_balance_amt = d['fee_balance_amt']
        if 'fee_dbt_amt' in d:
            o.fee_dbt_amt = d['fee_dbt_amt']
        if 'freeze_amt' in d:
            o.freeze_amt = d['freeze_amt']
        if 'grant_account' in d:
            o.grant_account = d['grant_account']
        if 'invalid_date' in d:
            o.invalid_date = d['invalid_date']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'payer' in d:
            o.payer = d['payer']
        if 'platform_order_no' in d:
            o.platform_order_no = d['platform_order_no']
        if 'rct_amt' in d:
            o.rct_amt = d['rct_amt']
        if 'rcv_balance_amt' in d:
            o.rcv_balance_amt = d['rcv_balance_amt']
        if 'receivable_amt' in d:
            o.receivable_amt = d['receivable_amt']
        if 'refund_amt' in d:
            o.refund_amt = d['refund_amt']
        if 'status' in d:
            o.status = d['status']
        if 'trade_origin_amt' in d:
            o.trade_origin_amt = d['trade_origin_amt']
        if 'transfer_amt' in d:
            o.transfer_amt = d['transfer_amt']
        return o


