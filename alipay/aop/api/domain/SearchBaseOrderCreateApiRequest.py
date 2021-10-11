#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SearchBaseItems import SearchBaseItems


class SearchBaseOrderCreateApiRequest(object):

    def __init__(self):
        self._access_type = None
        self._appid = None
        self._base_items = None
        self._descprise = None
        self._is_draft = None
        self._order_id = None
        self._spec_code = None

    @property
    def access_type(self):
        return self._access_type

    @access_type.setter
    def access_type(self, value):
        self._access_type = value
    @property
    def appid(self):
        return self._appid

    @appid.setter
    def appid(self, value):
        self._appid = value
    @property
    def base_items(self):
        return self._base_items

    @base_items.setter
    def base_items(self, value):
        if isinstance(value, SearchBaseItems):
            self._base_items = value
        else:
            self._base_items = SearchBaseItems.from_alipay_dict(value)
    @property
    def descprise(self):
        return self._descprise

    @descprise.setter
    def descprise(self, value):
        self._descprise = value
    @property
    def is_draft(self):
        return self._is_draft

    @is_draft.setter
    def is_draft(self, value):
        self._is_draft = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def spec_code(self):
        return self._spec_code

    @spec_code.setter
    def spec_code(self, value):
        self._spec_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_type:
            if hasattr(self.access_type, 'to_alipay_dict'):
                params['access_type'] = self.access_type.to_alipay_dict()
            else:
                params['access_type'] = self.access_type
        if self.appid:
            if hasattr(self.appid, 'to_alipay_dict'):
                params['appid'] = self.appid.to_alipay_dict()
            else:
                params['appid'] = self.appid
        if self.base_items:
            if hasattr(self.base_items, 'to_alipay_dict'):
                params['base_items'] = self.base_items.to_alipay_dict()
            else:
                params['base_items'] = self.base_items
        if self.descprise:
            if hasattr(self.descprise, 'to_alipay_dict'):
                params['descprise'] = self.descprise.to_alipay_dict()
            else:
                params['descprise'] = self.descprise
        if self.is_draft:
            if hasattr(self.is_draft, 'to_alipay_dict'):
                params['is_draft'] = self.is_draft.to_alipay_dict()
            else:
                params['is_draft'] = self.is_draft
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.spec_code:
            if hasattr(self.spec_code, 'to_alipay_dict'):
                params['spec_code'] = self.spec_code.to_alipay_dict()
            else:
                params['spec_code'] = self.spec_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchBaseOrderCreateApiRequest()
        if 'access_type' in d:
            o.access_type = d['access_type']
        if 'appid' in d:
            o.appid = d['appid']
        if 'base_items' in d:
            o.base_items = d['base_items']
        if 'descprise' in d:
            o.descprise = d['descprise']
        if 'is_draft' in d:
            o.is_draft = d['is_draft']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'spec_code' in d:
            o.spec_code = d['spec_code']
        return o


