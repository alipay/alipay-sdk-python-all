#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalAqdualchannelMsgSendModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._alipay_user_open_id = None
        self._azr_msg_send = None
        self._ext_info = None
        self._msg_context = None
        self._msg_create_time = None
        self._msg_modified_time = None
        self._org_id = None
        self._out_biz_no = None
        self._template_code = None
        self._user_card_no = None
        self._user_card_type = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def alipay_user_open_id(self):
        return self._alipay_user_open_id

    @alipay_user_open_id.setter
    def alipay_user_open_id(self, value):
        self._alipay_user_open_id = value
    @property
    def azr_msg_send(self):
        return self._azr_msg_send

    @azr_msg_send.setter
    def azr_msg_send(self, value):
        self._azr_msg_send = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def msg_context(self):
        return self._msg_context

    @msg_context.setter
    def msg_context(self, value):
        self._msg_context = value
    @property
    def msg_create_time(self):
        return self._msg_create_time

    @msg_create_time.setter
    def msg_create_time(self, value):
        self._msg_create_time = value
    @property
    def msg_modified_time(self):
        return self._msg_modified_time

    @msg_modified_time.setter
    def msg_modified_time(self, value):
        self._msg_modified_time = value
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
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
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.alipay_user_open_id:
            if hasattr(self.alipay_user_open_id, 'to_alipay_dict'):
                params['alipay_user_open_id'] = self.alipay_user_open_id.to_alipay_dict()
            else:
                params['alipay_user_open_id'] = self.alipay_user_open_id
        if self.azr_msg_send:
            if hasattr(self.azr_msg_send, 'to_alipay_dict'):
                params['azr_msg_send'] = self.azr_msg_send.to_alipay_dict()
            else:
                params['azr_msg_send'] = self.azr_msg_send
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.msg_context:
            if hasattr(self.msg_context, 'to_alipay_dict'):
                params['msg_context'] = self.msg_context.to_alipay_dict()
            else:
                params['msg_context'] = self.msg_context
        if self.msg_create_time:
            if hasattr(self.msg_create_time, 'to_alipay_dict'):
                params['msg_create_time'] = self.msg_create_time.to_alipay_dict()
            else:
                params['msg_create_time'] = self.msg_create_time
        if self.msg_modified_time:
            if hasattr(self.msg_modified_time, 'to_alipay_dict'):
                params['msg_modified_time'] = self.msg_modified_time.to_alipay_dict()
            else:
                params['msg_modified_time'] = self.msg_modified_time
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
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
        o = AlipayCommerceMedicalAqdualchannelMsgSendModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'alipay_user_open_id' in d:
            o.alipay_user_open_id = d['alipay_user_open_id']
        if 'azr_msg_send' in d:
            o.azr_msg_send = d['azr_msg_send']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'msg_context' in d:
            o.msg_context = d['msg_context']
        if 'msg_create_time' in d:
            o.msg_create_time = d['msg_create_time']
        if 'msg_modified_time' in d:
            o.msg_modified_time = d['msg_modified_time']
        if 'org_id' in d:
            o.org_id = d['org_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'template_code' in d:
            o.template_code = d['template_code']
        if 'user_card_no' in d:
            o.user_card_no = d['user_card_no']
        if 'user_card_type' in d:
            o.user_card_type = d['user_card_type']
        return o


