#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommercePropertyFiledetectionQueryModel(object):

    def __init__(self):
        self._code = None
        self._coil_id = None
        self._community_id = None
        self._end_time = None
        self._file_ai_check = None
        self._open_id = None
        self._page_no = None
        self._page_size = None
        self._point_id = None
        self._qrcode_check = None
        self._serial_no = None
        self._start_time = None
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
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def file_ai_check(self):
        return self._file_ai_check

    @file_ai_check.setter
    def file_ai_check(self, value):
        self._file_ai_check = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
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
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
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
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.file_ai_check:
            if hasattr(self.file_ai_check, 'to_alipay_dict'):
                params['file_ai_check'] = self.file_ai_check.to_alipay_dict()
            else:
                params['file_ai_check'] = self.file_ai_check
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
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
        if self.serial_no:
            if hasattr(self.serial_no, 'to_alipay_dict'):
                params['serial_no'] = self.serial_no.to_alipay_dict()
            else:
                params['serial_no'] = self.serial_no
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
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
        o = AlipayCommercePropertyFiledetectionQueryModel()
        if 'code' in d:
            o.code = d['code']
        if 'coil_id' in d:
            o.coil_id = d['coil_id']
        if 'community_id' in d:
            o.community_id = d['community_id']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'file_ai_check' in d:
            o.file_ai_check = d['file_ai_check']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'point_id' in d:
            o.point_id = d['point_id']
        if 'qrcode_check' in d:
            o.qrcode_check = d['qrcode_check']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


