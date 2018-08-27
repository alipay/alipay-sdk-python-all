#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayEcapiprodCreditGetRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._credit_no = None
        self._entity_code = None
        self._entity_name = None
        self._isv_code = None
        self._org_code = None
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
    def credit_no(self):
        return self._credit_no

    @credit_no.setter
    def credit_no(self, value):
        self._credit_no = value
    @property
    def entity_code(self):
        return self._entity_code

    @entity_code.setter
    def entity_code(self, value):
        self._entity_code = value
    @property
    def entity_name(self):
        return self._entity_name

    @entity_name.setter
    def entity_name(self, value):
        self._entity_name = value
    @property
    def isv_code(self):
        return self._isv_code

    @isv_code.setter
    def isv_code(self, value):
        self._isv_code = value
    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value


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
        params[P_METHOD] = 'alipay.ecapiprod.credit.get'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.credit_no:
            if hasattr(self.credit_no, 'to_alipay_dict'):
                params['credit_no'] = json.dumps(obj=self.credit_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['credit_no'] = self.credit_no
        if self.entity_code:
            if hasattr(self.entity_code, 'to_alipay_dict'):
                params['entity_code'] = json.dumps(obj=self.entity_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['entity_code'] = self.entity_code
        if self.entity_name:
            if hasattr(self.entity_name, 'to_alipay_dict'):
                params['entity_name'] = json.dumps(obj=self.entity_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['entity_name'] = self.entity_name
        if self.isv_code:
            if hasattr(self.isv_code, 'to_alipay_dict'):
                params['isv_code'] = json.dumps(obj=self.isv_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['isv_code'] = self.isv_code
        if self.org_code:
            if hasattr(self.org_code, 'to_alipay_dict'):
                params['org_code'] = json.dumps(obj=self.org_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['org_code'] = self.org_code
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
