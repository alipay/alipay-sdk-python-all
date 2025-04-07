#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *

from alipay.aop.api.domain.SignAreaRequest import SignAreaRequest
from alipay.aop.api.domain.SignAreaRequest import SignAreaRequest



class AlipayCommerceRentEnterpriseSealSignRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._biz_desc = None
        self._biz_name = None
        self._biz_no = None
        self._pre_auth_no = None
        self._sign_area_org = None
        self._sign_area_person = None
        self._signer_user_cert_number = None
        self._signer_user_name = None
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
    def biz_desc(self):
        return self._biz_desc

    @biz_desc.setter
    def biz_desc(self, value):
        self._biz_desc = value
    @property
    def biz_name(self):
        return self._biz_name

    @biz_name.setter
    def biz_name(self, value):
        self._biz_name = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def pre_auth_no(self):
        return self._pre_auth_no

    @pre_auth_no.setter
    def pre_auth_no(self, value):
        self._pre_auth_no = value
    @property
    def sign_area_org(self):
        return self._sign_area_org

    @sign_area_org.setter
    def sign_area_org(self, value):
        if isinstance(value, SignAreaRequest):
            self._sign_area_org = value
        else:
            self._sign_area_org = SignAreaRequest.from_alipay_dict(value)
    @property
    def sign_area_person(self):
        return self._sign_area_person

    @sign_area_person.setter
    def sign_area_person(self, value):
        if isinstance(value, SignAreaRequest):
            self._sign_area_person = value
        else:
            self._sign_area_person = SignAreaRequest.from_alipay_dict(value)
    @property
    def signer_user_cert_number(self):
        return self._signer_user_cert_number

    @signer_user_cert_number.setter
    def signer_user_cert_number(self, value):
        self._signer_user_cert_number = value
    @property
    def signer_user_name(self):
        return self._signer_user_name

    @signer_user_name.setter
    def signer_user_name(self, value):
        self._signer_user_name = value

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
        params[P_METHOD] = 'alipay.commerce.rent.enterprise.seal.sign'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.biz_desc:
            if hasattr(self.biz_desc, 'to_alipay_dict'):
                params['biz_desc'] = json.dumps(obj=self.biz_desc.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['biz_desc'] = self.biz_desc
        if self.biz_name:
            if hasattr(self.biz_name, 'to_alipay_dict'):
                params['biz_name'] = json.dumps(obj=self.biz_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['biz_name'] = self.biz_name
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = json.dumps(obj=self.biz_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['biz_no'] = self.biz_no
        if self.pre_auth_no:
            if hasattr(self.pre_auth_no, 'to_alipay_dict'):
                params['pre_auth_no'] = json.dumps(obj=self.pre_auth_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['pre_auth_no'] = self.pre_auth_no
        if self.sign_area_org:
            if hasattr(self.sign_area_org, 'to_alipay_dict'):
                params['sign_area_org'] = json.dumps(obj=self.sign_area_org.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['sign_area_org'] = self.sign_area_org
        if self.sign_area_person:
            if hasattr(self.sign_area_person, 'to_alipay_dict'):
                params['sign_area_person'] = json.dumps(obj=self.sign_area_person.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['sign_area_person'] = self.sign_area_person
        if self.signer_user_cert_number:
            if hasattr(self.signer_user_cert_number, 'to_alipay_dict'):
                params['signer_user_cert_number'] = json.dumps(obj=self.signer_user_cert_number.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['signer_user_cert_number'] = self.signer_user_cert_number
        if self.signer_user_name:
            if hasattr(self.signer_user_name, 'to_alipay_dict'):
                params['signer_user_name'] = json.dumps(obj=self.signer_user_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['signer_user_name'] = self.signer_user_name
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
