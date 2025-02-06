#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContentVo import ContentVo


class AlipayCommerceMedicalIndustrydataImSyncModel(object):

    def __init__(self):
        self._alipay_chat_id = None
        self._alipay_order_id = None
        self._content = None
        self._merchant_user_id = None
        self._msg_type = None
        self._out_biz_no = None
        self._out_chat_id = None
        self._out_doctor_id = None
        self._out_msg_id = None
        self._provider_type = None
        self._service_provider_name = None

    @property
    def alipay_chat_id(self):
        return self._alipay_chat_id

    @alipay_chat_id.setter
    def alipay_chat_id(self, value):
        self._alipay_chat_id = value
    @property
    def alipay_order_id(self):
        return self._alipay_order_id

    @alipay_order_id.setter
    def alipay_order_id(self, value):
        self._alipay_order_id = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, ContentVo):
            self._content = value
        else:
            self._content = ContentVo.from_alipay_dict(value)
    @property
    def merchant_user_id(self):
        return self._merchant_user_id

    @merchant_user_id.setter
    def merchant_user_id(self, value):
        self._merchant_user_id = value
    @property
    def msg_type(self):
        return self._msg_type

    @msg_type.setter
    def msg_type(self, value):
        self._msg_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_chat_id(self):
        return self._out_chat_id

    @out_chat_id.setter
    def out_chat_id(self, value):
        self._out_chat_id = value
    @property
    def out_doctor_id(self):
        return self._out_doctor_id

    @out_doctor_id.setter
    def out_doctor_id(self, value):
        self._out_doctor_id = value
    @property
    def out_msg_id(self):
        return self._out_msg_id

    @out_msg_id.setter
    def out_msg_id(self, value):
        self._out_msg_id = value
    @property
    def provider_type(self):
        return self._provider_type

    @provider_type.setter
    def provider_type(self, value):
        self._provider_type = value
    @property
    def service_provider_name(self):
        return self._service_provider_name

    @service_provider_name.setter
    def service_provider_name(self, value):
        self._service_provider_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_chat_id:
            if hasattr(self.alipay_chat_id, 'to_alipay_dict'):
                params['alipay_chat_id'] = self.alipay_chat_id.to_alipay_dict()
            else:
                params['alipay_chat_id'] = self.alipay_chat_id
        if self.alipay_order_id:
            if hasattr(self.alipay_order_id, 'to_alipay_dict'):
                params['alipay_order_id'] = self.alipay_order_id.to_alipay_dict()
            else:
                params['alipay_order_id'] = self.alipay_order_id
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.merchant_user_id:
            if hasattr(self.merchant_user_id, 'to_alipay_dict'):
                params['merchant_user_id'] = self.merchant_user_id.to_alipay_dict()
            else:
                params['merchant_user_id'] = self.merchant_user_id
        if self.msg_type:
            if hasattr(self.msg_type, 'to_alipay_dict'):
                params['msg_type'] = self.msg_type.to_alipay_dict()
            else:
                params['msg_type'] = self.msg_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_chat_id:
            if hasattr(self.out_chat_id, 'to_alipay_dict'):
                params['out_chat_id'] = self.out_chat_id.to_alipay_dict()
            else:
                params['out_chat_id'] = self.out_chat_id
        if self.out_doctor_id:
            if hasattr(self.out_doctor_id, 'to_alipay_dict'):
                params['out_doctor_id'] = self.out_doctor_id.to_alipay_dict()
            else:
                params['out_doctor_id'] = self.out_doctor_id
        if self.out_msg_id:
            if hasattr(self.out_msg_id, 'to_alipay_dict'):
                params['out_msg_id'] = self.out_msg_id.to_alipay_dict()
            else:
                params['out_msg_id'] = self.out_msg_id
        if self.provider_type:
            if hasattr(self.provider_type, 'to_alipay_dict'):
                params['provider_type'] = self.provider_type.to_alipay_dict()
            else:
                params['provider_type'] = self.provider_type
        if self.service_provider_name:
            if hasattr(self.service_provider_name, 'to_alipay_dict'):
                params['service_provider_name'] = self.service_provider_name.to_alipay_dict()
            else:
                params['service_provider_name'] = self.service_provider_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalIndustrydataImSyncModel()
        if 'alipay_chat_id' in d:
            o.alipay_chat_id = d['alipay_chat_id']
        if 'alipay_order_id' in d:
            o.alipay_order_id = d['alipay_order_id']
        if 'content' in d:
            o.content = d['content']
        if 'merchant_user_id' in d:
            o.merchant_user_id = d['merchant_user_id']
        if 'msg_type' in d:
            o.msg_type = d['msg_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_chat_id' in d:
            o.out_chat_id = d['out_chat_id']
        if 'out_doctor_id' in d:
            o.out_doctor_id = d['out_doctor_id']
        if 'out_msg_id' in d:
            o.out_msg_id = d['out_msg_id']
        if 'provider_type' in d:
            o.provider_type = d['provider_type']
        if 'service_provider_name' in d:
            o.service_provider_name = d['service_provider_name']
        return o


