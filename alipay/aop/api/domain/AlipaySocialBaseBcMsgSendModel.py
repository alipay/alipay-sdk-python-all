#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NotifyParam import NotifyParam


class AlipaySocialBaseBcMsgSendModel(object):

    def __init__(self):
        self._app_min_version = None
        self._biz_app_id = None
        self._biz_context = None
        self._biz_memo = None
        self._biz_type = None
        self._channel = None
        self._client_msg_id = None
        self._consumer_user_id = None
        self._hidden_side = None
        self._link = None
        self._mark_read = None
        self._merchant_entity_id = None
        self._message_time = None
        self._monitor_param_map = None
        self._msg_op_type = None
        self._next_msg_content = None
        self._notify_param = None
        self._receiver_id = None
        self._receiver_user_type = None
        self._relation_type = None
        self._sender_id = None
        self._session_id = None
        self._template_code = None
        self._template_data = None

    @property
    def app_min_version(self):
        return self._app_min_version

    @app_min_version.setter
    def app_min_version(self, value):
        self._app_min_version = value
    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value
    @property
    def biz_context(self):
        return self._biz_context

    @biz_context.setter
    def biz_context(self, value):
        self._biz_context = value
    @property
    def biz_memo(self):
        return self._biz_memo

    @biz_memo.setter
    def biz_memo(self, value):
        self._biz_memo = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def client_msg_id(self):
        return self._client_msg_id

    @client_msg_id.setter
    def client_msg_id(self, value):
        self._client_msg_id = value
    @property
    def consumer_user_id(self):
        return self._consumer_user_id

    @consumer_user_id.setter
    def consumer_user_id(self, value):
        self._consumer_user_id = value
    @property
    def hidden_side(self):
        return self._hidden_side

    @hidden_side.setter
    def hidden_side(self, value):
        self._hidden_side = value
    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value
    @property
    def mark_read(self):
        return self._mark_read

    @mark_read.setter
    def mark_read(self, value):
        self._mark_read = value
    @property
    def merchant_entity_id(self):
        return self._merchant_entity_id

    @merchant_entity_id.setter
    def merchant_entity_id(self, value):
        self._merchant_entity_id = value
    @property
    def message_time(self):
        return self._message_time

    @message_time.setter
    def message_time(self, value):
        self._message_time = value
    @property
    def monitor_param_map(self):
        return self._monitor_param_map

    @monitor_param_map.setter
    def monitor_param_map(self, value):
        self._monitor_param_map = value
    @property
    def msg_op_type(self):
        return self._msg_op_type

    @msg_op_type.setter
    def msg_op_type(self, value):
        self._msg_op_type = value
    @property
    def next_msg_content(self):
        return self._next_msg_content

    @next_msg_content.setter
    def next_msg_content(self, value):
        self._next_msg_content = value
    @property
    def notify_param(self):
        return self._notify_param

    @notify_param.setter
    def notify_param(self, value):
        if isinstance(value, NotifyParam):
            self._notify_param = value
        else:
            self._notify_param = NotifyParam.from_alipay_dict(value)
    @property
    def receiver_id(self):
        return self._receiver_id

    @receiver_id.setter
    def receiver_id(self, value):
        self._receiver_id = value
    @property
    def receiver_user_type(self):
        return self._receiver_user_type

    @receiver_user_type.setter
    def receiver_user_type(self, value):
        self._receiver_user_type = value
    @property
    def relation_type(self):
        return self._relation_type

    @relation_type.setter
    def relation_type(self, value):
        self._relation_type = value
    @property
    def sender_id(self):
        return self._sender_id

    @sender_id.setter
    def sender_id(self, value):
        self._sender_id = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value
    @property
    def template_data(self):
        return self._template_data

    @template_data.setter
    def template_data(self, value):
        self._template_data = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_min_version:
            if hasattr(self.app_min_version, 'to_alipay_dict'):
                params['app_min_version'] = self.app_min_version.to_alipay_dict()
            else:
                params['app_min_version'] = self.app_min_version
        if self.biz_app_id:
            if hasattr(self.biz_app_id, 'to_alipay_dict'):
                params['biz_app_id'] = self.biz_app_id.to_alipay_dict()
            else:
                params['biz_app_id'] = self.biz_app_id
        if self.biz_context:
            if hasattr(self.biz_context, 'to_alipay_dict'):
                params['biz_context'] = self.biz_context.to_alipay_dict()
            else:
                params['biz_context'] = self.biz_context
        if self.biz_memo:
            if hasattr(self.biz_memo, 'to_alipay_dict'):
                params['biz_memo'] = self.biz_memo.to_alipay_dict()
            else:
                params['biz_memo'] = self.biz_memo
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.client_msg_id:
            if hasattr(self.client_msg_id, 'to_alipay_dict'):
                params['client_msg_id'] = self.client_msg_id.to_alipay_dict()
            else:
                params['client_msg_id'] = self.client_msg_id
        if self.consumer_user_id:
            if hasattr(self.consumer_user_id, 'to_alipay_dict'):
                params['consumer_user_id'] = self.consumer_user_id.to_alipay_dict()
            else:
                params['consumer_user_id'] = self.consumer_user_id
        if self.hidden_side:
            if hasattr(self.hidden_side, 'to_alipay_dict'):
                params['hidden_side'] = self.hidden_side.to_alipay_dict()
            else:
                params['hidden_side'] = self.hidden_side
        if self.link:
            if hasattr(self.link, 'to_alipay_dict'):
                params['link'] = self.link.to_alipay_dict()
            else:
                params['link'] = self.link
        if self.mark_read:
            if hasattr(self.mark_read, 'to_alipay_dict'):
                params['mark_read'] = self.mark_read.to_alipay_dict()
            else:
                params['mark_read'] = self.mark_read
        if self.merchant_entity_id:
            if hasattr(self.merchant_entity_id, 'to_alipay_dict'):
                params['merchant_entity_id'] = self.merchant_entity_id.to_alipay_dict()
            else:
                params['merchant_entity_id'] = self.merchant_entity_id
        if self.message_time:
            if hasattr(self.message_time, 'to_alipay_dict'):
                params['message_time'] = self.message_time.to_alipay_dict()
            else:
                params['message_time'] = self.message_time
        if self.monitor_param_map:
            if hasattr(self.monitor_param_map, 'to_alipay_dict'):
                params['monitor_param_map'] = self.monitor_param_map.to_alipay_dict()
            else:
                params['monitor_param_map'] = self.monitor_param_map
        if self.msg_op_type:
            if hasattr(self.msg_op_type, 'to_alipay_dict'):
                params['msg_op_type'] = self.msg_op_type.to_alipay_dict()
            else:
                params['msg_op_type'] = self.msg_op_type
        if self.next_msg_content:
            if hasattr(self.next_msg_content, 'to_alipay_dict'):
                params['next_msg_content'] = self.next_msg_content.to_alipay_dict()
            else:
                params['next_msg_content'] = self.next_msg_content
        if self.notify_param:
            if hasattr(self.notify_param, 'to_alipay_dict'):
                params['notify_param'] = self.notify_param.to_alipay_dict()
            else:
                params['notify_param'] = self.notify_param
        if self.receiver_id:
            if hasattr(self.receiver_id, 'to_alipay_dict'):
                params['receiver_id'] = self.receiver_id.to_alipay_dict()
            else:
                params['receiver_id'] = self.receiver_id
        if self.receiver_user_type:
            if hasattr(self.receiver_user_type, 'to_alipay_dict'):
                params['receiver_user_type'] = self.receiver_user_type.to_alipay_dict()
            else:
                params['receiver_user_type'] = self.receiver_user_type
        if self.relation_type:
            if hasattr(self.relation_type, 'to_alipay_dict'):
                params['relation_type'] = self.relation_type.to_alipay_dict()
            else:
                params['relation_type'] = self.relation_type
        if self.sender_id:
            if hasattr(self.sender_id, 'to_alipay_dict'):
                params['sender_id'] = self.sender_id.to_alipay_dict()
            else:
                params['sender_id'] = self.sender_id
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        if self.template_data:
            if hasattr(self.template_data, 'to_alipay_dict'):
                params['template_data'] = self.template_data.to_alipay_dict()
            else:
                params['template_data'] = self.template_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialBaseBcMsgSendModel()
        if 'app_min_version' in d:
            o.app_min_version = d['app_min_version']
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_context' in d:
            o.biz_context = d['biz_context']
        if 'biz_memo' in d:
            o.biz_memo = d['biz_memo']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'channel' in d:
            o.channel = d['channel']
        if 'client_msg_id' in d:
            o.client_msg_id = d['client_msg_id']
        if 'consumer_user_id' in d:
            o.consumer_user_id = d['consumer_user_id']
        if 'hidden_side' in d:
            o.hidden_side = d['hidden_side']
        if 'link' in d:
            o.link = d['link']
        if 'mark_read' in d:
            o.mark_read = d['mark_read']
        if 'merchant_entity_id' in d:
            o.merchant_entity_id = d['merchant_entity_id']
        if 'message_time' in d:
            o.message_time = d['message_time']
        if 'monitor_param_map' in d:
            o.monitor_param_map = d['monitor_param_map']
        if 'msg_op_type' in d:
            o.msg_op_type = d['msg_op_type']
        if 'next_msg_content' in d:
            o.next_msg_content = d['next_msg_content']
        if 'notify_param' in d:
            o.notify_param = d['notify_param']
        if 'receiver_id' in d:
            o.receiver_id = d['receiver_id']
        if 'receiver_user_type' in d:
            o.receiver_user_type = d['receiver_user_type']
        if 'relation_type' in d:
            o.relation_type = d['relation_type']
        if 'sender_id' in d:
            o.sender_id = d['sender_id']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'template_code' in d:
            o.template_code = d['template_code']
        if 'template_data' in d:
            o.template_data = d['template_data']
        return o


