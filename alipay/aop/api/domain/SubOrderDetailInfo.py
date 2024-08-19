#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TicketPassagerInfo import TicketPassagerInfo


class SubOrderDetailInfo(object):

    def __init__(self):
        self._good_desc = None
        self._good_id = None
        self._good_name = None
        self._num = None
        self._order_id = None
        self._passagers = None

    @property
    def good_desc(self):
        return self._good_desc

    @good_desc.setter
    def good_desc(self, value):
        self._good_desc = value
    @property
    def good_id(self):
        return self._good_id

    @good_id.setter
    def good_id(self, value):
        self._good_id = value
    @property
    def good_name(self):
        return self._good_name

    @good_name.setter
    def good_name(self, value):
        self._good_name = value
    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def passagers(self):
        return self._passagers

    @passagers.setter
    def passagers(self, value):
        if isinstance(value, list):
            self._passagers = list()
            for i in value:
                if isinstance(i, TicketPassagerInfo):
                    self._passagers.append(i)
                else:
                    self._passagers.append(TicketPassagerInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.good_desc:
            if hasattr(self.good_desc, 'to_alipay_dict'):
                params['good_desc'] = self.good_desc.to_alipay_dict()
            else:
                params['good_desc'] = self.good_desc
        if self.good_id:
            if hasattr(self.good_id, 'to_alipay_dict'):
                params['good_id'] = self.good_id.to_alipay_dict()
            else:
                params['good_id'] = self.good_id
        if self.good_name:
            if hasattr(self.good_name, 'to_alipay_dict'):
                params['good_name'] = self.good_name.to_alipay_dict()
            else:
                params['good_name'] = self.good_name
        if self.num:
            if hasattr(self.num, 'to_alipay_dict'):
                params['num'] = self.num.to_alipay_dict()
            else:
                params['num'] = self.num
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.passagers:
            if isinstance(self.passagers, list):
                for i in range(0, len(self.passagers)):
                    element = self.passagers[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.passagers[i] = element.to_alipay_dict()
            if hasattr(self.passagers, 'to_alipay_dict'):
                params['passagers'] = self.passagers.to_alipay_dict()
            else:
                params['passagers'] = self.passagers
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubOrderDetailInfo()
        if 'good_desc' in d:
            o.good_desc = d['good_desc']
        if 'good_id' in d:
            o.good_id = d['good_id']
        if 'good_name' in d:
            o.good_name = d['good_name']
        if 'num' in d:
            o.num = d['num']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'passagers' in d:
            o.passagers = d['passagers']
        return o


