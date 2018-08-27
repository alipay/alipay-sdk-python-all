#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLotteryPresentSendModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._lottery_type_id = None
        self._out_order_no = None
        self._stake_count = None
        self._swety_words = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def lottery_type_id(self):
        return self._lottery_type_id

    @lottery_type_id.setter
    def lottery_type_id(self, value):
        self._lottery_type_id = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def stake_count(self):
        return self._stake_count

    @stake_count.setter
    def stake_count(self, value):
        self._stake_count = value
    @property
    def swety_words(self):
        return self._swety_words

    @swety_words.setter
    def swety_words(self, value):
        self._swety_words = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.lottery_type_id:
            if hasattr(self.lottery_type_id, 'to_alipay_dict'):
                params['lottery_type_id'] = self.lottery_type_id.to_alipay_dict()
            else:
                params['lottery_type_id'] = self.lottery_type_id
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.stake_count:
            if hasattr(self.stake_count, 'to_alipay_dict'):
                params['stake_count'] = self.stake_count.to_alipay_dict()
            else:
                params['stake_count'] = self.stake_count
        if self.swety_words:
            if hasattr(self.swety_words, 'to_alipay_dict'):
                params['swety_words'] = self.swety_words.to_alipay_dict()
            else:
                params['swety_words'] = self.swety_words
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLotteryPresentSendModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'lottery_type_id' in d:
            o.lottery_type_id = d['lottery_type_id']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'stake_count' in d:
            o.stake_count = d['stake_count']
        if 'swety_words' in d:
            o.swety_words = d['swety_words']
        return o


