#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ComplaintProcessorResponse(object):

    def __init__(self):
        self._card_id = None
        self._complaint_id = None
        self._complaint_status = None
        self._complaint_type = None
        self._content = None
        self._create_time = None
        self._image_url_list = None
        self._merchant_name = None
        self._merchant_pid = None
        self._operator = None
        self._reply_content = None

    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def complaint_id(self):
        return self._complaint_id

    @complaint_id.setter
    def complaint_id(self, value):
        self._complaint_id = value
    @property
    def complaint_status(self):
        return self._complaint_status

    @complaint_status.setter
    def complaint_status(self, value):
        self._complaint_status = value
    @property
    def complaint_type(self):
        return self._complaint_type

    @complaint_type.setter
    def complaint_type(self, value):
        self._complaint_type = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def image_url_list(self):
        return self._image_url_list

    @image_url_list.setter
    def image_url_list(self, value):
        if isinstance(value, list):
            self._image_url_list = list()
            for i in value:
                self._image_url_list.append(i)
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def reply_content(self):
        return self._reply_content

    @reply_content.setter
    def reply_content(self, value):
        self._reply_content = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.complaint_id:
            if hasattr(self.complaint_id, 'to_alipay_dict'):
                params['complaint_id'] = self.complaint_id.to_alipay_dict()
            else:
                params['complaint_id'] = self.complaint_id
        if self.complaint_status:
            if hasattr(self.complaint_status, 'to_alipay_dict'):
                params['complaint_status'] = self.complaint_status.to_alipay_dict()
            else:
                params['complaint_status'] = self.complaint_status
        if self.complaint_type:
            if hasattr(self.complaint_type, 'to_alipay_dict'):
                params['complaint_type'] = self.complaint_type.to_alipay_dict()
            else:
                params['complaint_type'] = self.complaint_type
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.image_url_list:
            if isinstance(self.image_url_list, list):
                for i in range(0, len(self.image_url_list)):
                    element = self.image_url_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.image_url_list[i] = element.to_alipay_dict()
            if hasattr(self.image_url_list, 'to_alipay_dict'):
                params['image_url_list'] = self.image_url_list.to_alipay_dict()
            else:
                params['image_url_list'] = self.image_url_list
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.reply_content:
            if hasattr(self.reply_content, 'to_alipay_dict'):
                params['reply_content'] = self.reply_content.to_alipay_dict()
            else:
                params['reply_content'] = self.reply_content
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ComplaintProcessorResponse()
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'complaint_id' in d:
            o.complaint_id = d['complaint_id']
        if 'complaint_status' in d:
            o.complaint_status = d['complaint_status']
        if 'complaint_type' in d:
            o.complaint_type = d['complaint_type']
        if 'content' in d:
            o.content = d['content']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'image_url_list' in d:
            o.image_url_list = d['image_url_list']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'operator' in d:
            o.operator = d['operator']
        if 'reply_content' in d:
            o.reply_content = d['reply_content']
        return o


