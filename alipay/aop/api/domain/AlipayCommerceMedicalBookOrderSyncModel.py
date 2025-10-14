#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BookOrderDetailVO import BookOrderDetailVO


class AlipayCommerceMedicalBookOrderSyncModel(object):

    def __init__(self):
        self._book_order_detail = None
        self._open_id = None
        self._user_id = None

    @property
    def book_order_detail(self):
        return self._book_order_detail

    @book_order_detail.setter
    def book_order_detail(self, value):
        if isinstance(value, BookOrderDetailVO):
            self._book_order_detail = value
        else:
            self._book_order_detail = BookOrderDetailVO.from_alipay_dict(value)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.book_order_detail:
            if hasattr(self.book_order_detail, 'to_alipay_dict'):
                params['book_order_detail'] = self.book_order_detail.to_alipay_dict()
            else:
                params['book_order_detail'] = self.book_order_detail
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        o = AlipayCommerceMedicalBookOrderSyncModel()
        if 'book_order_detail' in d:
            o.book_order_detail = d['book_order_detail']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


