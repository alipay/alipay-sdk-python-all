#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LotteryPresent(object):

    def __init__(self):
        self._alipay_user_id = None
        self._lottery_type_name = None
        self._present_date = None
        self._present_id = None
        self._stake_count = None
        self._status = None
        self._status_desc = None
        self._sweety_words = None
        self._win_fee = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def lottery_type_name(self):
        return self._lottery_type_name

    @lottery_type_name.setter
    def lottery_type_name(self, value):
        self._lottery_type_name = value
    @property
    def present_date(self):
        return self._present_date

    @present_date.setter
    def present_date(self, value):
        self._present_date = value
    @property
    def present_id(self):
        return self._present_id

    @present_id.setter
    def present_id(self, value):
        self._present_id = value
    @property
    def stake_count(self):
        return self._stake_count

    @stake_count.setter
    def stake_count(self, value):
        self._stake_count = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_desc(self):
        return self._status_desc

    @status_desc.setter
    def status_desc(self, value):
        self._status_desc = value
    @property
    def sweety_words(self):
        return self._sweety_words

    @sweety_words.setter
    def sweety_words(self, value):
        self._sweety_words = value
    @property
    def win_fee(self):
        return self._win_fee

    @win_fee.setter
    def win_fee(self, value):
        self._win_fee = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.lottery_type_name:
            if hasattr(self.lottery_type_name, 'to_alipay_dict'):
                params['lottery_type_name'] = self.lottery_type_name.to_alipay_dict()
            else:
                params['lottery_type_name'] = self.lottery_type_name
        if self.present_date:
            if hasattr(self.present_date, 'to_alipay_dict'):
                params['present_date'] = self.present_date.to_alipay_dict()
            else:
                params['present_date'] = self.present_date
        if self.present_id:
            if hasattr(self.present_id, 'to_alipay_dict'):
                params['present_id'] = self.present_id.to_alipay_dict()
            else:
                params['present_id'] = self.present_id
        if self.stake_count:
            if hasattr(self.stake_count, 'to_alipay_dict'):
                params['stake_count'] = self.stake_count.to_alipay_dict()
            else:
                params['stake_count'] = self.stake_count
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_desc:
            if hasattr(self.status_desc, 'to_alipay_dict'):
                params['status_desc'] = self.status_desc.to_alipay_dict()
            else:
                params['status_desc'] = self.status_desc
        if self.sweety_words:
            if hasattr(self.sweety_words, 'to_alipay_dict'):
                params['sweety_words'] = self.sweety_words.to_alipay_dict()
            else:
                params['sweety_words'] = self.sweety_words
        if self.win_fee:
            if hasattr(self.win_fee, 'to_alipay_dict'):
                params['win_fee'] = self.win_fee.to_alipay_dict()
            else:
                params['win_fee'] = self.win_fee
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LotteryPresent()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'lottery_type_name' in d:
            o.lottery_type_name = d['lottery_type_name']
        if 'present_date' in d:
            o.present_date = d['present_date']
        if 'present_id' in d:
            o.present_id = d['present_id']
        if 'stake_count' in d:
            o.stake_count = d['stake_count']
        if 'status' in d:
            o.status = d['status']
        if 'status_desc' in d:
            o.status_desc = d['status_desc']
        if 'sweety_words' in d:
            o.sweety_words = d['sweety_words']
        if 'win_fee' in d:
            o.win_fee = d['win_fee']
        return o


