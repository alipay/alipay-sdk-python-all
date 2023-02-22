#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IdTypeUserDetail import IdTypeUserDetail
from alipay.aop.api.domain.IdTypeUserDetail import IdTypeUserDetail


class AlipayOpenAppIdtypetestallOpenidbizmockQueryModel(object):

    def __init__(self):
        self._id_type = None
        self._id_type_list = None
        self._list_id_type = None
        self._list_open_id = None
        self._list_user_id = None
        self._open_id = None
        self._open_id_list = None
        self._user_detail = None
        self._user_detail_list = None
        self._user_id = None
        self._user_id_list = None

    @property
    def id_type(self):
        return self._id_type

    @id_type.setter
    def id_type(self, value):
        self._id_type = value
    @property
    def id_type_list(self):
        return self._id_type_list

    @id_type_list.setter
    def id_type_list(self, value):
        self._id_type_list = value
    @property
    def list_id_type(self):
        return self._list_id_type

    @list_id_type.setter
    def list_id_type(self, value):
        self._list_id_type = value
    @property
    def list_open_id(self):
        return self._list_open_id

    @list_open_id.setter
    def list_open_id(self, value):
        self._list_open_id = value
    @property
    def list_user_id(self):
        return self._list_user_id

    @list_user_id.setter
    def list_user_id(self, value):
        self._list_user_id = value
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
    def user_detail(self):
        return self._user_detail

    @user_detail.setter
    def user_detail(self, value):
        if isinstance(value, IdTypeUserDetail):
            self._user_detail = value
        else:
            self._user_detail = IdTypeUserDetail.from_alipay_dict(value)
    @property
    def user_detail_list(self):
        return self._user_detail_list

    @user_detail_list.setter
    def user_detail_list(self, value):
        if isinstance(value, list):
            self._user_detail_list = list()
            for i in value:
                if isinstance(i, IdTypeUserDetail):
                    self._user_detail_list.append(i)
                else:
                    self._user_detail_list.append(IdTypeUserDetail.from_alipay_dict(i))
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
        if self.id_type:
            if hasattr(self.id_type, 'to_alipay_dict'):
                params['id_type'] = self.id_type.to_alipay_dict()
            else:
                params['id_type'] = self.id_type
        if self.id_type_list:
            if hasattr(self.id_type_list, 'to_alipay_dict'):
                params['id_type_list'] = self.id_type_list.to_alipay_dict()
            else:
                params['id_type_list'] = self.id_type_list
        if self.list_id_type:
            if hasattr(self.list_id_type, 'to_alipay_dict'):
                params['list_id_type'] = self.list_id_type.to_alipay_dict()
            else:
                params['list_id_type'] = self.list_id_type
        if self.list_open_id:
            if hasattr(self.list_open_id, 'to_alipay_dict'):
                params['list_open_id'] = self.list_open_id.to_alipay_dict()
            else:
                params['list_open_id'] = self.list_open_id
        if self.list_user_id:
            if hasattr(self.list_user_id, 'to_alipay_dict'):
                params['list_user_id'] = self.list_user_id.to_alipay_dict()
            else:
                params['list_user_id'] = self.list_user_id
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
        if self.user_detail:
            if hasattr(self.user_detail, 'to_alipay_dict'):
                params['user_detail'] = self.user_detail.to_alipay_dict()
            else:
                params['user_detail'] = self.user_detail
        if self.user_detail_list:
            if isinstance(self.user_detail_list, list):
                for i in range(0, len(self.user_detail_list)):
                    element = self.user_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.user_detail_list, 'to_alipay_dict'):
                params['user_detail_list'] = self.user_detail_list.to_alipay_dict()
            else:
                params['user_detail_list'] = self.user_detail_list
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
        o = AlipayOpenAppIdtypetestallOpenidbizmockQueryModel()
        if 'id_type' in d:
            o.id_type = d['id_type']
        if 'id_type_list' in d:
            o.id_type_list = d['id_type_list']
        if 'list_id_type' in d:
            o.list_id_type = d['list_id_type']
        if 'list_open_id' in d:
            o.list_open_id = d['list_open_id']
        if 'list_user_id' in d:
            o.list_user_id = d['list_user_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'open_id_list' in d:
            o.open_id_list = d['open_id_list']
        if 'user_detail' in d:
            o.user_detail = d['user_detail']
        if 'user_detail_list' in d:
            o.user_detail_list = d['user_detail_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_id_list' in d:
            o.user_id_list = d['user_id_list']
        return o


