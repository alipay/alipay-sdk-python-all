#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LifeServiceAttr import LifeServiceAttr


class AlipayCommerceLifeserviceBookingSyncModel(object):

    def __init__(self):
        self._action = None
        self._booking_attr = None
        self._booking_id = None
        self._shop_id = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def booking_attr(self):
        return self._booking_attr

    @booking_attr.setter
    def booking_attr(self, value):
        if isinstance(value, list):
            self._booking_attr = list()
            for i in value:
                if isinstance(i, LifeServiceAttr):
                    self._booking_attr.append(i)
                else:
                    self._booking_attr.append(LifeServiceAttr.from_alipay_dict(i))
    @property
    def booking_id(self):
        return self._booking_id

    @booking_id.setter
    def booking_id(self, value):
        self._booking_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.booking_attr:
            if isinstance(self.booking_attr, list):
                for i in range(0, len(self.booking_attr)):
                    element = self.booking_attr[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.booking_attr[i] = element.to_alipay_dict()
            if hasattr(self.booking_attr, 'to_alipay_dict'):
                params['booking_attr'] = self.booking_attr.to_alipay_dict()
            else:
                params['booking_attr'] = self.booking_attr
        if self.booking_id:
            if hasattr(self.booking_id, 'to_alipay_dict'):
                params['booking_id'] = self.booking_id.to_alipay_dict()
            else:
                params['booking_id'] = self.booking_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLifeserviceBookingSyncModel()
        if 'action' in d:
            o.action = d['action']
        if 'booking_attr' in d:
            o.booking_attr = d['booking_attr']
        if 'booking_id' in d:
            o.booking_id = d['booking_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


