#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlipmcMetaqMessageOpenMqBody import AlipmcMetaqMessageOpenMqBody


class AlipmcMetaqMessageOpenMqDTO(object):

    def __init__(self):
        self._alipmc_message_id = None
        self._app_name = None
        self._body = None
        self._group_id = None
        self._message_timestamp = None
        self._message_type = None

    @property
    def alipmc_message_id(self):
        return self._alipmc_message_id

    @alipmc_message_id.setter
    def alipmc_message_id(self, value):
        self._alipmc_message_id = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        if isinstance(value, AlipmcMetaqMessageOpenMqBody):
            self._body = value
        else:
            self._body = AlipmcMetaqMessageOpenMqBody.from_alipay_dict(value)
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def message_timestamp(self):
        return self._message_timestamp

    @message_timestamp.setter
    def message_timestamp(self, value):
        self._message_timestamp = value
    @property
    def message_type(self):
        return self._message_type

    @message_type.setter
    def message_type(self, value):
        self._message_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipmc_message_id:
            if hasattr(self.alipmc_message_id, 'to_alipay_dict'):
                params['alipmc_message_id'] = self.alipmc_message_id.to_alipay_dict()
            else:
                params['alipmc_message_id'] = self.alipmc_message_id
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.body:
            if hasattr(self.body, 'to_alipay_dict'):
                params['body'] = self.body.to_alipay_dict()
            else:
                params['body'] = self.body
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.message_timestamp:
            if hasattr(self.message_timestamp, 'to_alipay_dict'):
                params['message_timestamp'] = self.message_timestamp.to_alipay_dict()
            else:
                params['message_timestamp'] = self.message_timestamp
        if self.message_type:
            if hasattr(self.message_type, 'to_alipay_dict'):
                params['message_type'] = self.message_type.to_alipay_dict()
            else:
                params['message_type'] = self.message_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipmcMetaqMessageOpenMqDTO()
        if 'alipmc_message_id' in d:
            o.alipmc_message_id = d['alipmc_message_id']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'body' in d:
            o.body = d['body']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'message_timestamp' in d:
            o.message_timestamp = d['message_timestamp']
        if 'message_type' in d:
            o.message_type = d['message_type']
        return o


