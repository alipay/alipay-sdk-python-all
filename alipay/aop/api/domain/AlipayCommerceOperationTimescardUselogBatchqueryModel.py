#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationTimescardUselogBatchqueryModel(object):

    def __init__(self):
        self._card_id = None
        self._log_time_end = None
        self._log_time_start = None
        self._page_num = None
        self._page_size = None
        self._scene_code = None
        self._user_id = None

    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def log_time_end(self):
        return self._log_time_end

    @log_time_end.setter
    def log_time_end(self, value):
        self._log_time_end = value
    @property
    def log_time_start(self):
        return self._log_time_start

    @log_time_start.setter
    def log_time_start(self, value):
        self._log_time_start = value
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
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.log_time_end:
            if hasattr(self.log_time_end, 'to_alipay_dict'):
                params['log_time_end'] = self.log_time_end.to_alipay_dict()
            else:
                params['log_time_end'] = self.log_time_end
        if self.log_time_start:
            if hasattr(self.log_time_start, 'to_alipay_dict'):
                params['log_time_start'] = self.log_time_start.to_alipay_dict()
            else:
                params['log_time_start'] = self.log_time_start
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
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationTimescardUselogBatchqueryModel()
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'log_time_end' in d:
            o.log_time_end = d['log_time_end']
        if 'log_time_start' in d:
            o.log_time_start = d['log_time_start']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


