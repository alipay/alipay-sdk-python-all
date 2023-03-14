#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IdTypeUserDetail(object):

    def __init__(self):
        self._expect_id_type_1 = None
        self._expect_id_type_2 = None
        self._expect_id_type_3 = None
        self._expect_list_string_open_id = None
        self._expect_list_string_user_id = None
        self._expect_open_id = None
        self._expect_open_id_list = None
        self._expect_user_id = None
        self._expect_user_id_list = None
        self._id_type_1 = None
        self._id_type_2 = None
        self._id_type_3 = None
        self._list_string_open_id = None
        self._list_string_user_id = None
        self._open_id = None
        self._open_id_list = None
        self._user_id = None
        self._user_id_list = None

    @property
    def expect_id_type_1(self):
        return self._expect_id_type_1

    @expect_id_type_1.setter
    def expect_id_type_1(self, value):
        self._expect_id_type_1 = value
    @property
    def expect_id_type_2(self):
        return self._expect_id_type_2

    @expect_id_type_2.setter
    def expect_id_type_2(self, value):
        self._expect_id_type_2 = value
    @property
    def expect_id_type_3(self):
        return self._expect_id_type_3

    @expect_id_type_3.setter
    def expect_id_type_3(self, value):
        self._expect_id_type_3 = value
    @property
    def expect_list_string_open_id(self):
        return self._expect_list_string_open_id

    @expect_list_string_open_id.setter
    def expect_list_string_open_id(self, value):
        self._expect_list_string_open_id = value
    @property
    def expect_list_string_user_id(self):
        return self._expect_list_string_user_id

    @expect_list_string_user_id.setter
    def expect_list_string_user_id(self, value):
        self._expect_list_string_user_id = value
    @property
    def expect_open_id(self):
        return self._expect_open_id

    @expect_open_id.setter
    def expect_open_id(self, value):
        self._expect_open_id = value
    @property
    def expect_open_id_list(self):
        return self._expect_open_id_list

    @expect_open_id_list.setter
    def expect_open_id_list(self, value):
        if isinstance(value, list):
            self._expect_open_id_list = list()
            for i in value:
                self._expect_open_id_list.append(i)
    @property
    def expect_user_id(self):
        return self._expect_user_id

    @expect_user_id.setter
    def expect_user_id(self, value):
        self._expect_user_id = value
    @property
    def expect_user_id_list(self):
        return self._expect_user_id_list

    @expect_user_id_list.setter
    def expect_user_id_list(self, value):
        if isinstance(value, list):
            self._expect_user_id_list = list()
            for i in value:
                self._expect_user_id_list.append(i)
    @property
    def id_type_1(self):
        return self._id_type_1

    @id_type_1.setter
    def id_type_1(self, value):
        self._id_type_1 = value
    @property
    def id_type_2(self):
        return self._id_type_2

    @id_type_2.setter
    def id_type_2(self, value):
        self._id_type_2 = value
    @property
    def id_type_3(self):
        return self._id_type_3

    @id_type_3.setter
    def id_type_3(self, value):
        self._id_type_3 = value
    @property
    def list_string_open_id(self):
        return self._list_string_open_id

    @list_string_open_id.setter
    def list_string_open_id(self, value):
        self._list_string_open_id = value
    @property
    def list_string_user_id(self):
        return self._list_string_user_id

    @list_string_user_id.setter
    def list_string_user_id(self, value):
        self._list_string_user_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def open_id_list(self):
        return self._open_id_list

    @open_id_list.setter
    def open_id_list(self, value):
        if isinstance(value, list):
            self._open_id_list = list()
            for i in value:
                self._open_id_list.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_id_list(self):
        return self._user_id_list

    @user_id_list.setter
    def user_id_list(self, value):
        if isinstance(value, list):
            self._user_id_list = list()
            for i in value:
                self._user_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.expect_id_type_1:
            if hasattr(self.expect_id_type_1, 'to_alipay_dict'):
                params['expect_id_type_1'] = self.expect_id_type_1.to_alipay_dict()
            else:
                params['expect_id_type_1'] = self.expect_id_type_1
        if self.expect_id_type_2:
            if hasattr(self.expect_id_type_2, 'to_alipay_dict'):
                params['expect_id_type_2'] = self.expect_id_type_2.to_alipay_dict()
            else:
                params['expect_id_type_2'] = self.expect_id_type_2
        if self.expect_id_type_3:
            if hasattr(self.expect_id_type_3, 'to_alipay_dict'):
                params['expect_id_type_3'] = self.expect_id_type_3.to_alipay_dict()
            else:
                params['expect_id_type_3'] = self.expect_id_type_3
        if self.expect_list_string_open_id:
            if hasattr(self.expect_list_string_open_id, 'to_alipay_dict'):
                params['expect_list_string_open_id'] = self.expect_list_string_open_id.to_alipay_dict()
            else:
                params['expect_list_string_open_id'] = self.expect_list_string_open_id
        if self.expect_list_string_user_id:
            if hasattr(self.expect_list_string_user_id, 'to_alipay_dict'):
                params['expect_list_string_user_id'] = self.expect_list_string_user_id.to_alipay_dict()
            else:
                params['expect_list_string_user_id'] = self.expect_list_string_user_id
        if self.expect_open_id:
            if hasattr(self.expect_open_id, 'to_alipay_dict'):
                params['expect_open_id'] = self.expect_open_id.to_alipay_dict()
            else:
                params['expect_open_id'] = self.expect_open_id
        if self.expect_open_id_list:
            if isinstance(self.expect_open_id_list, list):
                for i in range(0, len(self.expect_open_id_list)):
                    element = self.expect_open_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.expect_open_id_list[i] = element.to_alipay_dict()
            if hasattr(self.expect_open_id_list, 'to_alipay_dict'):
                params['expect_open_id_list'] = self.expect_open_id_list.to_alipay_dict()
            else:
                params['expect_open_id_list'] = self.expect_open_id_list
        if self.expect_user_id:
            if hasattr(self.expect_user_id, 'to_alipay_dict'):
                params['expect_user_id'] = self.expect_user_id.to_alipay_dict()
            else:
                params['expect_user_id'] = self.expect_user_id
        if self.expect_user_id_list:
            if isinstance(self.expect_user_id_list, list):
                for i in range(0, len(self.expect_user_id_list)):
                    element = self.expect_user_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.expect_user_id_list[i] = element.to_alipay_dict()
            if hasattr(self.expect_user_id_list, 'to_alipay_dict'):
                params['expect_user_id_list'] = self.expect_user_id_list.to_alipay_dict()
            else:
                params['expect_user_id_list'] = self.expect_user_id_list
        if self.id_type_1:
            if hasattr(self.id_type_1, 'to_alipay_dict'):
                params['id_type_1'] = self.id_type_1.to_alipay_dict()
            else:
                params['id_type_1'] = self.id_type_1
        if self.id_type_2:
            if hasattr(self.id_type_2, 'to_alipay_dict'):
                params['id_type_2'] = self.id_type_2.to_alipay_dict()
            else:
                params['id_type_2'] = self.id_type_2
        if self.id_type_3:
            if hasattr(self.id_type_3, 'to_alipay_dict'):
                params['id_type_3'] = self.id_type_3.to_alipay_dict()
            else:
                params['id_type_3'] = self.id_type_3
        if self.list_string_open_id:
            if hasattr(self.list_string_open_id, 'to_alipay_dict'):
                params['list_string_open_id'] = self.list_string_open_id.to_alipay_dict()
            else:
                params['list_string_open_id'] = self.list_string_open_id
        if self.list_string_user_id:
            if hasattr(self.list_string_user_id, 'to_alipay_dict'):
                params['list_string_user_id'] = self.list_string_user_id.to_alipay_dict()
            else:
                params['list_string_user_id'] = self.list_string_user_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.open_id_list:
            if isinstance(self.open_id_list, list):
                for i in range(0, len(self.open_id_list)):
                    element = self.open_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.open_id_list[i] = element.to_alipay_dict()
            if hasattr(self.open_id_list, 'to_alipay_dict'):
                params['open_id_list'] = self.open_id_list.to_alipay_dict()
            else:
                params['open_id_list'] = self.open_id_list
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_id_list:
            if isinstance(self.user_id_list, list):
                for i in range(0, len(self.user_id_list)):
                    element = self.user_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_id_list[i] = element.to_alipay_dict()
            if hasattr(self.user_id_list, 'to_alipay_dict'):
                params['user_id_list'] = self.user_id_list.to_alipay_dict()
            else:
                params['user_id_list'] = self.user_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IdTypeUserDetail()
        if 'expect_id_type_1' in d:
            o.expect_id_type_1 = d['expect_id_type_1']
        if 'expect_id_type_2' in d:
            o.expect_id_type_2 = d['expect_id_type_2']
        if 'expect_id_type_3' in d:
            o.expect_id_type_3 = d['expect_id_type_3']
        if 'expect_list_string_open_id' in d:
            o.expect_list_string_open_id = d['expect_list_string_open_id']
        if 'expect_list_string_user_id' in d:
            o.expect_list_string_user_id = d['expect_list_string_user_id']
        if 'expect_open_id' in d:
            o.expect_open_id = d['expect_open_id']
        if 'expect_open_id_list' in d:
            o.expect_open_id_list = d['expect_open_id_list']
        if 'expect_user_id' in d:
            o.expect_user_id = d['expect_user_id']
        if 'expect_user_id_list' in d:
            o.expect_user_id_list = d['expect_user_id_list']
        if 'id_type_1' in d:
            o.id_type_1 = d['id_type_1']
        if 'id_type_2' in d:
            o.id_type_2 = d['id_type_2']
        if 'id_type_3' in d:
            o.id_type_3 = d['id_type_3']
        if 'list_string_open_id' in d:
            o.list_string_open_id = d['list_string_open_id']
        if 'list_string_user_id' in d:
            o.list_string_user_id = d['list_string_user_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'open_id_list' in d:
            o.open_id_list = d['open_id_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_id_list' in d:
            o.user_id_list = d['user_id_list']
        return o


