#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyComplexTypesTheFourth import RainyComplexTypesTheFourth


class AlipayDataDataserviceOldapitreeRainystestQueryModel(object):

    def __init__(self):
        self._complex_ref = None
        self._idjson_open_ids = None
        self._idtype_open_id = None
        self._idtype_user_id = None
        self._open_id = None
        self._user_id = None
        self._user_id_idtype = None

    @property
    def complex_ref(self):
        return self._complex_ref

    @complex_ref.setter
    def complex_ref(self, value):
        if isinstance(value, RainyComplexTypesTheFourth):
            self._complex_ref = value
        else:
            self._complex_ref = RainyComplexTypesTheFourth.from_alipay_dict(value)
    @property
    def idjson_open_ids(self):
        return self._idjson_open_ids

    @idjson_open_ids.setter
    def idjson_open_ids(self, value):
        if isinstance(value, list):
            self._idjson_open_ids = list()
            for i in value:
                self._idjson_open_ids.append(i)
    @property
    def idtype_open_id(self):
        return self._idtype_open_id

    @idtype_open_id.setter
    def idtype_open_id(self, value):
        self._idtype_open_id = value
    @property
    def idtype_user_id(self):
        return self._idtype_user_id

    @idtype_user_id.setter
    def idtype_user_id(self, value):
        self._idtype_user_id = value
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
        if self.complex_ref:
            if hasattr(self.complex_ref, 'to_alipay_dict'):
                params['complex_ref'] = self.complex_ref.to_alipay_dict()
            else:
                params['complex_ref'] = self.complex_ref
        if self.idjson_open_ids:
            if isinstance(self.idjson_open_ids, list):
                for i in range(0, len(self.idjson_open_ids)):
                    element = self.idjson_open_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.idjson_open_ids[i] = element.to_alipay_dict()
            if hasattr(self.idjson_open_ids, 'to_alipay_dict'):
                params['idjson_open_ids'] = self.idjson_open_ids.to_alipay_dict()
            else:
                params['idjson_open_ids'] = self.idjson_open_ids
        if self.idtype_open_id:
            if hasattr(self.idtype_open_id, 'to_alipay_dict'):
                params['idtype_open_id'] = self.idtype_open_id.to_alipay_dict()
            else:
                params['idtype_open_id'] = self.idtype_open_id
        if self.idtype_user_id:
            if hasattr(self.idtype_user_id, 'to_alipay_dict'):
                params['idtype_user_id'] = self.idtype_user_id.to_alipay_dict()
            else:
                params['idtype_user_id'] = self.idtype_user_id
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
        o = AlipayDataDataserviceOldapitreeRainystestQueryModel()
        if 'complex_ref' in d:
            o.complex_ref = d['complex_ref']
        if 'idjson_open_ids' in d:
            o.idjson_open_ids = d['idjson_open_ids']
        if 'idtype_open_id' in d:
            o.idtype_open_id = d['idtype_open_id']
        if 'idtype_user_id' in d:
            o.idtype_user_id = d['idtype_user_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_id_idtype' in d:
            o.user_id_idtype = d['user_id_idtype']
        return o


