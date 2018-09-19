#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayOpenPublicLifeCreateRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._contact_email = None
        self._contact_name = None
        self._contact_tel = None
        self._customer_tel = None
        self._description = None
        self._extend_data = None
        self._life_name = None
        self._mcc_code = None
        self._public_biz_type = None
        self._show_style = None
        self._user_id = None
        self._background = None
        self._logo = None
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
    def contact_email(self):
        return self._contact_email

    @contact_email.setter
    def contact_email(self, value):
        self._contact_email = value
    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def contact_tel(self):
        return self._contact_tel

    @contact_tel.setter
    def contact_tel(self, value):
        self._contact_tel = value
    @property
    def customer_tel(self):
        return self._customer_tel

    @customer_tel.setter
    def customer_tel(self, value):
        self._customer_tel = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def extend_data(self):
        return self._extend_data

    @extend_data.setter
    def extend_data(self, value):
        self._extend_data = value
    @property
    def life_name(self):
        return self._life_name

    @life_name.setter
    def life_name(self, value):
        self._life_name = value
    @property
    def mcc_code(self):
        return self._mcc_code

    @mcc_code.setter
    def mcc_code(self, value):
        self._mcc_code = value
    @property
    def public_biz_type(self):
        return self._public_biz_type

    @public_biz_type.setter
    def public_biz_type(self, value):
        self._public_biz_type = value
    @property
    def show_style(self):
        return self._show_style

    @show_style.setter
    def show_style(self, value):
        self._show_style = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, value):
        if not isinstance(value, FileItem):
            return
        self._background = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        if not isinstance(value, FileItem):
            return
        self._logo = value

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
        params[P_METHOD] = 'alipay.open.public.life.create'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.contact_email:
            if hasattr(self.contact_email, 'to_alipay_dict'):
                params['contact_email'] = json.dumps(obj=self.contact_email.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['contact_email'] = self.contact_email
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = json.dumps(obj=self.contact_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['contact_name'] = self.contact_name
        if self.contact_tel:
            if hasattr(self.contact_tel, 'to_alipay_dict'):
                params['contact_tel'] = json.dumps(obj=self.contact_tel.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['contact_tel'] = self.contact_tel
        if self.customer_tel:
            if hasattr(self.customer_tel, 'to_alipay_dict'):
                params['customer_tel'] = json.dumps(obj=self.customer_tel.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['customer_tel'] = self.customer_tel
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = json.dumps(obj=self.description.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['description'] = self.description
        if self.extend_data:
            if hasattr(self.extend_data, 'to_alipay_dict'):
                params['extend_data'] = json.dumps(obj=self.extend_data.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['extend_data'] = self.extend_data
        if self.life_name:
            if hasattr(self.life_name, 'to_alipay_dict'):
                params['life_name'] = json.dumps(obj=self.life_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['life_name'] = self.life_name
        if self.mcc_code:
            if hasattr(self.mcc_code, 'to_alipay_dict'):
                params['mcc_code'] = json.dumps(obj=self.mcc_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['mcc_code'] = self.mcc_code
        if self.public_biz_type:
            if hasattr(self.public_biz_type, 'to_alipay_dict'):
                params['public_biz_type'] = json.dumps(obj=self.public_biz_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['public_biz_type'] = self.public_biz_type
        if self.show_style:
            if hasattr(self.show_style, 'to_alipay_dict'):
                params['show_style'] = json.dumps(obj=self.show_style.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['show_style'] = self.show_style
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = json.dumps(obj=self.user_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['user_id'] = self.user_id
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
        if self.background:
            multipart_params['background'] = self.background
        if self.logo:
            multipart_params['logo'] = self.logo
        return multipart_params
