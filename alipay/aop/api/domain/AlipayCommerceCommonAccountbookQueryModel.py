#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCommonAccountbookQueryModel(object):

    def __init__(self):
        self._account_book_id = None
        self._page_no = None
        self._page_size = None
        self._sign_user_id = None
        self._sign_user_open_id = None

    @property
    def account_book_id(self):
        return self._account_book_id

    @account_book_id.setter
    def account_book_id(self, value):
        self._account_book_id = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
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
    def sign_user_open_id(self):
        return self._sign_user_open_id

    @sign_user_open_id.setter
    def sign_user_open_id(self, value):
        self._sign_user_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_book_id:
            if hasattr(self.account_book_id, 'to_alipay_dict'):
                params['account_book_id'] = self.account_book_id.to_alipay_dict()
            else:
                params['account_book_id'] = self.account_book_id
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
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
        if self.sign_user_open_id:
            if hasattr(self.sign_user_open_id, 'to_alipay_dict'):
                params['sign_user_open_id'] = self.sign_user_open_id.to_alipay_dict()
            else:
                params['sign_user_open_id'] = self.sign_user_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCommonAccountbookQueryModel()
        if 'account_book_id' in d:
            o.account_book_id = d['account_book_id']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'sign_user_id' in d:
            o.sign_user_id = d['sign_user_id']
        if 'sign_user_open_id' in d:
            o.sign_user_open_id = d['sign_user_open_id']
        return o


