#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MedicalRegisterButtonExtInfo import MedicalRegisterButtonExtInfo
from alipay.aop.api.domain.MedicalRegisterButtonExtInfo import MedicalRegisterButtonExtInfo
from alipay.aop.api.domain.MedicalRegisterButtonPopInfo import MedicalRegisterButtonPopInfo
from alipay.aop.api.domain.MedicalRegisterButtonPopInfo import MedicalRegisterButtonPopInfo


class MedicalRegisterButtonInfo(object):

    def __init__(self):
        self._button_code = None
        self._button_ext_info = None
        self._button_ext_info_model = None
        self._button_order = None
        self._button_pop_info_model = None
        self._button_pop_up = None
        self._button_style = None
        self._button_text = None
        self._button_tips = None
        self._button_url = None
        self._button_url_json = None

    @property
    def button_code(self):
        return self._button_code

    @button_code.setter
    def button_code(self, value):
        self._button_code = value
    @property
    def button_ext_info(self):
        return self._button_ext_info

    @button_ext_info.setter
    def button_ext_info(self, value):
        if isinstance(value, MedicalRegisterButtonExtInfo):
            self._button_ext_info = value
        else:
            self._button_ext_info = MedicalRegisterButtonExtInfo.from_alipay_dict(value)
    @property
    def button_ext_info_model(self):
        return self._button_ext_info_model

    @button_ext_info_model.setter
    def button_ext_info_model(self, value):
        if isinstance(value, MedicalRegisterButtonExtInfo):
            self._button_ext_info_model = value
        else:
            self._button_ext_info_model = MedicalRegisterButtonExtInfo.from_alipay_dict(value)
    @property
    def button_order(self):
        return self._button_order

    @button_order.setter
    def button_order(self, value):
        self._button_order = value
    @property
    def button_pop_info_model(self):
        return self._button_pop_info_model

    @button_pop_info_model.setter
    def button_pop_info_model(self, value):
        if isinstance(value, MedicalRegisterButtonPopInfo):
            self._button_pop_info_model = value
        else:
            self._button_pop_info_model = MedicalRegisterButtonPopInfo.from_alipay_dict(value)
    @property
    def button_pop_up(self):
        return self._button_pop_up

    @button_pop_up.setter
    def button_pop_up(self, value):
        if isinstance(value, MedicalRegisterButtonPopInfo):
            self._button_pop_up = value
        else:
            self._button_pop_up = MedicalRegisterButtonPopInfo.from_alipay_dict(value)
    @property
    def button_style(self):
        return self._button_style

    @button_style.setter
    def button_style(self, value):
        self._button_style = value
    @property
    def button_text(self):
        return self._button_text

    @button_text.setter
    def button_text(self, value):
        self._button_text = value
    @property
    def button_tips(self):
        return self._button_tips

    @button_tips.setter
    def button_tips(self, value):
        self._button_tips = value
    @property
    def button_url(self):
        return self._button_url

    @button_url.setter
    def button_url(self, value):
        self._button_url = value
    @property
    def button_url_json(self):
        return self._button_url_json

    @button_url_json.setter
    def button_url_json(self, value):
        self._button_url_json = value


    def to_alipay_dict(self):
        params = dict()
        if self.button_code:
            if hasattr(self.button_code, 'to_alipay_dict'):
                params['button_code'] = self.button_code.to_alipay_dict()
            else:
                params['button_code'] = self.button_code
        if self.button_ext_info:
            if hasattr(self.button_ext_info, 'to_alipay_dict'):
                params['button_ext_info'] = self.button_ext_info.to_alipay_dict()
            else:
                params['button_ext_info'] = self.button_ext_info
        if self.button_ext_info_model:
            if hasattr(self.button_ext_info_model, 'to_alipay_dict'):
                params['button_ext_info_model'] = self.button_ext_info_model.to_alipay_dict()
            else:
                params['button_ext_info_model'] = self.button_ext_info_model
        if self.button_order:
            if hasattr(self.button_order, 'to_alipay_dict'):
                params['button_order'] = self.button_order.to_alipay_dict()
            else:
                params['button_order'] = self.button_order
        if self.button_pop_info_model:
            if hasattr(self.button_pop_info_model, 'to_alipay_dict'):
                params['button_pop_info_model'] = self.button_pop_info_model.to_alipay_dict()
            else:
                params['button_pop_info_model'] = self.button_pop_info_model
        if self.button_pop_up:
            if hasattr(self.button_pop_up, 'to_alipay_dict'):
                params['button_pop_up'] = self.button_pop_up.to_alipay_dict()
            else:
                params['button_pop_up'] = self.button_pop_up
        if self.button_style:
            if hasattr(self.button_style, 'to_alipay_dict'):
                params['button_style'] = self.button_style.to_alipay_dict()
            else:
                params['button_style'] = self.button_style
        if self.button_text:
            if hasattr(self.button_text, 'to_alipay_dict'):
                params['button_text'] = self.button_text.to_alipay_dict()
            else:
                params['button_text'] = self.button_text
        if self.button_tips:
            if hasattr(self.button_tips, 'to_alipay_dict'):
                params['button_tips'] = self.button_tips.to_alipay_dict()
            else:
                params['button_tips'] = self.button_tips
        if self.button_url:
            if hasattr(self.button_url, 'to_alipay_dict'):
                params['button_url'] = self.button_url.to_alipay_dict()
            else:
                params['button_url'] = self.button_url
        if self.button_url_json:
            if hasattr(self.button_url_json, 'to_alipay_dict'):
                params['button_url_json'] = self.button_url_json.to_alipay_dict()
            else:
                params['button_url_json'] = self.button_url_json
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalRegisterButtonInfo()
        if 'button_code' in d:
            o.button_code = d['button_code']
        if 'button_ext_info' in d:
            o.button_ext_info = d['button_ext_info']
        if 'button_ext_info_model' in d:
            o.button_ext_info_model = d['button_ext_info_model']
        if 'button_order' in d:
            o.button_order = d['button_order']
        if 'button_pop_info_model' in d:
            o.button_pop_info_model = d['button_pop_info_model']
        if 'button_pop_up' in d:
            o.button_pop_up = d['button_pop_up']
        if 'button_style' in d:
            o.button_style = d['button_style']
        if 'button_text' in d:
            o.button_text = d['button_text']
        if 'button_tips' in d:
            o.button_tips = d['button_tips']
        if 'button_url' in d:
            o.button_url = d['button_url']
        if 'button_url_json' in d:
            o.button_url_json = d['button_url_json']
        return o


