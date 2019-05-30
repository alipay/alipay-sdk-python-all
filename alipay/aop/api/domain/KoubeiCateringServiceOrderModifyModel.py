#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BookInfoModify import BookInfoModify
from alipay.aop.api.domain.QueueInfoModify import QueueInfoModify


class KoubeiCateringServiceOrderModifyModel(object):

    def __init__(self):
        self._book_info = None
        self._order_no = None
        self._order_state = None
        self._order_sub_state = None
        self._order_type = None
        self._out_order_no = None
        self._queue_info = None
        self._refuse_reason = None
        self._refuse_type = None
        self._sync_timestamp = None
        self._sync_type = None

    @property
    def book_info(self):
        return self._book_info

    @book_info.setter
    def book_info(self, value):
        if isinstance(value, BookInfoModify):
            self._book_info = value
        else:
            self._book_info = BookInfoModify.from_alipay_dict(value)
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_state(self):
        return self._order_state

    @order_state.setter
    def order_state(self, value):
        self._order_state = value
    @property
    def order_sub_state(self):
        return self._order_sub_state

    @order_sub_state.setter
    def order_sub_state(self, value):
        self._order_sub_state = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def queue_info(self):
        return self._queue_info

    @queue_info.setter
    def queue_info(self, value):
        if isinstance(value, QueueInfoModify):
            self._queue_info = value
        else:
            self._queue_info = QueueInfoModify.from_alipay_dict(value)
    @property
    def refuse_reason(self):
        return self._refuse_reason

    @refuse_reason.setter
    def refuse_reason(self, value):
        self._refuse_reason = value
    @property
    def refuse_type(self):
        return self._refuse_type

    @refuse_type.setter
    def refuse_type(self, value):
        self._refuse_type = value
    @property
    def sync_timestamp(self):
        return self._sync_timestamp

    @sync_timestamp.setter
    def sync_timestamp(self, value):
        self._sync_timestamp = value
    @property
    def sync_type(self):
        return self._sync_type

    @sync_type.setter
    def sync_type(self, value):
        self._sync_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.book_info:
            if hasattr(self.book_info, 'to_alipay_dict'):
                params['book_info'] = self.book_info.to_alipay_dict()
            else:
                params['book_info'] = self.book_info
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.order_state:
            if hasattr(self.order_state, 'to_alipay_dict'):
                params['order_state'] = self.order_state.to_alipay_dict()
            else:
                params['order_state'] = self.order_state
        if self.order_sub_state:
            if hasattr(self.order_sub_state, 'to_alipay_dict'):
                params['order_sub_state'] = self.order_sub_state.to_alipay_dict()
            else:
                params['order_sub_state'] = self.order_sub_state
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.queue_info:
            if hasattr(self.queue_info, 'to_alipay_dict'):
                params['queue_info'] = self.queue_info.to_alipay_dict()
            else:
                params['queue_info'] = self.queue_info
        if self.refuse_reason:
            if hasattr(self.refuse_reason, 'to_alipay_dict'):
                params['refuse_reason'] = self.refuse_reason.to_alipay_dict()
            else:
                params['refuse_reason'] = self.refuse_reason
        if self.refuse_type:
            if hasattr(self.refuse_type, 'to_alipay_dict'):
                params['refuse_type'] = self.refuse_type.to_alipay_dict()
            else:
                params['refuse_type'] = self.refuse_type
        if self.sync_timestamp:
            if hasattr(self.sync_timestamp, 'to_alipay_dict'):
                params['sync_timestamp'] = self.sync_timestamp.to_alipay_dict()
            else:
                params['sync_timestamp'] = self.sync_timestamp
        if self.sync_type:
            if hasattr(self.sync_type, 'to_alipay_dict'):
                params['sync_type'] = self.sync_type.to_alipay_dict()
            else:
                params['sync_type'] = self.sync_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringServiceOrderModifyModel()
        if 'book_info' in d:
            o.book_info = d['book_info']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'order_state' in d:
            o.order_state = d['order_state']
        if 'order_sub_state' in d:
            o.order_sub_state = d['order_sub_state']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'queue_info' in d:
            o.queue_info = d['queue_info']
        if 'refuse_reason' in d:
            o.refuse_reason = d['refuse_reason']
        if 'refuse_type' in d:
            o.refuse_type = d['refuse_type']
        if 'sync_timestamp' in d:
            o.sync_timestamp = d['sync_timestamp']
        if 'sync_type' in d:
            o.sync_type = d['sync_type']
        return o


