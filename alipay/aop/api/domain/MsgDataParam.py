#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MsgDataParam(object):

    def __init__(self):
        self._consultation_order_id = None
        self._consultation_time = None
        self._doctor_name = None
        self._introduction = None
        self._latest_conversation_time = None
        self._latest_msg_content = None
        self._msg_id = None
        self._msg_time = None
        self._msg_type = None
        self._patient_name = None
        self._redirect_url = None
        self._redirect_urls = None

    @property
    def consultation_order_id(self):
        return self._consultation_order_id

    @consultation_order_id.setter
    def consultation_order_id(self, value):
        self._consultation_order_id = value
    @property
    def consultation_time(self):
        return self._consultation_time

    @consultation_time.setter
    def consultation_time(self, value):
        self._consultation_time = value
    @property
    def doctor_name(self):
        return self._doctor_name

    @doctor_name.setter
    def doctor_name(self, value):
        self._doctor_name = value
    @property
    def introduction(self):
        return self._introduction

    @introduction.setter
    def introduction(self, value):
        self._introduction = value
    @property
    def latest_conversation_time(self):
        return self._latest_conversation_time

    @latest_conversation_time.setter
    def latest_conversation_time(self, value):
        self._latest_conversation_time = value
    @property
    def latest_msg_content(self):
        return self._latest_msg_content

    @latest_msg_content.setter
    def latest_msg_content(self, value):
        self._latest_msg_content = value
    @property
    def msg_id(self):
        return self._msg_id

    @msg_id.setter
    def msg_id(self, value):
        self._msg_id = value
    @property
    def msg_time(self):
        return self._msg_time

    @msg_time.setter
    def msg_time(self, value):
        self._msg_time = value
    @property
    def msg_type(self):
        return self._msg_type

    @msg_type.setter
    def msg_type(self, value):
        self._msg_type = value
    @property
    def patient_name(self):
        return self._patient_name

    @patient_name.setter
    def patient_name(self, value):
        self._patient_name = value
    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value
    @property
    def redirect_urls(self):
        return self._redirect_urls

    @redirect_urls.setter
    def redirect_urls(self, value):
        if isinstance(value, list):
            self._redirect_urls = list()
            for i in value:
                self._redirect_urls.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.consultation_order_id:
            if hasattr(self.consultation_order_id, 'to_alipay_dict'):
                params['consultation_order_id'] = self.consultation_order_id.to_alipay_dict()
            else:
                params['consultation_order_id'] = self.consultation_order_id
        if self.consultation_time:
            if hasattr(self.consultation_time, 'to_alipay_dict'):
                params['consultation_time'] = self.consultation_time.to_alipay_dict()
            else:
                params['consultation_time'] = self.consultation_time
        if self.doctor_name:
            if hasattr(self.doctor_name, 'to_alipay_dict'):
                params['doctor_name'] = self.doctor_name.to_alipay_dict()
            else:
                params['doctor_name'] = self.doctor_name
        if self.introduction:
            if hasattr(self.introduction, 'to_alipay_dict'):
                params['introduction'] = self.introduction.to_alipay_dict()
            else:
                params['introduction'] = self.introduction
        if self.latest_conversation_time:
            if hasattr(self.latest_conversation_time, 'to_alipay_dict'):
                params['latest_conversation_time'] = self.latest_conversation_time.to_alipay_dict()
            else:
                params['latest_conversation_time'] = self.latest_conversation_time
        if self.latest_msg_content:
            if hasattr(self.latest_msg_content, 'to_alipay_dict'):
                params['latest_msg_content'] = self.latest_msg_content.to_alipay_dict()
            else:
                params['latest_msg_content'] = self.latest_msg_content
        if self.msg_id:
            if hasattr(self.msg_id, 'to_alipay_dict'):
                params['msg_id'] = self.msg_id.to_alipay_dict()
            else:
                params['msg_id'] = self.msg_id
        if self.msg_time:
            if hasattr(self.msg_time, 'to_alipay_dict'):
                params['msg_time'] = self.msg_time.to_alipay_dict()
            else:
                params['msg_time'] = self.msg_time
        if self.msg_type:
            if hasattr(self.msg_type, 'to_alipay_dict'):
                params['msg_type'] = self.msg_type.to_alipay_dict()
            else:
                params['msg_type'] = self.msg_type
        if self.patient_name:
            if hasattr(self.patient_name, 'to_alipay_dict'):
                params['patient_name'] = self.patient_name.to_alipay_dict()
            else:
                params['patient_name'] = self.patient_name
        if self.redirect_url:
            if hasattr(self.redirect_url, 'to_alipay_dict'):
                params['redirect_url'] = self.redirect_url.to_alipay_dict()
            else:
                params['redirect_url'] = self.redirect_url
        if self.redirect_urls:
            if isinstance(self.redirect_urls, list):
                for i in range(0, len(self.redirect_urls)):
                    element = self.redirect_urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.redirect_urls[i] = element.to_alipay_dict()
            if hasattr(self.redirect_urls, 'to_alipay_dict'):
                params['redirect_urls'] = self.redirect_urls.to_alipay_dict()
            else:
                params['redirect_urls'] = self.redirect_urls
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MsgDataParam()
        if 'consultation_order_id' in d:
            o.consultation_order_id = d['consultation_order_id']
        if 'consultation_time' in d:
            o.consultation_time = d['consultation_time']
        if 'doctor_name' in d:
            o.doctor_name = d['doctor_name']
        if 'introduction' in d:
            o.introduction = d['introduction']
        if 'latest_conversation_time' in d:
            o.latest_conversation_time = d['latest_conversation_time']
        if 'latest_msg_content' in d:
            o.latest_msg_content = d['latest_msg_content']
        if 'msg_id' in d:
            o.msg_id = d['msg_id']
        if 'msg_time' in d:
            o.msg_time = d['msg_time']
        if 'msg_type' in d:
            o.msg_type = d['msg_type']
        if 'patient_name' in d:
            o.patient_name = d['patient_name']
        if 'redirect_url' in d:
            o.redirect_url = d['redirect_url']
        if 'redirect_urls' in d:
            o.redirect_urls = d['redirect_urls']
        return o


