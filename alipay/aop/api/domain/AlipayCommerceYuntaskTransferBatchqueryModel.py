#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceYuntaskTransferBatchqueryModel(object):

    def __init__(self):
        self._page_num = None
        self._page_size = None
        self._sign_user_id = None
        self._trans_date_end = None
        self._trans_date_start = None
        self._type = None

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
    def sign_user_id(self):
        return self._sign_user_id

    @sign_user_id.setter
    def sign_user_id(self, value):
        self._sign_user_id = value
    @property
    def trans_date_end(self):
        return self._trans_date_end

    @trans_date_end.setter
    def trans_date_end(self, value):
        self._trans_date_end = value
    @property
    def trans_date_start(self):
        return self._trans_date_start

    @trans_date_start.setter
    def trans_date_start(self, value):
        self._trans_date_start = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.sign_user_id:
            if hasattr(self.sign_user_id, 'to_alipay_dict'):
                params['sign_user_id'] = self.sign_user_id.to_alipay_dict()
            else:
                params['sign_user_id'] = self.sign_user_id
        if self.trans_date_end:
            if hasattr(self.trans_date_end, 'to_alipay_dict'):
                params['trans_date_end'] = self.trans_date_end.to_alipay_dict()
            else:
                params['trans_date_end'] = self.trans_date_end
        if self.trans_date_start:
            if hasattr(self.trans_date_start, 'to_alipay_dict'):
                params['trans_date_start'] = self.trans_date_start.to_alipay_dict()
            else:
                params['trans_date_start'] = self.trans_date_start
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceYuntaskTransferBatchqueryModel()
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'sign_user_id' in d:
            o.sign_user_id = d['sign_user_id']
        if 'trans_date_end' in d:
            o.trans_date_end = d['trans_date_end']
        if 'trans_date_start' in d:
            o.trans_date_start = d['trans_date_start']
        if 'type' in d:
            o.type = d['type']
        return o


