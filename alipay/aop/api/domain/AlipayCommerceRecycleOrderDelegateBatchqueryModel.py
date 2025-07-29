#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRecycleOrderDelegateBatchqueryModel(object):

    def __init__(self):
        self._delegate_type = None
        self._open_id = None
        self._order_status = None
        self._order_status_list = None
        self._page_no = None
        self._page_size = None
        self._recycle_category_list = None
        self._user_id = None

    @property
    def delegate_type(self):
        return self._delegate_type

    @delegate_type.setter
    def delegate_type(self, value):
        self._delegate_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_status_list(self):
        return self._order_status_list

    @order_status_list.setter
    def order_status_list(self, value):
        if isinstance(value, list):
            self._order_status_list = list()
            for i in value:
                self._order_status_list.append(i)
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
    @property
    def recycle_category_list(self):
        return self._recycle_category_list

    @recycle_category_list.setter
    def recycle_category_list(self, value):
        if isinstance(value, list):
            self._recycle_category_list = list()
            for i in value:
                self._recycle_category_list.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.delegate_type:
            if hasattr(self.delegate_type, 'to_alipay_dict'):
                params['delegate_type'] = self.delegate_type.to_alipay_dict()
            else:
                params['delegate_type'] = self.delegate_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.order_status_list:
            if isinstance(self.order_status_list, list):
                for i in range(0, len(self.order_status_list)):
                    element = self.order_status_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_status_list[i] = element.to_alipay_dict()
            if hasattr(self.order_status_list, 'to_alipay_dict'):
                params['order_status_list'] = self.order_status_list.to_alipay_dict()
            else:
                params['order_status_list'] = self.order_status_list
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
        if self.recycle_category_list:
            if isinstance(self.recycle_category_list, list):
                for i in range(0, len(self.recycle_category_list)):
                    element = self.recycle_category_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.recycle_category_list[i] = element.to_alipay_dict()
            if hasattr(self.recycle_category_list, 'to_alipay_dict'):
                params['recycle_category_list'] = self.recycle_category_list.to_alipay_dict()
            else:
                params['recycle_category_list'] = self.recycle_category_list
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRecycleOrderDelegateBatchqueryModel()
        if 'delegate_type' in d:
            o.delegate_type = d['delegate_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_status_list' in d:
            o.order_status_list = d['order_status_list']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'recycle_category_list' in d:
            o.recycle_category_list = d['recycle_category_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


