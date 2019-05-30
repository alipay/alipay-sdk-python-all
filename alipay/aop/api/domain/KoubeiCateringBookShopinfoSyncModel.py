#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringBookShopinfoSyncModel(object):

    def __init__(self):
        self._book_keep_time = None
        self._book_text = None
        self._max_book_time = None
        self._max_box_num = None
        self._min_book_num = None
        self._min_book_time = None
        self._min_box_num = None
        self._out_shop_id = None
        self._remark_flag = None
        self._shop_id = None
        self._shop_state = None
        self._support_box = None
        self._support_quick_book = None
        self._sync_timestamp = None

    @property
    def book_keep_time(self):
        return self._book_keep_time

    @book_keep_time.setter
    def book_keep_time(self, value):
        self._book_keep_time = value
    @property
    def book_text(self):
        return self._book_text

    @book_text.setter
    def book_text(self, value):
        self._book_text = value
    @property
    def max_book_time(self):
        return self._max_book_time

    @max_book_time.setter
    def max_book_time(self, value):
        self._max_book_time = value
    @property
    def max_box_num(self):
        return self._max_box_num

    @max_box_num.setter
    def max_box_num(self, value):
        self._max_box_num = value
    @property
    def min_book_num(self):
        return self._min_book_num

    @min_book_num.setter
    def min_book_num(self, value):
        self._min_book_num = value
    @property
    def min_book_time(self):
        return self._min_book_time

    @min_book_time.setter
    def min_book_time(self, value):
        self._min_book_time = value
    @property
    def min_box_num(self):
        return self._min_box_num

    @min_box_num.setter
    def min_box_num(self, value):
        self._min_box_num = value
    @property
    def out_shop_id(self):
        return self._out_shop_id

    @out_shop_id.setter
    def out_shop_id(self, value):
        self._out_shop_id = value
    @property
    def remark_flag(self):
        return self._remark_flag

    @remark_flag.setter
    def remark_flag(self, value):
        self._remark_flag = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_state(self):
        return self._shop_state

    @shop_state.setter
    def shop_state(self, value):
        self._shop_state = value
    @property
    def support_box(self):
        return self._support_box

    @support_box.setter
    def support_box(self, value):
        self._support_box = value
    @property
    def support_quick_book(self):
        return self._support_quick_book

    @support_quick_book.setter
    def support_quick_book(self, value):
        self._support_quick_book = value
    @property
    def sync_timestamp(self):
        return self._sync_timestamp

    @sync_timestamp.setter
    def sync_timestamp(self, value):
        self._sync_timestamp = value


    def to_alipay_dict(self):
        params = dict()
        if self.book_keep_time:
            if hasattr(self.book_keep_time, 'to_alipay_dict'):
                params['book_keep_time'] = self.book_keep_time.to_alipay_dict()
            else:
                params['book_keep_time'] = self.book_keep_time
        if self.book_text:
            if hasattr(self.book_text, 'to_alipay_dict'):
                params['book_text'] = self.book_text.to_alipay_dict()
            else:
                params['book_text'] = self.book_text
        if self.max_book_time:
            if hasattr(self.max_book_time, 'to_alipay_dict'):
                params['max_book_time'] = self.max_book_time.to_alipay_dict()
            else:
                params['max_book_time'] = self.max_book_time
        if self.max_box_num:
            if hasattr(self.max_box_num, 'to_alipay_dict'):
                params['max_box_num'] = self.max_box_num.to_alipay_dict()
            else:
                params['max_box_num'] = self.max_box_num
        if self.min_book_num:
            if hasattr(self.min_book_num, 'to_alipay_dict'):
                params['min_book_num'] = self.min_book_num.to_alipay_dict()
            else:
                params['min_book_num'] = self.min_book_num
        if self.min_book_time:
            if hasattr(self.min_book_time, 'to_alipay_dict'):
                params['min_book_time'] = self.min_book_time.to_alipay_dict()
            else:
                params['min_book_time'] = self.min_book_time
        if self.min_box_num:
            if hasattr(self.min_box_num, 'to_alipay_dict'):
                params['min_box_num'] = self.min_box_num.to_alipay_dict()
            else:
                params['min_box_num'] = self.min_box_num
        if self.out_shop_id:
            if hasattr(self.out_shop_id, 'to_alipay_dict'):
                params['out_shop_id'] = self.out_shop_id.to_alipay_dict()
            else:
                params['out_shop_id'] = self.out_shop_id
        if self.remark_flag:
            if hasattr(self.remark_flag, 'to_alipay_dict'):
                params['remark_flag'] = self.remark_flag.to_alipay_dict()
            else:
                params['remark_flag'] = self.remark_flag
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_state:
            if hasattr(self.shop_state, 'to_alipay_dict'):
                params['shop_state'] = self.shop_state.to_alipay_dict()
            else:
                params['shop_state'] = self.shop_state
        if self.support_box:
            if hasattr(self.support_box, 'to_alipay_dict'):
                params['support_box'] = self.support_box.to_alipay_dict()
            else:
                params['support_box'] = self.support_box
        if self.support_quick_book:
            if hasattr(self.support_quick_book, 'to_alipay_dict'):
                params['support_quick_book'] = self.support_quick_book.to_alipay_dict()
            else:
                params['support_quick_book'] = self.support_quick_book
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
        o = KoubeiCateringBookShopinfoSyncModel()
        if 'book_keep_time' in d:
            o.book_keep_time = d['book_keep_time']
        if 'book_text' in d:
            o.book_text = d['book_text']
        if 'max_book_time' in d:
            o.max_book_time = d['max_book_time']
        if 'max_box_num' in d:
            o.max_box_num = d['max_box_num']
        if 'min_book_num' in d:
            o.min_book_num = d['min_book_num']
        if 'min_book_time' in d:
            o.min_book_time = d['min_book_time']
        if 'min_box_num' in d:
            o.min_box_num = d['min_box_num']
        if 'out_shop_id' in d:
            o.out_shop_id = d['out_shop_id']
        if 'remark_flag' in d:
            o.remark_flag = d['remark_flag']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_state' in d:
            o.shop_state = d['shop_state']
        if 'support_box' in d:
            o.support_box = d['support_box']
        if 'support_quick_book' in d:
            o.support_quick_book = d['support_quick_book']
        if 'sync_timestamp' in d:
            o.sync_timestamp = d['sync_timestamp']
        return o


