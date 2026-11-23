#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceNfcmarketingOrdermessageSyncModel(object):

    def __init__(self):
        self._event_status = None
        self._event_type = None
        self._message_id = None
        self._message_info = None
        self._order_no = None
        self._out_biz_no = None
        self._refund_order_no = None
        self._session_product_id = None
        self._topic = None

    @property
    def event_status(self):
        return self._event_status

    @event_status.setter
    def event_status(self, value):
        self._event_status = value
    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
    @property
    def message_id(self):
        return self._message_id

    @message_id.setter
    def message_id(self, value):
        self._message_id = value
    @property
    def message_info(self):
        return self._message_info

    @message_info.setter
    def message_info(self, value):
        self._message_info = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def refund_order_no(self):
        return self._refund_order_no

    @refund_order_no.setter
    def refund_order_no(self, value):
        self._refund_order_no = value
    @property
    def session_product_id(self):
        return self._session_product_id

    @session_product_id.setter
    def session_product_id(self, value):
        self._session_product_id = value
    @property
    def topic(self):
        return self._topic

    @topic.setter
    def topic(self, value):
        self._topic = value


    def to_alipay_dict(self):
        params = dict()
        if self.event_status:
            if hasattr(self.event_status, 'to_alipay_dict'):
                params['event_status'] = self.event_status.to_alipay_dict()
            else:
                params['event_status'] = self.event_status
        if self.event_type:
            if hasattr(self.event_type, 'to_alipay_dict'):
                params['event_type'] = self.event_type.to_alipay_dict()
            else:
                params['event_type'] = self.event_type
        if self.message_id:
            if hasattr(self.message_id, 'to_alipay_dict'):
                params['message_id'] = self.message_id.to_alipay_dict()
            else:
                params['message_id'] = self.message_id
        if self.message_info:
            if hasattr(self.message_info, 'to_alipay_dict'):
                params['message_info'] = self.message_info.to_alipay_dict()
            else:
                params['message_info'] = self.message_info
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.refund_order_no:
            if hasattr(self.refund_order_no, 'to_alipay_dict'):
                params['refund_order_no'] = self.refund_order_no.to_alipay_dict()
            else:
                params['refund_order_no'] = self.refund_order_no
        if self.session_product_id:
            if hasattr(self.session_product_id, 'to_alipay_dict'):
                params['session_product_id'] = self.session_product_id.to_alipay_dict()
            else:
                params['session_product_id'] = self.session_product_id
        if self.topic:
            if hasattr(self.topic, 'to_alipay_dict'):
                params['topic'] = self.topic.to_alipay_dict()
            else:
                params['topic'] = self.topic
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceNfcmarketingOrdermessageSyncModel()
        if 'event_status' in d:
            o.event_status = d['event_status']
        if 'event_type' in d:
            o.event_type = d['event_type']
        if 'message_id' in d:
            o.message_id = d['message_id']
        if 'message_info' in d:
            o.message_info = d['message_info']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'refund_order_no' in d:
            o.refund_order_no = d['refund_order_no']
        if 'session_product_id' in d:
            o.session_product_id = d['session_product_id']
        if 'topic' in d:
            o.topic = d['topic']
        return o


