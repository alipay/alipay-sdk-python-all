#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CalendarRoomPriceInfo(object):

    def __init__(self):
        self._check_in_date = None
        self._item_id = None

    @property
    def check_in_date(self):
        return self._check_in_date

    @check_in_date.setter
    def check_in_date(self, value):
        self._check_in_date = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_in_date:
            if hasattr(self.check_in_date, 'to_alipay_dict'):
                params['check_in_date'] = self.check_in_date.to_alipay_dict()
            else:
                params['check_in_date'] = self.check_in_date
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CalendarRoomPriceInfo()
        if 'check_in_date' in d:
            o.check_in_date = d['check_in_date']
        if 'item_id' in d:
            o.item_id = d['item_id']
        return o


