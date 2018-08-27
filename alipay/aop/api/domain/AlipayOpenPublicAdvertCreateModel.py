#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AdvertItem import AdvertItem


class AlipayOpenPublicAdvertCreateModel(object):

    def __init__(self):
        self._advert_items = None

    @property
    def advert_items(self):
        return self._advert_items

    @advert_items.setter
    def advert_items(self, value):
        if isinstance(value, list):
            self._advert_items = list()
            for i in value:
                if isinstance(i, AdvertItem):
                    self._advert_items.append(i)
                else:
                    self._advert_items.append(AdvertItem.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.advert_items:
            if isinstance(self.advert_items, list):
                for i in range(0, len(self.advert_items)):
                    element = self.advert_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.advert_items[i] = element.to_alipay_dict()
            if hasattr(self.advert_items, 'to_alipay_dict'):
                params['advert_items'] = self.advert_items.to_alipay_dict()
            else:
                params['advert_items'] = self.advert_items
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicAdvertCreateModel()
        if 'advert_items' in d:
            o.advert_items = d['advert_items']
        return o


