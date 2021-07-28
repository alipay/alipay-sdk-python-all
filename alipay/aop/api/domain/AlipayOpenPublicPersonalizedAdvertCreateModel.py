#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AdvertItem import AdvertItem


class AlipayOpenPublicPersonalizedAdvertCreateModel(object):

    def __init__(self):
        self._advert_items = None
        self._group_id = None
        self._mobile_client_type = None

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
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def mobile_client_type(self):
        return self._mobile_client_type

    @mobile_client_type.setter
    def mobile_client_type(self, value):
        self._mobile_client_type = value


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
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.mobile_client_type:
            if hasattr(self.mobile_client_type, 'to_alipay_dict'):
                params['mobile_client_type'] = self.mobile_client_type.to_alipay_dict()
            else:
                params['mobile_client_type'] = self.mobile_client_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicPersonalizedAdvertCreateModel()
        if 'advert_items' in d:
            o.advert_items = d['advert_items']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'mobile_client_type' in d:
            o.mobile_client_type = d['mobile_client_type']
        return o


