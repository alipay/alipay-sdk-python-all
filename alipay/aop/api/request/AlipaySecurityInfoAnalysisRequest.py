#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipaySecurityInfoAnalysisRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._env_client_base_band = None
        self._env_client_base_station = None
        self._env_client_coordinates = None
        self._env_client_imei = None
        self._env_client_imsi = None
        self._env_client_ios_udid = None
        self._env_client_ip = None
        self._env_client_mac = None
        self._env_client_screen = None
        self._env_client_uuid = None
        self._js_token_id = None
        self._partner_id = None
        self._scene_code = None
        self._user_account_no = None
        self._user_bind_bankcard = None
        self._user_bind_bankcard_type = None
        self._user_bind_mobile = None
        self._user_identity_type = None
        self._user_real_name = None
        self._user_reg_date = None
        self._user_reg_email = None
        self._user_reg_mobile = None
        self._userr_identity_no = None
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
    def env_client_base_band(self):
        return self._env_client_base_band

    @env_client_base_band.setter
    def env_client_base_band(self, value):
        self._env_client_base_band = value
    @property
    def env_client_base_station(self):
        return self._env_client_base_station

    @env_client_base_station.setter
    def env_client_base_station(self, value):
        self._env_client_base_station = value
    @property
    def env_client_coordinates(self):
        return self._env_client_coordinates

    @env_client_coordinates.setter
    def env_client_coordinates(self, value):
        self._env_client_coordinates = value
    @property
    def env_client_imei(self):
        return self._env_client_imei

    @env_client_imei.setter
    def env_client_imei(self, value):
        self._env_client_imei = value
    @property
    def env_client_imsi(self):
        return self._env_client_imsi

    @env_client_imsi.setter
    def env_client_imsi(self, value):
        self._env_client_imsi = value
    @property
    def env_client_ios_udid(self):
        return self._env_client_ios_udid

    @env_client_ios_udid.setter
    def env_client_ios_udid(self, value):
        self._env_client_ios_udid = value
    @property
    def env_client_ip(self):
        return self._env_client_ip

    @env_client_ip.setter
    def env_client_ip(self, value):
        self._env_client_ip = value
    @property
    def env_client_mac(self):
        return self._env_client_mac

    @env_client_mac.setter
    def env_client_mac(self, value):
        self._env_client_mac = value
    @property
    def env_client_screen(self):
        return self._env_client_screen

    @env_client_screen.setter
    def env_client_screen(self, value):
        self._env_client_screen = value
    @property
    def env_client_uuid(self):
        return self._env_client_uuid

    @env_client_uuid.setter
    def env_client_uuid(self, value):
        self._env_client_uuid = value
    @property
    def js_token_id(self):
        return self._js_token_id

    @js_token_id.setter
    def js_token_id(self, value):
        self._js_token_id = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def user_account_no(self):
        return self._user_account_no

    @user_account_no.setter
    def user_account_no(self, value):
        self._user_account_no = value
    @property
    def user_bind_bankcard(self):
        return self._user_bind_bankcard

    @user_bind_bankcard.setter
    def user_bind_bankcard(self, value):
        self._user_bind_bankcard = value
    @property
    def user_bind_bankcard_type(self):
        return self._user_bind_bankcard_type

    @user_bind_bankcard_type.setter
    def user_bind_bankcard_type(self, value):
        self._user_bind_bankcard_type = value
    @property
    def user_bind_mobile(self):
        return self._user_bind_mobile

    @user_bind_mobile.setter
    def user_bind_mobile(self, value):
        self._user_bind_mobile = value
    @property
    def user_identity_type(self):
        return self._user_identity_type

    @user_identity_type.setter
    def user_identity_type(self, value):
        self._user_identity_type = value
    @property
    def user_real_name(self):
        return self._user_real_name

    @user_real_name.setter
    def user_real_name(self, value):
        self._user_real_name = value
    @property
    def user_reg_date(self):
        return self._user_reg_date

    @user_reg_date.setter
    def user_reg_date(self, value):
        self._user_reg_date = value
    @property
    def user_reg_email(self):
        return self._user_reg_email

    @user_reg_email.setter
    def user_reg_email(self, value):
        self._user_reg_email = value
    @property
    def user_reg_mobile(self):
        return self._user_reg_mobile

    @user_reg_mobile.setter
    def user_reg_mobile(self, value):
        self._user_reg_mobile = value
    @property
    def userr_identity_no(self):
        return self._userr_identity_no

    @userr_identity_no.setter
    def userr_identity_no(self, value):
        self._userr_identity_no = value


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
        params[P_METHOD] = 'alipay.security.info.analysis'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.env_client_base_band:
            if hasattr(self.env_client_base_band, 'to_alipay_dict'):
                params['env_client_base_band'] = json.dumps(obj=self.env_client_base_band.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['env_client_base_band'] = self.env_client_base_band
        if self.env_client_base_station:
            if hasattr(self.env_client_base_station, 'to_alipay_dict'):
                params['env_client_base_station'] = json.dumps(obj=self.env_client_base_station.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['env_client_base_station'] = self.env_client_base_station
        if self.env_client_coordinates:
            if hasattr(self.env_client_coordinates, 'to_alipay_dict'):
                params['env_client_coordinates'] = json.dumps(obj=self.env_client_coordinates.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['env_client_coordinates'] = self.env_client_coordinates
        if self.env_client_imei:
            if hasattr(self.env_client_imei, 'to_alipay_dict'):
                params['env_client_imei'] = json.dumps(obj=self.env_client_imei.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['env_client_imei'] = self.env_client_imei
        if self.env_client_imsi:
            if hasattr(self.env_client_imsi, 'to_alipay_dict'):
                params['env_client_imsi'] = json.dumps(obj=self.env_client_imsi.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['env_client_imsi'] = self.env_client_imsi
        if self.env_client_ios_udid:
            if hasattr(self.env_client_ios_udid, 'to_alipay_dict'):
                params['env_client_ios_udid'] = json.dumps(obj=self.env_client_ios_udid.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['env_client_ios_udid'] = self.env_client_ios_udid
        if self.env_client_ip:
            if hasattr(self.env_client_ip, 'to_alipay_dict'):
                params['env_client_ip'] = json.dumps(obj=self.env_client_ip.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['env_client_ip'] = self.env_client_ip
        if self.env_client_mac:
            if hasattr(self.env_client_mac, 'to_alipay_dict'):
                params['env_client_mac'] = json.dumps(obj=self.env_client_mac.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['env_client_mac'] = self.env_client_mac
        if self.env_client_screen:
            if hasattr(self.env_client_screen, 'to_alipay_dict'):
                params['env_client_screen'] = json.dumps(obj=self.env_client_screen.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['env_client_screen'] = self.env_client_screen
        if self.env_client_uuid:
            if hasattr(self.env_client_uuid, 'to_alipay_dict'):
                params['env_client_uuid'] = json.dumps(obj=self.env_client_uuid.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['env_client_uuid'] = self.env_client_uuid
        if self.js_token_id:
            if hasattr(self.js_token_id, 'to_alipay_dict'):
                params['js_token_id'] = json.dumps(obj=self.js_token_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['js_token_id'] = self.js_token_id
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = json.dumps(obj=self.partner_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['partner_id'] = self.partner_id
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = json.dumps(obj=self.scene_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['scene_code'] = self.scene_code
        if self.user_account_no:
            if hasattr(self.user_account_no, 'to_alipay_dict'):
                params['user_account_no'] = json.dumps(obj=self.user_account_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['user_account_no'] = self.user_account_no
        if self.user_bind_bankcard:
            if hasattr(self.user_bind_bankcard, 'to_alipay_dict'):
                params['user_bind_bankcard'] = json.dumps(obj=self.user_bind_bankcard.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['user_bind_bankcard'] = self.user_bind_bankcard
        if self.user_bind_bankcard_type:
            if hasattr(self.user_bind_bankcard_type, 'to_alipay_dict'):
                params['user_bind_bankcard_type'] = json.dumps(obj=self.user_bind_bankcard_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['user_bind_bankcard_type'] = self.user_bind_bankcard_type
        if self.user_bind_mobile:
            if hasattr(self.user_bind_mobile, 'to_alipay_dict'):
                params['user_bind_mobile'] = json.dumps(obj=self.user_bind_mobile.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['user_bind_mobile'] = self.user_bind_mobile
        if self.user_identity_type:
            if hasattr(self.user_identity_type, 'to_alipay_dict'):
                params['user_identity_type'] = json.dumps(obj=self.user_identity_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['user_identity_type'] = self.user_identity_type
        if self.user_real_name:
            if hasattr(self.user_real_name, 'to_alipay_dict'):
                params['user_real_name'] = json.dumps(obj=self.user_real_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['user_real_name'] = self.user_real_name
        if self.user_reg_date:
            if hasattr(self.user_reg_date, 'to_alipay_dict'):
                params['user_reg_date'] = json.dumps(obj=self.user_reg_date.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['user_reg_date'] = self.user_reg_date
        if self.user_reg_email:
            if hasattr(self.user_reg_email, 'to_alipay_dict'):
                params['user_reg_email'] = json.dumps(obj=self.user_reg_email.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['user_reg_email'] = self.user_reg_email
        if self.user_reg_mobile:
            if hasattr(self.user_reg_mobile, 'to_alipay_dict'):
                params['user_reg_mobile'] = json.dumps(obj=self.user_reg_mobile.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['user_reg_mobile'] = self.user_reg_mobile
        if self.userr_identity_no:
            if hasattr(self.userr_identity_no, 'to_alipay_dict'):
                params['userr_identity_no'] = json.dumps(obj=self.userr_identity_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['userr_identity_no'] = self.userr_identity_no
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
