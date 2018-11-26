#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipaySecurityProdAfsrcVulCreateRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._business = None
        self._company = None
        self._detail = None
        self._hid = None
        self._level = None
        self._mobile_phone = None
        self._name = None
        self._nick = None
        self._status = None
        self._submit_time = None
        self._type_sub_first_id = None
        self._type_sub_first_name = None
        self._type_sub_second_id = None
        self._type_sub_second_name = None
        self._type_union_first_id = None
        self._type_union_second_id = None
        self._url = None
        self._user_id = None
        self._attachment = None
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
    def business(self):
        return self._business

    @business.setter
    def business(self, value):
        self._business = value
    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        self._company = value
    @property
    def detail(self):
        return self._detail

    @detail.setter
    def detail(self, value):
        self._detail = value
    @property
    def hid(self):
        return self._hid

    @hid.setter
    def hid(self, value):
        self._hid = value
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def mobile_phone(self):
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, value):
        self._mobile_phone = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def nick(self):
        return self._nick

    @nick.setter
    def nick(self, value):
        self._nick = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def submit_time(self):
        return self._submit_time

    @submit_time.setter
    def submit_time(self, value):
        self._submit_time = value
    @property
    def type_sub_first_id(self):
        return self._type_sub_first_id

    @type_sub_first_id.setter
    def type_sub_first_id(self, value):
        self._type_sub_first_id = value
    @property
    def type_sub_first_name(self):
        return self._type_sub_first_name

    @type_sub_first_name.setter
    def type_sub_first_name(self, value):
        self._type_sub_first_name = value
    @property
    def type_sub_second_id(self):
        return self._type_sub_second_id

    @type_sub_second_id.setter
    def type_sub_second_id(self, value):
        self._type_sub_second_id = value
    @property
    def type_sub_second_name(self):
        return self._type_sub_second_name

    @type_sub_second_name.setter
    def type_sub_second_name(self, value):
        self._type_sub_second_name = value
    @property
    def type_union_first_id(self):
        return self._type_union_first_id

    @type_union_first_id.setter
    def type_union_first_id(self, value):
        self._type_union_first_id = value
    @property
    def type_union_second_id(self):
        return self._type_union_second_id

    @type_union_second_id.setter
    def type_union_second_id(self, value):
        self._type_union_second_id = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def attachment(self):
        return self._attachment

    @attachment.setter
    def attachment(self, value):
        if not isinstance(value, FileItem):
            return
        self._attachment = value

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
        params[P_METHOD] = 'alipay.security.prod.afsrc.vul.create'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.business:
            if hasattr(self.business, 'to_alipay_dict'):
                params['business'] = json.dumps(obj=self.business.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['business'] = self.business
        if self.company:
            if hasattr(self.company, 'to_alipay_dict'):
                params['company'] = json.dumps(obj=self.company.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['company'] = self.company
        if self.detail:
            if hasattr(self.detail, 'to_alipay_dict'):
                params['detail'] = json.dumps(obj=self.detail.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['detail'] = self.detail
        if self.hid:
            if hasattr(self.hid, 'to_alipay_dict'):
                params['hid'] = json.dumps(obj=self.hid.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['hid'] = self.hid
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = json.dumps(obj=self.level.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['level'] = self.level
        if self.mobile_phone:
            if hasattr(self.mobile_phone, 'to_alipay_dict'):
                params['mobile_phone'] = json.dumps(obj=self.mobile_phone.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['mobile_phone'] = self.mobile_phone
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = json.dumps(obj=self.name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['name'] = self.name
        if self.nick:
            if hasattr(self.nick, 'to_alipay_dict'):
                params['nick'] = json.dumps(obj=self.nick.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['nick'] = self.nick
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = json.dumps(obj=self.status.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['status'] = self.status
        if self.submit_time:
            if hasattr(self.submit_time, 'to_alipay_dict'):
                params['submit_time'] = json.dumps(obj=self.submit_time.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['submit_time'] = self.submit_time
        if self.type_sub_first_id:
            if hasattr(self.type_sub_first_id, 'to_alipay_dict'):
                params['type_sub_first_id'] = json.dumps(obj=self.type_sub_first_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['type_sub_first_id'] = self.type_sub_first_id
        if self.type_sub_first_name:
            if hasattr(self.type_sub_first_name, 'to_alipay_dict'):
                params['type_sub_first_name'] = json.dumps(obj=self.type_sub_first_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['type_sub_first_name'] = self.type_sub_first_name
        if self.type_sub_second_id:
            if hasattr(self.type_sub_second_id, 'to_alipay_dict'):
                params['type_sub_second_id'] = json.dumps(obj=self.type_sub_second_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['type_sub_second_id'] = self.type_sub_second_id
        if self.type_sub_second_name:
            if hasattr(self.type_sub_second_name, 'to_alipay_dict'):
                params['type_sub_second_name'] = json.dumps(obj=self.type_sub_second_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['type_sub_second_name'] = self.type_sub_second_name
        if self.type_union_first_id:
            if hasattr(self.type_union_first_id, 'to_alipay_dict'):
                params['type_union_first_id'] = json.dumps(obj=self.type_union_first_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['type_union_first_id'] = self.type_union_first_id
        if self.type_union_second_id:
            if hasattr(self.type_union_second_id, 'to_alipay_dict'):
                params['type_union_second_id'] = json.dumps(obj=self.type_union_second_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['type_union_second_id'] = self.type_union_second_id
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = json.dumps(obj=self.url.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['url'] = self.url
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
        if self.attachment:
            multipart_params['attachment'] = self.attachment
        return multipart_params
