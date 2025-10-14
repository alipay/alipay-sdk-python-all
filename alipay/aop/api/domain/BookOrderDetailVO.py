#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BookInfoVO import BookInfoVO
from alipay.aop.api.domain.BookOrderVO import BookOrderVO


class BookOrderDetailVO(object):

    def __init__(self):
        self._book_infos = None
        self._book_order = None

    @property
    def book_infos(self):
        return self._book_infos

    @book_infos.setter
    def book_infos(self, value):
        if isinstance(value, list):
            self._book_infos = list()
            for i in value:
                if isinstance(i, BookInfoVO):
                    self._book_infos.append(i)
                else:
                    self._book_infos.append(BookInfoVO.from_alipay_dict(i))
    @property
    def book_order(self):
        return self._book_order

    @book_order.setter
    def book_order(self, value):
        if isinstance(value, BookOrderVO):
            self._book_order = value
        else:
            self._book_order = BookOrderVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.book_infos:
            if isinstance(self.book_infos, list):
                for i in range(0, len(self.book_infos)):
                    element = self.book_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.book_infos[i] = element.to_alipay_dict()
            if hasattr(self.book_infos, 'to_alipay_dict'):
                params['book_infos'] = self.book_infos.to_alipay_dict()
            else:
                params['book_infos'] = self.book_infos
        if self.book_order:
            if hasattr(self.book_order, 'to_alipay_dict'):
                params['book_order'] = self.book_order.to_alipay_dict()
            else:
                params['book_order'] = self.book_order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BookOrderDetailVO()
        if 'book_infos' in d:
            o.book_infos = d['book_infos']
        if 'book_order' in d:
            o.book_order = d['book_order']
        return o


