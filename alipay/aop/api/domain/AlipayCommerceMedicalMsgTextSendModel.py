#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalMsgTextSendModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._biz_principal = None
        self._msg_content = None
        self._msg_create_time = None
        self._msg_modified_time = None
        self._open_id = None
        self._org_id = None
        self._out_biz_no = None
        self._phone_no = None
        self._template_id = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def biz_principal(self):
        return self._biz_principal

    @biz_principal.setter
    def biz_principal(self, value):
        self._biz_principal = value
    @property
    def msg_content(self):
        return self._msg_content

    @msg_content.setter
    def msg_content(self, value):
        self._msg_content = value
    @property
    def msg_create_time(self):
        return self._msg_create_time

    @msg_create_time.setter
    def msg_create_time(self, value):
        self._msg_create_time = value
    @property
    def msg_modified_time(self):
        return self._msg_modified_time

    @msg_modified_time.setter
    def msg_modified_time(self, value):
        self._msg_modified_time = value
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
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, value):
        self._phone_no = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.biz_principal:
            if hasattr(self.biz_principal, 'to_alipay_dict'):
                params['biz_principal'] = self.biz_principal.to_alipay_dict()
            else:
                params['biz_principal'] = self.biz_principal
        if self.msg_content:
            if hasattr(self.msg_content, 'to_alipay_dict'):
                params['msg_content'] = self.msg_content.to_alipay_dict()
            else:
                params['msg_content'] = self.msg_content
        if self.msg_create_time:
            if hasattr(self.msg_create_time, 'to_alipay_dict'):
                params['msg_create_time'] = self.msg_create_time.to_alipay_dict()
            else:
                params['msg_create_time'] = self.msg_create_time
        if self.msg_modified_time:
            if hasattr(self.msg_modified_time, 'to_alipay_dict'):
                params['msg_modified_time'] = self.msg_modified_time.to_alipay_dict()
            else:
                params['msg_modified_time'] = self.msg_modified_time
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
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.phone_no:
            if hasattr(self.phone_no, 'to_alipay_dict'):
                params['phone_no'] = self.phone_no.to_alipay_dict()
            else:
                params['phone_no'] = self.phone_no
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalMsgTextSendModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'biz_principal' in d:
            o.biz_principal = d['biz_principal']
        if 'msg_content' in d:
            o.msg_content = d['msg_content']
        if 'msg_create_time' in d:
            o.msg_create_time = d['msg_create_time']
        if 'msg_modified_time' in d:
            o.msg_modified_time = d['msg_modified_time']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'org_id' in d:
            o.org_id = d['org_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'phone_no' in d:
            o.phone_no = d['phone_no']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


