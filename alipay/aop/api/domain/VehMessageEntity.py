#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VehMessageEntity(object):

    def __init__(self):
        self._certificate_number = None
        self._certificate_type = None
        self._certificate_username = None
        self._ext_info = None
        self._mark = None
        self._msg_template_id = None
        self._out_msg_id = None
        self._target_url = None
        self._uid = None

    @property
    def certificate_number(self):
        return self._certificate_number

    @certificate_number.setter
    def certificate_number(self, value):
        self._certificate_number = value
    @property
    def certificate_type(self):
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, value):
        self._certificate_type = value
    @property
    def certificate_username(self):
        return self._certificate_username

    @certificate_username.setter
    def certificate_username(self, value):
        self._certificate_username = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, value):
        self._mark = value
    @property
    def msg_template_id(self):
        return self._msg_template_id

    @msg_template_id.setter
    def msg_template_id(self, value):
        self._msg_template_id = value
    @property
    def out_msg_id(self):
        return self._out_msg_id

    @out_msg_id.setter
    def out_msg_id(self, value):
        self._out_msg_id = value
    @property
    def target_url(self):
        return self._target_url

    @target_url.setter
    def target_url(self, value):
        self._target_url = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_number:
            if hasattr(self.certificate_number, 'to_alipay_dict'):
                params['certificate_number'] = self.certificate_number.to_alipay_dict()
            else:
                params['certificate_number'] = self.certificate_number
        if self.certificate_type:
            if hasattr(self.certificate_type, 'to_alipay_dict'):
                params['certificate_type'] = self.certificate_type.to_alipay_dict()
            else:
                params['certificate_type'] = self.certificate_type
        if self.certificate_username:
            if hasattr(self.certificate_username, 'to_alipay_dict'):
                params['certificate_username'] = self.certificate_username.to_alipay_dict()
            else:
                params['certificate_username'] = self.certificate_username
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.mark:
            if hasattr(self.mark, 'to_alipay_dict'):
                params['mark'] = self.mark.to_alipay_dict()
            else:
                params['mark'] = self.mark
        if self.msg_template_id:
            if hasattr(self.msg_template_id, 'to_alipay_dict'):
                params['msg_template_id'] = self.msg_template_id.to_alipay_dict()
            else:
                params['msg_template_id'] = self.msg_template_id
        if self.out_msg_id:
            if hasattr(self.out_msg_id, 'to_alipay_dict'):
                params['out_msg_id'] = self.out_msg_id.to_alipay_dict()
            else:
                params['out_msg_id'] = self.out_msg_id
        if self.target_url:
            if hasattr(self.target_url, 'to_alipay_dict'):
                params['target_url'] = self.target_url.to_alipay_dict()
            else:
                params['target_url'] = self.target_url
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VehMessageEntity()
        if 'certificate_number' in d:
            o.certificate_number = d['certificate_number']
        if 'certificate_type' in d:
            o.certificate_type = d['certificate_type']
        if 'certificate_username' in d:
            o.certificate_username = d['certificate_username']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'mark' in d:
            o.mark = d['mark']
        if 'msg_template_id' in d:
            o.msg_template_id = d['msg_template_id']
        if 'out_msg_id' in d:
            o.out_msg_id = d['out_msg_id']
        if 'target_url' in d:
            o.target_url = d['target_url']
        if 'uid' in d:
            o.uid = d['uid']
        return o


