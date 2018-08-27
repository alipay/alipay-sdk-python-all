#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KoubeiOperationContext import KoubeiOperationContext


class KoubeiItemBatchqueryModel(object):

    def __init__(self):
        self._auth_code = None
        self._item_ids = None
        self._operation_context = None
        self._page_no = None
        self._page_size = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def item_ids(self):
        return self._item_ids

    @item_ids.setter
    def item_ids(self, value):
        self._item_ids = value
    @property
    def operation_context(self):
        return self._operation_context

    @operation_context.setter
    def operation_context(self, value):
        if isinstance(value, KoubeiOperationContext):
            self._operation_context = value
        else:
            self._operation_context = KoubeiOperationContext.from_alipay_dict(value)
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
        if self.item_ids:
            if hasattr(self.item_ids, 'to_alipay_dict'):
                params['item_ids'] = self.item_ids.to_alipay_dict()
            else:
                params['item_ids'] = self.item_ids
        if self.operation_context:
            if hasattr(self.operation_context, 'to_alipay_dict'):
                params['operation_context'] = self.operation_context.to_alipay_dict()
            else:
                params['operation_context'] = self.operation_context
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiItemBatchqueryModel()
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'item_ids' in d:
            o.item_ids = d['item_ids']
        if 'operation_context' in d:
            o.operation_context = d['operation_context']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


