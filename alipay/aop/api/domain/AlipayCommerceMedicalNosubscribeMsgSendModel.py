#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MedicalNoSubscribeMsgSendArg import MedicalNoSubscribeMsgSendArg


class AlipayCommerceMedicalNosubscribeMsgSendModel(object):

    def __init__(self):
        self._alipay_open_id = None
        self._alipay_user_id = None
        self._msg_arg_list = None
        self._out_msg_id = None
        self._template_code = None
        self._user_card_no = None
        self._user_card_type = None

    @property
    def alipay_open_id(self):
        return self._alipay_open_id

    @alipay_open_id.setter
    def alipay_open_id(self, value):
        self._alipay_open_id = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def msg_arg_list(self):
        return self._msg_arg_list

    @msg_arg_list.setter
    def msg_arg_list(self, value):
        if isinstance(value, list):
            self._msg_arg_list = list()
            for i in value:
                if isinstance(i, MedicalNoSubscribeMsgSendArg):
                    self._msg_arg_list.append(i)
                else:
                    self._msg_arg_list.append(MedicalNoSubscribeMsgSendArg.from_alipay_dict(i))
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
    def user_card_no(self):
        return self._user_card_no

    @user_card_no.setter
    def user_card_no(self, value):
        self._user_card_no = value
    @property
    def user_card_type(self):
        return self._user_card_type

    @user_card_type.setter
    def user_card_type(self, value):
        self._user_card_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_open_id:
            if hasattr(self.alipay_open_id, 'to_alipay_dict'):
                params['alipay_open_id'] = self.alipay_open_id.to_alipay_dict()
            else:
                params['alipay_open_id'] = self.alipay_open_id
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
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
        if self.user_card_no:
            if hasattr(self.user_card_no, 'to_alipay_dict'):
                params['user_card_no'] = self.user_card_no.to_alipay_dict()
            else:
                params['user_card_no'] = self.user_card_no
        if self.user_card_type:
            if hasattr(self.user_card_type, 'to_alipay_dict'):
                params['user_card_type'] = self.user_card_type.to_alipay_dict()
            else:
                params['user_card_type'] = self.user_card_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalNosubscribeMsgSendModel()
        if 'alipay_open_id' in d:
            o.alipay_open_id = d['alipay_open_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'msg_arg_list' in d:
            o.msg_arg_list = d['msg_arg_list']
        if 'out_msg_id' in d:
            o.out_msg_id = d['out_msg_id']
        if 'template_code' in d:
            o.template_code = d['template_code']
        if 'user_card_no' in d:
            o.user_card_no = d['user_card_no']
        if 'user_card_type' in d:
            o.user_card_type = d['user_card_type']
        return o


