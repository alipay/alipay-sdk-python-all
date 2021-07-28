#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SnApplyInfo(object):

    def __init__(self):
        self._apply_id = None
        self._content = None
        self._gmt_create = None
        self._item_id = None
        self._sn_count = None
        self._status = None
        self._supplier_id = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def sn_count(self):
        return self._sn_count

    @sn_count.setter
    def sn_count(self, value):
        self._sn_count = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.sn_count:
            if hasattr(self.sn_count, 'to_alipay_dict'):
                params['sn_count'] = self.sn_count.to_alipay_dict()
            else:
                params['sn_count'] = self.sn_count
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SnApplyInfo()
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'content' in d:
            o.content = d['content']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'sn_count' in d:
            o.sn_count = d['sn_count']
        if 'status' in d:
            o.status = d['status']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        return o


