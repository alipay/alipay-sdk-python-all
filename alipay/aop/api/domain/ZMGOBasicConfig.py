#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZMGOBasicConfig(object):

    def __init__(self):
        self._biz_type = None
        self._contact = None
        self._isv_pid = None
        self._merchant_custom_logo = None
        self._out_biz_no = None
        self._partner_id = None
        self._template_name = None
        self._template_no = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, value):
        self._contact = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def merchant_custom_logo(self):
        return self._merchant_custom_logo

    @merchant_custom_logo.setter
    def merchant_custom_logo(self, value):
        self._merchant_custom_logo = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def template_name(self):
        return self._template_name

    @template_name.setter
    def template_name(self, value):
        self._template_name = value
    @property
    def template_no(self):
        return self._template_no

    @template_no.setter
    def template_no(self, value):
        self._template_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.contact:
            if hasattr(self.contact, 'to_alipay_dict'):
                params['contact'] = self.contact.to_alipay_dict()
            else:
                params['contact'] = self.contact
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.merchant_custom_logo:
            if hasattr(self.merchant_custom_logo, 'to_alipay_dict'):
                params['merchant_custom_logo'] = self.merchant_custom_logo.to_alipay_dict()
            else:
                params['merchant_custom_logo'] = self.merchant_custom_logo
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.template_name:
            if hasattr(self.template_name, 'to_alipay_dict'):
                params['template_name'] = self.template_name.to_alipay_dict()
            else:
                params['template_name'] = self.template_name
        if self.template_no:
            if hasattr(self.template_no, 'to_alipay_dict'):
                params['template_no'] = self.template_no.to_alipay_dict()
            else:
                params['template_no'] = self.template_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZMGOBasicConfig()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'contact' in d:
            o.contact = d['contact']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'merchant_custom_logo' in d:
            o.merchant_custom_logo = d['merchant_custom_logo']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'template_name' in d:
            o.template_name = d['template_name']
        if 'template_no' in d:
            o.template_no = d['template_no']
        return o


