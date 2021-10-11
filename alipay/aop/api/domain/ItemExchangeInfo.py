#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemExchangeInfo(object):

    def __init__(self):
        self._exchange_token = None
        self._item_code = None
        self._item_logo = None
        self._item_name = None
        self._point_amount = None
        self._point_exchange_note = None
        self._point_unit = None

    @property
    def exchange_token(self):
        return self._exchange_token

    @exchange_token.setter
    def exchange_token(self, value):
        self._exchange_token = value
    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def item_logo(self):
        return self._item_logo

    @item_logo.setter
    def item_logo(self, value):
        self._item_logo = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def point_amount(self):
        return self._point_amount

    @point_amount.setter
    def point_amount(self, value):
        self._point_amount = value
    @property
    def point_exchange_note(self):
        return self._point_exchange_note

    @point_exchange_note.setter
    def point_exchange_note(self, value):
        self._point_exchange_note = value
    @property
    def point_unit(self):
        return self._point_unit

    @point_unit.setter
    def point_unit(self, value):
        self._point_unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.exchange_token:
            if hasattr(self.exchange_token, 'to_alipay_dict'):
                params['exchange_token'] = self.exchange_token.to_alipay_dict()
            else:
                params['exchange_token'] = self.exchange_token
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
        if self.item_logo:
            if hasattr(self.item_logo, 'to_alipay_dict'):
                params['item_logo'] = self.item_logo.to_alipay_dict()
            else:
                params['item_logo'] = self.item_logo
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.point_amount:
            if hasattr(self.point_amount, 'to_alipay_dict'):
                params['point_amount'] = self.point_amount.to_alipay_dict()
            else:
                params['point_amount'] = self.point_amount
        if self.point_exchange_note:
            if hasattr(self.point_exchange_note, 'to_alipay_dict'):
                params['point_exchange_note'] = self.point_exchange_note.to_alipay_dict()
            else:
                params['point_exchange_note'] = self.point_exchange_note
        if self.point_unit:
            if hasattr(self.point_unit, 'to_alipay_dict'):
                params['point_unit'] = self.point_unit.to_alipay_dict()
            else:
                params['point_unit'] = self.point_unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemExchangeInfo()
        if 'exchange_token' in d:
            o.exchange_token = d['exchange_token']
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'item_logo' in d:
            o.item_logo = d['item_logo']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'point_amount' in d:
            o.point_amount = d['point_amount']
        if 'point_exchange_note' in d:
            o.point_exchange_note = d['point_exchange_note']
        if 'point_unit' in d:
            o.point_unit = d['point_unit']
        return o


