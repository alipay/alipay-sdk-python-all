#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TicketCodeQueryResponse(object):

    def __init__(self):
        self._available_quantity = None
        self._effect_date = None
        self._expire_date = None
        self._item_goods_ids = None
        self._item_id = None
        self._item_name = None
        self._ticket_display_mode = None
        self._ticket_id = None
        self._ticket_status = None
        self._time_cards = None
        self._total_quantity = None

    @property
    def available_quantity(self):
        return self._available_quantity

    @available_quantity.setter
    def available_quantity(self, value):
        self._available_quantity = value
    @property
    def effect_date(self):
        return self._effect_date

    @effect_date.setter
    def effect_date(self, value):
        self._effect_date = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def item_goods_ids(self):
        return self._item_goods_ids

    @item_goods_ids.setter
    def item_goods_ids(self, value):
        if isinstance(value, list):
            self._item_goods_ids = list()
            for i in value:
                self._item_goods_ids.append(i)
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def ticket_display_mode(self):
        return self._ticket_display_mode

    @ticket_display_mode.setter
    def ticket_display_mode(self, value):
        self._ticket_display_mode = value
    @property
    def ticket_id(self):
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, value):
        self._ticket_id = value
    @property
    def ticket_status(self):
        return self._ticket_status

    @ticket_status.setter
    def ticket_status(self, value):
        self._ticket_status = value
    @property
    def time_cards(self):
        return self._time_cards

    @time_cards.setter
    def time_cards(self, value):
        self._time_cards = value
    @property
    def total_quantity(self):
        return self._total_quantity

    @total_quantity.setter
    def total_quantity(self, value):
        self._total_quantity = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_quantity:
            if hasattr(self.available_quantity, 'to_alipay_dict'):
                params['available_quantity'] = self.available_quantity.to_alipay_dict()
            else:
                params['available_quantity'] = self.available_quantity
        if self.effect_date:
            if hasattr(self.effect_date, 'to_alipay_dict'):
                params['effect_date'] = self.effect_date.to_alipay_dict()
            else:
                params['effect_date'] = self.effect_date
        if self.expire_date:
            if hasattr(self.expire_date, 'to_alipay_dict'):
                params['expire_date'] = self.expire_date.to_alipay_dict()
            else:
                params['expire_date'] = self.expire_date
        if self.item_goods_ids:
            if isinstance(self.item_goods_ids, list):
                for i in range(0, len(self.item_goods_ids)):
                    element = self.item_goods_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_goods_ids[i] = element.to_alipay_dict()
            if hasattr(self.item_goods_ids, 'to_alipay_dict'):
                params['item_goods_ids'] = self.item_goods_ids.to_alipay_dict()
            else:
                params['item_goods_ids'] = self.item_goods_ids
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.ticket_display_mode:
            if hasattr(self.ticket_display_mode, 'to_alipay_dict'):
                params['ticket_display_mode'] = self.ticket_display_mode.to_alipay_dict()
            else:
                params['ticket_display_mode'] = self.ticket_display_mode
        if self.ticket_id:
            if hasattr(self.ticket_id, 'to_alipay_dict'):
                params['ticket_id'] = self.ticket_id.to_alipay_dict()
            else:
                params['ticket_id'] = self.ticket_id
        if self.ticket_status:
            if hasattr(self.ticket_status, 'to_alipay_dict'):
                params['ticket_status'] = self.ticket_status.to_alipay_dict()
            else:
                params['ticket_status'] = self.ticket_status
        if self.time_cards:
            if hasattr(self.time_cards, 'to_alipay_dict'):
                params['time_cards'] = self.time_cards.to_alipay_dict()
            else:
                params['time_cards'] = self.time_cards
        if self.total_quantity:
            if hasattr(self.total_quantity, 'to_alipay_dict'):
                params['total_quantity'] = self.total_quantity.to_alipay_dict()
            else:
                params['total_quantity'] = self.total_quantity
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TicketCodeQueryResponse()
        if 'available_quantity' in d:
            o.available_quantity = d['available_quantity']
        if 'effect_date' in d:
            o.effect_date = d['effect_date']
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'item_goods_ids' in d:
            o.item_goods_ids = d['item_goods_ids']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'ticket_display_mode' in d:
            o.ticket_display_mode = d['ticket_display_mode']
        if 'ticket_id' in d:
            o.ticket_id = d['ticket_id']
        if 'ticket_status' in d:
            o.ticket_status = d['ticket_status']
        if 'time_cards' in d:
            o.time_cards = d['time_cards']
        if 'total_quantity' in d:
            o.total_quantity = d['total_quantity']
        return o


