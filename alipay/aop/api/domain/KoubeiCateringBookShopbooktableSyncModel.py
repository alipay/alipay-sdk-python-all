#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BookTime import BookTime


class KoubeiCateringBookShopbooktableSyncModel(object):

    def __init__(self):
        self._book_time = None
        self._out_shop_id = None
        self._shop_id = None
        self._sync_timestamp = None

    @property
    def book_time(self):
        return self._book_time

    @book_time.setter
    def book_time(self, value):
        if isinstance(value, list):
            self._book_time = list()
            for i in value:
                if isinstance(i, BookTime):
                    self._book_time.append(i)
                else:
                    self._book_time.append(BookTime.from_alipay_dict(i))
    @property
    def out_shop_id(self):
        return self._out_shop_id

    @out_shop_id.setter
    def out_shop_id(self, value):
        self._out_shop_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def sync_timestamp(self):
        return self._sync_timestamp

    @sync_timestamp.setter
    def sync_timestamp(self, value):
        self._sync_timestamp = value


    def to_alipay_dict(self):
        params = dict()
        if self.book_time:
            if isinstance(self.book_time, list):
                for i in range(0, len(self.book_time)):
                    element = self.book_time[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.book_time[i] = element.to_alipay_dict()
            if hasattr(self.book_time, 'to_alipay_dict'):
                params['book_time'] = self.book_time.to_alipay_dict()
            else:
                params['book_time'] = self.book_time
        if self.out_shop_id:
            if hasattr(self.out_shop_id, 'to_alipay_dict'):
                params['out_shop_id'] = self.out_shop_id.to_alipay_dict()
            else:
                params['out_shop_id'] = self.out_shop_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.sync_timestamp:
            if hasattr(self.sync_timestamp, 'to_alipay_dict'):
                params['sync_timestamp'] = self.sync_timestamp.to_alipay_dict()
            else:
                params['sync_timestamp'] = self.sync_timestamp
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringBookShopbooktableSyncModel()
        if 'book_time' in d:
            o.book_time = d['book_time']
        if 'out_shop_id' in d:
            o.out_shop_id = d['out_shop_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'sync_timestamp' in d:
            o.sync_timestamp = d['sync_timestamp']
        return o


