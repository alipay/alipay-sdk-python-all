#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MedicalSubscribeMsgSendArg import MedicalSubscribeMsgSendArg


class AlipayCommerceMedicalSubscribemsgSendModel(object):

    def __init__(self):
        self._msg_arg_list = None
        self._out_msg_id = None
        self._template_code = None
        self._to_open_id = None
        self._to_user_id = None

    @property
    def msg_arg_list(self):
        return self._msg_arg_list

    @msg_arg_list.setter
    def msg_arg_list(self, value):
        if isinstance(value, list):
            self._msg_arg_list = list()
            for i in value:
                if isinstance(i, MedicalSubscribeMsgSendArg):
                    self._msg_arg_list.append(i)
                else:
                    self._msg_arg_list.append(MedicalSubscribeMsgSendArg.from_alipay_dict(i))
    @property
    def out_msg_id(self):
        return self._out_msg_id

    @out_msg_id.setter
    def out_msg_id(self, value):
        self._out_msg_id = value
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value
    @property
    def to_open_id(self):
        return self._to_open_id

    @to_open_id.setter
    def to_open_id(self, value):
        self._to_open_id = value
    @property
    def to_user_id(self):
        return self._to_user_id

    @to_user_id.setter
    def to_user_id(self, value):
        self._to_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.msg_arg_list:
            if isinstance(self.msg_arg_list, list):
                for i in range(0, len(self.msg_arg_list)):
                    element = self.msg_arg_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.msg_arg_list[i] = element.to_alipay_dict()
            if hasattr(self.msg_arg_list, 'to_alipay_dict'):
                params['msg_arg_list'] = self.msg_arg_list.to_alipay_dict()
            else:
                params['msg_arg_list'] = self.msg_arg_list
        if self.out_msg_id:
            if hasattr(self.out_msg_id, 'to_alipay_dict'):
                params['out_msg_id'] = self.out_msg_id.to_alipay_dict()
            else:
                params['out_msg_id'] = self.out_msg_id
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        if self.to_open_id:
            if hasattr(self.to_open_id, 'to_alipay_dict'):
                params['to_open_id'] = self.to_open_id.to_alipay_dict()
            else:
                params['to_open_id'] = self.to_open_id
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
        o = AlipayCommerceMedicalSubscribemsgSendModel()
        if 'msg_arg_list' in d:
            o.msg_arg_list = d['msg_arg_list']
        if 'out_msg_id' in d:
            o.out_msg_id = d['out_msg_id']
        if 'template_code' in d:
            o.template_code = d['template_code']
        if 'to_open_id' in d:
            o.to_open_id = d['to_open_id']
        if 'to_user_id' in d:
            o.to_user_id = d['to_user_id']
        return o


