#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnxinkaDeliverDetailResponse(object):

    def __init__(self):
        self._agent_commission = None
        self._agent_name = None
        self._card_no = None
        self._merchant_order_no = None
        self._order_id = None
        self._refund_agent_commission = None
        self._refund_amount = None
        self._refund_cash = None
        self._refund_saas_commission = None
        self._refund_time = None
        self._saas_commission = None
        self._saas_name = None
        self._settle_batch_no = None
        self._settle_pid = None
        self._settle_shop_id = None
        self._settle_shop_memo = None
        self._settle_shop_name = None
        self._third_settlement_amount = None
        self._trade_no = None
        self._use_amount = None
        self._use_cash = None
        self._use_status = None
        self._use_time = None

    @property
    def agent_commission(self):
        return self._agent_commission

    @agent_commission.setter
    def agent_commission(self, value):
        self._agent_commission = value
    @property
    def agent_name(self):
        return self._agent_name

    @agent_name.setter
    def agent_name(self, value):
        self._agent_name = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def refund_agent_commission(self):
        return self._refund_agent_commission

    @refund_agent_commission.setter
    def refund_agent_commission(self, value):
        self._refund_agent_commission = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_cash(self):
        return self._refund_cash

    @refund_cash.setter
    def refund_cash(self, value):
        self._refund_cash = value
    @property
    def refund_saas_commission(self):
        return self._refund_saas_commission

    @refund_saas_commission.setter
    def refund_saas_commission(self, value):
        self._refund_saas_commission = value
    @property
    def refund_time(self):
        return self._refund_time

    @refund_time.setter
    def refund_time(self, value):
        self._refund_time = value
    @property
    def saas_commission(self):
        return self._saas_commission

    @saas_commission.setter
    def saas_commission(self, value):
        self._saas_commission = value
    @property
    def saas_name(self):
        return self._saas_name

    @saas_name.setter
    def saas_name(self, value):
        self._saas_name = value
    @property
    def settle_batch_no(self):
        return self._settle_batch_no

    @settle_batch_no.setter
    def settle_batch_no(self, value):
        self._settle_batch_no = value
    @property
    def settle_pid(self):
        return self._settle_pid

    @settle_pid.setter
    def settle_pid(self, value):
        self._settle_pid = value
    @property
    def settle_shop_id(self):
        return self._settle_shop_id

    @settle_shop_id.setter
    def settle_shop_id(self, value):
        self._settle_shop_id = value
    @property
    def settle_shop_memo(self):
        return self._settle_shop_memo

    @settle_shop_memo.setter
    def settle_shop_memo(self, value):
        self._settle_shop_memo = value
    @property
    def settle_shop_name(self):
        return self._settle_shop_name

    @settle_shop_name.setter
    def settle_shop_name(self, value):
        self._settle_shop_name = value
    @property
    def third_settlement_amount(self):
        return self._third_settlement_amount

    @third_settlement_amount.setter
    def third_settlement_amount(self, value):
        self._third_settlement_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def use_amount(self):
        return self._use_amount

    @use_amount.setter
    def use_amount(self, value):
        self._use_amount = value
    @property
    def use_cash(self):
        return self._use_cash

    @use_cash.setter
    def use_cash(self, value):
        self._use_cash = value
    @property
    def use_status(self):
        return self._use_status

    @use_status.setter
    def use_status(self, value):
        self._use_status = value
    @property
    def use_time(self):
        return self._use_time

    @use_time.setter
    def use_time(self, value):
        self._use_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_commission:
            if hasattr(self.agent_commission, 'to_alipay_dict'):
                params['agent_commission'] = self.agent_commission.to_alipay_dict()
            else:
                params['agent_commission'] = self.agent_commission
        if self.agent_name:
            if hasattr(self.agent_name, 'to_alipay_dict'):
                params['agent_name'] = self.agent_name.to_alipay_dict()
            else:
                params['agent_name'] = self.agent_name
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.refund_agent_commission:
            if hasattr(self.refund_agent_commission, 'to_alipay_dict'):
                params['refund_agent_commission'] = self.refund_agent_commission.to_alipay_dict()
            else:
                params['refund_agent_commission'] = self.refund_agent_commission
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_cash:
            if hasattr(self.refund_cash, 'to_alipay_dict'):
                params['refund_cash'] = self.refund_cash.to_alipay_dict()
            else:
                params['refund_cash'] = self.refund_cash
        if self.refund_saas_commission:
            if hasattr(self.refund_saas_commission, 'to_alipay_dict'):
                params['refund_saas_commission'] = self.refund_saas_commission.to_alipay_dict()
            else:
                params['refund_saas_commission'] = self.refund_saas_commission
        if self.refund_time:
            if hasattr(self.refund_time, 'to_alipay_dict'):
                params['refund_time'] = self.refund_time.to_alipay_dict()
            else:
                params['refund_time'] = self.refund_time
        if self.saas_commission:
            if hasattr(self.saas_commission, 'to_alipay_dict'):
                params['saas_commission'] = self.saas_commission.to_alipay_dict()
            else:
                params['saas_commission'] = self.saas_commission
        if self.saas_name:
            if hasattr(self.saas_name, 'to_alipay_dict'):
                params['saas_name'] = self.saas_name.to_alipay_dict()
            else:
                params['saas_name'] = self.saas_name
        if self.settle_batch_no:
            if hasattr(self.settle_batch_no, 'to_alipay_dict'):
                params['settle_batch_no'] = self.settle_batch_no.to_alipay_dict()
            else:
                params['settle_batch_no'] = self.settle_batch_no
        if self.settle_pid:
            if hasattr(self.settle_pid, 'to_alipay_dict'):
                params['settle_pid'] = self.settle_pid.to_alipay_dict()
            else:
                params['settle_pid'] = self.settle_pid
        if self.settle_shop_id:
            if hasattr(self.settle_shop_id, 'to_alipay_dict'):
                params['settle_shop_id'] = self.settle_shop_id.to_alipay_dict()
            else:
                params['settle_shop_id'] = self.settle_shop_id
        if self.settle_shop_memo:
            if hasattr(self.settle_shop_memo, 'to_alipay_dict'):
                params['settle_shop_memo'] = self.settle_shop_memo.to_alipay_dict()
            else:
                params['settle_shop_memo'] = self.settle_shop_memo
        if self.settle_shop_name:
            if hasattr(self.settle_shop_name, 'to_alipay_dict'):
                params['settle_shop_name'] = self.settle_shop_name.to_alipay_dict()
            else:
                params['settle_shop_name'] = self.settle_shop_name
        if self.third_settlement_amount:
            if hasattr(self.third_settlement_amount, 'to_alipay_dict'):
                params['third_settlement_amount'] = self.third_settlement_amount.to_alipay_dict()
            else:
                params['third_settlement_amount'] = self.third_settlement_amount
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.use_amount:
            if hasattr(self.use_amount, 'to_alipay_dict'):
                params['use_amount'] = self.use_amount.to_alipay_dict()
            else:
                params['use_amount'] = self.use_amount
        if self.use_cash:
            if hasattr(self.use_cash, 'to_alipay_dict'):
                params['use_cash'] = self.use_cash.to_alipay_dict()
            else:
                params['use_cash'] = self.use_cash
        if self.use_status:
            if hasattr(self.use_status, 'to_alipay_dict'):
                params['use_status'] = self.use_status.to_alipay_dict()
            else:
                params['use_status'] = self.use_status
        if self.use_time:
            if hasattr(self.use_time, 'to_alipay_dict'):
                params['use_time'] = self.use_time.to_alipay_dict()
            else:
                params['use_time'] = self.use_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnxinkaDeliverDetailResponse()
        if 'agent_commission' in d:
            o.agent_commission = d['agent_commission']
        if 'agent_name' in d:
            o.agent_name = d['agent_name']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'refund_agent_commission' in d:
            o.refund_agent_commission = d['refund_agent_commission']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_cash' in d:
            o.refund_cash = d['refund_cash']
        if 'refund_saas_commission' in d:
            o.refund_saas_commission = d['refund_saas_commission']
        if 'refund_time' in d:
            o.refund_time = d['refund_time']
        if 'saas_commission' in d:
            o.saas_commission = d['saas_commission']
        if 'saas_name' in d:
            o.saas_name = d['saas_name']
        if 'settle_batch_no' in d:
            o.settle_batch_no = d['settle_batch_no']
        if 'settle_pid' in d:
            o.settle_pid = d['settle_pid']
        if 'settle_shop_id' in d:
            o.settle_shop_id = d['settle_shop_id']
        if 'settle_shop_memo' in d:
            o.settle_shop_memo = d['settle_shop_memo']
        if 'settle_shop_name' in d:
            o.settle_shop_name = d['settle_shop_name']
        if 'third_settlement_amount' in d:
            o.third_settlement_amount = d['third_settlement_amount']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'use_amount' in d:
            o.use_amount = d['use_amount']
        if 'use_cash' in d:
            o.use_cash = d['use_cash']
        if 'use_status' in d:
            o.use_status = d['use_status']
        if 'use_time' in d:
            o.use_time = d['use_time']
        return o


