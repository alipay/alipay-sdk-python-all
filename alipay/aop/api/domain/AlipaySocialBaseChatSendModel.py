#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialBaseChatSendModel(object):

    def __init__(self):
        self._biz_memo = None
        self._client_msg_id = None
        self._link = None
        self._receiver_id = None
        self._receiver_usertype = None
        self._template_data = None
        self._template_type = None

    @property
    def biz_memo(self):
        return self._biz_memo

    @biz_memo.setter
    def biz_memo(self, value):
        self._biz_memo = value
    @property
    def client_msg_id(self):
        return self._client_msg_id

    @client_msg_id.setter
    def client_msg_id(self, value):
        self._client_msg_id = value
    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value
    @property
    def receiver_id(self):
        return self._receiver_id

    @receiver_id.setter
    def receiver_id(self, value):
        self._receiver_id = value
    @property
    def receiver_usertype(self):
        return self._receiver_usertype

    @receiver_usertype.setter
    def receiver_usertype(self, value):
        self._receiver_usertype = value
    @property
    def template_data(self):
        return self._template_data

    @template_data.setter
    def template_data(self, value):
        self._template_data = value
    @property
    def template_type(self):
        return self._template_type

    @template_type.setter
    def template_type(self, value):
        self._template_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_memo:
            if hasattr(self.biz_memo, 'to_alipay_dict'):
                params['biz_memo'] = self.biz_memo.to_alipay_dict()
            else:
                params['biz_memo'] = self.biz_memo
        if self.client_msg_id:
            if hasattr(self.client_msg_id, 'to_alipay_dict'):
                params['client_msg_id'] = self.client_msg_id.to_alipay_dict()
            else:
                params['client_msg_id'] = self.client_msg_id
        if self.link:
            if hasattr(self.link, 'to_alipay_dict'):
                params['link'] = self.link.to_alipay_dict()
            else:
                params['link'] = self.link
        if self.receiver_id:
            if hasattr(self.receiver_id, 'to_alipay_dict'):
                params['receiver_id'] = self.receiver_id.to_alipay_dict()
            else:
                params['receiver_id'] = self.receiver_id
        if self.receiver_usertype:
            if hasattr(self.receiver_usertype, 'to_alipay_dict'):
                params['receiver_usertype'] = self.receiver_usertype.to_alipay_dict()
            else:
                params['receiver_usertype'] = self.receiver_usertype
        if self.template_data:
            if hasattr(self.template_data, 'to_alipay_dict'):
                params['template_data'] = self.template_data.to_alipay_dict()
            else:
                params['template_data'] = self.template_data
        if self.template_type:
            if hasattr(self.template_type, 'to_alipay_dict'):
                params['template_type'] = self.template_type.to_alipay_dict()
            else:
                params['template_type'] = self.template_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialBaseChatSendModel()
        if 'biz_memo' in d:
            o.biz_memo = d['biz_memo']
        if 'client_msg_id' in d:
            o.client_msg_id = d['client_msg_id']
        if 'link' in d:
            o.link = d['link']
        if 'receiver_id' in d:
            o.receiver_id = d['receiver_id']
        if 'receiver_usertype' in d:
            o.receiver_usertype = d['receiver_usertype']
        if 'template_data' in d:
            o.template_data = d['template_data']
        if 'template_type' in d:
            o.template_type = d['template_type']
        return o


