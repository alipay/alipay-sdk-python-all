#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SpecialCardInfoModel(object):

    def __init__(self):
        self._action_link = None
        self._action_name = None
        self._card_business_types_full_name = None
        self._card_business_types_key = None
        self._card_desc = None
        self._card_no = None
        self._card_title = None
        self._card_type = None
        self._code_status = None
        self._effective_dentification_types = None
        self._image_url = None

    @property
    def action_link(self):
        return self._action_link

    @action_link.setter
    def action_link(self, value):
        self._action_link = value
    @property
    def action_name(self):
        return self._action_name

    @action_name.setter
    def action_name(self, value):
        self._action_name = value
    @property
    def card_business_types_full_name(self):
        return self._card_business_types_full_name

    @card_business_types_full_name.setter
    def card_business_types_full_name(self, value):
        self._card_business_types_full_name = value
    @property
    def card_business_types_key(self):
        return self._card_business_types_key

    @card_business_types_key.setter
    def card_business_types_key(self, value):
        if isinstance(value, list):
            self._card_business_types_key = list()
            for i in value:
                self._card_business_types_key.append(i)
    @property
    def card_desc(self):
        return self._card_desc

    @card_desc.setter
    def card_desc(self, value):
        self._card_desc = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def card_title(self):
        return self._card_title

    @card_title.setter
    def card_title(self, value):
        self._card_title = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def code_status(self):
        return self._code_status

    @code_status.setter
    def code_status(self, value):
        self._code_status = value
    @property
    def effective_dentification_types(self):
        return self._effective_dentification_types

    @effective_dentification_types.setter
    def effective_dentification_types(self, value):
        if isinstance(value, list):
            self._effective_dentification_types = list()
            for i in value:
                self._effective_dentification_types.append(i)
    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_link:
            if hasattr(self.action_link, 'to_alipay_dict'):
                params['action_link'] = self.action_link.to_alipay_dict()
            else:
                params['action_link'] = self.action_link
        if self.action_name:
            if hasattr(self.action_name, 'to_alipay_dict'):
                params['action_name'] = self.action_name.to_alipay_dict()
            else:
                params['action_name'] = self.action_name
        if self.card_business_types_full_name:
            if hasattr(self.card_business_types_full_name, 'to_alipay_dict'):
                params['card_business_types_full_name'] = self.card_business_types_full_name.to_alipay_dict()
            else:
                params['card_business_types_full_name'] = self.card_business_types_full_name
        if self.card_business_types_key:
            if isinstance(self.card_business_types_key, list):
                for i in range(0, len(self.card_business_types_key)):
                    element = self.card_business_types_key[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.card_business_types_key[i] = element.to_alipay_dict()
            if hasattr(self.card_business_types_key, 'to_alipay_dict'):
                params['card_business_types_key'] = self.card_business_types_key.to_alipay_dict()
            else:
                params['card_business_types_key'] = self.card_business_types_key
        if self.card_desc:
            if hasattr(self.card_desc, 'to_alipay_dict'):
                params['card_desc'] = self.card_desc.to_alipay_dict()
            else:
                params['card_desc'] = self.card_desc
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.card_title:
            if hasattr(self.card_title, 'to_alipay_dict'):
                params['card_title'] = self.card_title.to_alipay_dict()
            else:
                params['card_title'] = self.card_title
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.code_status:
            if hasattr(self.code_status, 'to_alipay_dict'):
                params['code_status'] = self.code_status.to_alipay_dict()
            else:
                params['code_status'] = self.code_status
        if self.effective_dentification_types:
            if isinstance(self.effective_dentification_types, list):
                for i in range(0, len(self.effective_dentification_types)):
                    element = self.effective_dentification_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.effective_dentification_types[i] = element.to_alipay_dict()
            if hasattr(self.effective_dentification_types, 'to_alipay_dict'):
                params['effective_dentification_types'] = self.effective_dentification_types.to_alipay_dict()
            else:
                params['effective_dentification_types'] = self.effective_dentification_types
        if self.image_url:
            if hasattr(self.image_url, 'to_alipay_dict'):
                params['image_url'] = self.image_url.to_alipay_dict()
            else:
                params['image_url'] = self.image_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SpecialCardInfoModel()
        if 'action_link' in d:
            o.action_link = d['action_link']
        if 'action_name' in d:
            o.action_name = d['action_name']
        if 'card_business_types_full_name' in d:
            o.card_business_types_full_name = d['card_business_types_full_name']
        if 'card_business_types_key' in d:
            o.card_business_types_key = d['card_business_types_key']
        if 'card_desc' in d:
            o.card_desc = d['card_desc']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'card_title' in d:
            o.card_title = d['card_title']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'code_status' in d:
            o.code_status = d['code_status']
        if 'effective_dentification_types' in d:
            o.effective_dentification_types = d['effective_dentification_types']
        if 'image_url' in d:
            o.image_url = d['image_url']
        return o


