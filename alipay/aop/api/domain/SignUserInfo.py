#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SignUserInfo(object):

    def __init__(self):
        self._agreement_gmt_create = None
        self._agreement_id = None
        self._agreement_url = None
        self._agreement_version = None
        self._face_verification_id = None
        self._face_verification_platform = None
        self._face_verification_time = None
        self._id_card = None
        self._real_name = None
        self._sign_datetime = None

    @property
    def agreement_gmt_create(self):
        return self._agreement_gmt_create

    @agreement_gmt_create.setter
    def agreement_gmt_create(self, value):
        self._agreement_gmt_create = value
    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def agreement_url(self):
        return self._agreement_url

    @agreement_url.setter
    def agreement_url(self, value):
        self._agreement_url = value
    @property
    def agreement_version(self):
        return self._agreement_version

    @agreement_version.setter
    def agreement_version(self, value):
        self._agreement_version = value
    @property
    def face_verification_id(self):
        return self._face_verification_id

    @face_verification_id.setter
    def face_verification_id(self, value):
        self._face_verification_id = value
    @property
    def face_verification_platform(self):
        return self._face_verification_platform

    @face_verification_platform.setter
    def face_verification_platform(self, value):
        self._face_verification_platform = value
    @property
    def face_verification_time(self):
        return self._face_verification_time

    @face_verification_time.setter
    def face_verification_time(self, value):
        self._face_verification_time = value
    @property
    def id_card(self):
        return self._id_card

    @id_card.setter
    def id_card(self, value):
        self._id_card = value
    @property
    def real_name(self):
        return self._real_name

    @real_name.setter
    def real_name(self, value):
        self._real_name = value
    @property
    def sign_datetime(self):
        return self._sign_datetime

    @sign_datetime.setter
    def sign_datetime(self, value):
        self._sign_datetime = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_gmt_create:
            if hasattr(self.agreement_gmt_create, 'to_alipay_dict'):
                params['agreement_gmt_create'] = self.agreement_gmt_create.to_alipay_dict()
            else:
                params['agreement_gmt_create'] = self.agreement_gmt_create
        if self.agreement_id:
            if hasattr(self.agreement_id, 'to_alipay_dict'):
                params['agreement_id'] = self.agreement_id.to_alipay_dict()
            else:
                params['agreement_id'] = self.agreement_id
        if self.agreement_url:
            if hasattr(self.agreement_url, 'to_alipay_dict'):
                params['agreement_url'] = self.agreement_url.to_alipay_dict()
            else:
                params['agreement_url'] = self.agreement_url
        if self.agreement_version:
            if hasattr(self.agreement_version, 'to_alipay_dict'):
                params['agreement_version'] = self.agreement_version.to_alipay_dict()
            else:
                params['agreement_version'] = self.agreement_version
        if self.face_verification_id:
            if hasattr(self.face_verification_id, 'to_alipay_dict'):
                params['face_verification_id'] = self.face_verification_id.to_alipay_dict()
            else:
                params['face_verification_id'] = self.face_verification_id
        if self.face_verification_platform:
            if hasattr(self.face_verification_platform, 'to_alipay_dict'):
                params['face_verification_platform'] = self.face_verification_platform.to_alipay_dict()
            else:
                params['face_verification_platform'] = self.face_verification_platform
        if self.face_verification_time:
            if hasattr(self.face_verification_time, 'to_alipay_dict'):
                params['face_verification_time'] = self.face_verification_time.to_alipay_dict()
            else:
                params['face_verification_time'] = self.face_verification_time
        if self.id_card:
            if hasattr(self.id_card, 'to_alipay_dict'):
                params['id_card'] = self.id_card.to_alipay_dict()
            else:
                params['id_card'] = self.id_card
        if self.real_name:
            if hasattr(self.real_name, 'to_alipay_dict'):
                params['real_name'] = self.real_name.to_alipay_dict()
            else:
                params['real_name'] = self.real_name
        if self.sign_datetime:
            if hasattr(self.sign_datetime, 'to_alipay_dict'):
                params['sign_datetime'] = self.sign_datetime.to_alipay_dict()
            else:
                params['sign_datetime'] = self.sign_datetime
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignUserInfo()
        if 'agreement_gmt_create' in d:
            o.agreement_gmt_create = d['agreement_gmt_create']
        if 'agreement_id' in d:
            o.agreement_id = d['agreement_id']
        if 'agreement_url' in d:
            o.agreement_url = d['agreement_url']
        if 'agreement_version' in d:
            o.agreement_version = d['agreement_version']
        if 'face_verification_id' in d:
            o.face_verification_id = d['face_verification_id']
        if 'face_verification_platform' in d:
            o.face_verification_platform = d['face_verification_platform']
        if 'face_verification_time' in d:
            o.face_verification_time = d['face_verification_time']
        if 'id_card' in d:
            o.id_card = d['id_card']
        if 'real_name' in d:
            o.real_name = d['real_name']
        if 'sign_datetime' in d:
            o.sign_datetime = d['sign_datetime']
        return o


