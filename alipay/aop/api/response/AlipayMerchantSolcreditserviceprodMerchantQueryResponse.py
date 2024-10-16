#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OtherSettleAccountDTO import OtherSettleAccountDTO
from alipay.aop.api.domain.PromiseConfigDTO import PromiseConfigDTO
from alipay.aop.api.domain.RiskConfigDTO import RiskConfigDTO


class AlipayMerchantSolcreditserviceprodMerchantQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantSolcreditserviceprodMerchantQueryResponse, self).__init__()
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
        self._review_fail_reason = None
        self._review_status = None
        self._review_version_no = None
        self._risk_config = None
        self._scene_code = None
        self._smid = None
        self._status = None
        self._version_no = None

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
    def review_fail_reason(self):
        return self._review_fail_reason

    @review_fail_reason.setter
    def review_fail_reason(self, value):
        self._review_fail_reason = value
    @property
    def review_status(self):
        return self._review_status

    @review_status.setter
    def review_status(self, value):
        self._review_status = value
    @property
    def review_version_no(self):
        return self._review_version_no

    @review_version_no.setter
    def review_version_no(self, value):
        self._review_version_no = value
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
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def version_no(self):
        return self._version_no

    @version_no.setter
    def version_no(self, value):
        self._version_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantSolcreditserviceprodMerchantQueryResponse, self).parse_response_content(response_content)
        if 'alipay_settlement_account' in response:
            self.alipay_settlement_account = response['alipay_settlement_account']
        if 'app_jump_link' in response:
            self.app_jump_link = response['app_jump_link']
        if 'contact_email' in response:
            self.contact_email = response['contact_email']
        if 'contact_number' in response:
            self.contact_number = response['contact_number']
        if 'isv_separate_ledger_rate' in response:
            self.isv_separate_ledger_rate = response['isv_separate_ledger_rate']
        if 'logo_url' in response:
            self.logo_url = response['logo_url']
        if 'merchant_app_id' in response:
            self.merchant_app_id = response['merchant_app_id']
        if 'merchant_name' in response:
            self.merchant_name = response['merchant_name']
        if 'other_settle_account_list' in response:
            self.other_settle_account_list = response['other_settle_account_list']
        if 'promise_config' in response:
            self.promise_config = response['promise_config']
        if 'review_fail_reason' in response:
            self.review_fail_reason = response['review_fail_reason']
        if 'review_status' in response:
            self.review_status = response['review_status']
        if 'review_version_no' in response:
            self.review_version_no = response['review_version_no']
        if 'risk_config' in response:
            self.risk_config = response['risk_config']
        if 'scene_code' in response:
            self.scene_code = response['scene_code']
        if 'smid' in response:
            self.smid = response['smid']
        if 'status' in response:
            self.status = response['status']
        if 'version_no' in response:
            self.version_no = response['version_no']
