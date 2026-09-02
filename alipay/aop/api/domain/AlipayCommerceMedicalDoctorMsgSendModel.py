#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalDoctorMsgSendModel(object):

    def __init__(self):
        self._aq_user_id = None
        self._aq_user_open_id = None
        self._avatar = None
        self._client_msg_id = None
        self._conversation_id = None
        self._conversation_name = None
        self._conversation_type = None
        self._latest_msg_time = None
        self._link = None
        self._msg_data = None
        self._msg_id = None
        self._msg_template_code = None
        self._msg_type = None
        self._out_app_id = None
        self._out_biz_id = None
        self._out_biz_name = None
        self._receiver_type = None
        self._receivers = None
        self._send_types = None
        self._show_content = None
        self._template_params = None
        self._un_read_count = None

    @property
    def aq_user_id(self):
        return self._aq_user_id

    @aq_user_id.setter
    def aq_user_id(self, value):
        self._aq_user_id = value
    @property
    def aq_user_open_id(self):
        return self._aq_user_open_id

    @aq_user_open_id.setter
    def aq_user_open_id(self, value):
        self._aq_user_open_id = value
    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        self._avatar = value
    @property
    def client_msg_id(self):
        return self._client_msg_id

    @client_msg_id.setter
    def client_msg_id(self, value):
        self._client_msg_id = value
    @property
    def conversation_id(self):
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, value):
        self._conversation_id = value
    @property
    def conversation_name(self):
        return self._conversation_name

    @conversation_name.setter
    def conversation_name(self, value):
        self._conversation_name = value
    @property
    def conversation_type(self):
        return self._conversation_type

    @conversation_type.setter
    def conversation_type(self, value):
        self._conversation_type = value
    @property
    def latest_msg_time(self):
        return self._latest_msg_time

    @latest_msg_time.setter
    def latest_msg_time(self, value):
        self._latest_msg_time = value
    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value
    @property
    def msg_data(self):
        return self._msg_data

    @msg_data.setter
    def msg_data(self, value):
        self._msg_data = value
    @property
    def msg_id(self):
        return self._msg_id

    @msg_id.setter
    def msg_id(self, value):
        self._msg_id = value
    @property
    def msg_template_code(self):
        return self._msg_template_code

    @msg_template_code.setter
    def msg_template_code(self, value):
        self._msg_template_code = value
    @property
    def msg_type(self):
        return self._msg_type

    @msg_type.setter
    def msg_type(self, value):
        self._msg_type = value
    @property
    def out_app_id(self):
        return self._out_app_id

    @out_app_id.setter
    def out_app_id(self, value):
        self._out_app_id = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def out_biz_name(self):
        return self._out_biz_name

    @out_biz_name.setter
    def out_biz_name(self, value):
        self._out_biz_name = value
    @property
    def receiver_type(self):
        return self._receiver_type

    @receiver_type.setter
    def receiver_type(self, value):
        self._receiver_type = value
    @property
    def receivers(self):
        return self._receivers

    @receivers.setter
    def receivers(self, value):
        self._receivers = value
    @property
    def send_types(self):
        return self._send_types

    @send_types.setter
    def send_types(self, value):
        self._send_types = value
    @property
    def show_content(self):
        return self._show_content

    @show_content.setter
    def show_content(self, value):
        self._show_content = value
    @property
    def template_params(self):
        return self._template_params

    @template_params.setter
    def template_params(self, value):
        self._template_params = value
    @property
    def un_read_count(self):
        return self._un_read_count

    @un_read_count.setter
    def un_read_count(self, value):
        self._un_read_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.aq_user_id:
            if hasattr(self.aq_user_id, 'to_alipay_dict'):
                params['aq_user_id'] = self.aq_user_id.to_alipay_dict()
            else:
                params['aq_user_id'] = self.aq_user_id
        if self.aq_user_open_id:
            if hasattr(self.aq_user_open_id, 'to_alipay_dict'):
                params['aq_user_open_id'] = self.aq_user_open_id.to_alipay_dict()
            else:
                params['aq_user_open_id'] = self.aq_user_open_id
        if self.avatar:
            if hasattr(self.avatar, 'to_alipay_dict'):
                params['avatar'] = self.avatar.to_alipay_dict()
            else:
                params['avatar'] = self.avatar
        if self.client_msg_id:
            if hasattr(self.client_msg_id, 'to_alipay_dict'):
                params['client_msg_id'] = self.client_msg_id.to_alipay_dict()
            else:
                params['client_msg_id'] = self.client_msg_id
        if self.conversation_id:
            if hasattr(self.conversation_id, 'to_alipay_dict'):
                params['conversation_id'] = self.conversation_id.to_alipay_dict()
            else:
                params['conversation_id'] = self.conversation_id
        if self.conversation_name:
            if hasattr(self.conversation_name, 'to_alipay_dict'):
                params['conversation_name'] = self.conversation_name.to_alipay_dict()
            else:
                params['conversation_name'] = self.conversation_name
        if self.conversation_type:
            if hasattr(self.conversation_type, 'to_alipay_dict'):
                params['conversation_type'] = self.conversation_type.to_alipay_dict()
            else:
                params['conversation_type'] = self.conversation_type
        if self.latest_msg_time:
            if hasattr(self.latest_msg_time, 'to_alipay_dict'):
                params['latest_msg_time'] = self.latest_msg_time.to_alipay_dict()
            else:
                params['latest_msg_time'] = self.latest_msg_time
        if self.link:
            if hasattr(self.link, 'to_alipay_dict'):
                params['link'] = self.link.to_alipay_dict()
            else:
                params['link'] = self.link
        if self.msg_data:
            if hasattr(self.msg_data, 'to_alipay_dict'):
                params['msg_data'] = self.msg_data.to_alipay_dict()
            else:
                params['msg_data'] = self.msg_data
        if self.msg_id:
            if hasattr(self.msg_id, 'to_alipay_dict'):
                params['msg_id'] = self.msg_id.to_alipay_dict()
            else:
                params['msg_id'] = self.msg_id
        if self.msg_template_code:
            if hasattr(self.msg_template_code, 'to_alipay_dict'):
                params['msg_template_code'] = self.msg_template_code.to_alipay_dict()
            else:
                params['msg_template_code'] = self.msg_template_code
        if self.msg_type:
            if hasattr(self.msg_type, 'to_alipay_dict'):
                params['msg_type'] = self.msg_type.to_alipay_dict()
            else:
                params['msg_type'] = self.msg_type
        if self.out_app_id:
            if hasattr(self.out_app_id, 'to_alipay_dict'):
                params['out_app_id'] = self.out_app_id.to_alipay_dict()
            else:
                params['out_app_id'] = self.out_app_id
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.out_biz_name:
            if hasattr(self.out_biz_name, 'to_alipay_dict'):
                params['out_biz_name'] = self.out_biz_name.to_alipay_dict()
            else:
                params['out_biz_name'] = self.out_biz_name
        if self.receiver_type:
            if hasattr(self.receiver_type, 'to_alipay_dict'):
                params['receiver_type'] = self.receiver_type.to_alipay_dict()
            else:
                params['receiver_type'] = self.receiver_type
        if self.receivers:
            if hasattr(self.receivers, 'to_alipay_dict'):
                params['receivers'] = self.receivers.to_alipay_dict()
            else:
                params['receivers'] = self.receivers
        if self.send_types:
            if hasattr(self.send_types, 'to_alipay_dict'):
                params['send_types'] = self.send_types.to_alipay_dict()
            else:
                params['send_types'] = self.send_types
        if self.show_content:
            if hasattr(self.show_content, 'to_alipay_dict'):
                params['show_content'] = self.show_content.to_alipay_dict()
            else:
                params['show_content'] = self.show_content
        if self.template_params:
            if hasattr(self.template_params, 'to_alipay_dict'):
                params['template_params'] = self.template_params.to_alipay_dict()
            else:
                params['template_params'] = self.template_params
        if self.un_read_count:
            if hasattr(self.un_read_count, 'to_alipay_dict'):
                params['un_read_count'] = self.un_read_count.to_alipay_dict()
            else:
                params['un_read_count'] = self.un_read_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalDoctorMsgSendModel()
        if 'aq_user_id' in d:
            o.aq_user_id = d['aq_user_id']
        if 'aq_user_open_id' in d:
            o.aq_user_open_id = d['aq_user_open_id']
        if 'avatar' in d:
            o.avatar = d['avatar']
        if 'client_msg_id' in d:
            o.client_msg_id = d['client_msg_id']
        if 'conversation_id' in d:
            o.conversation_id = d['conversation_id']
        if 'conversation_name' in d:
            o.conversation_name = d['conversation_name']
        if 'conversation_type' in d:
            o.conversation_type = d['conversation_type']
        if 'latest_msg_time' in d:
            o.latest_msg_time = d['latest_msg_time']
        if 'link' in d:
            o.link = d['link']
        if 'msg_data' in d:
            o.msg_data = d['msg_data']
        if 'msg_id' in d:
            o.msg_id = d['msg_id']
        if 'msg_template_code' in d:
            o.msg_template_code = d['msg_template_code']
        if 'msg_type' in d:
            o.msg_type = d['msg_type']
        if 'out_app_id' in d:
            o.out_app_id = d['out_app_id']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'out_biz_name' in d:
            o.out_biz_name = d['out_biz_name']
        if 'receiver_type' in d:
            o.receiver_type = d['receiver_type']
        if 'receivers' in d:
            o.receivers = d['receivers']
        if 'send_types' in d:
            o.send_types = d['send_types']
        if 'show_content' in d:
            o.show_content = d['show_content']
        if 'template_params' in d:
            o.template_params = d['template_params']
        if 'un_read_count' in d:
            o.un_read_count = d['un_read_count']
        return o


