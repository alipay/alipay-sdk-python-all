#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OfflineLaborProjectRegistRecord(object):

    def __init__(self):
        self._alipay_account = None
        self._alipay_register_id = None
        self._birth_date = None
        self._certified = None
        self._face_auth_status = None
        self._gender = None
        self._health_cert = None
        self._id_card_number = None
        self._job_name = None
        self._open_id = None
        self._out_regist_id = None
        self._out_register_id = None
        self._out_register_no = None
        self._phone_number = None
        self._project_name = None
        self._register_time = None
        self._social_risk_info = None
        self._user_id = None
        self._user_name = None

    @property
    def alipay_account(self):
        return self._alipay_account

    @alipay_account.setter
    def alipay_account(self, value):
        self._alipay_account = value
    @property
    def alipay_register_id(self):
        return self._alipay_register_id

    @alipay_register_id.setter
    def alipay_register_id(self, value):
        self._alipay_register_id = value
    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = value
    @property
    def certified(self):
        return self._certified

    @certified.setter
    def certified(self, value):
        self._certified = value
    @property
    def face_auth_status(self):
        return self._face_auth_status

    @face_auth_status.setter
    def face_auth_status(self, value):
        self._face_auth_status = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def health_cert(self):
        return self._health_cert

    @health_cert.setter
    def health_cert(self, value):
        self._health_cert = value
    @property
    def id_card_number(self):
        return self._id_card_number

    @id_card_number.setter
    def id_card_number(self, value):
        self._id_card_number = value
    @property
    def job_name(self):
        return self._job_name

    @job_name.setter
    def job_name(self, value):
        self._job_name = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_regist_id(self):
        return self._out_regist_id

    @out_regist_id.setter
    def out_regist_id(self, value):
        self._out_regist_id = value
    @property
    def out_register_id(self):
        return self._out_register_id

    @out_register_id.setter
    def out_register_id(self, value):
        self._out_register_id = value
    @property
    def out_register_no(self):
        return self._out_register_no

    @out_register_no.setter
    def out_register_no(self, value):
        self._out_register_no = value
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value
    @property
    def project_name(self):
        return self._project_name

    @project_name.setter
    def project_name(self, value):
        self._project_name = value
    @property
    def register_time(self):
        return self._register_time

    @register_time.setter
    def register_time(self, value):
        self._register_time = value
    @property
    def social_risk_info(self):
        return self._social_risk_info

    @social_risk_info.setter
    def social_risk_info(self, value):
        self._social_risk_info = value
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
        if self.alipay_account:
            if hasattr(self.alipay_account, 'to_alipay_dict'):
                params['alipay_account'] = self.alipay_account.to_alipay_dict()
            else:
                params['alipay_account'] = self.alipay_account
        if self.alipay_register_id:
            if hasattr(self.alipay_register_id, 'to_alipay_dict'):
                params['alipay_register_id'] = self.alipay_register_id.to_alipay_dict()
            else:
                params['alipay_register_id'] = self.alipay_register_id
        if self.birth_date:
            if hasattr(self.birth_date, 'to_alipay_dict'):
                params['birth_date'] = self.birth_date.to_alipay_dict()
            else:
                params['birth_date'] = self.birth_date
        if self.certified:
            if hasattr(self.certified, 'to_alipay_dict'):
                params['certified'] = self.certified.to_alipay_dict()
            else:
                params['certified'] = self.certified
        if self.face_auth_status:
            if hasattr(self.face_auth_status, 'to_alipay_dict'):
                params['face_auth_status'] = self.face_auth_status.to_alipay_dict()
            else:
                params['face_auth_status'] = self.face_auth_status
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.health_cert:
            if hasattr(self.health_cert, 'to_alipay_dict'):
                params['health_cert'] = self.health_cert.to_alipay_dict()
            else:
                params['health_cert'] = self.health_cert
        if self.id_card_number:
            if hasattr(self.id_card_number, 'to_alipay_dict'):
                params['id_card_number'] = self.id_card_number.to_alipay_dict()
            else:
                params['id_card_number'] = self.id_card_number
        if self.job_name:
            if hasattr(self.job_name, 'to_alipay_dict'):
                params['job_name'] = self.job_name.to_alipay_dict()
            else:
                params['job_name'] = self.job_name
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_regist_id:
            if hasattr(self.out_regist_id, 'to_alipay_dict'):
                params['out_regist_id'] = self.out_regist_id.to_alipay_dict()
            else:
                params['out_regist_id'] = self.out_regist_id
        if self.out_register_id:
            if hasattr(self.out_register_id, 'to_alipay_dict'):
                params['out_register_id'] = self.out_register_id.to_alipay_dict()
            else:
                params['out_register_id'] = self.out_register_id
        if self.out_register_no:
            if hasattr(self.out_register_no, 'to_alipay_dict'):
                params['out_register_no'] = self.out_register_no.to_alipay_dict()
            else:
                params['out_register_no'] = self.out_register_no
        if self.phone_number:
            if hasattr(self.phone_number, 'to_alipay_dict'):
                params['phone_number'] = self.phone_number.to_alipay_dict()
            else:
                params['phone_number'] = self.phone_number
        if self.project_name:
            if hasattr(self.project_name, 'to_alipay_dict'):
                params['project_name'] = self.project_name.to_alipay_dict()
            else:
                params['project_name'] = self.project_name
        if self.register_time:
            if hasattr(self.register_time, 'to_alipay_dict'):
                params['register_time'] = self.register_time.to_alipay_dict()
            else:
                params['register_time'] = self.register_time
        if self.social_risk_info:
            if hasattr(self.social_risk_info, 'to_alipay_dict'):
                params['social_risk_info'] = self.social_risk_info.to_alipay_dict()
            else:
                params['social_risk_info'] = self.social_risk_info
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
        o = OfflineLaborProjectRegistRecord()
        if 'alipay_account' in d:
            o.alipay_account = d['alipay_account']
        if 'alipay_register_id' in d:
            o.alipay_register_id = d['alipay_register_id']
        if 'birth_date' in d:
            o.birth_date = d['birth_date']
        if 'certified' in d:
            o.certified = d['certified']
        if 'face_auth_status' in d:
            o.face_auth_status = d['face_auth_status']
        if 'gender' in d:
            o.gender = d['gender']
        if 'health_cert' in d:
            o.health_cert = d['health_cert']
        if 'id_card_number' in d:
            o.id_card_number = d['id_card_number']
        if 'job_name' in d:
            o.job_name = d['job_name']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_regist_id' in d:
            o.out_regist_id = d['out_regist_id']
        if 'out_register_id' in d:
            o.out_register_id = d['out_register_id']
        if 'out_register_no' in d:
            o.out_register_no = d['out_register_no']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        if 'project_name' in d:
            o.project_name = d['project_name']
        if 'register_time' in d:
            o.register_time = d['register_time']
        if 'social_risk_info' in d:
            o.social_risk_info = d['social_risk_info']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


