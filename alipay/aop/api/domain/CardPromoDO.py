#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardPromoDO(object):

    def __init__(self):
        self._card_id = None
        self._card_level = None
        self._limit = None
        self._promo_icon = None
        self._promo_title = None
        self._received = None
        self._target_mark_count = None

    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def card_level(self):
        return self._card_level

    @card_level.setter
    def card_level(self, value):
        self._card_level = value
    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, value):
        self._limit = value
    @property
    def promo_icon(self):
        return self._promo_icon

    @promo_icon.setter
    def promo_icon(self, value):
        self._promo_icon = value
    @property
    def promo_title(self):
        return self._promo_title

    @promo_title.setter
    def promo_title(self, value):
        self._promo_title = value
    @property
    def received(self):
        return self._received

    @received.setter
    def received(self, value):
        self._received = value
    @property
    def target_mark_count(self):
        return self._target_mark_count

    @target_mark_count.setter
    def target_mark_count(self, value):
        self._target_mark_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.card_level:
            if hasattr(self.card_level, 'to_alipay_dict'):
                params['card_level'] = self.card_level.to_alipay_dict()
            else:
                params['card_level'] = self.card_level
        if self.limit:
            if hasattr(self.limit, 'to_alipay_dict'):
                params['limit'] = self.limit.to_alipay_dict()
            else:
                params['limit'] = self.limit
        if self.promo_icon:
            if hasattr(self.promo_icon, 'to_alipay_dict'):
                params['promo_icon'] = self.promo_icon.to_alipay_dict()
            else:
                params['promo_icon'] = self.promo_icon
        if self.promo_title:
            if hasattr(self.promo_title, 'to_alipay_dict'):
                params['promo_title'] = self.promo_title.to_alipay_dict()
            else:
                params['promo_title'] = self.promo_title
        if self.received:
            if hasattr(self.received, 'to_alipay_dict'):
                params['received'] = self.received.to_alipay_dict()
            else:
                params['received'] = self.received
        if self.target_mark_count:
            if hasattr(self.target_mark_count, 'to_alipay_dict'):
                params['target_mark_count'] = self.target_mark_count.to_alipay_dict()
            else:
                params['target_mark_count'] = self.target_mark_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardPromoDO()
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'card_level' in d:
            o.card_level = d['card_level']
        if 'limit' in d:
            o.limit = d['limit']
        if 'promo_icon' in d:
            o.promo_icon = d['promo_icon']
        if 'promo_title' in d:
            o.promo_title = d['promo_title']
        if 'received' in d:
            o.received = d['received']
        if 'target_mark_count' in d:
            o.target_mark_count = d['target_mark_count']
        return o


