#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CBDMessageBody import CBDMessageBody


class AlipayInsCbddoctorMessageSendModel(object):

    def __init__(self):
        self._client_msg_id = None
        self._message = None
        self._service_order_id = None

    @property
    def client_msg_id(self):
        return self._client_msg_id

    @client_msg_id.setter
    def client_msg_id(self, value):
        self._client_msg_id = value
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        if isinstance(value, CBDMessageBody):
            self._message = value
        else:
            self._message = CBDMessageBody.from_alipay_dict(value)
    @property
    def service_order_id(self):
        return self._service_order_id

    @service_order_id.setter
    def service_order_id(self, value):
        self._service_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.client_msg_id:
            if hasattr(self.client_msg_id, 'to_alipay_dict'):
                params['client_msg_id'] = self.client_msg_id.to_alipay_dict()
            else:
                params['client_msg_id'] = self.client_msg_id
        if self.message:
            if hasattr(self.message, 'to_alipay_dict'):
                params['message'] = self.message.to_alipay_dict()
            else:
                params['message'] = self.message
        if self.service_order_id:
            if hasattr(self.service_order_id, 'to_alipay_dict'):
                params['service_order_id'] = self.service_order_id.to_alipay_dict()
            else:
                params['service_order_id'] = self.service_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsCbddoctorMessageSendModel()
        if 'client_msg_id' in d:
            o.client_msg_id = d['client_msg_id']
        if 'message' in d:
            o.message = d['message']
        if 'service_order_id' in d:
            o.service_order_id = d['service_order_id']
        return o


