#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IdTypeTestComplexParam import IdTypeTestComplexParam
from alipay.aop.api.domain.IdTypeTestComplexParam import IdTypeTestComplexParam


class AlipayOpenAppIdtypetestallOpenidbizmockBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppIdtypetestallOpenidbizmockBatchqueryResponse, self).__init__()
        self._id_type = None
        self._id_type_list = None
        self._id_type_test_complex_param = None
        self._id_type_test_complex_param_list = None
        self._open_id = None
        self._open_id_list = None
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
    def id_type_test_complex_param(self):
        return self._id_type_test_complex_param

    @id_type_test_complex_param.setter
    def id_type_test_complex_param(self, value):
        if isinstance(value, IdTypeTestComplexParam):
            self._id_type_test_complex_param = value
        else:
            self._id_type_test_complex_param = IdTypeTestComplexParam.from_alipay_dict(value)
    @property
    def id_type_test_complex_param_list(self):
        return self._id_type_test_complex_param_list

    @id_type_test_complex_param_list.setter
    def id_type_test_complex_param_list(self, value):
        if isinstance(value, list):
            self._id_type_test_complex_param_list = list()
            for i in value:
                if isinstance(i, IdTypeTestComplexParam):
                    self._id_type_test_complex_param_list.append(i)
                else:
                    self._id_type_test_complex_param_list.append(IdTypeTestComplexParam.from_alipay_dict(i))
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
        response = super(AlipayOpenAppIdtypetestallOpenidbizmockBatchqueryResponse, self).parse_response_content(response_content)
        if 'id_type' in response:
            self.id_type = response['id_type']
        if 'id_type_list' in response:
            self.id_type_list = response['id_type_list']
        if 'id_type_test_complex_param' in response:
            self.id_type_test_complex_param = response['id_type_test_complex_param']
        if 'id_type_test_complex_param_list' in response:
            self.id_type_test_complex_param_list = response['id_type_test_complex_param_list']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'open_id_list' in response:
            self.open_id_list = response['open_id_list']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'user_id_list' in response:
            self.user_id_list = response['user_id_list']
        if 'zone_name' in response:
            self.zone_name = response['zone_name']
        if 'zone_type' in response:
            self.zone_type = response['zone_type']
