#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HeaderParam import HeaderParam


class AlipayOpenSpMcpInfoModifyModel(object):

    def __init__(self):
        self._ability_code = None
        self._api_key = None
        self._encrypt_app_id = None
        self._header_list = None
        self._mcp_chinese_name = None
        self._mcp_desc = None
        self._mcp_icon_pic = None
        self._mcp_server_url = None
        self._parameter_name = None
        self._request_timeout = None
        self._response_timeout = None
        self._support_account_type = None
        self._support_protocols = None

    @property
    def ability_code(self):
        return self._ability_code

    @ability_code.setter
    def ability_code(self, value):
        self._ability_code = value
    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, value):
        self._api_key = value
    @property
    def encrypt_app_id(self):
        return self._encrypt_app_id

    @encrypt_app_id.setter
    def encrypt_app_id(self, value):
        self._encrypt_app_id = value
    @property
    def header_list(self):
        return self._header_list

    @header_list.setter
    def header_list(self, value):
        if isinstance(value, list):
            self._header_list = list()
            for i in value:
                if isinstance(i, HeaderParam):
                    self._header_list.append(i)
                else:
                    self._header_list.append(HeaderParam.from_alipay_dict(i))
    @property
    def mcp_chinese_name(self):
        return self._mcp_chinese_name

    @mcp_chinese_name.setter
    def mcp_chinese_name(self, value):
        self._mcp_chinese_name = value
    @property
    def mcp_desc(self):
        return self._mcp_desc

    @mcp_desc.setter
    def mcp_desc(self, value):
        self._mcp_desc = value
    @property
    def mcp_icon_pic(self):
        return self._mcp_icon_pic

    @mcp_icon_pic.setter
    def mcp_icon_pic(self, value):
        self._mcp_icon_pic = value
    @property
    def mcp_server_url(self):
        return self._mcp_server_url

    @mcp_server_url.setter
    def mcp_server_url(self, value):
        self._mcp_server_url = value
    @property
    def parameter_name(self):
        return self._parameter_name

    @parameter_name.setter
    def parameter_name(self, value):
        self._parameter_name = value
    @property
    def request_timeout(self):
        return self._request_timeout

    @request_timeout.setter
    def request_timeout(self, value):
        self._request_timeout = value
    @property
    def response_timeout(self):
        return self._response_timeout

    @response_timeout.setter
    def response_timeout(self, value):
        self._response_timeout = value
    @property
    def support_account_type(self):
        return self._support_account_type

    @support_account_type.setter
    def support_account_type(self, value):
        if isinstance(value, list):
            self._support_account_type = list()
            for i in value:
                self._support_account_type.append(i)
    @property
    def support_protocols(self):
        return self._support_protocols

    @support_protocols.setter
    def support_protocols(self, value):
        self._support_protocols = value


    def to_alipay_dict(self):
        params = dict()
        if self.ability_code:
            if hasattr(self.ability_code, 'to_alipay_dict'):
                params['ability_code'] = self.ability_code.to_alipay_dict()
            else:
                params['ability_code'] = self.ability_code
        if self.api_key:
            if hasattr(self.api_key, 'to_alipay_dict'):
                params['api_key'] = self.api_key.to_alipay_dict()
            else:
                params['api_key'] = self.api_key
        if self.encrypt_app_id:
            if hasattr(self.encrypt_app_id, 'to_alipay_dict'):
                params['encrypt_app_id'] = self.encrypt_app_id.to_alipay_dict()
            else:
                params['encrypt_app_id'] = self.encrypt_app_id
        if self.header_list:
            if isinstance(self.header_list, list):
                for i in range(0, len(self.header_list)):
                    element = self.header_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.header_list[i] = element.to_alipay_dict()
            if hasattr(self.header_list, 'to_alipay_dict'):
                params['header_list'] = self.header_list.to_alipay_dict()
            else:
                params['header_list'] = self.header_list
        if self.mcp_chinese_name:
            if hasattr(self.mcp_chinese_name, 'to_alipay_dict'):
                params['mcp_chinese_name'] = self.mcp_chinese_name.to_alipay_dict()
            else:
                params['mcp_chinese_name'] = self.mcp_chinese_name
        if self.mcp_desc:
            if hasattr(self.mcp_desc, 'to_alipay_dict'):
                params['mcp_desc'] = self.mcp_desc.to_alipay_dict()
            else:
                params['mcp_desc'] = self.mcp_desc
        if self.mcp_icon_pic:
            if hasattr(self.mcp_icon_pic, 'to_alipay_dict'):
                params['mcp_icon_pic'] = self.mcp_icon_pic.to_alipay_dict()
            else:
                params['mcp_icon_pic'] = self.mcp_icon_pic
        if self.mcp_server_url:
            if hasattr(self.mcp_server_url, 'to_alipay_dict'):
                params['mcp_server_url'] = self.mcp_server_url.to_alipay_dict()
            else:
                params['mcp_server_url'] = self.mcp_server_url
        if self.parameter_name:
            if hasattr(self.parameter_name, 'to_alipay_dict'):
                params['parameter_name'] = self.parameter_name.to_alipay_dict()
            else:
                params['parameter_name'] = self.parameter_name
        if self.request_timeout:
            if hasattr(self.request_timeout, 'to_alipay_dict'):
                params['request_timeout'] = self.request_timeout.to_alipay_dict()
            else:
                params['request_timeout'] = self.request_timeout
        if self.response_timeout:
            if hasattr(self.response_timeout, 'to_alipay_dict'):
                params['response_timeout'] = self.response_timeout.to_alipay_dict()
            else:
                params['response_timeout'] = self.response_timeout
        if self.support_account_type:
            if isinstance(self.support_account_type, list):
                for i in range(0, len(self.support_account_type)):
                    element = self.support_account_type[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.support_account_type[i] = element.to_alipay_dict()
            if hasattr(self.support_account_type, 'to_alipay_dict'):
                params['support_account_type'] = self.support_account_type.to_alipay_dict()
            else:
                params['support_account_type'] = self.support_account_type
        if self.support_protocols:
            if hasattr(self.support_protocols, 'to_alipay_dict'):
                params['support_protocols'] = self.support_protocols.to_alipay_dict()
            else:
                params['support_protocols'] = self.support_protocols
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpMcpInfoModifyModel()
        if 'ability_code' in d:
            o.ability_code = d['ability_code']
        if 'api_key' in d:
            o.api_key = d['api_key']
        if 'encrypt_app_id' in d:
            o.encrypt_app_id = d['encrypt_app_id']
        if 'header_list' in d:
            o.header_list = d['header_list']
        if 'mcp_chinese_name' in d:
            o.mcp_chinese_name = d['mcp_chinese_name']
        if 'mcp_desc' in d:
            o.mcp_desc = d['mcp_desc']
        if 'mcp_icon_pic' in d:
            o.mcp_icon_pic = d['mcp_icon_pic']
        if 'mcp_server_url' in d:
            o.mcp_server_url = d['mcp_server_url']
        if 'parameter_name' in d:
            o.parameter_name = d['parameter_name']
        if 'request_timeout' in d:
            o.request_timeout = d['request_timeout']
        if 'response_timeout' in d:
            o.response_timeout = d['response_timeout']
        if 'support_account_type' in d:
            o.support_account_type = d['support_account_type']
        if 'support_protocols' in d:
            o.support_protocols = d['support_protocols']
        return o


