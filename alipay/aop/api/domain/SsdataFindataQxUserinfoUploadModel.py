#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SsdataFindataQxUserinfoUploadModel(object):

    def __init__(self):
        self._ext_params = None
        self._id_card_no = None
        self._org_biz_no = None
        self._phone = None
        self._user_name = None

    @property
    def ext_params(self):
        return self._ext_params

    @ext_params.setter
    def ext_params(self, value):
        self._ext_params = value
    @property
    def id_card_no(self):
        return self._id_card_no

    @id_card_no.setter
    def id_card_no(self, value):
        self._id_card_no = value
    @property
    def org_biz_no(self):
        return self._org_biz_no

    @org_biz_no.setter
    def org_biz_no(self, value):
        self._org_biz_no = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_params:
            if hasattr(self.ext_params, 'to_alipay_dict'):
                params['ext_params'] = self.ext_params.to_alipay_dict()
            else:
                params['ext_params'] = self.ext_params
        if self.id_card_no:
            if hasattr(self.id_card_no, 'to_alipay_dict'):
                params['id_card_no'] = self.id_card_no.to_alipay_dict()
            else:
                params['id_card_no'] = self.id_card_no
        if self.org_biz_no:
            if hasattr(self.org_biz_no, 'to_alipay_dict'):
                params['org_biz_no'] = self.org_biz_no.to_alipay_dict()
            else:
                params['org_biz_no'] = self.org_biz_no
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
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
        o = SsdataFindataQxUserinfoUploadModel()
        if 'ext_params' in d:
            o.ext_params = d['ext_params']
        if 'id_card_no' in d:
            o.id_card_no = d['id_card_no']
        if 'org_biz_no' in d:
            o.org_biz_no = d['org_biz_no']
        if 'phone' in d:
            o.phone = d['phone']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


