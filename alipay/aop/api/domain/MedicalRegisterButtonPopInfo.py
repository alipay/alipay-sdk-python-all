#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalRegisterButtonPopInfo(object):

    def __init__(self):
        self._cancel_button_text = None
        self._confirm_button_text = None
        self._content = None
        self._hospital_phone = None
        self._position = None
        self._title = None

    @property
    def cancel_button_text(self):
        return self._cancel_button_text

    @cancel_button_text.setter
    def cancel_button_text(self, value):
        self._cancel_button_text = value
    @property
    def confirm_button_text(self):
        return self._confirm_button_text

    @confirm_button_text.setter
    def confirm_button_text(self, value):
        self._confirm_button_text = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def hospital_phone(self):
        return self._hospital_phone

    @hospital_phone.setter
    def hospital_phone(self, value):
        self._hospital_phone = value
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.cancel_button_text:
            if hasattr(self.cancel_button_text, 'to_alipay_dict'):
                params['cancel_button_text'] = self.cancel_button_text.to_alipay_dict()
            else:
                params['cancel_button_text'] = self.cancel_button_text
        if self.confirm_button_text:
            if hasattr(self.confirm_button_text, 'to_alipay_dict'):
                params['confirm_button_text'] = self.confirm_button_text.to_alipay_dict()
            else:
                params['confirm_button_text'] = self.confirm_button_text
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.hospital_phone:
            if hasattr(self.hospital_phone, 'to_alipay_dict'):
                params['hospital_phone'] = self.hospital_phone.to_alipay_dict()
            else:
                params['hospital_phone'] = self.hospital_phone
        if self.position:
            if hasattr(self.position, 'to_alipay_dict'):
                params['position'] = self.position.to_alipay_dict()
            else:
                params['position'] = self.position
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalRegisterButtonPopInfo()
        if 'cancel_button_text' in d:
            o.cancel_button_text = d['cancel_button_text']
        if 'confirm_button_text' in d:
            o.confirm_button_text = d['confirm_button_text']
        if 'content' in d:
            o.content = d['content']
        if 'hospital_phone' in d:
            o.hospital_phone = d['hospital_phone']
        if 'position' in d:
            o.position = d['position']
        if 'title' in d:
            o.title = d['title']
        return o


