#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OtherSettleAccountDTO import OtherSettleAccountDTO
from alipay.aop.api.domain.PromiseConfigDTO import PromiseConfigDTO
from alipay.aop.api.domain.RiskConfigDTO import RiskConfigDTO


class AlipayMerchantSolcreditserviceprodMerchantCreateormodifyModel(object):

    def __init__(self):
        self._alipay_settlement_account = None
        self._app_jump_link = None
        self._contact_email = None
        self._contact_number = None
        self._isv_separate_ledger_rate = None
        self._logo_url = None
        self._merchant_app_id = None
        self._merchant_name = None
        self._other_settle_account_list = None
        self._promise_config = None
        self._risk_config = None
        self._scene_code = None
        self._smid = None

    @property
    def alipay_settlement_account(self):
        return self._alipay_settlement_account

    @alipay_settlement_account.setter
    def alipay_settlement_account(self, value):
        self._alipay_settlement_account = value
    @property
    def app_jump_link(self):
        return self._app_jump_link

    @app_jump_link.setter
    def app_jump_link(self, value):
        self._app_jump_link = value
    @property
    def contact_email(self):
        return self._contact_email

    @contact_email.setter
    def contact_email(self, value):
        self._contact_email = value
    @property
    def contact_number(self):
        return self._contact_number

    @contact_number.setter
    def contact_number(self, value):
        self._contact_number = value
    @property
    def isv_separate_ledger_rate(self):
        return self._isv_separate_ledger_rate

    @isv_separate_ledger_rate.setter
    def isv_separate_ledger_rate(self, value):
        self._isv_separate_ledger_rate = value
    @property
    def logo_url(self):
        return self._logo_url

    @logo_url.setter
    def logo_url(self, value):
        self._logo_url = value
    @property
    def merchant_app_id(self):
        return self._merchant_app_id

    @merchant_app_id.setter
    def merchant_app_id(self, value):
        self._merchant_app_id = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def other_settle_account_list(self):
        return self._other_settle_account_list

    @other_settle_account_list.setter
    def other_settle_account_list(self, value):
        if isinstance(value, list):
            self._other_settle_account_list = list()
            for i in value:
                if isinstance(i, OtherSettleAccountDTO):
                    self._other_settle_account_list.append(i)
                else:
                    self._other_settle_account_list.append(OtherSettleAccountDTO.from_alipay_dict(i))
    @property
    def promise_config(self):
        return self._promise_config

    @promise_config.setter
    def promise_config(self, value):
        if isinstance(value, PromiseConfigDTO):
            self._promise_config = value
        else:
            self._promise_config = PromiseConfigDTO.from_alipay_dict(value)
    @property
    def risk_config(self):
        return self._risk_config

    @risk_config.setter
    def risk_config(self, value):
        if isinstance(value, RiskConfigDTO):
            self._risk_config = value
        else:
            self._risk_config = RiskConfigDTO.from_alipay_dict(value)
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_settlement_account:
            if hasattr(self.alipay_settlement_account, 'to_alipay_dict'):
                params['alipay_settlement_account'] = self.alipay_settlement_account.to_alipay_dict()
            else:
                params['alipay_settlement_account'] = self.alipay_settlement_account
        if self.app_jump_link:
            if hasattr(self.app_jump_link, 'to_alipay_dict'):
                params['app_jump_link'] = self.app_jump_link.to_alipay_dict()
            else:
                params['app_jump_link'] = self.app_jump_link
        if self.contact_email:
            if hasattr(self.contact_email, 'to_alipay_dict'):
                params['contact_email'] = self.contact_email.to_alipay_dict()
            else:
                params['contact_email'] = self.contact_email
        if self.contact_number:
            if hasattr(self.contact_number, 'to_alipay_dict'):
                params['contact_number'] = self.contact_number.to_alipay_dict()
            else:
                params['contact_number'] = self.contact_number
        if self.isv_separate_ledger_rate:
            if hasattr(self.isv_separate_ledger_rate, 'to_alipay_dict'):
                params['isv_separate_ledger_rate'] = self.isv_separate_ledger_rate.to_alipay_dict()
            else:
                params['isv_separate_ledger_rate'] = self.isv_separate_ledger_rate
        if self.logo_url:
            if hasattr(self.logo_url, 'to_alipay_dict'):
                params['logo_url'] = self.logo_url.to_alipay_dict()
            else:
                params['logo_url'] = self.logo_url
        if self.merchant_app_id:
            if hasattr(self.merchant_app_id, 'to_alipay_dict'):
                params['merchant_app_id'] = self.merchant_app_id.to_alipay_dict()
            else:
                params['merchant_app_id'] = self.merchant_app_id
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.other_settle_account_list:
            if isinstance(self.other_settle_account_list, list):
                for i in range(0, len(self.other_settle_account_list)):
                    element = self.other_settle_account_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.other_settle_account_list[i] = element.to_alipay_dict()
            if hasattr(self.other_settle_account_list, 'to_alipay_dict'):
                params['other_settle_account_list'] = self.other_settle_account_list.to_alipay_dict()
            else:
                params['other_settle_account_list'] = self.other_settle_account_list
        if self.promise_config:
            if hasattr(self.promise_config, 'to_alipay_dict'):
                params['promise_config'] = self.promise_config.to_alipay_dict()
            else:
                params['promise_config'] = self.promise_config
        if self.risk_config:
            if hasattr(self.risk_config, 'to_alipay_dict'):
                params['risk_config'] = self.risk_config.to_alipay_dict()
            else:
                params['risk_config'] = self.risk_config
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantSolcreditserviceprodMerchantCreateormodifyModel()
        if 'alipay_settlement_account' in d:
            o.alipay_settlement_account = d['alipay_settlement_account']
        if 'app_jump_link' in d:
            o.app_jump_link = d['app_jump_link']
        if 'contact_email' in d:
            o.contact_email = d['contact_email']
        if 'contact_number' in d:
            o.contact_number = d['contact_number']
        if 'isv_separate_ledger_rate' in d:
            o.isv_separate_ledger_rate = d['isv_separate_ledger_rate']
        if 'logo_url' in d:
            o.logo_url = d['logo_url']
        if 'merchant_app_id' in d:
            o.merchant_app_id = d['merchant_app_id']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'other_settle_account_list' in d:
            o.other_settle_account_list = d['other_settle_account_list']
        if 'promise_config' in d:
            o.promise_config = d['promise_config']
        if 'risk_config' in d:
            o.risk_config = d['risk_config']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'smid' in d:
            o.smid = d['smid']
        return o


