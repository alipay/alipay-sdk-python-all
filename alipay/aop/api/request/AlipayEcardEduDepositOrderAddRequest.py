#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayEcardEduDepositOrderAddRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._agent_code = None
        self._agreement_id = None
        self._alipay_user_id = None
        self._card_name = None
        self._card_no = None
        self._deposit_amount = None
        self._mobile_no = None
        self._public_id = None
        self._share_mobile_no = None
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
    def agent_code(self):
        return self._agent_code

    @agent_code.setter
    def agent_code(self, value):
        self._agent_code = value
    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def card_name(self):
        return self._card_name

    @card_name.setter
    def card_name(self, value):
        self._card_name = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def deposit_amount(self):
        return self._deposit_amount

    @deposit_amount.setter
    def deposit_amount(self, value):
        self._deposit_amount = value
    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, value):
        self._mobile_no = value
    @property
    def public_id(self):
        return self._public_id

    @public_id.setter
    def public_id(self, value):
        self._public_id = value
    @property
    def share_mobile_no(self):
        return self._share_mobile_no

    @share_mobile_no.setter
    def share_mobile_no(self, value):
        self._share_mobile_no = value


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
        params[P_METHOD] = 'alipay.ecard.edu.deposit.order.add'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.agent_code:
            if hasattr(self.agent_code, 'to_alipay_dict'):
                params['agent_code'] = json.dumps(obj=self.agent_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['agent_code'] = self.agent_code
        if self.agreement_id:
            if hasattr(self.agreement_id, 'to_alipay_dict'):
                params['agreement_id'] = json.dumps(obj=self.agreement_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['agreement_id'] = self.agreement_id
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = json.dumps(obj=self.alipay_user_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.card_name:
            if hasattr(self.card_name, 'to_alipay_dict'):
                params['card_name'] = json.dumps(obj=self.card_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['card_name'] = self.card_name
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = json.dumps(obj=self.card_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['card_no'] = self.card_no
        if self.deposit_amount:
            if hasattr(self.deposit_amount, 'to_alipay_dict'):
                params['deposit_amount'] = json.dumps(obj=self.deposit_amount.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['deposit_amount'] = self.deposit_amount
        if self.mobile_no:
            if hasattr(self.mobile_no, 'to_alipay_dict'):
                params['mobile_no'] = json.dumps(obj=self.mobile_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['mobile_no'] = self.mobile_no
        if self.public_id:
            if hasattr(self.public_id, 'to_alipay_dict'):
                params['public_id'] = json.dumps(obj=self.public_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['public_id'] = self.public_id
        if self.share_mobile_no:
            if hasattr(self.share_mobile_no, 'to_alipay_dict'):
                params['share_mobile_no'] = json.dumps(obj=self.share_mobile_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['share_mobile_no'] = self.share_mobile_no
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
