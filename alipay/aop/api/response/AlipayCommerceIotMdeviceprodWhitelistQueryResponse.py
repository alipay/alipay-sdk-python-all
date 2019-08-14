#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotMdeviceprodWhitelistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotMdeviceprodWhitelistQueryResponse, self).__init__()
        self._app_project_id = None
        self._app_white_list_status = None
        self._effective_time = None
        self._expire_time = None
        self._ext_info = None
        self._gmt_create = None
        self._gmt_modified = None
        self._group_type = None
        self._group_value = None
        self._remark = None
        self._user_identify_type = None
        self._user_identify_value = None

    @property
    def app_project_id(self):
        return self._app_project_id

    @app_project_id.setter
    def app_project_id(self, value):
        self._app_project_id = value
    @property
    def app_white_list_status(self):
        return self._app_white_list_status

    @app_white_list_status.setter
    def app_white_list_status(self, value):
        self._app_white_list_status = value
    @property
    def effective_time(self):
        return self._effective_time

    @effective_time.setter
    def effective_time(self, value):
        self._effective_time = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def group_type(self):
        return self._group_type

    @group_type.setter
    def group_type(self, value):
        self._group_type = value
    @property
    def group_value(self):
        return self._group_value

    @group_value.setter
    def group_value(self, value):
        self._group_value = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def user_identify_type(self):
        return self._user_identify_type

    @user_identify_type.setter
    def user_identify_type(self, value):
        self._user_identify_type = value
    @property
    def user_identify_value(self):
        return self._user_identify_value

    @user_identify_value.setter
    def user_identify_value(self, value):
        self._user_identify_value = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotMdeviceprodWhitelistQueryResponse, self).parse_response_content(response_content)
        if 'app_project_id' in response:
            self.app_project_id = response['app_project_id']
        if 'app_white_list_status' in response:
            self.app_white_list_status = response['app_white_list_status']
        if 'effective_time' in response:
            self.effective_time = response['effective_time']
        if 'expire_time' in response:
            self.expire_time = response['expire_time']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'group_type' in response:
            self.group_type = response['group_type']
        if 'group_value' in response:
            self.group_value = response['group_value']
        if 'remark' in response:
            self.remark = response['remark']
        if 'user_identify_type' in response:
            self.user_identify_type = response['user_identify_type']
        if 'user_identify_value' in response:
            self.user_identify_value = response['user_identify_value']
