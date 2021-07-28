#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotSdarttoolMessageSendModel(object):

    def __init__(self):
        self._bi_da = None
        self._device_query_type = None
        self._immediate_msg = None
        self._item_id = None
        self._msg_content = None
        self._msg_content_type = None
        self._msg_expire = None
        self._msg_priority = None
        self._msg_type = None
        self._service_id = None
        self._sn = None
        self._supplier_id = None

    @property
    def bi_da(self):
        return self._bi_da

    @bi_da.setter
    def bi_da(self, value):
        self._bi_da = value
    @property
    def device_query_type(self):
        return self._device_query_type

    @device_query_type.setter
    def device_query_type(self, value):
        self._device_query_type = value
    @property
    def immediate_msg(self):
        return self._immediate_msg

    @immediate_msg.setter
    def immediate_msg(self, value):
        self._immediate_msg = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def msg_content(self):
        return self._msg_content

    @msg_content.setter
    def msg_content(self, value):
        self._msg_content = value
    @property
    def msg_content_type(self):
        return self._msg_content_type

    @msg_content_type.setter
    def msg_content_type(self, value):
        self._msg_content_type = value
    @property
    def msg_expire(self):
        return self._msg_expire

    @msg_expire.setter
    def msg_expire(self, value):
        self._msg_expire = value
    @property
    def msg_priority(self):
        return self._msg_priority

    @msg_priority.setter
    def msg_priority(self, value):
        self._msg_priority = value
    @property
    def msg_type(self):
        return self._msg_type

    @msg_type.setter
    def msg_type(self, value):
        self._msg_type = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bi_da:
            if hasattr(self.bi_da, 'to_alipay_dict'):
                params['bi_da'] = self.bi_da.to_alipay_dict()
            else:
                params['bi_da'] = self.bi_da
        if self.device_query_type:
            if hasattr(self.device_query_type, 'to_alipay_dict'):
                params['device_query_type'] = self.device_query_type.to_alipay_dict()
            else:
                params['device_query_type'] = self.device_query_type
        if self.immediate_msg:
            if hasattr(self.immediate_msg, 'to_alipay_dict'):
                params['immediate_msg'] = self.immediate_msg.to_alipay_dict()
            else:
                params['immediate_msg'] = self.immediate_msg
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.msg_content:
            if hasattr(self.msg_content, 'to_alipay_dict'):
                params['msg_content'] = self.msg_content.to_alipay_dict()
            else:
                params['msg_content'] = self.msg_content
        if self.msg_content_type:
            if hasattr(self.msg_content_type, 'to_alipay_dict'):
                params['msg_content_type'] = self.msg_content_type.to_alipay_dict()
            else:
                params['msg_content_type'] = self.msg_content_type
        if self.msg_expire:
            if hasattr(self.msg_expire, 'to_alipay_dict'):
                params['msg_expire'] = self.msg_expire.to_alipay_dict()
            else:
                params['msg_expire'] = self.msg_expire
        if self.msg_priority:
            if hasattr(self.msg_priority, 'to_alipay_dict'):
                params['msg_priority'] = self.msg_priority.to_alipay_dict()
            else:
                params['msg_priority'] = self.msg_priority
        if self.msg_type:
            if hasattr(self.msg_type, 'to_alipay_dict'):
                params['msg_type'] = self.msg_type.to_alipay_dict()
            else:
                params['msg_type'] = self.msg_type
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
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
        o = AlipayCommerceIotSdarttoolMessageSendModel()
        if 'bi_da' in d:
            o.bi_da = d['bi_da']
        if 'device_query_type' in d:
            o.device_query_type = d['device_query_type']
        if 'immediate_msg' in d:
            o.immediate_msg = d['immediate_msg']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'msg_content' in d:
            o.msg_content = d['msg_content']
        if 'msg_content_type' in d:
            o.msg_content_type = d['msg_content_type']
        if 'msg_expire' in d:
            o.msg_expire = d['msg_expire']
        if 'msg_priority' in d:
            o.msg_priority = d['msg_priority']
        if 'msg_type' in d:
            o.msg_type = d['msg_type']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'sn' in d:
            o.sn = d['sn']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        return o


