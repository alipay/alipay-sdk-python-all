#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHomedoctorMessageCreateModel(object):

    def __init__(self):
        self._message_batch_no = None
        self._message_biz_type = None
        self._message_content = None
        self._message_content_digest = None
        self._message_content_icon = None
        self._message_content_picture = None
        self._message_content_url = None
        self._message_sender = None
        self._message_template_type = None
        self._open_id_text = None

    @property
    def message_batch_no(self):
        return self._message_batch_no

    @message_batch_no.setter
    def message_batch_no(self, value):
        self._message_batch_no = value
    @property
    def message_biz_type(self):
        return self._message_biz_type

    @message_biz_type.setter
    def message_biz_type(self, value):
        self._message_biz_type = value
    @property
    def message_content(self):
        return self._message_content

    @message_content.setter
    def message_content(self, value):
        self._message_content = value
    @property
    def message_content_digest(self):
        return self._message_content_digest

    @message_content_digest.setter
    def message_content_digest(self, value):
        self._message_content_digest = value
    @property
    def message_content_icon(self):
        return self._message_content_icon

    @message_content_icon.setter
    def message_content_icon(self, value):
        self._message_content_icon = value
    @property
    def message_content_picture(self):
        return self._message_content_picture

    @message_content_picture.setter
    def message_content_picture(self, value):
        self._message_content_picture = value
    @property
    def message_content_url(self):
        return self._message_content_url

    @message_content_url.setter
    def message_content_url(self, value):
        self._message_content_url = value
    @property
    def message_sender(self):
        return self._message_sender

    @message_sender.setter
    def message_sender(self, value):
        self._message_sender = value
    @property
    def message_template_type(self):
        return self._message_template_type

    @message_template_type.setter
    def message_template_type(self, value):
        self._message_template_type = value
    @property
    def open_id_text(self):
        return self._open_id_text

    @open_id_text.setter
    def open_id_text(self, value):
        self._open_id_text = value


    def to_alipay_dict(self):
        params = dict()
        if self.message_batch_no:
            if hasattr(self.message_batch_no, 'to_alipay_dict'):
                params['message_batch_no'] = self.message_batch_no.to_alipay_dict()
            else:
                params['message_batch_no'] = self.message_batch_no
        if self.message_biz_type:
            if hasattr(self.message_biz_type, 'to_alipay_dict'):
                params['message_biz_type'] = self.message_biz_type.to_alipay_dict()
            else:
                params['message_biz_type'] = self.message_biz_type
        if self.message_content:
            if hasattr(self.message_content, 'to_alipay_dict'):
                params['message_content'] = self.message_content.to_alipay_dict()
            else:
                params['message_content'] = self.message_content
        if self.message_content_digest:
            if hasattr(self.message_content_digest, 'to_alipay_dict'):
                params['message_content_digest'] = self.message_content_digest.to_alipay_dict()
            else:
                params['message_content_digest'] = self.message_content_digest
        if self.message_content_icon:
            if hasattr(self.message_content_icon, 'to_alipay_dict'):
                params['message_content_icon'] = self.message_content_icon.to_alipay_dict()
            else:
                params['message_content_icon'] = self.message_content_icon
        if self.message_content_picture:
            if hasattr(self.message_content_picture, 'to_alipay_dict'):
                params['message_content_picture'] = self.message_content_picture.to_alipay_dict()
            else:
                params['message_content_picture'] = self.message_content_picture
        if self.message_content_url:
            if hasattr(self.message_content_url, 'to_alipay_dict'):
                params['message_content_url'] = self.message_content_url.to_alipay_dict()
            else:
                params['message_content_url'] = self.message_content_url
        if self.message_sender:
            if hasattr(self.message_sender, 'to_alipay_dict'):
                params['message_sender'] = self.message_sender.to_alipay_dict()
            else:
                params['message_sender'] = self.message_sender
        if self.message_template_type:
            if hasattr(self.message_template_type, 'to_alipay_dict'):
                params['message_template_type'] = self.message_template_type.to_alipay_dict()
            else:
                params['message_template_type'] = self.message_template_type
        if self.open_id_text:
            if hasattr(self.open_id_text, 'to_alipay_dict'):
                params['open_id_text'] = self.open_id_text.to_alipay_dict()
            else:
                params['open_id_text'] = self.open_id_text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHomedoctorMessageCreateModel()
        if 'message_batch_no' in d:
            o.message_batch_no = d['message_batch_no']
        if 'message_biz_type' in d:
            o.message_biz_type = d['message_biz_type']
        if 'message_content' in d:
            o.message_content = d['message_content']
        if 'message_content_digest' in d:
            o.message_content_digest = d['message_content_digest']
        if 'message_content_icon' in d:
            o.message_content_icon = d['message_content_icon']
        if 'message_content_picture' in d:
            o.message_content_picture = d['message_content_picture']
        if 'message_content_url' in d:
            o.message_content_url = d['message_content_url']
        if 'message_sender' in d:
            o.message_sender = d['message_sender']
        if 'message_template_type' in d:
            o.message_template_type = d['message_template_type']
        if 'open_id_text' in d:
            o.open_id_text = d['open_id_text']
        return o


