#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniOrderAnxinitemdeliverBatchqueryModel(object):

    def __init__(self):
        self._card_no = None
        self._mini_app_id = None
        self._page_num = None
        self._page_size = None
        self._trade_no = None
        self._use_status = None
        self._use_time = None

    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def use_status(self):
        return self._use_status

    @use_status.setter
    def use_status(self, value):
        if isinstance(value, list):
            self._use_status = list()
            for i in value:
                self._use_status.append(i)
    @property
    def use_time(self):
        return self._use_time

    @use_time.setter
    def use_time(self, value):
        self._use_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.use_status:
            if isinstance(self.use_status, list):
                for i in range(0, len(self.use_status)):
                    element = self.use_status[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.use_status[i] = element.to_alipay_dict()
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
        o = AlipayOpenMiniOrderAnxinitemdeliverBatchqueryModel()
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'use_status' in d:
            o.use_status = d['use_status']
        if 'use_time' in d:
            o.use_time = d['use_time']
        return o


