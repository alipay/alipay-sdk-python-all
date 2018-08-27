#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayEbppPdeductSignAddRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._agent_channel = None
        self._agent_code = None
        self._bill_key = None
        self._biz_type = None
        self._charge_inst = None
        self._deduct_prod_code = None
        self._deduct_type = None
        self._ext_user_info = None
        self._extend_field = None
        self._notify_config = None
        self._out_agreement_id = None
        self._owner_name = None
        self._pay_config = None
        self._pay_password_token = None
        self._pid = None
        self._sign_expire_date = None
        self._sub_biz_type = None
        self._user_id = None
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
    def agent_channel(self):
        return self._agent_channel

    @agent_channel.setter
    def agent_channel(self, value):
        self._agent_channel = value
    @property
    def agent_code(self):
        return self._agent_code

    @agent_code.setter
    def agent_code(self, value):
        self._agent_code = value
    @property
    def bill_key(self):
        return self._bill_key

    @bill_key.setter
    def bill_key(self, value):
        self._bill_key = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def charge_inst(self):
        return self._charge_inst

    @charge_inst.setter
    def charge_inst(self, value):
        self._charge_inst = value
    @property
    def deduct_prod_code(self):
        return self._deduct_prod_code

    @deduct_prod_code.setter
    def deduct_prod_code(self, value):
        self._deduct_prod_code = value
    @property
    def deduct_type(self):
        return self._deduct_type

    @deduct_type.setter
    def deduct_type(self, value):
        self._deduct_type = value
    @property
    def ext_user_info(self):
        return self._ext_user_info

    @ext_user_info.setter
    def ext_user_info(self, value):
        self._ext_user_info = value
    @property
    def extend_field(self):
        return self._extend_field

    @extend_field.setter
    def extend_field(self, value):
        self._extend_field = value
    @property
    def notify_config(self):
        return self._notify_config

    @notify_config.setter
    def notify_config(self, value):
        self._notify_config = value
    @property
    def out_agreement_id(self):
        return self._out_agreement_id

    @out_agreement_id.setter
    def out_agreement_id(self, value):
        self._out_agreement_id = value
    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, value):
        self._owner_name = value
    @property
    def pay_config(self):
        return self._pay_config

    @pay_config.setter
    def pay_config(self, value):
        self._pay_config = value
    @property
    def pay_password_token(self):
        return self._pay_password_token

    @pay_password_token.setter
    def pay_password_token(self, value):
        self._pay_password_token = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def sign_expire_date(self):
        return self._sign_expire_date

    @sign_expire_date.setter
    def sign_expire_date(self, value):
        self._sign_expire_date = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


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
        params[P_METHOD] = 'alipay.ebpp.pdeduct.sign.add'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.agent_channel:
            if hasattr(self.agent_channel, 'to_alipay_dict'):
                params['agent_channel'] = json.dumps(obj=self.agent_channel.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['agent_channel'] = self.agent_channel
        if self.agent_code:
            if hasattr(self.agent_code, 'to_alipay_dict'):
                params['agent_code'] = json.dumps(obj=self.agent_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['agent_code'] = self.agent_code
        if self.bill_key:
            if hasattr(self.bill_key, 'to_alipay_dict'):
                params['bill_key'] = json.dumps(obj=self.bill_key.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['bill_key'] = self.bill_key
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = json.dumps(obj=self.biz_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['biz_type'] = self.biz_type
        if self.charge_inst:
            if hasattr(self.charge_inst, 'to_alipay_dict'):
                params['charge_inst'] = json.dumps(obj=self.charge_inst.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['charge_inst'] = self.charge_inst
        if self.deduct_prod_code:
            if hasattr(self.deduct_prod_code, 'to_alipay_dict'):
                params['deduct_prod_code'] = json.dumps(obj=self.deduct_prod_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['deduct_prod_code'] = self.deduct_prod_code
        if self.deduct_type:
            if hasattr(self.deduct_type, 'to_alipay_dict'):
                params['deduct_type'] = json.dumps(obj=self.deduct_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['deduct_type'] = self.deduct_type
        if self.ext_user_info:
            if hasattr(self.ext_user_info, 'to_alipay_dict'):
                params['ext_user_info'] = json.dumps(obj=self.ext_user_info.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['ext_user_info'] = self.ext_user_info
        if self.extend_field:
            if hasattr(self.extend_field, 'to_alipay_dict'):
                params['extend_field'] = json.dumps(obj=self.extend_field.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['extend_field'] = self.extend_field
        if self.notify_config:
            if hasattr(self.notify_config, 'to_alipay_dict'):
                params['notify_config'] = json.dumps(obj=self.notify_config.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['notify_config'] = self.notify_config
        if self.out_agreement_id:
            if hasattr(self.out_agreement_id, 'to_alipay_dict'):
                params['out_agreement_id'] = json.dumps(obj=self.out_agreement_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['out_agreement_id'] = self.out_agreement_id
        if self.owner_name:
            if hasattr(self.owner_name, 'to_alipay_dict'):
                params['owner_name'] = json.dumps(obj=self.owner_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['owner_name'] = self.owner_name
        if self.pay_config:
            if hasattr(self.pay_config, 'to_alipay_dict'):
                params['pay_config'] = json.dumps(obj=self.pay_config.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['pay_config'] = self.pay_config
        if self.pay_password_token:
            if hasattr(self.pay_password_token, 'to_alipay_dict'):
                params['pay_password_token'] = json.dumps(obj=self.pay_password_token.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['pay_password_token'] = self.pay_password_token
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = json.dumps(obj=self.pid.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['pid'] = self.pid
        if self.sign_expire_date:
            if hasattr(self.sign_expire_date, 'to_alipay_dict'):
                params['sign_expire_date'] = json.dumps(obj=self.sign_expire_date.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['sign_expire_date'] = self.sign_expire_date
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = json.dumps(obj=self.sub_biz_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['sub_biz_type'] = self.sub_biz_type
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
        return multipart_params
