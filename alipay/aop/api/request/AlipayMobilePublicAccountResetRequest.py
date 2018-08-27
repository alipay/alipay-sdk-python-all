#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayMobilePublicAccountResetRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._agreement_id = None
        self._bind_account_no = None
        self._biz_content = None
        self._display_name = None
        self._from_user_id = None
        self._real_name = None
        self._version = "1.0"
        self._terminal_type = None
        self._terminal_info = None
        self._prod_code = None
        self._notify_url = None
        self._return_url = None
        self._udf_params = None
        self._need_encrypt = False

    @property
    def biz_model(self):
        return self._biz_model

    @biz_model.setter
    def biz_model(self, value):
        self._biz_model = value

    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def bind_account_no(self):
        return self._bind_account_no

    @bind_account_no.setter
    def bind_account_no(self, value):
        self._bind_account_no = value
    @property
    def biz_content(self):
        return self._biz_content

    @biz_content.setter
    def biz_content(self, value):
        self._biz_content = value
    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        self._display_name = value
    @property
    def from_user_id(self):
        return self._from_user_id

    @from_user_id.setter
    def from_user_id(self, value):
        self._from_user_id = value
    @property
    def real_name(self):
        return self._real_name

    @real_name.setter
    def real_name(self, value):
        self._real_name = value


    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value

    @property
    def terminal_type(self):
        return self._terminal_type

    @terminal_type.setter
    def terminal_type(self, value):
        self._terminal_type = value

    @property
    def terminal_info(self):
        return self._terminal_info

    @terminal_info.setter
    def terminal_info(self, value):
        self._terminal_info = value

    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value

    @property
    def notify_url(self):
        return self._notify_url

    @notify_url.setter
    def notify_url(self, value):
        self._notify_url = value

    @property
    def return_url(self):
        return self._return_url

    @return_url.setter
    def return_url(self, value):
        self._return_url = value

    @property
    def udf_params(self):
        return self._udf_params

    @udf_params.setter
    def udf_params(self, value):
        if not isinstance(value, dict):
            return
        self._udf_params = value

    @property
    def need_encrypt(self):
        return self._need_encrypt

    @need_encrypt.setter
    def need_encrypt(self, value):
        self._need_encrypt = value

    def add_other_text_param(self, key, value):
        if not self.udf_params:
            self.udf_params = dict()
        self.udf_params[key] = value

    def get_params(self):
        params = dict()
        params[P_METHOD] = 'alipay.mobile.public.account.reset'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.agreement_id:
            if hasattr(self.agreement_id, 'to_alipay_dict'):
                params['agreement_id'] = json.dumps(obj=self.agreement_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['agreement_id'] = self.agreement_id
        if self.bind_account_no:
            if hasattr(self.bind_account_no, 'to_alipay_dict'):
                params['bind_account_no'] = json.dumps(obj=self.bind_account_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['bind_account_no'] = self.bind_account_no
        if self.biz_content:
            if hasattr(self.biz_content, 'to_alipay_dict'):
                params['biz_content'] = json.dumps(obj=self.biz_content.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['biz_content'] = self.biz_content
        if self.display_name:
            if hasattr(self.display_name, 'to_alipay_dict'):
                params['display_name'] = json.dumps(obj=self.display_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['display_name'] = self.display_name
        if self.from_user_id:
            if hasattr(self.from_user_id, 'to_alipay_dict'):
                params['from_user_id'] = json.dumps(obj=self.from_user_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['from_user_id'] = self.from_user_id
        if self.real_name:
            if hasattr(self.real_name, 'to_alipay_dict'):
                params['real_name'] = json.dumps(obj=self.real_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['real_name'] = self.real_name
        if self.terminal_type:
            params['terminal_type'] = self.terminal_type
        if self.terminal_info:
            params['terminal_info'] = self.terminal_info
        if self.prod_code:
            params['prod_code'] = self.prod_code
        if self.notify_url:
            params['notify_url'] = self.notify_url
        if self.return_url:
            params['return_url'] = self.return_url
        if self.udf_params:
            params.update(self.udf_params)
        return params

    def get_multipart_params(self):
        multipart_params = dict()
        return multipart_params
