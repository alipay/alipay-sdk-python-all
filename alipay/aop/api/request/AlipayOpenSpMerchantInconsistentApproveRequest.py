#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayOpenSpMerchantInconsistentApproveRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._back_card = None
        self._commitment_letter = None
        self._front_card = None
        self._handheld_business_license = None
        self._handheld_card = None
        self._item_code = None
        self._merchant_pid = None
        self._mini_appid = None
        self._out_biz_no = None
        self._promotor_pid = None
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
    def back_card(self):
        return self._back_card

    @back_card.setter
    def back_card(self, value):
        self._back_card = value
    @property
    def commitment_letter(self):
        return self._commitment_letter

    @commitment_letter.setter
    def commitment_letter(self, value):
        self._commitment_letter = value
    @property
    def front_card(self):
        return self._front_card

    @front_card.setter
    def front_card(self, value):
        self._front_card = value
    @property
    def handheld_business_license(self):
        return self._handheld_business_license

    @handheld_business_license.setter
    def handheld_business_license(self, value):
        self._handheld_business_license = value
    @property
    def handheld_card(self):
        return self._handheld_card

    @handheld_card.setter
    def handheld_card(self, value):
        self._handheld_card = value
    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def mini_appid(self):
        return self._mini_appid

    @mini_appid.setter
    def mini_appid(self, value):
        self._mini_appid = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def promotor_pid(self):
        return self._promotor_pid

    @promotor_pid.setter
    def promotor_pid(self, value):
        self._promotor_pid = value


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
        params[P_METHOD] = 'alipay.open.sp.merchant.inconsistent.approve'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.back_card:
            if hasattr(self.back_card, 'to_alipay_dict'):
                params['back_card'] = json.dumps(obj=self.back_card.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['back_card'] = self.back_card
        if self.commitment_letter:
            if hasattr(self.commitment_letter, 'to_alipay_dict'):
                params['commitment_letter'] = json.dumps(obj=self.commitment_letter.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['commitment_letter'] = self.commitment_letter
        if self.front_card:
            if hasattr(self.front_card, 'to_alipay_dict'):
                params['front_card'] = json.dumps(obj=self.front_card.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['front_card'] = self.front_card
        if self.handheld_business_license:
            if hasattr(self.handheld_business_license, 'to_alipay_dict'):
                params['handheld_business_license'] = json.dumps(obj=self.handheld_business_license.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['handheld_business_license'] = self.handheld_business_license
        if self.handheld_card:
            if hasattr(self.handheld_card, 'to_alipay_dict'):
                params['handheld_card'] = json.dumps(obj=self.handheld_card.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['handheld_card'] = self.handheld_card
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = json.dumps(obj=self.item_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['item_code'] = self.item_code
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = json.dumps(obj=self.merchant_pid.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.mini_appid:
            if hasattr(self.mini_appid, 'to_alipay_dict'):
                params['mini_appid'] = json.dumps(obj=self.mini_appid.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['mini_appid'] = self.mini_appid
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = json.dumps(obj=self.out_biz_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.promotor_pid:
            if hasattr(self.promotor_pid, 'to_alipay_dict'):
                params['promotor_pid'] = json.dumps(obj=self.promotor_pid.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['promotor_pid'] = self.promotor_pid
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
