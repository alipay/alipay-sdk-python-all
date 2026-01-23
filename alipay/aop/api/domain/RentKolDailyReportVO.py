#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentKolDailyReportVO(object):

    def __init__(self):
        self._corp_name = None
        self._date = None
        self._nick_name = None
        self._search_word = None
        self._settled_cnt = None
        self._settled_cnt_15_to_30 = None
        self._settled_cnt_over_30 = None
        self._share_type = None
        self._to_be_settle_cnt = None
        self._to_be_settle_cnt_15_to_30 = None
        self._to_be_settle_cnt_over_30 = None
        self._uv_cnt = None

    @property
    def corp_name(self):
        return self._corp_name

    @corp_name.setter
    def corp_name(self, value):
        self._corp_name = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value
    @property
    def search_word(self):
        return self._search_word

    @search_word.setter
    def search_word(self, value):
        self._search_word = value
    @property
    def settled_cnt(self):
        return self._settled_cnt

    @settled_cnt.setter
    def settled_cnt(self, value):
        self._settled_cnt = value
    @property
    def settled_cnt_15_to_30(self):
        return self._settled_cnt_15_to_30

    @settled_cnt_15_to_30.setter
    def settled_cnt_15_to_30(self, value):
        self._settled_cnt_15_to_30 = value
    @property
    def settled_cnt_over_30(self):
        return self._settled_cnt_over_30

    @settled_cnt_over_30.setter
    def settled_cnt_over_30(self, value):
        self._settled_cnt_over_30 = value
    @property
    def share_type(self):
        return self._share_type

    @share_type.setter
    def share_type(self, value):
        self._share_type = value
    @property
    def to_be_settle_cnt(self):
        return self._to_be_settle_cnt

    @to_be_settle_cnt.setter
    def to_be_settle_cnt(self, value):
        self._to_be_settle_cnt = value
    @property
    def to_be_settle_cnt_15_to_30(self):
        return self._to_be_settle_cnt_15_to_30

    @to_be_settle_cnt_15_to_30.setter
    def to_be_settle_cnt_15_to_30(self, value):
        self._to_be_settle_cnt_15_to_30 = value
    @property
    def to_be_settle_cnt_over_30(self):
        return self._to_be_settle_cnt_over_30

    @to_be_settle_cnt_over_30.setter
    def to_be_settle_cnt_over_30(self, value):
        self._to_be_settle_cnt_over_30 = value
    @property
    def uv_cnt(self):
        return self._uv_cnt

    @uv_cnt.setter
    def uv_cnt(self, value):
        self._uv_cnt = value


    def to_alipay_dict(self):
        params = dict()
        if self.corp_name:
            if hasattr(self.corp_name, 'to_alipay_dict'):
                params['corp_name'] = self.corp_name.to_alipay_dict()
            else:
                params['corp_name'] = self.corp_name
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.nick_name:
            if hasattr(self.nick_name, 'to_alipay_dict'):
                params['nick_name'] = self.nick_name.to_alipay_dict()
            else:
                params['nick_name'] = self.nick_name
        if self.search_word:
            if hasattr(self.search_word, 'to_alipay_dict'):
                params['search_word'] = self.search_word.to_alipay_dict()
            else:
                params['search_word'] = self.search_word
        if self.settled_cnt:
            if hasattr(self.settled_cnt, 'to_alipay_dict'):
                params['settled_cnt'] = self.settled_cnt.to_alipay_dict()
            else:
                params['settled_cnt'] = self.settled_cnt
        if self.settled_cnt_15_to_30:
            if hasattr(self.settled_cnt_15_to_30, 'to_alipay_dict'):
                params['settled_cnt_15_to_30'] = self.settled_cnt_15_to_30.to_alipay_dict()
            else:
                params['settled_cnt_15_to_30'] = self.settled_cnt_15_to_30
        if self.settled_cnt_over_30:
            if hasattr(self.settled_cnt_over_30, 'to_alipay_dict'):
                params['settled_cnt_over_30'] = self.settled_cnt_over_30.to_alipay_dict()
            else:
                params['settled_cnt_over_30'] = self.settled_cnt_over_30
        if self.share_type:
            if hasattr(self.share_type, 'to_alipay_dict'):
                params['share_type'] = self.share_type.to_alipay_dict()
            else:
                params['share_type'] = self.share_type
        if self.to_be_settle_cnt:
            if hasattr(self.to_be_settle_cnt, 'to_alipay_dict'):
                params['to_be_settle_cnt'] = self.to_be_settle_cnt.to_alipay_dict()
            else:
                params['to_be_settle_cnt'] = self.to_be_settle_cnt
        if self.to_be_settle_cnt_15_to_30:
            if hasattr(self.to_be_settle_cnt_15_to_30, 'to_alipay_dict'):
                params['to_be_settle_cnt_15_to_30'] = self.to_be_settle_cnt_15_to_30.to_alipay_dict()
            else:
                params['to_be_settle_cnt_15_to_30'] = self.to_be_settle_cnt_15_to_30
        if self.to_be_settle_cnt_over_30:
            if hasattr(self.to_be_settle_cnt_over_30, 'to_alipay_dict'):
                params['to_be_settle_cnt_over_30'] = self.to_be_settle_cnt_over_30.to_alipay_dict()
            else:
                params['to_be_settle_cnt_over_30'] = self.to_be_settle_cnt_over_30
        if self.uv_cnt:
            if hasattr(self.uv_cnt, 'to_alipay_dict'):
                params['uv_cnt'] = self.uv_cnt.to_alipay_dict()
            else:
                params['uv_cnt'] = self.uv_cnt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentKolDailyReportVO()
        if 'corp_name' in d:
            o.corp_name = d['corp_name']
        if 'date' in d:
            o.date = d['date']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        if 'search_word' in d:
            o.search_word = d['search_word']
        if 'settled_cnt' in d:
            o.settled_cnt = d['settled_cnt']
        if 'settled_cnt_15_to_30' in d:
            o.settled_cnt_15_to_30 = d['settled_cnt_15_to_30']
        if 'settled_cnt_over_30' in d:
            o.settled_cnt_over_30 = d['settled_cnt_over_30']
        if 'share_type' in d:
            o.share_type = d['share_type']
        if 'to_be_settle_cnt' in d:
            o.to_be_settle_cnt = d['to_be_settle_cnt']
        if 'to_be_settle_cnt_15_to_30' in d:
            o.to_be_settle_cnt_15_to_30 = d['to_be_settle_cnt_15_to_30']
        if 'to_be_settle_cnt_over_30' in d:
            o.to_be_settle_cnt_over_30 = d['to_be_settle_cnt_over_30']
        if 'uv_cnt' in d:
            o.uv_cnt = d['uv_cnt']
        return o


