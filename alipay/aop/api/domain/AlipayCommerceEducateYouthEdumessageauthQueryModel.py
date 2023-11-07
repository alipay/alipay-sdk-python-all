#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateYouthEdumessageauthQueryModel(object):

    def __init__(self):
        self._biz_code = None
        self._from_app_id = None
        self._inst_id = None
        self._msg_enum_list = None
        self._open_id = None
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
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def msg_enum_list(self):
        return self._msg_enum_list

    @msg_enum_list.setter
    def msg_enum_list(self, value):
        if isinstance(value, list):
            self._msg_enum_list = list()
            for i in value:
                self._msg_enum_list.append(i)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
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
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.msg_enum_list:
            if isinstance(self.msg_enum_list, list):
                for i in range(0, len(self.msg_enum_list)):
                    element = self.msg_enum_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.msg_enum_list[i] = element.to_alipay_dict()
            if hasattr(self.msg_enum_list, 'to_alipay_dict'):
                params['msg_enum_list'] = self.msg_enum_list.to_alipay_dict()
            else:
                params['msg_enum_list'] = self.msg_enum_list
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        o = AlipayCommerceEducateYouthEdumessageauthQueryModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'from_app_id' in d:
            o.from_app_id = d['from_app_id']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'msg_enum_list' in d:
            o.msg_enum_list = d['msg_enum_list']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'to_user_id' in d:
            o.to_user_id = d['to_user_id']
        return o


