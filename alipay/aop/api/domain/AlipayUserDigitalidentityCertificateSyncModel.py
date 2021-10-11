#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserDigitalidentityCertificateSyncModel(object):

    def __init__(self):
        self._apply_info_verify_mode = None
        self._certificate_id = None
        self._certificate_instance_code = None
        self._ext_info = None
        self._status = None
        self._sync_token = None
        self._user_apply_cert_no = None
        self._user_apply_cert_type = None
        self._user_id = None
        self._user_name = None

    @property
    def apply_info_verify_mode(self):
        return self._apply_info_verify_mode

    @apply_info_verify_mode.setter
    def apply_info_verify_mode(self, value):
        self._apply_info_verify_mode = value
    @property
    def certificate_id(self):
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, value):
        self._certificate_id = value
    @property
    def certificate_instance_code(self):
        return self._certificate_instance_code

    @certificate_instance_code.setter
    def certificate_instance_code(self, value):
        self._certificate_instance_code = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sync_token(self):
        return self._sync_token

    @sync_token.setter
    def sync_token(self, value):
        self._sync_token = value
    @property
    def user_apply_cert_no(self):
        return self._user_apply_cert_no

    @user_apply_cert_no.setter
    def user_apply_cert_no(self, value):
        self._user_apply_cert_no = value
    @property
    def user_apply_cert_type(self):
        return self._user_apply_cert_type

    @user_apply_cert_type.setter
    def user_apply_cert_type(self, value):
        self._user_apply_cert_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_info_verify_mode:
            if hasattr(self.apply_info_verify_mode, 'to_alipay_dict'):
                params['apply_info_verify_mode'] = self.apply_info_verify_mode.to_alipay_dict()
            else:
                params['apply_info_verify_mode'] = self.apply_info_verify_mode
        if self.certificate_id:
            if hasattr(self.certificate_id, 'to_alipay_dict'):
                params['certificate_id'] = self.certificate_id.to_alipay_dict()
            else:
                params['certificate_id'] = self.certificate_id
        if self.certificate_instance_code:
            if hasattr(self.certificate_instance_code, 'to_alipay_dict'):
                params['certificate_instance_code'] = self.certificate_instance_code.to_alipay_dict()
            else:
                params['certificate_instance_code'] = self.certificate_instance_code
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sync_token:
            if hasattr(self.sync_token, 'to_alipay_dict'):
                params['sync_token'] = self.sync_token.to_alipay_dict()
            else:
                params['sync_token'] = self.sync_token
        if self.user_apply_cert_no:
            if hasattr(self.user_apply_cert_no, 'to_alipay_dict'):
                params['user_apply_cert_no'] = self.user_apply_cert_no.to_alipay_dict()
            else:
                params['user_apply_cert_no'] = self.user_apply_cert_no
        if self.user_apply_cert_type:
            if hasattr(self.user_apply_cert_type, 'to_alipay_dict'):
                params['user_apply_cert_type'] = self.user_apply_cert_type.to_alipay_dict()
            else:
                params['user_apply_cert_type'] = self.user_apply_cert_type
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserDigitalidentityCertificateSyncModel()
        if 'apply_info_verify_mode' in d:
            o.apply_info_verify_mode = d['apply_info_verify_mode']
        if 'certificate_id' in d:
            o.certificate_id = d['certificate_id']
        if 'certificate_instance_code' in d:
            o.certificate_instance_code = d['certificate_instance_code']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'status' in d:
            o.status = d['status']
        if 'sync_token' in d:
            o.sync_token = d['sync_token']
        if 'user_apply_cert_no' in d:
            o.user_apply_cert_no = d['user_apply_cert_no']
        if 'user_apply_cert_type' in d:
            o.user_apply_cert_type = d['user_apply_cert_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


