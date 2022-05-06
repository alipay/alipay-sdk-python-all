#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserMemberCitycardSyncModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._biz_occur_time = None
        self._city_code = None
        self._out_card_no = None
        self._trade_no = None
        self._valid_end = None
        self._valid_start = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def biz_occur_time(self):
        return self._biz_occur_time

    @biz_occur_time.setter
    def biz_occur_time(self, value):
        self._biz_occur_time = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def out_card_no(self):
        return self._out_card_no

    @out_card_no.setter
    def out_card_no(self, value):
        self._out_card_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def valid_end(self):
        return self._valid_end

    @valid_end.setter
    def valid_end(self, value):
        self._valid_end = value
    @property
    def valid_start(self):
        return self._valid_start

    @valid_start.setter
    def valid_start(self, value):
        self._valid_start = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.biz_occur_time:
            if hasattr(self.biz_occur_time, 'to_alipay_dict'):
                params['biz_occur_time'] = self.biz_occur_time.to_alipay_dict()
            else:
                params['biz_occur_time'] = self.biz_occur_time
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.out_card_no:
            if hasattr(self.out_card_no, 'to_alipay_dict'):
                params['out_card_no'] = self.out_card_no.to_alipay_dict()
            else:
                params['out_card_no'] = self.out_card_no
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.valid_end:
            if hasattr(self.valid_end, 'to_alipay_dict'):
                params['valid_end'] = self.valid_end.to_alipay_dict()
            else:
                params['valid_end'] = self.valid_end
        if self.valid_start:
            if hasattr(self.valid_start, 'to_alipay_dict'):
                params['valid_start'] = self.valid_start.to_alipay_dict()
            else:
                params['valid_start'] = self.valid_start
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserMemberCitycardSyncModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'biz_occur_time' in d:
            o.biz_occur_time = d['biz_occur_time']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'out_card_no' in d:
            o.out_card_no = d['out_card_no']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'valid_end' in d:
            o.valid_end = d['valid_end']
        if 'valid_start' in d:
            o.valid_start = d['valid_start']
        return o


