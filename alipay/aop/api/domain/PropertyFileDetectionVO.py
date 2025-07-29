#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PropertyFileDetectionVO(object):

    def __init__(self):
        self._code = None
        self._coil_id = None
        self._community_id = None
        self._create_time = None
        self._file_ai_check = None
        self._file_ai_check_reason = None
        self._file_id = None
        self._file_url = None
        self._open_id = None
        self._point_id = None
        self._qrcode_check = None
        self._qrcode_check_reason = None
        self._serial_no = None
        self._sign_in_id = None
        self._user_id = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def coil_id(self):
        return self._coil_id

    @coil_id.setter
    def coil_id(self, value):
        self._coil_id = value
    @property
    def community_id(self):
        return self._community_id

    @community_id.setter
    def community_id(self, value):
        self._community_id = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def file_ai_check(self):
        return self._file_ai_check

    @file_ai_check.setter
    def file_ai_check(self, value):
        self._file_ai_check = value
    @property
    def file_ai_check_reason(self):
        return self._file_ai_check_reason

    @file_ai_check_reason.setter
    def file_ai_check_reason(self, value):
        self._file_ai_check_reason = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def point_id(self):
        return self._point_id

    @point_id.setter
    def point_id(self, value):
        self._point_id = value
    @property
    def qrcode_check(self):
        return self._qrcode_check

    @qrcode_check.setter
    def qrcode_check(self, value):
        self._qrcode_check = value
    @property
    def qrcode_check_reason(self):
        return self._qrcode_check_reason

    @qrcode_check_reason.setter
    def qrcode_check_reason(self, value):
        self._qrcode_check_reason = value
    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value
    @property
    def sign_in_id(self):
        return self._sign_in_id

    @sign_in_id.setter
    def sign_in_id(self, value):
        self._sign_in_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.coil_id:
            if hasattr(self.coil_id, 'to_alipay_dict'):
                params['coil_id'] = self.coil_id.to_alipay_dict()
            else:
                params['coil_id'] = self.coil_id
        if self.community_id:
            if hasattr(self.community_id, 'to_alipay_dict'):
                params['community_id'] = self.community_id.to_alipay_dict()
            else:
                params['community_id'] = self.community_id
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.file_ai_check:
            if hasattr(self.file_ai_check, 'to_alipay_dict'):
                params['file_ai_check'] = self.file_ai_check.to_alipay_dict()
            else:
                params['file_ai_check'] = self.file_ai_check
        if self.file_ai_check_reason:
            if hasattr(self.file_ai_check_reason, 'to_alipay_dict'):
                params['file_ai_check_reason'] = self.file_ai_check_reason.to_alipay_dict()
            else:
                params['file_ai_check_reason'] = self.file_ai_check_reason
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.file_url:
            if hasattr(self.file_url, 'to_alipay_dict'):
                params['file_url'] = self.file_url.to_alipay_dict()
            else:
                params['file_url'] = self.file_url
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.point_id:
            if hasattr(self.point_id, 'to_alipay_dict'):
                params['point_id'] = self.point_id.to_alipay_dict()
            else:
                params['point_id'] = self.point_id
        if self.qrcode_check:
            if hasattr(self.qrcode_check, 'to_alipay_dict'):
                params['qrcode_check'] = self.qrcode_check.to_alipay_dict()
            else:
                params['qrcode_check'] = self.qrcode_check
        if self.qrcode_check_reason:
            if hasattr(self.qrcode_check_reason, 'to_alipay_dict'):
                params['qrcode_check_reason'] = self.qrcode_check_reason.to_alipay_dict()
            else:
                params['qrcode_check_reason'] = self.qrcode_check_reason
        if self.serial_no:
            if hasattr(self.serial_no, 'to_alipay_dict'):
                params['serial_no'] = self.serial_no.to_alipay_dict()
            else:
                params['serial_no'] = self.serial_no
        if self.sign_in_id:
            if hasattr(self.sign_in_id, 'to_alipay_dict'):
                params['sign_in_id'] = self.sign_in_id.to_alipay_dict()
            else:
                params['sign_in_id'] = self.sign_in_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PropertyFileDetectionVO()
        if 'code' in d:
            o.code = d['code']
        if 'coil_id' in d:
            o.coil_id = d['coil_id']
        if 'community_id' in d:
            o.community_id = d['community_id']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'file_ai_check' in d:
            o.file_ai_check = d['file_ai_check']
        if 'file_ai_check_reason' in d:
            o.file_ai_check_reason = d['file_ai_check_reason']
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'file_url' in d:
            o.file_url = d['file_url']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'point_id' in d:
            o.point_id = d['point_id']
        if 'qrcode_check' in d:
            o.qrcode_check = d['qrcode_check']
        if 'qrcode_check_reason' in d:
            o.qrcode_check_reason = d['qrcode_check_reason']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        if 'sign_in_id' in d:
            o.sign_in_id = d['sign_in_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


