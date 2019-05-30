#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SchoolCardInfo(object):

    def __init__(self):
        self._alipay_card_no = None
        self._auth_type = None
        self._campus_no = None
        self._card_type = None
        self._create_time = None
        self._display_code_type = None
        self._name = None
        self._physical_card_number = None
        self._school_id = None
        self._school_name = None
        self._school_stdcode = None
        self._short_code = None
        self._status = None
        self._user_id = None

    @property
    def alipay_card_no(self):
        return self._alipay_card_no

    @alipay_card_no.setter
    def alipay_card_no(self, value):
        self._alipay_card_no = value
    @property
    def auth_type(self):
        return self._auth_type

    @auth_type.setter
    def auth_type(self, value):
        self._auth_type = value
    @property
    def campus_no(self):
        return self._campus_no

    @campus_no.setter
    def campus_no(self, value):
        self._campus_no = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def display_code_type(self):
        return self._display_code_type

    @display_code_type.setter
    def display_code_type(self, value):
        self._display_code_type = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def physical_card_number(self):
        return self._physical_card_number

    @physical_card_number.setter
    def physical_card_number(self, value):
        self._physical_card_number = value
    @property
    def school_id(self):
        return self._school_id

    @school_id.setter
    def school_id(self, value):
        self._school_id = value
    @property
    def school_name(self):
        return self._school_name

    @school_name.setter
    def school_name(self, value):
        self._school_name = value
    @property
    def school_stdcode(self):
        return self._school_stdcode

    @school_stdcode.setter
    def school_stdcode(self, value):
        self._school_stdcode = value
    @property
    def short_code(self):
        return self._short_code

    @short_code.setter
    def short_code(self, value):
        self._short_code = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_card_no:
            if hasattr(self.alipay_card_no, 'to_alipay_dict'):
                params['alipay_card_no'] = self.alipay_card_no.to_alipay_dict()
            else:
                params['alipay_card_no'] = self.alipay_card_no
        if self.auth_type:
            if hasattr(self.auth_type, 'to_alipay_dict'):
                params['auth_type'] = self.auth_type.to_alipay_dict()
            else:
                params['auth_type'] = self.auth_type
        if self.campus_no:
            if hasattr(self.campus_no, 'to_alipay_dict'):
                params['campus_no'] = self.campus_no.to_alipay_dict()
            else:
                params['campus_no'] = self.campus_no
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.display_code_type:
            if hasattr(self.display_code_type, 'to_alipay_dict'):
                params['display_code_type'] = self.display_code_type.to_alipay_dict()
            else:
                params['display_code_type'] = self.display_code_type
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.physical_card_number:
            if hasattr(self.physical_card_number, 'to_alipay_dict'):
                params['physical_card_number'] = self.physical_card_number.to_alipay_dict()
            else:
                params['physical_card_number'] = self.physical_card_number
        if self.school_id:
            if hasattr(self.school_id, 'to_alipay_dict'):
                params['school_id'] = self.school_id.to_alipay_dict()
            else:
                params['school_id'] = self.school_id
        if self.school_name:
            if hasattr(self.school_name, 'to_alipay_dict'):
                params['school_name'] = self.school_name.to_alipay_dict()
            else:
                params['school_name'] = self.school_name
        if self.school_stdcode:
            if hasattr(self.school_stdcode, 'to_alipay_dict'):
                params['school_stdcode'] = self.school_stdcode.to_alipay_dict()
            else:
                params['school_stdcode'] = self.school_stdcode
        if self.short_code:
            if hasattr(self.short_code, 'to_alipay_dict'):
                params['short_code'] = self.short_code.to_alipay_dict()
            else:
                params['short_code'] = self.short_code
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        o = SchoolCardInfo()
        if 'alipay_card_no' in d:
            o.alipay_card_no = d['alipay_card_no']
        if 'auth_type' in d:
            o.auth_type = d['auth_type']
        if 'campus_no' in d:
            o.campus_no = d['campus_no']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'display_code_type' in d:
            o.display_code_type = d['display_code_type']
        if 'name' in d:
            o.name = d['name']
        if 'physical_card_number' in d:
            o.physical_card_number = d['physical_card_number']
        if 'school_id' in d:
            o.school_id = d['school_id']
        if 'school_name' in d:
            o.school_name = d['school_name']
        if 'school_stdcode' in d:
            o.school_stdcode = d['school_stdcode']
        if 'short_code' in d:
            o.short_code = d['short_code']
        if 'status' in d:
            o.status = d['status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


