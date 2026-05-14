#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AcquirePayFlowTransDetailInfo(object):

    def __init__(self):
        self._alipay_total_amt = None
        self._alipay_total_cnt = None
        self._cash_amt = None
        self._cash_cnt = None
        self._credit_card_amt = None
        self._credit_card_cnt = None
        self._debit_card_amt = None
        self._debit_card_cnt = None
        self._fraud_amt = None
        self._fraud_cnt = None
        self._other_amt = None
        self._other_cnt = None
        self._total_amt = None
        self._total_cnt = None
        self._vintage = None
        self._wx_total_amt = None
        self._wx_total_cnt = None

    @property
    def alipay_total_amt(self):
        return self._alipay_total_amt

    @alipay_total_amt.setter
    def alipay_total_amt(self, value):
        self._alipay_total_amt = value
    @property
    def alipay_total_cnt(self):
        return self._alipay_total_cnt

    @alipay_total_cnt.setter
    def alipay_total_cnt(self, value):
        self._alipay_total_cnt = value
    @property
    def cash_amt(self):
        return self._cash_amt

    @cash_amt.setter
    def cash_amt(self, value):
        self._cash_amt = value
    @property
    def cash_cnt(self):
        return self._cash_cnt

    @cash_cnt.setter
    def cash_cnt(self, value):
        self._cash_cnt = value
    @property
    def credit_card_amt(self):
        return self._credit_card_amt

    @credit_card_amt.setter
    def credit_card_amt(self, value):
        self._credit_card_amt = value
    @property
    def credit_card_cnt(self):
        return self._credit_card_cnt

    @credit_card_cnt.setter
    def credit_card_cnt(self, value):
        self._credit_card_cnt = value
    @property
    def debit_card_amt(self):
        return self._debit_card_amt

    @debit_card_amt.setter
    def debit_card_amt(self, value):
        self._debit_card_amt = value
    @property
    def debit_card_cnt(self):
        return self._debit_card_cnt

    @debit_card_cnt.setter
    def debit_card_cnt(self, value):
        self._debit_card_cnt = value
    @property
    def fraud_amt(self):
        return self._fraud_amt

    @fraud_amt.setter
    def fraud_amt(self, value):
        self._fraud_amt = value
    @property
    def fraud_cnt(self):
        return self._fraud_cnt

    @fraud_cnt.setter
    def fraud_cnt(self, value):
        self._fraud_cnt = value
    @property
    def other_amt(self):
        return self._other_amt

    @other_amt.setter
    def other_amt(self, value):
        self._other_amt = value
    @property
    def other_cnt(self):
        return self._other_cnt

    @other_cnt.setter
    def other_cnt(self, value):
        self._other_cnt = value
    @property
    def total_amt(self):
        return self._total_amt

    @total_amt.setter
    def total_amt(self, value):
        self._total_amt = value
    @property
    def total_cnt(self):
        return self._total_cnt

    @total_cnt.setter
    def total_cnt(self, value):
        self._total_cnt = value
    @property
    def vintage(self):
        return self._vintage

    @vintage.setter
    def vintage(self, value):
        self._vintage = value
    @property
    def wx_total_amt(self):
        return self._wx_total_amt

    @wx_total_amt.setter
    def wx_total_amt(self, value):
        self._wx_total_amt = value
    @property
    def wx_total_cnt(self):
        return self._wx_total_cnt

    @wx_total_cnt.setter
    def wx_total_cnt(self, value):
        self._wx_total_cnt = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_total_amt:
            if hasattr(self.alipay_total_amt, 'to_alipay_dict'):
                params['alipay_total_amt'] = self.alipay_total_amt.to_alipay_dict()
            else:
                params['alipay_total_amt'] = self.alipay_total_amt
        if self.alipay_total_cnt:
            if hasattr(self.alipay_total_cnt, 'to_alipay_dict'):
                params['alipay_total_cnt'] = self.alipay_total_cnt.to_alipay_dict()
            else:
                params['alipay_total_cnt'] = self.alipay_total_cnt
        if self.cash_amt:
            if hasattr(self.cash_amt, 'to_alipay_dict'):
                params['cash_amt'] = self.cash_amt.to_alipay_dict()
            else:
                params['cash_amt'] = self.cash_amt
        if self.cash_cnt:
            if hasattr(self.cash_cnt, 'to_alipay_dict'):
                params['cash_cnt'] = self.cash_cnt.to_alipay_dict()
            else:
                params['cash_cnt'] = self.cash_cnt
        if self.credit_card_amt:
            if hasattr(self.credit_card_amt, 'to_alipay_dict'):
                params['credit_card_amt'] = self.credit_card_amt.to_alipay_dict()
            else:
                params['credit_card_amt'] = self.credit_card_amt
        if self.credit_card_cnt:
            if hasattr(self.credit_card_cnt, 'to_alipay_dict'):
                params['credit_card_cnt'] = self.credit_card_cnt.to_alipay_dict()
            else:
                params['credit_card_cnt'] = self.credit_card_cnt
        if self.debit_card_amt:
            if hasattr(self.debit_card_amt, 'to_alipay_dict'):
                params['debit_card_amt'] = self.debit_card_amt.to_alipay_dict()
            else:
                params['debit_card_amt'] = self.debit_card_amt
        if self.debit_card_cnt:
            if hasattr(self.debit_card_cnt, 'to_alipay_dict'):
                params['debit_card_cnt'] = self.debit_card_cnt.to_alipay_dict()
            else:
                params['debit_card_cnt'] = self.debit_card_cnt
        if self.fraud_amt:
            if hasattr(self.fraud_amt, 'to_alipay_dict'):
                params['fraud_amt'] = self.fraud_amt.to_alipay_dict()
            else:
                params['fraud_amt'] = self.fraud_amt
        if self.fraud_cnt:
            if hasattr(self.fraud_cnt, 'to_alipay_dict'):
                params['fraud_cnt'] = self.fraud_cnt.to_alipay_dict()
            else:
                params['fraud_cnt'] = self.fraud_cnt
        if self.other_amt:
            if hasattr(self.other_amt, 'to_alipay_dict'):
                params['other_amt'] = self.other_amt.to_alipay_dict()
            else:
                params['other_amt'] = self.other_amt
        if self.other_cnt:
            if hasattr(self.other_cnt, 'to_alipay_dict'):
                params['other_cnt'] = self.other_cnt.to_alipay_dict()
            else:
                params['other_cnt'] = self.other_cnt
        if self.total_amt:
            if hasattr(self.total_amt, 'to_alipay_dict'):
                params['total_amt'] = self.total_amt.to_alipay_dict()
            else:
                params['total_amt'] = self.total_amt
        if self.total_cnt:
            if hasattr(self.total_cnt, 'to_alipay_dict'):
                params['total_cnt'] = self.total_cnt.to_alipay_dict()
            else:
                params['total_cnt'] = self.total_cnt
        if self.vintage:
            if hasattr(self.vintage, 'to_alipay_dict'):
                params['vintage'] = self.vintage.to_alipay_dict()
            else:
                params['vintage'] = self.vintage
        if self.wx_total_amt:
            if hasattr(self.wx_total_amt, 'to_alipay_dict'):
                params['wx_total_amt'] = self.wx_total_amt.to_alipay_dict()
            else:
                params['wx_total_amt'] = self.wx_total_amt
        if self.wx_total_cnt:
            if hasattr(self.wx_total_cnt, 'to_alipay_dict'):
                params['wx_total_cnt'] = self.wx_total_cnt.to_alipay_dict()
            else:
                params['wx_total_cnt'] = self.wx_total_cnt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AcquirePayFlowTransDetailInfo()
        if 'alipay_total_amt' in d:
            o.alipay_total_amt = d['alipay_total_amt']
        if 'alipay_total_cnt' in d:
            o.alipay_total_cnt = d['alipay_total_cnt']
        if 'cash_amt' in d:
            o.cash_amt = d['cash_amt']
        if 'cash_cnt' in d:
            o.cash_cnt = d['cash_cnt']
        if 'credit_card_amt' in d:
            o.credit_card_amt = d['credit_card_amt']
        if 'credit_card_cnt' in d:
            o.credit_card_cnt = d['credit_card_cnt']
        if 'debit_card_amt' in d:
            o.debit_card_amt = d['debit_card_amt']
        if 'debit_card_cnt' in d:
            o.debit_card_cnt = d['debit_card_cnt']
        if 'fraud_amt' in d:
            o.fraud_amt = d['fraud_amt']
        if 'fraud_cnt' in d:
            o.fraud_cnt = d['fraud_cnt']
        if 'other_amt' in d:
            o.other_amt = d['other_amt']
        if 'other_cnt' in d:
            o.other_cnt = d['other_cnt']
        if 'total_amt' in d:
            o.total_amt = d['total_amt']
        if 'total_cnt' in d:
            o.total_cnt = d['total_cnt']
        if 'vintage' in d:
            o.vintage = d['vintage']
        if 'wx_total_amt' in d:
            o.wx_total_amt = d['wx_total_amt']
        if 'wx_total_cnt' in d:
            o.wx_total_cnt = d['wx_total_cnt']
        return o


