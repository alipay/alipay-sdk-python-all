#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IdTypeUserDetail import IdTypeUserDetail
from alipay.aop.api.domain.IdTypeUserDetail import IdTypeUserDetail


class AlipayOpenAppIdtypetestallOpenidbizmockQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppIdtypetestallOpenidbizmockQueryResponse, self).__init__()
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
        self._zone_name = None
        self._zone_type = None

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
    @property
    def zone_name(self):
        return self._zone_name

    @zone_name.setter
    def zone_name(self, value):
        self._zone_name = value
    @property
    def zone_type(self):
        return self._zone_type

    @zone_type.setter
    def zone_type(self, value):
        self._zone_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppIdtypetestallOpenidbizmockQueryResponse, self).parse_response_content(response_content)
        if 'id_type' in response:
            self.id_type = response['id_type']
        if 'id_type_list' in response:
            self.id_type_list = response['id_type_list']
        if 'list_id_type' in response:
            self.list_id_type = response['list_id_type']
        if 'list_open_id' in response:
            self.list_open_id = response['list_open_id']
        if 'list_user_id' in response:
            self.list_user_id = response['list_user_id']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'open_id_list' in response:
            self.open_id_list = response['open_id_list']
        if 'user_detail' in response:
            self.user_detail = response['user_detail']
        if 'user_detail_list' in response:
            self.user_detail_list = response['user_detail_list']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'user_id_list' in response:
            self.user_id_list = response['user_id_list']
        if 'zone_name' in response:
            self.zone_name = response['zone_name']
        if 'zone_type' in response:
            self.zone_type = response['zone_type']
