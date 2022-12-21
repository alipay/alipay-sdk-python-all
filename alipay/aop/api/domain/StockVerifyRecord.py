#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StockVerifyRecord(object):

    def __init__(self):
        self._diff_count = None
        self._diff_offline_amt = None
        self._diff_online_amt = None
        self._offline_miss_count = None
        self._offline_miss_online_amt = None
        self._online_miss_count = None
        self._online_miss_offline_amt = None
        self._success_amt = None
        self._success_count = None
        self._verify_date = None

    @property
    def diff_count(self):
        return self._diff_count

    @diff_count.setter
    def diff_count(self, value):
        self._diff_count = value
    @property
    def diff_offline_amt(self):
        return self._diff_offline_amt

    @diff_offline_amt.setter
    def diff_offline_amt(self, value):
        self._diff_offline_amt = value
    @property
    def diff_online_amt(self):
        return self._diff_online_amt

    @diff_online_amt.setter
    def diff_online_amt(self, value):
        self._diff_online_amt = value
    @property
    def offline_miss_count(self):
        return self._offline_miss_count

    @offline_miss_count.setter
    def offline_miss_count(self, value):
        self._offline_miss_count = value
    @property
    def offline_miss_online_amt(self):
        return self._offline_miss_online_amt

    @offline_miss_online_amt.setter
    def offline_miss_online_amt(self, value):
        self._offline_miss_online_amt = value
    @property
    def online_miss_count(self):
        return self._online_miss_count

    @online_miss_count.setter
    def online_miss_count(self, value):
        self._online_miss_count = value
    @property
    def online_miss_offline_amt(self):
        return self._online_miss_offline_amt

    @online_miss_offline_amt.setter
    def online_miss_offline_amt(self, value):
        self._online_miss_offline_amt = value
    @property
    def success_amt(self):
        return self._success_amt

    @success_amt.setter
    def success_amt(self, value):
        self._success_amt = value
    @property
    def success_count(self):
        return self._success_count

    @success_count.setter
    def success_count(self, value):
        self._success_count = value
    @property
    def verify_date(self):
        return self._verify_date

    @verify_date.setter
    def verify_date(self, value):
        self._verify_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.diff_count:
            if hasattr(self.diff_count, 'to_alipay_dict'):
                params['diff_count'] = self.diff_count.to_alipay_dict()
            else:
                params['diff_count'] = self.diff_count
        if self.diff_offline_amt:
            if hasattr(self.diff_offline_amt, 'to_alipay_dict'):
                params['diff_offline_amt'] = self.diff_offline_amt.to_alipay_dict()
            else:
                params['diff_offline_amt'] = self.diff_offline_amt
        if self.diff_online_amt:
            if hasattr(self.diff_online_amt, 'to_alipay_dict'):
                params['diff_online_amt'] = self.diff_online_amt.to_alipay_dict()
            else:
                params['diff_online_amt'] = self.diff_online_amt
        if self.offline_miss_count:
            if hasattr(self.offline_miss_count, 'to_alipay_dict'):
                params['offline_miss_count'] = self.offline_miss_count.to_alipay_dict()
            else:
                params['offline_miss_count'] = self.offline_miss_count
        if self.offline_miss_online_amt:
            if hasattr(self.offline_miss_online_amt, 'to_alipay_dict'):
                params['offline_miss_online_amt'] = self.offline_miss_online_amt.to_alipay_dict()
            else:
                params['offline_miss_online_amt'] = self.offline_miss_online_amt
        if self.online_miss_count:
            if hasattr(self.online_miss_count, 'to_alipay_dict'):
                params['online_miss_count'] = self.online_miss_count.to_alipay_dict()
            else:
                params['online_miss_count'] = self.online_miss_count
        if self.online_miss_offline_amt:
            if hasattr(self.online_miss_offline_amt, 'to_alipay_dict'):
                params['online_miss_offline_amt'] = self.online_miss_offline_amt.to_alipay_dict()
            else:
                params['online_miss_offline_amt'] = self.online_miss_offline_amt
        if self.success_amt:
            if hasattr(self.success_amt, 'to_alipay_dict'):
                params['success_amt'] = self.success_amt.to_alipay_dict()
            else:
                params['success_amt'] = self.success_amt
        if self.success_count:
            if hasattr(self.success_count, 'to_alipay_dict'):
                params['success_count'] = self.success_count.to_alipay_dict()
            else:
                params['success_count'] = self.success_count
        if self.verify_date:
            if hasattr(self.verify_date, 'to_alipay_dict'):
                params['verify_date'] = self.verify_date.to_alipay_dict()
            else:
                params['verify_date'] = self.verify_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StockVerifyRecord()
        if 'diff_count' in d:
            o.diff_count = d['diff_count']
        if 'diff_offline_amt' in d:
            o.diff_offline_amt = d['diff_offline_amt']
        if 'diff_online_amt' in d:
            o.diff_online_amt = d['diff_online_amt']
        if 'offline_miss_count' in d:
            o.offline_miss_count = d['offline_miss_count']
        if 'offline_miss_online_amt' in d:
            o.offline_miss_online_amt = d['offline_miss_online_amt']
        if 'online_miss_count' in d:
            o.online_miss_count = d['online_miss_count']
        if 'online_miss_offline_amt' in d:
            o.online_miss_offline_amt = d['online_miss_offline_amt']
        if 'success_amt' in d:
            o.success_amt = d['success_amt']
        if 'success_count' in d:
            o.success_count = d['success_count']
        if 'verify_date' in d:
            o.verify_date = d['verify_date']
        return o


