#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Complaint(object):

    def __init__(self):
        self._card_id = None
        self._complaint_id = None
        self._complaint_name = None
        self._complaint_phone = None
        self._complaint_status = None
        self._complaint_type = None
        self._content = None
        self._create_time = None
        self._image_url_list = None
        self._isv_reply_url = None
        self._merchant_reply_url = None
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
    def complaint_name(self):
        return self._complaint_name

    @complaint_name.setter
    def complaint_name(self, value):
        self._complaint_name = value
    @property
    def complaint_phone(self):
        return self._complaint_phone

    @complaint_phone.setter
    def complaint_phone(self, value):
        self._complaint_phone = value
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
    def isv_reply_url(self):
        return self._isv_reply_url

    @isv_reply_url.setter
    def isv_reply_url(self, value):
        self._isv_reply_url = value
    @property
    def merchant_reply_url(self):
        return self._merchant_reply_url

    @merchant_reply_url.setter
    def merchant_reply_url(self, value):
        self._merchant_reply_url = value
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
        if self.complaint_name:
            if hasattr(self.complaint_name, 'to_alipay_dict'):
                params['complaint_name'] = self.complaint_name.to_alipay_dict()
            else:
                params['complaint_name'] = self.complaint_name
        if self.complaint_phone:
            if hasattr(self.complaint_phone, 'to_alipay_dict'):
                params['complaint_phone'] = self.complaint_phone.to_alipay_dict()
            else:
                params['complaint_phone'] = self.complaint_phone
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
        if self.isv_reply_url:
            if hasattr(self.isv_reply_url, 'to_alipay_dict'):
                params['isv_reply_url'] = self.isv_reply_url.to_alipay_dict()
            else:
                params['isv_reply_url'] = self.isv_reply_url
        if self.merchant_reply_url:
            if hasattr(self.merchant_reply_url, 'to_alipay_dict'):
                params['merchant_reply_url'] = self.merchant_reply_url.to_alipay_dict()
            else:
                params['merchant_reply_url'] = self.merchant_reply_url
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
        o = Complaint()
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'complaint_id' in d:
            o.complaint_id = d['complaint_id']
        if 'complaint_name' in d:
            o.complaint_name = d['complaint_name']
        if 'complaint_phone' in d:
            o.complaint_phone = d['complaint_phone']
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
        if 'isv_reply_url' in d:
            o.isv_reply_url = d['isv_reply_url']
        if 'merchant_reply_url' in d:
            o.merchant_reply_url = d['merchant_reply_url']
        if 'reply_content' in d:
            o.reply_content = d['reply_content']
        return o


