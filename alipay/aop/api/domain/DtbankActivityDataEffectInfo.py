#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DtbankActivityDataEffectInfo(object):

    def __init__(self):
        self._avg_order_write_off_discount_amt = None
        self._avg_user_write_off_discount_amt = None
        self._data_update_time = None
        self._total_camp_refund_amt = None
        self._total_expire_amt = None
        self._total_expire_cnt = None
        self._total_order_refund_cnt = None
        self._total_receive_amt = None
        self._total_receive_times = None
        self._total_receive_user_cnt = None
        self._total_write_off_discount_amt = None
        self._total_write_off_order_cnt = None
        self._total_write_off_user_cnt = None

    @property
    def avg_order_write_off_discount_amt(self):
        return self._avg_order_write_off_discount_amt

    @avg_order_write_off_discount_amt.setter
    def avg_order_write_off_discount_amt(self, value):
        self._avg_order_write_off_discount_amt = value
    @property
    def avg_user_write_off_discount_amt(self):
        return self._avg_user_write_off_discount_amt

    @avg_user_write_off_discount_amt.setter
    def avg_user_write_off_discount_amt(self, value):
        self._avg_user_write_off_discount_amt = value
    @property
    def data_update_time(self):
        return self._data_update_time

    @data_update_time.setter
    def data_update_time(self, value):
        self._data_update_time = value
    @property
    def total_camp_refund_amt(self):
        return self._total_camp_refund_amt

    @total_camp_refund_amt.setter
    def total_camp_refund_amt(self, value):
        self._total_camp_refund_amt = value
    @property
    def total_expire_amt(self):
        return self._total_expire_amt

    @total_expire_amt.setter
    def total_expire_amt(self, value):
        self._total_expire_amt = value
    @property
    def total_expire_cnt(self):
        return self._total_expire_cnt

    @total_expire_cnt.setter
    def total_expire_cnt(self, value):
        self._total_expire_cnt = value
    @property
    def total_order_refund_cnt(self):
        return self._total_order_refund_cnt

    @total_order_refund_cnt.setter
    def total_order_refund_cnt(self, value):
        self._total_order_refund_cnt = value
    @property
    def total_receive_amt(self):
        return self._total_receive_amt

    @total_receive_amt.setter
    def total_receive_amt(self, value):
        self._total_receive_amt = value
    @property
    def total_receive_times(self):
        return self._total_receive_times

    @total_receive_times.setter
    def total_receive_times(self, value):
        self._total_receive_times = value
    @property
    def total_receive_user_cnt(self):
        return self._total_receive_user_cnt

    @total_receive_user_cnt.setter
    def total_receive_user_cnt(self, value):
        self._total_receive_user_cnt = value
    @property
    def total_write_off_discount_amt(self):
        return self._total_write_off_discount_amt

    @total_write_off_discount_amt.setter
    def total_write_off_discount_amt(self, value):
        self._total_write_off_discount_amt = value
    @property
    def total_write_off_order_cnt(self):
        return self._total_write_off_order_cnt

    @total_write_off_order_cnt.setter
    def total_write_off_order_cnt(self, value):
        self._total_write_off_order_cnt = value
    @property
    def total_write_off_user_cnt(self):
        return self._total_write_off_user_cnt

    @total_write_off_user_cnt.setter
    def total_write_off_user_cnt(self, value):
        self._total_write_off_user_cnt = value


    def to_alipay_dict(self):
        params = dict()
        if self.avg_order_write_off_discount_amt:
            if hasattr(self.avg_order_write_off_discount_amt, 'to_alipay_dict'):
                params['avg_order_write_off_discount_amt'] = self.avg_order_write_off_discount_amt.to_alipay_dict()
            else:
                params['avg_order_write_off_discount_amt'] = self.avg_order_write_off_discount_amt
        if self.avg_user_write_off_discount_amt:
            if hasattr(self.avg_user_write_off_discount_amt, 'to_alipay_dict'):
                params['avg_user_write_off_discount_amt'] = self.avg_user_write_off_discount_amt.to_alipay_dict()
            else:
                params['avg_user_write_off_discount_amt'] = self.avg_user_write_off_discount_amt
        if self.data_update_time:
            if hasattr(self.data_update_time, 'to_alipay_dict'):
                params['data_update_time'] = self.data_update_time.to_alipay_dict()
            else:
                params['data_update_time'] = self.data_update_time
        if self.total_camp_refund_amt:
            if hasattr(self.total_camp_refund_amt, 'to_alipay_dict'):
                params['total_camp_refund_amt'] = self.total_camp_refund_amt.to_alipay_dict()
            else:
                params['total_camp_refund_amt'] = self.total_camp_refund_amt
        if self.total_expire_amt:
            if hasattr(self.total_expire_amt, 'to_alipay_dict'):
                params['total_expire_amt'] = self.total_expire_amt.to_alipay_dict()
            else:
                params['total_expire_amt'] = self.total_expire_amt
        if self.total_expire_cnt:
            if hasattr(self.total_expire_cnt, 'to_alipay_dict'):
                params['total_expire_cnt'] = self.total_expire_cnt.to_alipay_dict()
            else:
                params['total_expire_cnt'] = self.total_expire_cnt
        if self.total_order_refund_cnt:
            if hasattr(self.total_order_refund_cnt, 'to_alipay_dict'):
                params['total_order_refund_cnt'] = self.total_order_refund_cnt.to_alipay_dict()
            else:
                params['total_order_refund_cnt'] = self.total_order_refund_cnt
        if self.total_receive_amt:
            if hasattr(self.total_receive_amt, 'to_alipay_dict'):
                params['total_receive_amt'] = self.total_receive_amt.to_alipay_dict()
            else:
                params['total_receive_amt'] = self.total_receive_amt
        if self.total_receive_times:
            if hasattr(self.total_receive_times, 'to_alipay_dict'):
                params['total_receive_times'] = self.total_receive_times.to_alipay_dict()
            else:
                params['total_receive_times'] = self.total_receive_times
        if self.total_receive_user_cnt:
            if hasattr(self.total_receive_user_cnt, 'to_alipay_dict'):
                params['total_receive_user_cnt'] = self.total_receive_user_cnt.to_alipay_dict()
            else:
                params['total_receive_user_cnt'] = self.total_receive_user_cnt
        if self.total_write_off_discount_amt:
            if hasattr(self.total_write_off_discount_amt, 'to_alipay_dict'):
                params['total_write_off_discount_amt'] = self.total_write_off_discount_amt.to_alipay_dict()
            else:
                params['total_write_off_discount_amt'] = self.total_write_off_discount_amt
        if self.total_write_off_order_cnt:
            if hasattr(self.total_write_off_order_cnt, 'to_alipay_dict'):
                params['total_write_off_order_cnt'] = self.total_write_off_order_cnt.to_alipay_dict()
            else:
                params['total_write_off_order_cnt'] = self.total_write_off_order_cnt
        if self.total_write_off_user_cnt:
            if hasattr(self.total_write_off_user_cnt, 'to_alipay_dict'):
                params['total_write_off_user_cnt'] = self.total_write_off_user_cnt.to_alipay_dict()
            else:
                params['total_write_off_user_cnt'] = self.total_write_off_user_cnt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DtbankActivityDataEffectInfo()
        if 'avg_order_write_off_discount_amt' in d:
            o.avg_order_write_off_discount_amt = d['avg_order_write_off_discount_amt']
        if 'avg_user_write_off_discount_amt' in d:
            o.avg_user_write_off_discount_amt = d['avg_user_write_off_discount_amt']
        if 'data_update_time' in d:
            o.data_update_time = d['data_update_time']
        if 'total_camp_refund_amt' in d:
            o.total_camp_refund_amt = d['total_camp_refund_amt']
        if 'total_expire_amt' in d:
            o.total_expire_amt = d['total_expire_amt']
        if 'total_expire_cnt' in d:
            o.total_expire_cnt = d['total_expire_cnt']
        if 'total_order_refund_cnt' in d:
            o.total_order_refund_cnt = d['total_order_refund_cnt']
        if 'total_receive_amt' in d:
            o.total_receive_amt = d['total_receive_amt']
        if 'total_receive_times' in d:
            o.total_receive_times = d['total_receive_times']
        if 'total_receive_user_cnt' in d:
            o.total_receive_user_cnt = d['total_receive_user_cnt']
        if 'total_write_off_discount_amt' in d:
            o.total_write_off_discount_amt = d['total_write_off_discount_amt']
        if 'total_write_off_order_cnt' in d:
            o.total_write_off_order_cnt = d['total_write_off_order_cnt']
        if 'total_write_off_user_cnt' in d:
            o.total_write_off_user_cnt = d['total_write_off_user_cnt']
        return o


