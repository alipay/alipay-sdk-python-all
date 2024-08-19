#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceSearchboxStatusModifyModel(object):

    def __init__(self):
        self._category_id = None
        self._client_type = None
        self._item_id = None
        self._modify_type = None
        self._status = None

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def client_type(self):
        return self._client_type

    @client_type.setter
    def client_type(self, value):
        if isinstance(value, list):
            self._client_type = list()
            for i in value:
                self._client_type.append(i)
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def modify_type(self):
        return self._modify_type

    @modify_type.setter
    def modify_type(self, value):
        self._modify_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.client_type:
            if isinstance(self.client_type, list):
                for i in range(0, len(self.client_type)):
                    element = self.client_type[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.client_type[i] = element.to_alipay_dict()
            if hasattr(self.client_type, 'to_alipay_dict'):
                params['client_type'] = self.client_type.to_alipay_dict()
            else:
                params['client_type'] = self.client_type
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.modify_type:
            if hasattr(self.modify_type, 'to_alipay_dict'):
                params['modify_type'] = self.modify_type.to_alipay_dict()
            else:
                params['modify_type'] = self.modify_type
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceSearchboxStatusModifyModel()
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'client_type' in d:
            o.client_type = d['client_type']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'modify_type' in d:
            o.modify_type = d['modify_type']
        if 'status' in d:
            o.status = d['status']
        return o


