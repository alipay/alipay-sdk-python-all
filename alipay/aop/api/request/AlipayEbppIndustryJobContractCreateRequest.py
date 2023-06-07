#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *

from alipay.aop.api.domain.ContractCompanyInfo import ContractCompanyInfo
from alipay.aop.api.domain.ContractUserInfo import ContractUserInfo



class AlipayEbppIndustryJobContractCreateRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._company_list = None
        self._failure_redirect_url = None
        self._notice_url = None
        self._outer_biz_no = None
        self._redirect_url = None
        self._sign_platform = None
        self._user_list = None
        self._file_content = None
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
    def company_list(self):
        return self._company_list

    @company_list.setter
    def company_list(self, value):
        if isinstance(value, list):
            self._company_list = list()
            for i in value:
                if isinstance(i, ContractCompanyInfo):
                    self._company_list.append(i)
                else:
                    self._company_list.append(ContractCompanyInfo.from_alipay_dict(i))
    @property
    def failure_redirect_url(self):
        return self._failure_redirect_url

    @failure_redirect_url.setter
    def failure_redirect_url(self, value):
        self._failure_redirect_url = value
    @property
    def notice_url(self):
        return self._notice_url

    @notice_url.setter
    def notice_url(self, value):
        self._notice_url = value
    @property
    def outer_biz_no(self):
        return self._outer_biz_no

    @outer_biz_no.setter
    def outer_biz_no(self, value):
        self._outer_biz_no = value
    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value
    @property
    def sign_platform(self):
        return self._sign_platform

    @sign_platform.setter
    def sign_platform(self, value):
        self._sign_platform = value
    @property
    def user_list(self):
        return self._user_list

    @user_list.setter
    def user_list(self, value):
        if isinstance(value, list):
            self._user_list = list()
            for i in value:
                if isinstance(i, ContractUserInfo):
                    self._user_list.append(i)
                else:
                    self._user_list.append(ContractUserInfo.from_alipay_dict(i))

    @property
    def file_content(self):
        return self._file_content

    @file_content.setter
    def file_content(self, value):
        if not isinstance(value, FileItem):
            return
        self._file_content = value

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
        params[P_METHOD] = 'alipay.ebpp.industry.job.contract.create'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.company_list:
            if isinstance(self.company_list, list):
                for i in range(0, len(self.company_list)):
                    element = self.company_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.company_list[i] = element.to_alipay_dict()
                params['company_list'] = json.dumps(obj=self.company_list, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.failure_redirect_url:
            if hasattr(self.failure_redirect_url, 'to_alipay_dict'):
                params['failure_redirect_url'] = json.dumps(obj=self.failure_redirect_url.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['failure_redirect_url'] = self.failure_redirect_url
        if self.notice_url:
            if hasattr(self.notice_url, 'to_alipay_dict'):
                params['notice_url'] = json.dumps(obj=self.notice_url.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['notice_url'] = self.notice_url
        if self.outer_biz_no:
            if hasattr(self.outer_biz_no, 'to_alipay_dict'):
                params['outer_biz_no'] = json.dumps(obj=self.outer_biz_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['outer_biz_no'] = self.outer_biz_no
        if self.redirect_url:
            if hasattr(self.redirect_url, 'to_alipay_dict'):
                params['redirect_url'] = json.dumps(obj=self.redirect_url.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['redirect_url'] = self.redirect_url
        if self.sign_platform:
            if hasattr(self.sign_platform, 'to_alipay_dict'):
                params['sign_platform'] = json.dumps(obj=self.sign_platform.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['sign_platform'] = self.sign_platform
        if self.user_list:
            if isinstance(self.user_list, list):
                for i in range(0, len(self.user_list)):
                    element = self.user_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_list[i] = element.to_alipay_dict()
                params['user_list'] = json.dumps(obj=self.user_list, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
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
        if self.file_content:
            multipart_params['file_content'] = self.file_content
        return multipart_params
