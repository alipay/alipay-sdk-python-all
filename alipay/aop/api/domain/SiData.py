#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SiData(object):

    def __init__(self):
        self._request_id = None
        self._service_return_url = None
        self._target_extend_params = None
        self._target_idcard = None
        self._target_idcard_type = None
        self._target_mobile = None
        self._target_sicard_no = None
        self._target_user_id = None
        self._target_user_name = None
        self._template_data = None
        self._template_id = None
        self._template_version = None

    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def service_return_url(self):
        return self._service_return_url

    @service_return_url.setter
    def service_return_url(self, value):
        self._service_return_url = value
    @property
    def target_extend_params(self):
        return self._target_extend_params

    @target_extend_params.setter
    def target_extend_params(self, value):
        self._target_extend_params = value
    @property
    def target_idcard(self):
        return self._target_idcard

    @target_idcard.setter
    def target_idcard(self, value):
        self._target_idcard = value
    @property
    def target_idcard_type(self):
        return self._target_idcard_type

    @target_idcard_type.setter
    def target_idcard_type(self, value):
        self._target_idcard_type = value
    @property
    def target_mobile(self):
        return self._target_mobile

    @target_mobile.setter
    def target_mobile(self, value):
        self._target_mobile = value
    @property
    def target_sicard_no(self):
        return self._target_sicard_no

    @target_sicard_no.setter
    def target_sicard_no(self, value):
        self._target_sicard_no = value
    @property
    def target_user_id(self):
        return self._target_user_id

    @target_user_id.setter
    def target_user_id(self, value):
        self._target_user_id = value
    @property
    def target_user_name(self):
        return self._target_user_name

    @target_user_name.setter
    def target_user_name(self, value):
        self._target_user_name = value
    @property
    def template_data(self):
        return self._template_data

    @template_data.setter
    def template_data(self, value):
        self._template_data = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def template_version(self):
        return self._template_version

    @template_version.setter
    def template_version(self, value):
        self._template_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.service_return_url:
            if hasattr(self.service_return_url, 'to_alipay_dict'):
                params['service_return_url'] = self.service_return_url.to_alipay_dict()
            else:
                params['service_return_url'] = self.service_return_url
        if self.target_extend_params:
            if hasattr(self.target_extend_params, 'to_alipay_dict'):
                params['target_extend_params'] = self.target_extend_params.to_alipay_dict()
            else:
                params['target_extend_params'] = self.target_extend_params
        if self.target_idcard:
            if hasattr(self.target_idcard, 'to_alipay_dict'):
                params['target_idcard'] = self.target_idcard.to_alipay_dict()
            else:
                params['target_idcard'] = self.target_idcard
        if self.target_idcard_type:
            if hasattr(self.target_idcard_type, 'to_alipay_dict'):
                params['target_idcard_type'] = self.target_idcard_type.to_alipay_dict()
            else:
                params['target_idcard_type'] = self.target_idcard_type
        if self.target_mobile:
            if hasattr(self.target_mobile, 'to_alipay_dict'):
                params['target_mobile'] = self.target_mobile.to_alipay_dict()
            else:
                params['target_mobile'] = self.target_mobile
        if self.target_sicard_no:
            if hasattr(self.target_sicard_no, 'to_alipay_dict'):
                params['target_sicard_no'] = self.target_sicard_no.to_alipay_dict()
            else:
                params['target_sicard_no'] = self.target_sicard_no
        if self.target_user_id:
            if hasattr(self.target_user_id, 'to_alipay_dict'):
                params['target_user_id'] = self.target_user_id.to_alipay_dict()
            else:
                params['target_user_id'] = self.target_user_id
        if self.target_user_name:
            if hasattr(self.target_user_name, 'to_alipay_dict'):
                params['target_user_name'] = self.target_user_name.to_alipay_dict()
            else:
                params['target_user_name'] = self.target_user_name
        if self.template_data:
            if hasattr(self.template_data, 'to_alipay_dict'):
                params['template_data'] = self.template_data.to_alipay_dict()
            else:
                params['template_data'] = self.template_data
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.template_version:
            if hasattr(self.template_version, 'to_alipay_dict'):
                params['template_version'] = self.template_version.to_alipay_dict()
            else:
                params['template_version'] = self.template_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SiData()
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'service_return_url' in d:
            o.service_return_url = d['service_return_url']
        if 'target_extend_params' in d:
            o.target_extend_params = d['target_extend_params']
        if 'target_idcard' in d:
            o.target_idcard = d['target_idcard']
        if 'target_idcard_type' in d:
            o.target_idcard_type = d['target_idcard_type']
        if 'target_mobile' in d:
            o.target_mobile = d['target_mobile']
        if 'target_sicard_no' in d:
            o.target_sicard_no = d['target_sicard_no']
        if 'target_user_id' in d:
            o.target_user_id = d['target_user_id']
        if 'target_user_name' in d:
            o.target_user_name = d['target_user_name']
        if 'template_data' in d:
            o.template_data = d['template_data']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'template_version' in d:
            o.template_version = d['template_version']
        return o


