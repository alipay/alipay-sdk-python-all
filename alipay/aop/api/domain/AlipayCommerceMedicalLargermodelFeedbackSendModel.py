#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalLargermodelFeedbackSendModel(object):

    def __init__(self):
        self._card_data = None
        self._card_event = None
        self._card_service = None
        self._chat_id = None
        self._close_cloud_escort_flag = None
        self._feedback_ap = None
        self._feedback_channel = None
        self._feedback_class = None
        self._feedback_input = None
        self._feedback_select_content = None
        self._feedback_tag = None
        self._feedback_type = None
        self._hospital_id = None
        self._hospital_name = None
        self._open_id = None
        self._org_id = None
        self._out_user_id = None
        self._outer_user_type = None
        self._session_id = None
        self._ypz_id = None

    @property
    def card_data(self):
        return self._card_data

    @card_data.setter
    def card_data(self, value):
        self._card_data = value
    @property
    def card_event(self):
        return self._card_event

    @card_event.setter
    def card_event(self, value):
        self._card_event = value
    @property
    def card_service(self):
        return self._card_service

    @card_service.setter
    def card_service(self, value):
        self._card_service = value
    @property
    def chat_id(self):
        return self._chat_id

    @chat_id.setter
    def chat_id(self, value):
        self._chat_id = value
    @property
    def close_cloud_escort_flag(self):
        return self._close_cloud_escort_flag

    @close_cloud_escort_flag.setter
    def close_cloud_escort_flag(self, value):
        self._close_cloud_escort_flag = value
    @property
    def feedback_ap(self):
        return self._feedback_ap

    @feedback_ap.setter
    def feedback_ap(self, value):
        self._feedback_ap = value
    @property
    def feedback_channel(self):
        return self._feedback_channel

    @feedback_channel.setter
    def feedback_channel(self, value):
        self._feedback_channel = value
    @property
    def feedback_class(self):
        return self._feedback_class

    @feedback_class.setter
    def feedback_class(self, value):
        self._feedback_class = value
    @property
    def feedback_input(self):
        return self._feedback_input

    @feedback_input.setter
    def feedback_input(self, value):
        self._feedback_input = value
    @property
    def feedback_select_content(self):
        return self._feedback_select_content

    @feedback_select_content.setter
    def feedback_select_content(self, value):
        self._feedback_select_content = value
    @property
    def feedback_tag(self):
        return self._feedback_tag

    @feedback_tag.setter
    def feedback_tag(self, value):
        self._feedback_tag = value
    @property
    def feedback_type(self):
        return self._feedback_type

    @feedback_type.setter
    def feedback_type(self, value):
        self._feedback_type = value
    @property
    def hospital_id(self):
        return self._hospital_id

    @hospital_id.setter
    def hospital_id(self, value):
        self._hospital_id = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value
    @property
    def outer_user_type(self):
        return self._outer_user_type

    @outer_user_type.setter
    def outer_user_type(self, value):
        self._outer_user_type = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def ypz_id(self):
        return self._ypz_id

    @ypz_id.setter
    def ypz_id(self, value):
        self._ypz_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_data:
            if hasattr(self.card_data, 'to_alipay_dict'):
                params['card_data'] = self.card_data.to_alipay_dict()
            else:
                params['card_data'] = self.card_data
        if self.card_event:
            if hasattr(self.card_event, 'to_alipay_dict'):
                params['card_event'] = self.card_event.to_alipay_dict()
            else:
                params['card_event'] = self.card_event
        if self.card_service:
            if hasattr(self.card_service, 'to_alipay_dict'):
                params['card_service'] = self.card_service.to_alipay_dict()
            else:
                params['card_service'] = self.card_service
        if self.chat_id:
            if hasattr(self.chat_id, 'to_alipay_dict'):
                params['chat_id'] = self.chat_id.to_alipay_dict()
            else:
                params['chat_id'] = self.chat_id
        if self.close_cloud_escort_flag:
            if hasattr(self.close_cloud_escort_flag, 'to_alipay_dict'):
                params['close_cloud_escort_flag'] = self.close_cloud_escort_flag.to_alipay_dict()
            else:
                params['close_cloud_escort_flag'] = self.close_cloud_escort_flag
        if self.feedback_ap:
            if hasattr(self.feedback_ap, 'to_alipay_dict'):
                params['feedback_ap'] = self.feedback_ap.to_alipay_dict()
            else:
                params['feedback_ap'] = self.feedback_ap
        if self.feedback_channel:
            if hasattr(self.feedback_channel, 'to_alipay_dict'):
                params['feedback_channel'] = self.feedback_channel.to_alipay_dict()
            else:
                params['feedback_channel'] = self.feedback_channel
        if self.feedback_class:
            if hasattr(self.feedback_class, 'to_alipay_dict'):
                params['feedback_class'] = self.feedback_class.to_alipay_dict()
            else:
                params['feedback_class'] = self.feedback_class
        if self.feedback_input:
            if hasattr(self.feedback_input, 'to_alipay_dict'):
                params['feedback_input'] = self.feedback_input.to_alipay_dict()
            else:
                params['feedback_input'] = self.feedback_input
        if self.feedback_select_content:
            if hasattr(self.feedback_select_content, 'to_alipay_dict'):
                params['feedback_select_content'] = self.feedback_select_content.to_alipay_dict()
            else:
                params['feedback_select_content'] = self.feedback_select_content
        if self.feedback_tag:
            if hasattr(self.feedback_tag, 'to_alipay_dict'):
                params['feedback_tag'] = self.feedback_tag.to_alipay_dict()
            else:
                params['feedback_tag'] = self.feedback_tag
        if self.feedback_type:
            if hasattr(self.feedback_type, 'to_alipay_dict'):
                params['feedback_type'] = self.feedback_type.to_alipay_dict()
            else:
                params['feedback_type'] = self.feedback_type
        if self.hospital_id:
            if hasattr(self.hospital_id, 'to_alipay_dict'):
                params['hospital_id'] = self.hospital_id.to_alipay_dict()
            else:
                params['hospital_id'] = self.hospital_id
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        if self.outer_user_type:
            if hasattr(self.outer_user_type, 'to_alipay_dict'):
                params['outer_user_type'] = self.outer_user_type.to_alipay_dict()
            else:
                params['outer_user_type'] = self.outer_user_type
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.ypz_id:
            if hasattr(self.ypz_id, 'to_alipay_dict'):
                params['ypz_id'] = self.ypz_id.to_alipay_dict()
            else:
                params['ypz_id'] = self.ypz_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalLargermodelFeedbackSendModel()
        if 'card_data' in d:
            o.card_data = d['card_data']
        if 'card_event' in d:
            o.card_event = d['card_event']
        if 'card_service' in d:
            o.card_service = d['card_service']
        if 'chat_id' in d:
            o.chat_id = d['chat_id']
        if 'close_cloud_escort_flag' in d:
            o.close_cloud_escort_flag = d['close_cloud_escort_flag']
        if 'feedback_ap' in d:
            o.feedback_ap = d['feedback_ap']
        if 'feedback_channel' in d:
            o.feedback_channel = d['feedback_channel']
        if 'feedback_class' in d:
            o.feedback_class = d['feedback_class']
        if 'feedback_input' in d:
            o.feedback_input = d['feedback_input']
        if 'feedback_select_content' in d:
            o.feedback_select_content = d['feedback_select_content']
        if 'feedback_tag' in d:
            o.feedback_tag = d['feedback_tag']
        if 'feedback_type' in d:
            o.feedback_type = d['feedback_type']
        if 'hospital_id' in d:
            o.hospital_id = d['hospital_id']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'org_id' in d:
            o.org_id = d['org_id']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        if 'outer_user_type' in d:
            o.outer_user_type = d['outer_user_type']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'ypz_id' in d:
            o.ypz_id = d['ypz_id']
        return o


