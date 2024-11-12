#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PayFlowTransDetailInfoModel(object):

    def __init__(self):
        self._alipay_total_amt = None
        self._alipay_total_cnt = None
        self._all_days = None
        self._cash_amt = None
        self._cash_cnt = None
        self._credit_card_amt = None
        self._credit_card_cnt = None
        self._custom_num = None
        self._debit_card_amt = None
        self._debit_card_cnt = None
        self._failed_amt = None
        self._failed_cnt = None
        self._fraud_amt = None
        self._fraud_cnt = None
        self._high_amt = None
        self._high_cnt = None
        self._high_frequency_custom = None
        self._max_amt = None
        self._max_day_amt = None
        self._max_day_cnt = None
        self._min_amt = None
        self._min_day_amt = None
        self._min_day_cnt = None
        self._night_amt = None
        self._night_cnt = None
        self._other_amt = None
        self._other_cnt = None
        self._pct_90_ord_amt = None
        self._pct_95_ord_amt = None
        self._repeat_custom = None
        self._repeat_custom_amt = None
        self._repeat_custom_cnt = None
        self._total_amt = None
        self._total_cnt = None
        self._vintage = None
        self._wee_hours_amt = None
        self._wee_hours_cnt = None
        self._weekend_amt = None
        self._weekend_cnt = None
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
    def all_days(self):
        return self._all_days

    @all_days.setter
    def all_days(self, value):
        self._all_days = value
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
    def custom_num(self):
        return self._custom_num

    @custom_num.setter
    def custom_num(self, value):
        self._custom_num = value
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
    def failed_amt(self):
        return self._failed_amt

    @failed_amt.setter
    def failed_amt(self, value):
        self._failed_amt = value
    @property
    def failed_cnt(self):
        return self._failed_cnt

    @failed_cnt.setter
    def failed_cnt(self, value):
        self._failed_cnt = value
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
    def high_amt(self):
        return self._high_amt

    @high_amt.setter
    def high_amt(self, value):
        self._high_amt = value
    @property
    def high_cnt(self):
        return self._high_cnt

    @high_cnt.setter
    def high_cnt(self, value):
        self._high_cnt = value
    @property
    def high_frequency_custom(self):
        return self._high_frequency_custom

    @high_frequency_custom.setter
    def high_frequency_custom(self, value):
        self._high_frequency_custom = value
    @property
    def max_amt(self):
        return self._max_amt

    @max_amt.setter
    def max_amt(self, value):
        self._max_amt = value
    @property
    def max_day_amt(self):
        return self._max_day_amt

    @max_day_amt.setter
    def max_day_amt(self, value):
        self._max_day_amt = value
    @property
    def max_day_cnt(self):
        return self._max_day_cnt

    @max_day_cnt.setter
    def max_day_cnt(self, value):
        self._max_day_cnt = value
    @property
    def min_amt(self):
        return self._min_amt

    @min_amt.setter
    def min_amt(self, value):
        self._min_amt = value
    @property
    def min_day_amt(self):
        return self._min_day_amt

    @min_day_amt.setter
    def min_day_amt(self, value):
        self._min_day_amt = value
    @property
    def min_day_cnt(self):
        return self._min_day_cnt

    @min_day_cnt.setter
    def min_day_cnt(self, value):
        self._min_day_cnt = value
    @property
    def night_amt(self):
        return self._night_amt

    @night_amt.setter
    def night_amt(self, value):
        self._night_amt = value
    @property
    def night_cnt(self):
        return self._night_cnt

    @night_cnt.setter
    def night_cnt(self, value):
        self._night_cnt = value
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
    def pct_90_ord_amt(self):
        return self._pct_90_ord_amt

    @pct_90_ord_amt.setter
    def pct_90_ord_amt(self, value):
        self._pct_90_ord_amt = value
    @property
    def pct_95_ord_amt(self):
        return self._pct_95_ord_amt

    @pct_95_ord_amt.setter
    def pct_95_ord_amt(self, value):
        self._pct_95_ord_amt = value
    @property
    def repeat_custom(self):
        return self._repeat_custom

    @repeat_custom.setter
    def repeat_custom(self, value):
        self._repeat_custom = value
    @property
    def repeat_custom_amt(self):
        return self._repeat_custom_amt

    @repeat_custom_amt.setter
    def repeat_custom_amt(self, value):
        self._repeat_custom_amt = value
    @property
    def repeat_custom_cnt(self):
        return self._repeat_custom_cnt

    @repeat_custom_cnt.setter
    def repeat_custom_cnt(self, value):
        self._repeat_custom_cnt = value
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
    def wee_hours_amt(self):
        return self._wee_hours_amt

    @wee_hours_amt.setter
    def wee_hours_amt(self, value):
        self._wee_hours_amt = value
    @property
    def wee_hours_cnt(self):
        return self._wee_hours_cnt

    @wee_hours_cnt.setter
    def wee_hours_cnt(self, value):
        self._wee_hours_cnt = value
    @property
    def weekend_amt(self):
        return self._weekend_amt

    @weekend_amt.setter
    def weekend_amt(self, value):
        self._weekend_amt = value
    @property
    def weekend_cnt(self):
        return self._weekend_cnt

    @weekend_cnt.setter
    def weekend_cnt(self, value):
        self._weekend_cnt = value
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
        if self.all_days:
            if hasattr(self.all_days, 'to_alipay_dict'):
                params['all_days'] = self.all_days.to_alipay_dict()
            else:
                params['all_days'] = self.all_days
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
        if self.custom_num:
            if hasattr(self.custom_num, 'to_alipay_dict'):
                params['custom_num'] = self.custom_num.to_alipay_dict()
            else:
                params['custom_num'] = self.custom_num
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
        if self.failed_amt:
            if hasattr(self.failed_amt, 'to_alipay_dict'):
                params['failed_amt'] = self.failed_amt.to_alipay_dict()
            else:
                params['failed_amt'] = self.failed_amt
        if self.failed_cnt:
            if hasattr(self.failed_cnt, 'to_alipay_dict'):
                params['failed_cnt'] = self.failed_cnt.to_alipay_dict()
            else:
                params['failed_cnt'] = self.failed_cnt
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
        if self.high_amt:
            if hasattr(self.high_amt, 'to_alipay_dict'):
                params['high_amt'] = self.high_amt.to_alipay_dict()
            else:
                params['high_amt'] = self.high_amt
        if self.high_cnt:
            if hasattr(self.high_cnt, 'to_alipay_dict'):
                params['high_cnt'] = self.high_cnt.to_alipay_dict()
            else:
                params['high_cnt'] = self.high_cnt
        if self.high_frequency_custom:
            if hasattr(self.high_frequency_custom, 'to_alipay_dict'):
                params['high_frequency_custom'] = self.high_frequency_custom.to_alipay_dict()
            else:
                params['high_frequency_custom'] = self.high_frequency_custom
        if self.max_amt:
            if hasattr(self.max_amt, 'to_alipay_dict'):
                params['max_amt'] = self.max_amt.to_alipay_dict()
            else:
                params['max_amt'] = self.max_amt
        if self.max_day_amt:
            if hasattr(self.max_day_amt, 'to_alipay_dict'):
                params['max_day_amt'] = self.max_day_amt.to_alipay_dict()
            else:
                params['max_day_amt'] = self.max_day_amt
        if self.max_day_cnt:
            if hasattr(self.max_day_cnt, 'to_alipay_dict'):
                params['max_day_cnt'] = self.max_day_cnt.to_alipay_dict()
            else:
                params['max_day_cnt'] = self.max_day_cnt
        if self.min_amt:
            if hasattr(self.min_amt, 'to_alipay_dict'):
                params['min_amt'] = self.min_amt.to_alipay_dict()
            else:
                params['min_amt'] = self.min_amt
        if self.min_day_amt:
            if hasattr(self.min_day_amt, 'to_alipay_dict'):
                params['min_day_amt'] = self.min_day_amt.to_alipay_dict()
            else:
                params['min_day_amt'] = self.min_day_amt
        if self.min_day_cnt:
            if hasattr(self.min_day_cnt, 'to_alipay_dict'):
                params['min_day_cnt'] = self.min_day_cnt.to_alipay_dict()
            else:
                params['min_day_cnt'] = self.min_day_cnt
        if self.night_amt:
            if hasattr(self.night_amt, 'to_alipay_dict'):
                params['night_amt'] = self.night_amt.to_alipay_dict()
            else:
                params['night_amt'] = self.night_amt
        if self.night_cnt:
            if hasattr(self.night_cnt, 'to_alipay_dict'):
                params['night_cnt'] = self.night_cnt.to_alipay_dict()
            else:
                params['night_cnt'] = self.night_cnt
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
        if self.pct_90_ord_amt:
            if hasattr(self.pct_90_ord_amt, 'to_alipay_dict'):
                params['pct_90_ord_amt'] = self.pct_90_ord_amt.to_alipay_dict()
            else:
                params['pct_90_ord_amt'] = self.pct_90_ord_amt
        if self.pct_95_ord_amt:
            if hasattr(self.pct_95_ord_amt, 'to_alipay_dict'):
                params['pct_95_ord_amt'] = self.pct_95_ord_amt.to_alipay_dict()
            else:
                params['pct_95_ord_amt'] = self.pct_95_ord_amt
        if self.repeat_custom:
            if hasattr(self.repeat_custom, 'to_alipay_dict'):
                params['repeat_custom'] = self.repeat_custom.to_alipay_dict()
            else:
                params['repeat_custom'] = self.repeat_custom
        if self.repeat_custom_amt:
            if hasattr(self.repeat_custom_amt, 'to_alipay_dict'):
                params['repeat_custom_amt'] = self.repeat_custom_amt.to_alipay_dict()
            else:
                params['repeat_custom_amt'] = self.repeat_custom_amt
        if self.repeat_custom_cnt:
            if hasattr(self.repeat_custom_cnt, 'to_alipay_dict'):
                params['repeat_custom_cnt'] = self.repeat_custom_cnt.to_alipay_dict()
            else:
                params['repeat_custom_cnt'] = self.repeat_custom_cnt
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
        if self.wee_hours_amt:
            if hasattr(self.wee_hours_amt, 'to_alipay_dict'):
                params['wee_hours_amt'] = self.wee_hours_amt.to_alipay_dict()
            else:
                params['wee_hours_amt'] = self.wee_hours_amt
        if self.wee_hours_cnt:
            if hasattr(self.wee_hours_cnt, 'to_alipay_dict'):
                params['wee_hours_cnt'] = self.wee_hours_cnt.to_alipay_dict()
            else:
                params['wee_hours_cnt'] = self.wee_hours_cnt
        if self.weekend_amt:
            if hasattr(self.weekend_amt, 'to_alipay_dict'):
                params['weekend_amt'] = self.weekend_amt.to_alipay_dict()
            else:
                params['weekend_amt'] = self.weekend_amt
        if self.weekend_cnt:
            if hasattr(self.weekend_cnt, 'to_alipay_dict'):
                params['weekend_cnt'] = self.weekend_cnt.to_alipay_dict()
            else:
                params['weekend_cnt'] = self.weekend_cnt
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
        o = PayFlowTransDetailInfoModel()
        if 'alipay_total_amt' in d:
            o.alipay_total_amt = d['alipay_total_amt']
        if 'alipay_total_cnt' in d:
            o.alipay_total_cnt = d['alipay_total_cnt']
        if 'all_days' in d:
            o.all_days = d['all_days']
        if 'cash_amt' in d:
            o.cash_amt = d['cash_amt']
        if 'cash_cnt' in d:
            o.cash_cnt = d['cash_cnt']
        if 'credit_card_amt' in d:
            o.credit_card_amt = d['credit_card_amt']
        if 'credit_card_cnt' in d:
            o.credit_card_cnt = d['credit_card_cnt']
        if 'custom_num' in d:
            o.custom_num = d['custom_num']
        if 'debit_card_amt' in d:
            o.debit_card_amt = d['debit_card_amt']
        if 'debit_card_cnt' in d:
            o.debit_card_cnt = d['debit_card_cnt']
        if 'failed_amt' in d:
            o.failed_amt = d['failed_amt']
        if 'failed_cnt' in d:
            o.failed_cnt = d['failed_cnt']
        if 'fraud_amt' in d:
            o.fraud_amt = d['fraud_amt']
        if 'fraud_cnt' in d:
            o.fraud_cnt = d['fraud_cnt']
        if 'high_amt' in d:
            o.high_amt = d['high_amt']
        if 'high_cnt' in d:
            o.high_cnt = d['high_cnt']
        if 'high_frequency_custom' in d:
            o.high_frequency_custom = d['high_frequency_custom']
        if 'max_amt' in d:
            o.max_amt = d['max_amt']
        if 'max_day_amt' in d:
            o.max_day_amt = d['max_day_amt']
        if 'max_day_cnt' in d:
            o.max_day_cnt = d['max_day_cnt']
        if 'min_amt' in d:
            o.min_amt = d['min_amt']
        if 'min_day_amt' in d:
            o.min_day_amt = d['min_day_amt']
        if 'min_day_cnt' in d:
            o.min_day_cnt = d['min_day_cnt']
        if 'night_amt' in d:
            o.night_amt = d['night_amt']
        if 'night_cnt' in d:
            o.night_cnt = d['night_cnt']
        if 'other_amt' in d:
            o.other_amt = d['other_amt']
        if 'other_cnt' in d:
            o.other_cnt = d['other_cnt']
        if 'pct_90_ord_amt' in d:
            o.pct_90_ord_amt = d['pct_90_ord_amt']
        if 'pct_95_ord_amt' in d:
            o.pct_95_ord_amt = d['pct_95_ord_amt']
        if 'repeat_custom' in d:
            o.repeat_custom = d['repeat_custom']
        if 'repeat_custom_amt' in d:
            o.repeat_custom_amt = d['repeat_custom_amt']
        if 'repeat_custom_cnt' in d:
            o.repeat_custom_cnt = d['repeat_custom_cnt']
        if 'total_amt' in d:
            o.total_amt = d['total_amt']
        if 'total_cnt' in d:
            o.total_cnt = d['total_cnt']
        if 'vintage' in d:
            o.vintage = d['vintage']
        if 'wee_hours_amt' in d:
            o.wee_hours_amt = d['wee_hours_amt']
        if 'wee_hours_cnt' in d:
            o.wee_hours_cnt = d['wee_hours_cnt']
        if 'weekend_amt' in d:
            o.weekend_amt = d['weekend_amt']
        if 'weekend_cnt' in d:
            o.weekend_cnt = d['weekend_cnt']
        if 'wx_total_amt' in d:
            o.wx_total_amt = d['wx_total_amt']
        if 'wx_total_cnt' in d:
            o.wx_total_cnt = d['wx_total_cnt']
        return o


