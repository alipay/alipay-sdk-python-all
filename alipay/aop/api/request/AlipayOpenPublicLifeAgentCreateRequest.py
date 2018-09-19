#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayOpenPublicLifeAgentCreateRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._account = None
        self._business_license_no = None
        self._contact_email = None
        self._contact_mobile = None
        self._contact_name = None
        self._mcc_code = None
        self._out_biz_no = None
        self._public_desc = None
        self._public_name = None
        self._background_pic = None
        self._business_license_auth_pic = None
        self._business_license_pic = None
        self._logo_pic = None
        self._own_intellectual_pic = None
        self._shop_scene_pic = None
        self._shop_sign_board_pic = None
        self._special_license_pic = None
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
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value
    @property
    def business_license_no(self):
        return self._business_license_no

    @business_license_no.setter
    def business_license_no(self, value):
        self._business_license_no = value
    @property
    def contact_email(self):
        return self._contact_email

    @contact_email.setter
    def contact_email(self, value):
        self._contact_email = value
    @property
    def contact_mobile(self):
        return self._contact_mobile

    @contact_mobile.setter
    def contact_mobile(self, value):
        self._contact_mobile = value
    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def mcc_code(self):
        return self._mcc_code

    @mcc_code.setter
    def mcc_code(self, value):
        self._mcc_code = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def public_desc(self):
        return self._public_desc

    @public_desc.setter
    def public_desc(self, value):
        self._public_desc = value
    @property
    def public_name(self):
        return self._public_name

    @public_name.setter
    def public_name(self, value):
        self._public_name = value

    @property
    def background_pic(self):
        return self._background_pic

    @background_pic.setter
    def background_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._background_pic = value
    @property
    def business_license_auth_pic(self):
        return self._business_license_auth_pic

    @business_license_auth_pic.setter
    def business_license_auth_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._business_license_auth_pic = value
    @property
    def business_license_pic(self):
        return self._business_license_pic

    @business_license_pic.setter
    def business_license_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._business_license_pic = value
    @property
    def logo_pic(self):
        return self._logo_pic

    @logo_pic.setter
    def logo_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._logo_pic = value
    @property
    def own_intellectual_pic(self):
        return self._own_intellectual_pic

    @own_intellectual_pic.setter
    def own_intellectual_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._own_intellectual_pic = value
    @property
    def shop_scene_pic(self):
        return self._shop_scene_pic

    @shop_scene_pic.setter
    def shop_scene_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._shop_scene_pic = value
    @property
    def shop_sign_board_pic(self):
        return self._shop_sign_board_pic

    @shop_sign_board_pic.setter
    def shop_sign_board_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._shop_sign_board_pic = value
    @property
    def special_license_pic(self):
        return self._special_license_pic

    @special_license_pic.setter
    def special_license_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._special_license_pic = value

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
        params[P_METHOD] = 'alipay.open.public.life.agent.create'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.account:
            if hasattr(self.account, 'to_alipay_dict'):
                params['account'] = json.dumps(obj=self.account.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['account'] = self.account
        if self.business_license_no:
            if hasattr(self.business_license_no, 'to_alipay_dict'):
                params['business_license_no'] = json.dumps(obj=self.business_license_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['business_license_no'] = self.business_license_no
        if self.contact_email:
            if hasattr(self.contact_email, 'to_alipay_dict'):
                params['contact_email'] = json.dumps(obj=self.contact_email.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['contact_email'] = self.contact_email
        if self.contact_mobile:
            if hasattr(self.contact_mobile, 'to_alipay_dict'):
                params['contact_mobile'] = json.dumps(obj=self.contact_mobile.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['contact_mobile'] = self.contact_mobile
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = json.dumps(obj=self.contact_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['contact_name'] = self.contact_name
        if self.mcc_code:
            if hasattr(self.mcc_code, 'to_alipay_dict'):
                params['mcc_code'] = json.dumps(obj=self.mcc_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['mcc_code'] = self.mcc_code
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = json.dumps(obj=self.out_biz_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.public_desc:
            if hasattr(self.public_desc, 'to_alipay_dict'):
                params['public_desc'] = json.dumps(obj=self.public_desc.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['public_desc'] = self.public_desc
        if self.public_name:
            if hasattr(self.public_name, 'to_alipay_dict'):
                params['public_name'] = json.dumps(obj=self.public_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['public_name'] = self.public_name
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
        if self.background_pic:
            multipart_params['background_pic'] = self.background_pic
        if self.business_license_auth_pic:
            multipart_params['business_license_auth_pic'] = self.business_license_auth_pic
        if self.business_license_pic:
            multipart_params['business_license_pic'] = self.business_license_pic
        if self.logo_pic:
            multipart_params['logo_pic'] = self.logo_pic
        if self.own_intellectual_pic:
            multipart_params['own_intellectual_pic'] = self.own_intellectual_pic
        if self.shop_scene_pic:
            multipart_params['shop_scene_pic'] = self.shop_scene_pic
        if self.shop_sign_board_pic:
            multipart_params['shop_sign_board_pic'] = self.shop_sign_board_pic
        if self.special_license_pic:
            multipart_params['special_license_pic'] = self.special_license_pic
        return multipart_params
