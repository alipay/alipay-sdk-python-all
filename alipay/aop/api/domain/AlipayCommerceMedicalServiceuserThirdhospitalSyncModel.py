#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalServiceuserThirdhospitalSyncModel(object):

    def __init__(self):
        self._avatar = None
        self._department = None
        self._description = None
        self._doc_id = None
        self._hospital_id = None
        self._hospital_name = None
        self._id_card = None
        self._mini_app_id = None
        self._mobile = None
        self._source = None
        self._title = None
        self._user_name = None

    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        self._avatar = value
    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def doc_id(self):
        return self._doc_id

    @doc_id.setter
    def doc_id(self, value):
        self._doc_id = value
    @property
    def hospital_id(self):
        return self._hospital_id

    @hospital_id.setter
    def hospital_id(self, value):
        self._hospital_id = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def id_card(self):
        return self._id_card

    @id_card.setter
    def id_card(self, value):
        self._id_card = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.avatar:
            if hasattr(self.avatar, 'to_alipay_dict'):
                params['avatar'] = self.avatar.to_alipay_dict()
            else:
                params['avatar'] = self.avatar
        if self.department:
            if hasattr(self.department, 'to_alipay_dict'):
                params['department'] = self.department.to_alipay_dict()
            else:
                params['department'] = self.department
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.doc_id:
            if hasattr(self.doc_id, 'to_alipay_dict'):
                params['doc_id'] = self.doc_id.to_alipay_dict()
            else:
                params['doc_id'] = self.doc_id
        if self.hospital_id:
            if hasattr(self.hospital_id, 'to_alipay_dict'):
                params['hospital_id'] = self.hospital_id.to_alipay_dict()
            else:
                params['hospital_id'] = self.hospital_id
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.id_card:
            if hasattr(self.id_card, 'to_alipay_dict'):
                params['id_card'] = self.id_card.to_alipay_dict()
            else:
                params['id_card'] = self.id_card
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
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
        o = AlipayCommerceMedicalServiceuserThirdhospitalSyncModel()
        if 'avatar' in d:
            o.avatar = d['avatar']
        if 'department' in d:
            o.department = d['department']
        if 'description' in d:
            o.description = d['description']
        if 'doc_id' in d:
            o.doc_id = d['doc_id']
        if 'hospital_id' in d:
            o.hospital_id = d['hospital_id']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'id_card' in d:
            o.id_card = d['id_card']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'source' in d:
            o.source = d['source']
        if 'title' in d:
            o.title = d['title']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


