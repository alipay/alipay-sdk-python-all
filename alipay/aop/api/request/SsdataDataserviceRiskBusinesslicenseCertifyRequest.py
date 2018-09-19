#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class SsdataDataserviceRiskBusinesslicenseCertifyRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._address = None
        self._biz_id = None
        self._credit_code = None
        self._ent_legal_name = None
        self._ent_name = None
        self._expires = None
        self._expires_end = None
        self._expires_start = None
        self._ent_pros_pic = None
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
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def credit_code(self):
        return self._credit_code

    @credit_code.setter
    def credit_code(self, value):
        self._credit_code = value
    @property
    def ent_legal_name(self):
        return self._ent_legal_name

    @ent_legal_name.setter
    def ent_legal_name(self, value):
        self._ent_legal_name = value
    @property
    def ent_name(self):
        return self._ent_name

    @ent_name.setter
    def ent_name(self, value):
        self._ent_name = value
    @property
    def expires(self):
        return self._expires

    @expires.setter
    def expires(self, value):
        self._expires = value
    @property
    def expires_end(self):
        return self._expires_end

    @expires_end.setter
    def expires_end(self, value):
        self._expires_end = value
    @property
    def expires_start(self):
        return self._expires_start

    @expires_start.setter
    def expires_start(self, value):
        self._expires_start = value

    @property
    def ent_pros_pic(self):
        return self._ent_pros_pic

    @ent_pros_pic.setter
    def ent_pros_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._ent_pros_pic = value

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
        params[P_METHOD] = 'ssdata.dataservice.risk.businesslicense.certify'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = json.dumps(obj=self.address.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['address'] = self.address
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = json.dumps(obj=self.biz_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['biz_id'] = self.biz_id
        if self.credit_code:
            if hasattr(self.credit_code, 'to_alipay_dict'):
                params['credit_code'] = json.dumps(obj=self.credit_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['credit_code'] = self.credit_code
        if self.ent_legal_name:
            if hasattr(self.ent_legal_name, 'to_alipay_dict'):
                params['ent_legal_name'] = json.dumps(obj=self.ent_legal_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['ent_legal_name'] = self.ent_legal_name
        if self.ent_name:
            if hasattr(self.ent_name, 'to_alipay_dict'):
                params['ent_name'] = json.dumps(obj=self.ent_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['ent_name'] = self.ent_name
        if self.expires:
            if hasattr(self.expires, 'to_alipay_dict'):
                params['expires'] = json.dumps(obj=self.expires.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['expires'] = self.expires
        if self.expires_end:
            if hasattr(self.expires_end, 'to_alipay_dict'):
                params['expires_end'] = json.dumps(obj=self.expires_end.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['expires_end'] = self.expires_end
        if self.expires_start:
            if hasattr(self.expires_start, 'to_alipay_dict'):
                params['expires_start'] = json.dumps(obj=self.expires_start.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['expires_start'] = self.expires_start
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
        if self.ent_pros_pic:
            multipart_params['ent_pros_pic'] = self.ent_pros_pic
        return multipart_params
