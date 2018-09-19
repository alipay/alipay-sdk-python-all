#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MpPrizeInfoModel(object):

    def __init__(self):
        self._certlot_number = None
        self._frequency_count = None
        self._frequency_type = None
        self._prize_end_time = None
        self._prize_id = None
        self._prize_max_award_limit = None
        self._prize_name = None
        self._prize_start_time = None
        self._prize_total = None
        self._prize_type = None

    @property
    def certlot_number(self):
        return self._certlot_number

    @certlot_number.setter
    def certlot_number(self, value):
        self._certlot_number = value
    @property
    def frequency_count(self):
        return self._frequency_count

    @frequency_count.setter
    def frequency_count(self, value):
        self._frequency_count = value
    @property
    def frequency_type(self):
        return self._frequency_type

    @frequency_type.setter
    def frequency_type(self, value):
        self._frequency_type = value
    @property
    def prize_end_time(self):
        return self._prize_end_time

    @prize_end_time.setter
    def prize_end_time(self, value):
        self._prize_end_time = value
    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value
    @property
    def prize_max_award_limit(self):
        return self._prize_max_award_limit

    @prize_max_award_limit.setter
    def prize_max_award_limit(self, value):
        self._prize_max_award_limit = value
    @property
    def prize_name(self):
        return self._prize_name

    @prize_name.setter
    def prize_name(self, value):
        self._prize_name = value
    @property
    def prize_start_time(self):
        return self._prize_start_time

    @prize_start_time.setter
    def prize_start_time(self, value):
        self._prize_start_time = value
    @property
    def prize_total(self):
        return self._prize_total

    @prize_total.setter
    def prize_total(self, value):
        self._prize_total = value
    @property
    def prize_type(self):
        return self._prize_type

    @prize_type.setter
    def prize_type(self, value):
        self._prize_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.certlot_number:
            if hasattr(self.certlot_number, 'to_alipay_dict'):
                params['certlot_number'] = self.certlot_number.to_alipay_dict()
            else:
                params['certlot_number'] = self.certlot_number
        if self.frequency_count:
            if hasattr(self.frequency_count, 'to_alipay_dict'):
                params['frequency_count'] = self.frequency_count.to_alipay_dict()
            else:
                params['frequency_count'] = self.frequency_count
        if self.frequency_type:
            if hasattr(self.frequency_type, 'to_alipay_dict'):
                params['frequency_type'] = self.frequency_type.to_alipay_dict()
            else:
                params['frequency_type'] = self.frequency_type
        if self.prize_end_time:
            if hasattr(self.prize_end_time, 'to_alipay_dict'):
                params['prize_end_time'] = self.prize_end_time.to_alipay_dict()
            else:
                params['prize_end_time'] = self.prize_end_time
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        if self.prize_max_award_limit:
            if hasattr(self.prize_max_award_limit, 'to_alipay_dict'):
                params['prize_max_award_limit'] = self.prize_max_award_limit.to_alipay_dict()
            else:
                params['prize_max_award_limit'] = self.prize_max_award_limit
        if self.prize_name:
            if hasattr(self.prize_name, 'to_alipay_dict'):
                params['prize_name'] = self.prize_name.to_alipay_dict()
            else:
                params['prize_name'] = self.prize_name
        if self.prize_start_time:
            if hasattr(self.prize_start_time, 'to_alipay_dict'):
                params['prize_start_time'] = self.prize_start_time.to_alipay_dict()
            else:
                params['prize_start_time'] = self.prize_start_time
        if self.prize_total:
            if hasattr(self.prize_total, 'to_alipay_dict'):
                params['prize_total'] = self.prize_total.to_alipay_dict()
            else:
                params['prize_total'] = self.prize_total
        if self.prize_type:
            if hasattr(self.prize_type, 'to_alipay_dict'):
                params['prize_type'] = self.prize_type.to_alipay_dict()
            else:
                params['prize_type'] = self.prize_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MpPrizeInfoModel()
        if 'certlot_number' in d:
            o.certlot_number = d['certlot_number']
        if 'frequency_count' in d:
            o.frequency_count = d['frequency_count']
        if 'frequency_type' in d:
            o.frequency_type = d['frequency_type']
        if 'prize_end_time' in d:
            o.prize_end_time = d['prize_end_time']
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'prize_max_award_limit' in d:
            o.prize_max_award_limit = d['prize_max_award_limit']
        if 'prize_name' in d:
            o.prize_name = d['prize_name']
        if 'prize_start_time' in d:
            o.prize_start_time = d['prize_start_time']
        if 'prize_total' in d:
            o.prize_total = d['prize_total']
        if 'prize_type' in d:
            o.prize_type = d['prize_type']
        return o


