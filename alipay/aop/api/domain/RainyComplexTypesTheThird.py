#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RainyComplexTypesTheThird(object):

    def __init__(self):
        self._idtype_open_id = None
        self._open_id = None
        self._user_id = None
        self._user_id_idtype = None

    @property
    def idtype_open_id(self):
        return self._idtype_open_id

    @idtype_open_id.setter
    def idtype_open_id(self, value):
        self._idtype_open_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_id_idtype(self):
        return self._user_id_idtype

    @user_id_idtype.setter
    def user_id_idtype(self, value):
        self._user_id_idtype = value


    def to_alipay_dict(self):
        params = dict()
        if self.idtype_open_id:
            if hasattr(self.idtype_open_id, 'to_alipay_dict'):
                params['idtype_open_id'] = self.idtype_open_id.to_alipay_dict()
            else:
                params['idtype_open_id'] = self.idtype_open_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_id_idtype:
            if hasattr(self.user_id_idtype, 'to_alipay_dict'):
                params['user_id_idtype'] = self.user_id_idtype.to_alipay_dict()
            else:
                params['user_id_idtype'] = self.user_id_idtype
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RainyComplexTypesTheThird()
        if 'idtype_open_id' in d:
            o.idtype_open_id = d['idtype_open_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_id_idtype' in d:
            o.user_id_idtype = d['user_id_idtype']
        return o


