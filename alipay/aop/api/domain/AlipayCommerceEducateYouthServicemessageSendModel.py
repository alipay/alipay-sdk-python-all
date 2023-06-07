#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateYouthServicemessageSendModel(object):

    def __init__(self):
        self._biz_code = None
        self._from_app_id = None
        self._message_properties = None
        self._msg_enum = None
        self._open_id = None
        self._out_biz_no = None
        self._to_user_id = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def from_app_id(self):
        return self._from_app_id

    @from_app_id.setter
    def from_app_id(self, value):
        self._from_app_id = value
    @property
    def message_properties(self):
        return self._message_properties

    @message_properties.setter
    def message_properties(self, value):
        self._message_properties = value
    @property
    def msg_enum(self):
        return self._msg_enum

    @msg_enum.setter
    def msg_enum(self, value):
        self._msg_enum = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def to_user_id(self):
        return self._to_user_id

    @to_user_id.setter
    def to_user_id(self, value):
        self._to_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.from_app_id:
            if hasattr(self.from_app_id, 'to_alipay_dict'):
                params['from_app_id'] = self.from_app_id.to_alipay_dict()
            else:
                params['from_app_id'] = self.from_app_id
        if self.message_properties:
            if hasattr(self.message_properties, 'to_alipay_dict'):
                params['message_properties'] = self.message_properties.to_alipay_dict()
            else:
                params['message_properties'] = self.message_properties
        if self.msg_enum:
            if hasattr(self.msg_enum, 'to_alipay_dict'):
                params['msg_enum'] = self.msg_enum.to_alipay_dict()
            else:
                params['msg_enum'] = self.msg_enum
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.to_user_id:
            if hasattr(self.to_user_id, 'to_alipay_dict'):
                params['to_user_id'] = self.to_user_id.to_alipay_dict()
            else:
                params['to_user_id'] = self.to_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateYouthServicemessageSendModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'from_app_id' in d:
            o.from_app_id = d['from_app_id']
        if 'message_properties' in d:
            o.message_properties = d['message_properties']
        if 'msg_enum' in d:
            o.msg_enum = d['msg_enum']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'to_user_id' in d:
            o.to_user_id = d['to_user_id']
        return o


