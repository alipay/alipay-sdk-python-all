#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayWeiboPucChargeRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._apd_id = None
        self._cell_id = None
        self._device_info_token = None
        self._exparam = None
        self._imei = None
        self._ip = None
        self._lac_id = None
        self._login_from = None
        self._mac = None
        self._partner_user_id = None
        self._tid = None
        self._token = None
        self._umid = None
        self._wireless_mac = None
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
    def apd_id(self):
        return self._apd_id

    @apd_id.setter
    def apd_id(self, value):
        self._apd_id = value
    @property
    def cell_id(self):
        return self._cell_id

    @cell_id.setter
    def cell_id(self, value):
        self._cell_id = value
    @property
    def device_info_token(self):
        return self._device_info_token

    @device_info_token.setter
    def device_info_token(self, value):
        self._device_info_token = value
    @property
    def exparam(self):
        return self._exparam

    @exparam.setter
    def exparam(self, value):
        self._exparam = value
    @property
    def imei(self):
        return self._imei

    @imei.setter
    def imei(self, value):
        self._imei = value
    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value):
        self._ip = value
    @property
    def lac_id(self):
        return self._lac_id

    @lac_id.setter
    def lac_id(self, value):
        self._lac_id = value
    @property
    def login_from(self):
        return self._login_from

    @login_from.setter
    def login_from(self, value):
        self._login_from = value
    @property
    def mac(self):
        return self._mac

    @mac.setter
    def mac(self, value):
        self._mac = value
    @property
    def partner_user_id(self):
        return self._partner_user_id

    @partner_user_id.setter
    def partner_user_id(self, value):
        self._partner_user_id = value
    @property
    def tid(self):
        return self._tid

    @tid.setter
    def tid(self, value):
        self._tid = value
    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value
    @property
    def umid(self):
        return self._umid

    @umid.setter
    def umid(self, value):
        self._umid = value
    @property
    def wireless_mac(self):
        return self._wireless_mac

    @wireless_mac.setter
    def wireless_mac(self, value):
        self._wireless_mac = value


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
        params[P_METHOD] = 'alipay.weibo.puc.charge'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.apd_id:
            if hasattr(self.apd_id, 'to_alipay_dict'):
                params['apd_id'] = json.dumps(obj=self.apd_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['apd_id'] = self.apd_id
        if self.cell_id:
            if hasattr(self.cell_id, 'to_alipay_dict'):
                params['cell_id'] = json.dumps(obj=self.cell_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['cell_id'] = self.cell_id
        if self.device_info_token:
            if hasattr(self.device_info_token, 'to_alipay_dict'):
                params['device_info_token'] = json.dumps(obj=self.device_info_token.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['device_info_token'] = self.device_info_token
        if self.exparam:
            if hasattr(self.exparam, 'to_alipay_dict'):
                params['exparam'] = json.dumps(obj=self.exparam.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['exparam'] = self.exparam
        if self.imei:
            if hasattr(self.imei, 'to_alipay_dict'):
                params['imei'] = json.dumps(obj=self.imei.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['imei'] = self.imei
        if self.ip:
            if hasattr(self.ip, 'to_alipay_dict'):
                params['ip'] = json.dumps(obj=self.ip.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['ip'] = self.ip
        if self.lac_id:
            if hasattr(self.lac_id, 'to_alipay_dict'):
                params['lac_id'] = json.dumps(obj=self.lac_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['lac_id'] = self.lac_id
        if self.login_from:
            if hasattr(self.login_from, 'to_alipay_dict'):
                params['login_from'] = json.dumps(obj=self.login_from.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['login_from'] = self.login_from
        if self.mac:
            if hasattr(self.mac, 'to_alipay_dict'):
                params['mac'] = json.dumps(obj=self.mac.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['mac'] = self.mac
        if self.partner_user_id:
            if hasattr(self.partner_user_id, 'to_alipay_dict'):
                params['partner_user_id'] = json.dumps(obj=self.partner_user_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['partner_user_id'] = self.partner_user_id
        if self.tid:
            if hasattr(self.tid, 'to_alipay_dict'):
                params['tid'] = json.dumps(obj=self.tid.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['tid'] = self.tid
        if self.token:
            if hasattr(self.token, 'to_alipay_dict'):
                params['token'] = json.dumps(obj=self.token.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['token'] = self.token
        if self.umid:
            if hasattr(self.umid, 'to_alipay_dict'):
                params['umid'] = json.dumps(obj=self.umid.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['umid'] = self.umid
        if self.wireless_mac:
            if hasattr(self.wireless_mac, 'to_alipay_dict'):
                params['wireless_mac'] = json.dumps(obj=self.wireless_mac.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['wireless_mac'] = self.wireless_mac
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
