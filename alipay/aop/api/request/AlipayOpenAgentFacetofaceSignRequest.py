#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *

from alipay.aop.api.domain.SignAddressInfo import SignAddressInfo



class AlipayOpenAgentFacetofaceSignRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._batch_no = None
        self._business_license_mobile = None
        self._business_license_no = None
        self._date_limitation = None
        self._long_term = None
        self._mcc_code = None
        self._rate = None
        self._shop_address = None
        self._shop_name = None
        self._sign_and_auth = None
        self._business_license_auth_pic = None
        self._business_license_pic = None
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
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def business_license_mobile(self):
        return self._business_license_mobile

    @business_license_mobile.setter
    def business_license_mobile(self, value):
        self._business_license_mobile = value
    @property
    def business_license_no(self):
        return self._business_license_no

    @business_license_no.setter
    def business_license_no(self, value):
        self._business_license_no = value
    @property
    def date_limitation(self):
        return self._date_limitation

    @date_limitation.setter
    def date_limitation(self, value):
        self._date_limitation = value
    @property
    def long_term(self):
        return self._long_term

    @long_term.setter
    def long_term(self, value):
        self._long_term = value
    @property
    def mcc_code(self):
        return self._mcc_code

    @mcc_code.setter
    def mcc_code(self, value):
        self._mcc_code = value
    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value
    @property
    def shop_address(self):
        return self._shop_address

    @shop_address.setter
    def shop_address(self, value):
        if isinstance(value, SignAddressInfo):
            self._shop_address = value
        else:
            self._shop_address = SignAddressInfo.from_alipay_dict(value)
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def sign_and_auth(self):
        return self._sign_and_auth

    @sign_and_auth.setter
    def sign_and_auth(self, value):
        self._sign_and_auth = value

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
        params[P_METHOD] = 'alipay.open.agent.facetoface.sign'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = json.dumps(obj=self.batch_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['batch_no'] = self.batch_no
        if self.business_license_mobile:
            if hasattr(self.business_license_mobile, 'to_alipay_dict'):
                params['business_license_mobile'] = json.dumps(obj=self.business_license_mobile.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['business_license_mobile'] = self.business_license_mobile
        if self.business_license_no:
            if hasattr(self.business_license_no, 'to_alipay_dict'):
                params['business_license_no'] = json.dumps(obj=self.business_license_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['business_license_no'] = self.business_license_no
        if self.date_limitation:
            if hasattr(self.date_limitation, 'to_alipay_dict'):
                params['date_limitation'] = json.dumps(obj=self.date_limitation.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['date_limitation'] = self.date_limitation
        if self.long_term:
            if hasattr(self.long_term, 'to_alipay_dict'):
                params['long_term'] = json.dumps(obj=self.long_term.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['long_term'] = self.long_term
        if self.mcc_code:
            if hasattr(self.mcc_code, 'to_alipay_dict'):
                params['mcc_code'] = json.dumps(obj=self.mcc_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['mcc_code'] = self.mcc_code
        if self.rate:
            if hasattr(self.rate, 'to_alipay_dict'):
                params['rate'] = json.dumps(obj=self.rate.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['rate'] = self.rate
        if self.shop_address:
            if hasattr(self.shop_address, 'to_alipay_dict'):
                params['shop_address'] = json.dumps(obj=self.shop_address.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['shop_address'] = self.shop_address
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = json.dumps(obj=self.shop_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['shop_name'] = self.shop_name
        if self.sign_and_auth:
            if hasattr(self.sign_and_auth, 'to_alipay_dict'):
                params['sign_and_auth'] = json.dumps(obj=self.sign_and_auth.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['sign_and_auth'] = self.sign_and_auth
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
        if self.business_license_auth_pic:
            multipart_params['business_license_auth_pic'] = self.business_license_auth_pic
        if self.business_license_pic:
            multipart_params['business_license_pic'] = self.business_license_pic
        if self.shop_scene_pic:
            multipart_params['shop_scene_pic'] = self.shop_scene_pic
        if self.shop_sign_board_pic:
            multipart_params['shop_sign_board_pic'] = self.shop_sign_board_pic
        if self.special_license_pic:
            multipart_params['special_license_pic'] = self.special_license_pic
        return multipart_params
